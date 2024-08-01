import streamlit as st
from tensorflow import keras
from PIL import Image
import numpy as np

apple = {0: {
    'name': 'Apple Black Rot',
    'cause': '''\n
    Fungal Pathogen: Botryosphaeria obtusa.\n
    Moisture and Humidity: Thrives in warm, wet conditions.\n
    Wounded Fruit: Cuts provide entry points.\n
    Lack of Management: Insufficient disease control measures.
''',
    'prevn': '''\n
    Sanitation: Remove infected material promptly.\n
    Fungicide Sprays: Apply at key growth stages.\n
    Pruning for Airflow: Improve ventilation around fruit.\n
    Timely Harvest: Avoid leaving apples on the tree for too long.
''',
}, 1: {
    'name': 'Cedar Apple Rust',
    'cause': '''\n
    Fungal Pathogen : The fungus responsible for Cedar Apple Rust requires both apple and cedar/juniper trees to complete its life cycle.\n
    Alternate Hosts (Cedar or Juniper Trees): The fungus overwinters on cedar or juniper trees and releases spores that can infect apple trees.\n
    Weather Conditions: Wet, cool spring weather is conducive to spore production and infection.\n
    Proximity of Cedar Trees to Apple Trees: The disease is more likely to occur if cedar or juniper trees are in close proximity to apple trees.
''',
    'prevn': '''\n
    Fungicide Applications: Apply fungicides during key infection periods.\n
    Removing Alternate Hosts: Eliminate nearby juniper or cedar trees if possible.\n
    Sanitation: Remove infected leaves and fruit to reduce spore production.\n
    Plant Resistant Apple Varieties: Choose apple varieties less susceptible to Cedar Apple Rust.
'''
}, 2: {
    'name': 'Apple Scab',
    'cause': '''\n
    Fungal Pathogen: Venturia inaequalis.\n
    Moisture and Humidity: Thrives in warm, wet conditions.\n
    Lack of Airflow: Dense foliage creates a humid environment, favoring fungal growth.\n
    Infected Debris: Fallen leaves and fruit from the previous season harbor spores, contributing to the disease cycle.
''',
    'prevn': '''\n
    Fungicide Applications: Apply fungicides in early spring before bud break and at regular intervals.\n
    Sanitation: Remove fallen leaves and infected debris to reduce overwintering spores.\n
    Proper Pruning: Improve air circulation by pruning for better ventilation.\n
    Resistant Varieties: Choose apple tree varieties less susceptible to Apple Scab.
'''
}
, 3: {
    'name': 'Apple Healthy',
    'cause': 'Your Crop is Safe',
    'prevn': 'Nothing to Prevent'
}
}

citrus = {
    0: {
        'name': 'Citrus Greening',
        'cause': '''\n
Bacterial Pathogen (Candidatus Liberibacter spp.): The primary cause is the bacterium Candidatus Liberibacter spp.\n
Insect Vectors (Citrus Psyllids): These insects transmit the bacteria when feeding on citrus trees.\n
Long Incubation Period: Trees can be infected for months before showing symptoms.\n
Impact on Vascular System: The bacterium disrupts the tree's vascular system, affecting nutrient distribution.
''',
        'prevn': '''\n
Use Disease-Free Plants: Start with healthy, disease-free citrus trees.\n
Insect Management: Control citrus psyllids, the insect vectors.\n
Sanitation: Remove and destroy infected trees and control weeds.\n
Nutrition and Care: Provide proper nutrition and care to maintain tree health.

''',
    },
    1: {
        'name': 'Citrus Healthy',
        'cause': 'Your crop is safe',
        'prevn': 'No need of Prevention'
    },
    2: {
        'name': 'Citrus Canker',
        'cause': '''\n
Bacterial Pathogen (Xanthomonas citri subsp. citri): The primary cause is the bacterium Xanthomonas citri subsp. citri.\n
Rain and Wind: Spread through rain splash and wind-blown rain.\n
Wounds or Injuries: Bacteria enter through natural openings or wounds.\n
Insect Vectors: Certain insects can transmit the bacterium to healthy plants.
''',
        'prevn': '''\n
Pruning and Sanitation: Remove and destroy infected plant material.\n
Copper Sprays: Apply copper-based fungicides as a preventive measure.\n
Quarantine Measures: Restrict movement of potentially infected plants and fruit.\n
Resistant Varieties: Consider planting citrus varieties less susceptible to canker.

'''
    },
    3: {
        'name': 'Citrus Black Spot',
        'cause': '''\n
Fungal Pathogen (Phyllosticta citricarpa): The primary cause is the fungus Phyllosticta citricarpa.\n
Moisture and Humidity: Thrives in wet, humid conditions.\n
Infected Debris: Spores overwinter on fallen leaves and fruit.\n
Warm Temperatures: Spreads most rapidly in warm, rainy weather.
''',
        'prevn': '''\n
Fungicide Applications: Apply fungicides during critical growth stages.\n
Sanitation: Remove and destroy infected leaves and fruit.\n
Pruning for Airflow: Improve ventilation to reduce humidity.\n
Resistant Varieties: Consider planting citrus varieties less susceptible to black spot.
'''
    }
}

