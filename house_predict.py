import streamlit as st
import pandas as pd
import pickle
# Load the trained model
model = pickle.load(open('house_prediction.pkl', 'rb'))
df = pd.read_csv('house_predictions.csv')

page_bg_img = """

<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.freepik.com%2Fphotos-gratuite%2Fabstrait-numerique-grille-fond-noir_53876-97647.jpg%3Fsemt%3Dais_hybrid%26w%3D740&f=1&nofb=1&ipt=3a551da015306bbddd270ba2ae800e19c0cd7a495531591dc2fac4df03aeca4c");
    background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

with st.sidebar:
    st.header("🏠 House Price Prediction")

    with st.expander("About this app"):
        st.write("""
                This House Price Prediction app uses Machine Learning 
                to predict the price of a house based on its features.
                 
                👉 Model: Random Forest Regression""")

    with st.expander("Limitations"):
        st.write("* Predictions may not be 100% accurate  \n\n* Model is still under improvement ")


# Define the Streamlit app
def main():
    st.title("🏠 House Price Prediction")
    # Input fields for user to enter house features
    col1, col2 = st.columns(2)
    location = col1.selectbox("Location", df['location'].unique())
    total_sqft = col1.number_input("Total Square Feet", min_value=300, max_value=10000, step=10)
    bhk = col2.number_input("Number of Bedrooms (BHK)", min_value=1, max_value=10, step=1)
    balcony = col2.number_input("Number of Balconies", min_value=0, max_value=5, step=1)
    bath = col2.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1)
    
    col1, col2 = st.columns([1,2])
    ratio=col1.select_slider("Selecte Currency", options=["INR", "USD"])

    # Predict button
    if col1.button("Predict Price"):
        input_data = pd.DataFrame({
            'location': [location],
            'total_sqft': [total_sqft],
            'bath': [bath],
            'balcony': [balcony],
            'bhk': [bhk]
        })
        predicted_price = model.predict(input_data)
        
        if ratio == "USD":
            st.subheader("House Price in USD:")
            st.success(f" {(predicted_price[0]*1044.28):.2f} USD")
        else:
            st.subheader("House Price in INR:")
            st.success(f" {(predicted_price[0]*100000):.2f} INR")

if __name__ == "__main__":
    main()