import streamlit as st
import pandas as pd
import pickle
# Load the trained model
model = pickle.load(open('house_prediction.pkl', 'rb'))
df = pd.read_csv('house_predictions.csv')

# Define the Streamlit app

def main():
    st.title("House Price Prediction")
    # Input fields for user to enter house features
    col1, col2 = st.columns(2)
    location = col1.selectbox("Location", df['location'].unique())
    total_sqft = col1.number_input("Total Square Feet", min_value=300, max_value=10000, step=10)
    bhk = col2.number_input("Number of Bedrooms (BHK)", min_value=1, max_value=10, step=1)
    balcony = col2.number_input("Number of Balconies", min_value=0, max_value=5, step=1)
    bath = col2.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1)
    
    # Predict button
    if st.button("Predict Price"):
        input_data = pd.DataFrame({
            'location': [location],
            'total_sqft': [total_sqft],
            'bath': [bath],
            'balcony': [balcony],
            'bhk': [bhk]
        })
        predicted_price = model.predict(input_data)
        st.success(f"Predicted House Price: {(predicted_price[0]*100000):.2f} INR")
if __name__ == "__main__":
    main()