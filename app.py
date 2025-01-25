import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Define the PredictionPipeline class (must be available for unpickling)
class PredictionPipeline:
    def __init__(self):
        self.scaler = None
        self.model = None

    def train(self, X, y):
        from sklearn.preprocessing import StandardScaler
        from sklearn.linear_model import LinearRegression
        
        # Initialize scaler and model
        self.scaler = StandardScaler()
        self.model = LinearRegression()
        
        # Scale the training data
        X_scaled = self.scaler.fit_transform(X)
        # Train the model
        self.model.fit(X_scaled, y)

    def predict(self, X):
        # Scale the input features
        X_scaled = self.scaler.transform(X)
        # Predict using the trained model
        return self.model.predict(X_scaled)

# Load the trained pipeline
pipeline = joblib.load('prediction_pipeline.pkl')

# Load images
banner_image = Image.open("banner.png")  
footer_image = Image.open("footer.png")  

# Title and Banner
st.image(banner_image, use_container_width=True)  # Updated to use_container_width
st.title("🎓 JAMB Candidates Prediction App")
st.markdown(
    """
    ### Predict the Number of Candidates for the Computer Science Department
    Welcome! This tool helps predict the number of candidates seeking admission into the Computer Science Department at UNN.
    Simply input the details below and click **Predict** to see the results! 🎉
    """
)

# Input Section with Styled Features
st.sidebar.header("Enter Input Details")
st.sidebar.markdown("🔽 **Fill in the details below:**")

total_applicants = st.sidebar.number_input("Total Number of Applicants", min_value=0, value=25000, step=100, help="Enter the total number of applicants for UNN.")
first_choice_applicants = st.sidebar.number_input("First Choice Applicants", min_value=0, value=5000, step=100, help="Number of applicants who selected Computer Science as their first choice.")
cut_off_mark = st.sidebar.slider("Cut Off Mark", min_value=180, max_value=400, value=220, step=1, help="Enter the cut-off mark for the department.")
quota = st.sidebar.number_input("Quota", min_value=0, value=150, step=1, help="The maximum number of slots available for Computer Science.")
state_quota = st.sidebar.number_input("State Quota Applicants", min_value=0, value=8000, step=100, help="Number of applicants from the university's home state.")
start_year = st.sidebar.slider("Start Year", min_value=1983, max_value=2100, value=2025, step=1, help="The academic year for which you want to predict.")

# Predict Button
if st.sidebar.button("Predict 🚀"):
    # Prepare input data
    input_data = pd.DataFrame({
        'Total_Applicants': [total_applicants],
        'First_Choice_Applicants': [first_choice_applicants],
        'Cut_Off_Mark': [cut_off_mark],
        'Quota': [quota],
        'State_Quota': [state_quota],
        'Start_Year': [start_year]
    })

    # Make prediction
    prediction = pipeline.predict(input_data)

    # Display Prediction
    st.success(f"📊 **Predicted Number of Candidates**: {round(prediction[0], 2)}")
    st.balloons()  # Fun balloons animation
else:
    st.info("👈 Enter details in the sidebar and click **Predict** to start.")

# Footer Section with Image
st.markdown("---")
st.image(footer_image, use_container_width=True)  # Updated to use_container_width
st.write("### Powered by AI 🧠 | Transforming Predictions into Insights")
