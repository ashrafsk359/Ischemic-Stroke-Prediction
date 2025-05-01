# 🧠 Ischemic Stroke Prediction

A machine learning project aimed at predicting the likelihood of ischemic strokes based on patient health metrics and lifestyle factors.

## 📌 Overview

This project utilizes a Random Forest classifier to predict the occurrence of ischemic strokes. It encompasses data preprocessing, model training, evaluation, and deployment through a Flask web application.

## 👥 Team Members

- S.V. Teja Reddy
- SK. Ashraf Sulthan
- S. Balachandra
- S. Srinivasulu

## 📂 Project Structure

```
ISCHEMIC_STROKE/
├── app.py
├── brain-stroke-prediction-decisiontree.ipynb
├── full_data.csv
├── rfc.pkl
├── Ischemic Stroke.pdf
├── README.md
├── images/
├── static/
└── template/
```

- **app.py**: Flask application script to run the web interface.
- **brain-stroke-prediction-decisiontree.ipynb**: Jupyter Notebook detailing data analysis and model training.
- **full_data.csv**: Dataset used for training and evaluation.
- **rfc.pkl**: Serialized Random Forest model.
- **Ischemic Stroke.pdf**: Comprehensive project report.
- **images/**: Contains visual assets for the application.
- **static/**: Holds static files like CSS and JavaScript.
- **template/**: Contains HTML templates for rendering web pages.

## 🧪 Dataset

- **Source**: [Brain Stroke Dataset on Kaggle](https://www.kaggle.com/datasets/jillanisofttech/brain-stroke-dataset)
- **Features**:
  - Age
  - Gender
  - Hypertension
  - Heart Disease
  - Smoking Status
  - BMI
  - Average Glucose Level
  - Stroke (Target Variable)

## 🚀 Getting Started

### Prerequisites

- Python 3.9
- pip (Python package installer)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ashrafsk359/Ischemic-Stroke-Prediction.git
   cd Ischemic-Stroke-Prediction/ISCHEMIC_STROKE
   ```

2. **Install Dependencies**:
   It's recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the Web Interface**:
   Open your browser and navigate to `http://localhost:5000` to use the stroke prediction tool.

## 📊 Model Details

- **Algorithm**: Random Forest Classifier
- **Evaluation Metrics**:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
- **Handling Imbalanced Data**: Techniques like SMOTE were employed to address class imbalance.

## 📈 Results

The Random Forest model achieved high accuracy and reliability in predicting ischemic strokes. Detailed performance metrics and visualizations are available in the Jupyter Notebook.

## 📄 Report

For an in-depth understanding of the project's methodology, data analysis, and findings, refer to the [Ischemic Stroke.pdf](./Ischemic%20Stroke.pdf) document included in the repository.

## 🤝 Acknowledgments

- **Dataset**: [Jillani Soft Tech on Kaggle](https://www.kaggle.com/datasets/jillanisofttech/brain-stroke-dataset)
- **Inspiration**: The project draws inspiration from various stroke prediction studies and machine learning applications in healthcare.

## 📬 Contact

For any inquiries or collaborations, please reach out to the respective team members through their GitHub profiles.