bell_pepper = {
    0: {
        'name': 'Bell Pepper Healthy',
        'cause': 'Your Crop is Safe',
        'prevn': 'Nothing to Prevent',
    },
    1: {
        'name': 'Bell Pepper Bacterial Spot',
        'cause': '''\n
Bacterial Pathogen (Xanthomonas campestris pv. vesicatoria): The primary cause is the bacterium Xanthomonas campestris pv. vesicatoria.\n
Moisture and Humidity: Wet and humid conditions promote bacterial growth and infection.\n
Planting in Infected Soil: Planting in soil with a history of bacterial spot can introduce the pathogen to the crop.\n
Wounding or Injuries: Wounds on the plant can serve as entry points for the bacteria, allowing infection to occur.
''',
        'prevn': '''\n
Crop Rotation: Avoid planting bell peppers in the same location year after year.\n
Sanitation: Remove and destroy infected plant material to prevent the spread of bacteria.\n
Avoid Overhead Irrigation: Use drip irrigation or soaker hoses to keep foliage dry.\n
Resistant Varieties: Select bell pepper varieties that are bred for resistance to bacterial spot.
''',
    }
}

grape = {
    0:{
      
    },
    1: {
        'name': 'Grape Black Rot',
        'cause': '''\nFungal Pathogen (Guignardia bidwellii): The primary cause is the fungus Guignardia bidwellii.\n
Warm, Wet Conditions: Thrives in warm, humid weather.\n
Overwintering on Infected Debris: Survival on fallen leaves and fruit from previous seasons.\n
Rain and Dew: Moisture on foliage aids in spore dispersal and infection.''',
        'prevn': '''\nFungicide Applications: Apply fungicides during critical growth stages.\n
Sanitation: Remove and destroy infected plant material.\n
Pruning for Airflow: Improve ventilation to reduce humidity.\n
Timely Harvest: Harvest grapes promptly to prevent overripening and infection.''',
    },
    2: {
        'name': 'Grape Healthy',
        'cause': 'Your Crop is Safe',
        'prevn': 'Nothing to Prevent',
    },
    3: {
        'name': 'Grape Isariopsis Leaf Spot',
        'cause': '''\nFungal Pathogen (Isariopsis griseola): The primary cause is the fungus Isariopsis griseola.\n
Warm, Humid Conditions: Thrives in warm, humid weather.\n
Overwintering on Infected Debris: Survival on fallen leaves and fruit from previous seasons.\n
Rain and Dew: Moisture on foliage aids in spore dispersal and infection.''',
        'prevn': '''\nFungicide Applications: Apply fungicides during critical growth stages.\n
Sanitation: Remove and destroy infected plant material.\n
Pruning for Airflow: Improve ventilation to reduce humidity.\n
Resistant Varieties: Consider planting grape varieties less susceptible to Isariopsis Leaf Spot.''',
    }
}

