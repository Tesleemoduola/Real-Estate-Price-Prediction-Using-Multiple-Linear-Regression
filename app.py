import streamlit as st # type: ignore
import pandas as pd # type: ignore

# Load the specific worksheet for Price Calculation
data = pd.read_excel(
    'real_estate_price_prediction.xlsx',
    sheet_name='Price Calculator',
    skiprows=7,
    engine='openpyxl'
)



# Set up the title
st.title("Real Estate Price Prediction")

# Display the price calculation formula
st.write("""
    ## Price Calculation Formula:
    **199968.14 + (12544.61 * Bed) + (3125.04 * Bath) + (59733.98 * Acre_Lot) + (72.41 * House_Size) + 
    (20233.54 * Garage) + (17976.29 * Swimming_Pool) + (-3962.18 * House_Age) + (1025.73 * Safety_Index)**
""")


st.markdown(r"""
    <style>
    .header {
        font-size: 30px;
        font-weight: bold;
        color: #8d0801;
        text-align: center;
        margin-bottom: 20px;
        background-image: url(r"C:\Users\bashy\Downloads\Streamlit Deployment\image\b1.jpg"); 
        background-size: cover;
        padding: 50px;
    }
        
    .social-icons img {
        width: 30px;
        height: auto;
        margin: 0 10px;
        cursor: pointer;
    }
    </style>
    <div class="header">
        House Price Predictor
    </div>
    """, unsafe_allow_html=True)

# Add a logo
st.image(r"C:\Users\oduol\OneDrive\Streamlit Deployment\image\housing.jpg", width=700)


# Input fields for the variables
col1, col2 = st.columns(2)

with col1:
    bed = st.number_input("Number of Bedrooms", min_value=0, value=2)
    bath = st.number_input("Number of Bathrooms", min_value=0, value=2)
    acre_lot = st.number_input("Acre Lot", min_value=0.0, value=1.0)
    house_size = st.number_input("House Size (sq ft)", min_value=0.0, value=1500.0)

with col2:
    garage = st.number_input("Number of Garages", min_value=0, value=2)
    swimming_pool = st.number_input("Swimming Pool (Yes=1, No=0)", min_value=0, max_value=1, value=1)
    house_age = st.number_input("House Age (years)", min_value=0, value=1)
    safety_index = st.number_input("Safety Index", min_value=0, value=90)

# Extract coefficients from the Excel worksheet
intercept = data.loc[data['Variable'] == 'Intercept', 'Coefficient'].values[0]
bed_coef = data.loc[data['Variable'] == 'Bed', 'Coefficient'].values[0]
bath_coef = data.loc[data['Variable'] == 'Bath', 'Coefficient'].values[0]
acre_lot_coef = data.loc[data['Variable'] == 'Acre_Lot', 'Coefficient'].values[0]
house_size_coef = data.loc[data['Variable'] == 'House_Size', 'Coefficient'].values[0]
garage_coef = data.loc[data['Variable'] == 'Garage', 'Coefficient'].values[0]
swimming_pool_coef = data.loc[data['Variable'] == 'Swimming_Pool', 'Coefficient'].values[0]
house_age_coef = data.loc[data['Variable'] == 'House_Age', 'Coefficient'].values[0]
safety_index_coef = data.loc[data['Variable'] == 'Safety_Index', 'Coefficient'].values[0]

# Calculate the predicted price
predicted_price = (intercept +
                   (bed_coef * bed) +
                   (bath_coef * bath) +
                   (acre_lot_coef * acre_lot) +
                   (house_size_coef * house_size) +
                   (garage_coef * garage) +
                   (swimming_pool_coef * swimming_pool) +
                   (house_age_coef * house_age) +
                   (safety_index_coef * safety_index))

# Display the predicted price
st.write("## Predicted Price:")
st.write(f"${predicted_price:,.2f}")


# Custom footer with social media links
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        padding: 10px;
    }
    .footer a {
        color: white;
        text-decoration: none;
        margin: 0 10px;
    }
    </style>
    <div class="footer">
        Developed by Tesleem Oduola - ©2024
        <br>
        <a href="https://x.com/oduolates" target="_blank">Twitter</a>
        <a href="https://www.linkedin.com/in/tesleemaderemioduola/" target="_blank">LinkedIn</a>
        <a href="https://github.com/Tesleemoduola" target="_blank">GitHub</a>
    </div>
    """, unsafe_allow_html=True)