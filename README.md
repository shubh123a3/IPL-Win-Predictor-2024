

# IPL Win Predictor 2024



https://github.com/user-attachments/assets/614fbb5a-7e0d-4e63-be11-e3e91a85c237

his repository contains the source code and data for predicting the probability of the winner of an IPL match using machine learning models.

## Overview

The IPL Win Predictor is designed to analyze historical match data and predict the outcome of future IPL matches. The project involves data preprocessing, feature engineering, model training, and evaluation. A Streamlit app is used for the front-end to interact with the model.

## Project Structure

- `IPl winner Predictor Notebook.ipynb`: Jupyter Notebook containing the data analysis, preprocessing, model training, and evaluation steps.
- `app.py`: Streamlit app for the user interface to input match details and get predictions.
- `deliveries.csv`: Dataset containing ball-by-ball details of IPL matches.
- `matches.csv`: Dataset containing details of IPL matches.
- `model_new.zip`: Saved trained model for prediction.

## Steps Performed

### 1. Data Collection
- Imported data from `deliveries.csv` and `matches.csv`.
- Merged and cleaned the datasets.

### 2. Data Preprocessing
- Handled missing values.
- Encoded categorical variables.
- Extracted useful features for prediction.

### 3. Feature Engineering
- Created new features like total runs, wickets, overs, etc.
- Normalized and scaled the features for better model performance.

### 4. Model Training
- Split the data into training and testing sets.
- Trained various machine learning models (e.g., Logistic Regression, Random Forest, etc.).
- Evaluated models using metrics like accuracy, precision, recall, and F1-score.

### 5. Model Evaluation
- Selected the best model based on performance metrics.
- Tuned hyperparameters for the best model.

### 6. Deployment
- Created a Streamlit app (`app.py`) for easy interaction.
- Loaded the trained model in the app to predict match outcomes based on user inputs.

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shubh123a3/IPL-Win-Predictor-2024.git
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## Future Enhancements
- Integrate live data for real-time predictions.
- Improve model accuracy by including more features.
- Deploy the app on a cloud platform for wider accessibility.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