corn = {
    0: {
        'name': 'Corn Common Rust',
        'cause': '''\nFungal Pathogen (Puccinia sorghi): The primary cause is the fungus Puccinia sorghi.\n
Moderate Temperatures and Humidity: Ideal conditions for spore germination and infection.\n
Overwintering Spores: Survival on volunteer corn and host plants from previous seasons.\n
Wet Conditions: Rain and dew facilitate spore dispersal and infection.''',
        'prevn':'''\nPlant Resistant Varieties: Choose corn varieties with resistance to common rust.\n
Crop Rotation: Avoid planting corn in the same location year after year.\n
Fungicide Treatments: Apply fungicides if the risk of infection is high.\n
Timely Planting: Planting early can help avoid peak infection periods.''',
    },
    1: {
        'name': 'Corn Gray Leaf Spot',
        'cause': '''\nFungal Pathogen (Cercospora zeae-maydis): The primary cause is the fungus Cercospora zeae-maydis.\n
Warm, Humid Conditions: Ideal environment for spore germination and disease development.\n
Overwintering Residues: Survival on infected crop debris from previous seasons.\n
Moisture on Foliage: Rain and dew provide a medium for spore dispersal and infection.''',
        'prevn': '''\nCrop Rotation: Avoid planting corn in the same field consecutively.\n
Fungicide Applications: Apply fungicides if gray leaf spot is a known issue.\n
Resistant Varieties: Choose corn varieties with resistance to gray leaf spot.\n
Timely Planting: Planting early can help avoid peak infection periods.''',
    },
    2:{
      'name': 'Corn Healthy',
       'cause': 'Your Crop is Safe',
       'prevn': 'Nothing to Prevent',
    },
    3: {
        'name': 'Corn Northern Leaf Blight',
        'cause': '''\nFungal Pathogen (Exserohilum turcicum): The primary cause is the fungus Exserohilum turcicum.\n
Warm, Humid Conditions: Ideal environment for spore germination and disease development.\n
Overwintering Residues: Survival on infected crop debris from previous seasons.\n
Rain and Dew: Moisture on foliage aids in spore dispersal and infection.''',
        'prevn': '''\nResistant Varieties: Select corn varieties with genetic resistance to northern leaf blight.\n
Crop Rotation: Avoid planting corn in the same field consecutively.\n
Fungicide Applications: Apply fungicides if northern leaf blight is a known issue.\n
Sanitation: Remove and destroy infected crop residues.
''',
    }
}

disease = {
    'Apple': apple,
    'Citrus' : citrus,
    'BellPepper': bell_pepper,
    'Grape': grape,
    'Corn': corn
}

# Load the selected deep learning model based on crop selection
@st.cache_data()
def load_model(crop):
    model_path = f"models/{crop.lower()}.h5"
    model = keras.models.load_model(model_path)
    return model

# Resize and preprocess the uploaded image
def preprocess_image(image):
    image = image.resize((224, 224))
    
    image = np.expand_dims(image, axis=0)
    return image

# Define the list of crop options
crop_options = ["Apple", "BellPepper", "Citrus", "Grape", "Corn"]

# Custom CSS for styling
custom_css = """
<style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    .st-eb {
        font-size: 24px;
        color: #0078C1;
    }
    .st-at {
        font-size: 18px;
    }
    .st-bt {
        font-size: 16px;
        color: #666;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Page title and description
st.title("Plant Disease Classification App")
st.markdown("This app can identify plant diseases and provide information about their causes and prevention.")

# Crop selection dropdown
selected_crop = st.selectbox("Select the Crop", crop_options)

# Image uploader
uploaded_image = st.file_uploader("Upload an image of the plant", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Load the selected model
    model = load_model(selected_crop)

    # Preprocess the uploaded image
    
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image")
    processed_image = preprocess_image(image)

    # Make a prediction
    prediction = model.predict(processed_image)
    predicted_class = np.argmax(prediction)

    # Display the prediction result
    st.subheader("Prediction:")
    st.markdown(f"<div class='st-eb'>Class:</div> <div class='st-bt'>{disease[selected_crop][predicted_class]['name']}</div>", unsafe_allow_html=True)
    # You can map the predicted class to the actual disease, cause, and prevention information.

    # Display disease information based on the predicted class
    st.subheader("Disease Information:")
    st.markdown(f"<div class='st-eb'>Cause:</div> <div class='st-at'>{disease[selected_crop][predicted_class]['cause']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='st-eb'>Prevention:</div> <div class='st-at'>{disease[selected_crop][predicted_class]['prevn']}</div>", unsafe_allow_html=True)
    
    # Repeat similar blocks for other crop-specific diseases.
