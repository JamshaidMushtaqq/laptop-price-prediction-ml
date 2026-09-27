# 💻 Laptop Price Prediction using Machine Learning

A Machine Learning project that predicts the estimated price of a laptop based on its specifications such as brand, RAM, CPU, GPU, storage, screen size, resolution, operating system, and other features.

The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and a Streamlit web application for making predictions.

## 📌 Project Overview

The main objective of this project is to build a Machine Learning model that can estimate laptop prices from laptop specifications.

The complete workflow is:

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Data Preprocessing
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Serialization
     ↓
Streamlit Web App
     ↓
Laptop Price Prediction
```

## 📂 Project Structure

```text
laptop-price-prediction-ml/
│
├── app.py
├── laptop_data.csv
├── laptop_price_predictor.ipynb
├── pipe.pkl
├── df.pkl
├── requirements.txt
└── README.md
```

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Streamlit
* Pickle
* Jupyter Notebook

## 📊 Dataset

The dataset contains laptop specifications and their corresponding prices.

Important features include:

* Company
* Laptop Type
* Screen Size
* Screen Resolution
* CPU
* RAM
* Storage
* GPU
* Operating System
* Weight
* Price

The target variable is:

```text
Price
```

## 🔧 Data Preprocessing

Several preprocessing and feature engineering techniques were applied.

### Data Cleaning

* Removed unnecessary columns
* Removed duplicate/unwanted records
* Converted RAM from values such as `8GB` to numerical values
* Converted weight from values such as `1.37kg` to numerical values

### Feature Engineering

New features were created from the existing data:

* Touchscreen
* IPS Display
* PPI (Pixels Per Inch)
* CPU Brand
* GPU Brand
* HDD Storage
* SSD Storage
* Simplified Operating System categories

### Categorical Encoding

Categorical variables were converted into numerical features using:

```text
OneHotEncoder
```

### Target Transformation

Because laptop prices are skewed, the target price was transformed using:

```python
np.log(Price)
```

During prediction, the transformation was reversed using:

```python
np.exp(prediction)
```

## 🤖 Machine Learning Models

Multiple regression algorithms were tested, including:

* Linear Regression
* Ridge Regression
* Lasso Regression
* KNN Regressor
* Decision Tree Regressor
* Support Vector Regression
* Random Forest Regressor
* Extra Trees Regressor
* AdaBoost Regressor
* Gradient Boosting Regressor
* XGBoost Regressor
* Voting Regressor
* Stacking Regressor

The models were evaluated using:

* R² Score
* Mean Absolute Error (MAE)

## 📈 Model Evaluation

The notebook contains the evaluation results of the different models.

The best-performing models in the recorded experiments were ensemble-based regression approaches, with the Voting Regressor achieving an R² score of approximately `0.89` on the test split.

The final serialized pipeline used by the application is stored in:

```text
pipe.pkl
```

> Note: The reported metrics are from the existing notebook run and may vary if the model is retrained with a different environment, random split, or preprocessing configuration.

## 🌐 Streamlit Web Application

The project includes a Streamlit application that allows users to enter laptop specifications and receive an estimated price.

The application takes inputs such as:

* Brand
* Laptop Type
* RAM
* Weight
* Touchscreen
* IPS Display
* Screen Size
* Screen Resolution
* CPU
* HDD
* SSD
* GPU
* Operating System

After clicking **Predict Price**, the trained Machine Learning pipeline generates an estimated laptop price.

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/laptop-price-prediction-ml.git
```

### 2. Open the project folder

```bash
cd laptop-price-prediction-ml
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

On Windows:

```powershell
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will normally open at:

```text
http://localhost:8501
```

## 📓 Jupyter Notebook

The complete Machine Learning workflow is available in:

```text
laptop_price_predictor.ipynb
```

The notebook covers:

1. Data loading
2. Data inspection
3. Data cleaning
4. Exploratory Data Analysis
5. Feature engineering
6. Train-test split
7. Preprocessing
8. Model training
9. Model evaluation
10. Final model serialization

## 💾 Saved Model

The trained pipeline is stored in:

```text
pipe.pkl
```

The processed dataframe used by the application is stored in:

```text
df.pkl
```

These files allow the Streamlit application to load the trained model without retraining it every time.

## 🎯 Future Improvements

Possible improvements include:

* Hyperparameter tuning
* Cross-validation
* More extensive feature engineering
* Testing on a larger and newer dataset
* Improving the Streamlit UI
* Adding model performance visualizations
* Deploying the application online
* Adding prediction confidence or uncertainty information

## 👨‍💻 Author

**Your Name**

GitHub: `https://github.com/YOUR-USERNAME`

## 📄 License

This project is intended for educational and demonstration purposes.
 
