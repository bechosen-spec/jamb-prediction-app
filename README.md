# 🎓 JAMB Candidates Prediction App

This **Streamlit web app** predicts the number of candidates seeking admission into the Computer Science Department at the University of Nigeria, Nsukka (UNN). It uses a machine learning model trained with historical data and provides an interactive interface for users to input key details and get predictions.

---

## 🚀 Features
- **User-Friendly Interface**:
  - Interactive sidebar for data input.
  - Instant predictions with animations and styled output.

- **Key Inputs**:
  - Total number of applicants.
  - First-choice applicants for Computer Science.
  - Department cut-off mark.
  - Admission quota and state quota.

- **Dynamic Visuals**:
  - Engaging banner and footer images for a polished look.
  - Balloon animation on successful prediction.

---

## 📂 Project Structure
```
jamb-prediction-app/
├── app.py                  # Main Streamlit app script
├── pipeline.py             # Defines the PredictionPipeline class (optional if applicable)
├── prediction_pipeline.pkl # Pretrained machine learning pipeline
├── banner.png              # Banner image
├── footer.png              # Footer image
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation (this file)
```

---

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package installer)

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/jamb-prediction-app.git
   cd jamb-prediction-app
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**:
   ```bash
   streamlit run app.py
   ```

5. **Access the App**:
   - Open the link provided by Streamlit (e.g., `http://localhost:8501`) in your browser.

---

## 🧠 How It Works
1. **Input Fields**:
   - Enter data such as total applicants, first-choice applicants, and the department's cut-off mark in the sidebar.

2. **Prediction**:
   - Click the **Predict** button to see the predicted number of candidates.

3. **Output**:
   - The app displays the predicted number of candidates with a success message and an engaging balloon animation.

---

## 📋 Example Input and Output

### Example Input:
| Feature                 | Value      |
|-------------------------|------------|
| Total Applicants        | 25,000     |
| First Choice Applicants | 5,000      |
| Cut Off Mark            | 220        |
| Quota                   | 150        |
| State Quota             | 8,000      |
| Start Year              | 2025       |

### Example Output:
```
📊 Predicted Number of Candidates: 5234.67
```

---

## 🌐 Deployment
This app can be deployed on **Streamlit Cloud** or any hosting platform supporting Python web apps.

### Deploy on Streamlit Cloud:
1. Push your code to a GitHub repository.
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud).
3. Select your repository and deploy the app.

---

## 🔧 Tools and Libraries
- **Streamlit**: For building the web interface.
- **Pandas**: For data manipulation.
- **Scikit-Learn**: For machine learning.
- **Pillow**: For image handling.
- **Joblib**: For saving and loading the trained pipeline.

---

## 🖼️ Screenshots

### Home Page:
![Banner](banner.png)

### Prediction Output:
![Footer](footer.png)

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📝 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 💬 Contact
For questions or suggestions:
- **Email**: bonifacechosen100@gmail.com
- **GitHub**: [Your GitHub Profile](https://github.com/your-username)

