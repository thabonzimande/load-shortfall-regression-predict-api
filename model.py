"""

    Helper functions for the pretrained model to be used within our API.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.

    Importantly, you will need to modify this file by adding
    your own data preprocessing steps within the `_preprocess_data()`
    function.
    ----------------------------------------------------------------------

    Description: This file contains several functions used to abstract aspects
    of model interaction within the API. This includes loading a model from
    file, data preprocessing, and model prediction.  

"""

# Helper Dependencies
import numpy as np
import pandas as pd
import pickle
import json

def _preprocess_data(data):
    """Private helper function to preprocess data for model prediction.

    NB: If you have utilised feature engineering/selection in order to create
    your final model you will need to define the code here.


    Parameters
    ----------
    data : str
        The data payload received within POST requests sent to our API.

    Returns
    -------
    Pandas DataFrame : <class 'pandas.core.frame.DataFrame'>
        The preprocessed data, ready to be used our model for prediction.
    """
    # Convert the json string to a python dictionary object
    feature_vector_dict = json.loads(data)
    # Load the dictionary as a Pandas DataFrame.
    feature_vector_df = pd.DataFrame.from_dict([feature_vector_dict])

    # ---------------------------------------------------------------
    # NOTE: You will need to swap the lines below for your own data
    # preprocessing methods.
    #
    # The code below is for demonstration purposes only. You will not
    # receive marks for submitting this code in an unchanged state.
    # ---------------------------------------------------------------

    # ----------- Replace this code with your own preprocessing steps --------
    # Regression Predict Student Solution

© Explore Data Science Academy

---
### Honour Code

I {**YOUR NAME, YOUR SURNAME**}, confirm - by submitting this document - that the solutions in this notebook are a result of my own work and that I abide by the [EDSA honour code](https://drive.google.com/file/d/1QDCjGZJ8-FmJE3bZdIQNwnJyQKPhHZBn/view?usp=sharing).

Non-compliance with the honour code constitutes a material breach of contract.

### Predict Overview: Spain Electricity Shortfall Challenge

The government of Spain is considering an expansion of it's renewable energy resource infrastructure investments. As such, they require information on the trends and patterns of the countries renewable sources and fossil fuel energy generation. Your company has been awarded the contract to:

- 1. analyse the supplied data;
- 2. identify potential errors in the data and clean the existing data set;
- 3. determine if additional features can be added to enrich the data set;
- 4. build a model that is capable of forecasting the three hourly demand shortfalls;
- 5. evaluate the accuracy of the best machine learning model;
- 6. determine what features were most important in the model’s prediction decision, and
- 7. explain the inner working of the model to a non-technical audience.

Formally the problem statement was given to you, the senior data scientist, by your manager via email reads as follow:

> In this project you are tasked to model the shortfall between the energy generated by means of fossil fuels and various renewable sources - for the country of Spain. The daily shortfall, which will be referred to as the target variable, will be modelled as a function of various city-specific weather features such as `pressure`, `wind speed`, `humidity`, etc. As with all data science projects, the provided features are rarely adequate predictors of the target variable. As such, you are required to perform feature engineering to ensure that you will be able to accurately model Spain's three hourly shortfalls.
 
On top of this, she has provided you with a starter notebook containing vague explanations of what the main outcomes are. 

<a id="cont"></a>

## Table of Contents

<a href=#one>1. Importing Packages</a>

<a href=#two>2. Loading Data</a>

<a href=#three>3. Exploratory Data Analysis (EDA)</a>

<a href=#four>4. Data Engineering</a>

<a href=#five>5. Modeling</a>

<a href=#six>6. Model Performance</a>

<a href=#seven>7. Model Explanations</a>

 <a id="one"></a>
## 1. Importing Packages
<a href=#cont>Back to Table of Contents</a>

---
    
| ⚡ Description: Importing Packages ⚡ |
| :--------------------------- |
| In this section you are required to import, and briefly discuss, the libraries that will be used throughout your analysis and modelling. |

---

# Libraries for data loading, data manipulation and data visulisation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import plotly.express as px
from statsmodels.graphics.correlation import plot_corr

# Libraries for data preparation and model building
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.metrics import mean_squared_error as MSE
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import math
from statsmodels.graphics.correlation import plot_corr
import statsmodels.formula.api as sm
from statsmodels.formula.api import ols
from scipy.stats import pearsonr
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
# Setting global constants to ensure notebook results are reproducible
#PARAMETER_CONSTANT = ###

<a id="two"></a>
## 2. Loading the Data
<a class="anchor" id="1.1"></a>
<a href=#cont>Back to Table of Contents</a>

---
    
| ⚡ Description: Loading the data ⚡ |
| :--------------------------- |
| In this section you are required to load the data from the `df_train` file into a DataFrame. |

---

# Loading the Train and Test datasets

#load the train data
train_data = pd.read_csv('df_train.csv')

#load the test data
test_data = pd.read_csv("df_test.csv")

Checking that they both were loaded without error

#checking that the train data is properly loaded
train_data.head()

#checking that the test data is properly loaded
test_data.head()

# <a id="three"></a>
## 3. Exploratory Data Analysis (EDA)
<a class="anchor" id="1.1"></a>
<a href=#cont>Back to Table of Contents</a>

---
    
| ⚡ Description: Exploratory data analysis ⚡ |
| :--------------------------- |
| In this section, you are required to perform an in-depth analysis of all the variables in the DataFrame. |

---


## Why is Exploratory Data Analysis so important?


Exploratory Data Analysis (EDA) helps us to understand our data without making any assumptions. EDA is a vital component before we continue with the modelling phase as it provides context and guidance on the course of action to take when developing the appropriate model. It will also assist in interpreting the results correctly. Without doing EDA you will not understand your data fully.

Non-graphical EDA:
- Involves calculations of summary/descriptive statistics

Graphical EDA:
- This type of analysis will contain data visualisations.

# Looking at basic summary/descriptive statistics:

# look at data statistics

## Basic Info

# We look at the info on the data
train_data.info()

- The columns time, Valencia_wind_deg, and Seville_pressure are non-numeric values and willl need to be converted during the feature engineering stage.


#looking at the shape
train_data.shape

- There are 8763 rows of data and 49 features 

#looking at descriptive statistics
train_data.describe()

- The five number summary displayed above for each feature (Minimum, Lower Quartile (Q1) = 25%, Median (Q2) = 50%, Upper Quartile (Q3) = 75%, Maximum) is also used for creating a box plot later in the project.

## Null Values

#checking the null values in the dataset
train_data.isnull().sum()

train_data["Valencia_pressure"]

- Valencia_pressure is the only feature that contains missing values

% of missing values:

#Calculating the percentage of missing values in each column
pd.DataFrame(data={'% of Missing Values':round(train_data.isna().sum()/train_data.isna().count()*100,2)})

- This may have been overlooked had I not performed further investigation. Since I found that Valencia_pressure's missing values missing account for 23.6% of all the values, I will consider removing them during the feature eningeering stage.

# plot relevant feature interactions

## Skewness, Kurtosis & Overall Outlier Visualization

As we have learnt both kurtosis and skew are important statistical measures. 

- Kurtosis is the measure of outliers present in the data. **High kurtosis (>3)** indicates a large number of outliers and **low kurtosis (<3)** a lack of outliers.  

Skew will indicate how symmetrical your data is. 
- Below is a table that explains the range of values with regards to skew.


|   Skew Value (x)  |       Description of Data      |
|:-------------------|:---------------:|
| -0.5 < x < 0.5              |Fairly Symmetrical |
| -1 < x < -0.5 | Moderate Negative Skew  | 
| 0.5 < x < 1             | Moderate Positive Skew  | 
|       x < -1     |High Negative Skew  | 
|       x > 1  |High Positve Skew | 

<div align="left" style="width: 500px; font-size: 80%; text-align: left; margin: 0 auto">
<img src="https://github.com/Explore-AI/Pictures/blob/f3aeedd2c056ddd233301c7186063618c1041140/regression_analysis_notebook/skew.jpg?raw=True"
     alt="Dummy image 1"
     style="float: left; padding-bottom=0.5em"
     width=500px/>
     For a more detailed explanation on skew and kurtosis read <a href="https://codeburst.io/2-important-statistics-terms-you-need-to-know-in-data-science-skewness-and-kurtosis-388fef94eeaa">here</a>.
</div>

## Skewness

#Looking at the skewness of skewness ofnthe train data
train_data.skew()

- Barcelona_rain_1h, Seville_rain_1h, Bilbao_snow_3h, Barcelona_pressure, Seville_rain_3h, Barcelona_rain_3h and Valencia_snow_3h are features that show a very high positive skewness.      

- The rest of the data exhibits a fair amount of symmetry with 2 features (Madrid_weather_id & Seville_weather_id) showing a negative skewness

## Kurtosis

#Checking the kurtosis of the train data 
train_data.kurtosis()

- Barcelona_rain_1h, Seville_rain_1h, Bilbao_snow_3h, Barcelona_pressure, Seville_rain_3h, Madrid_rain_1h, Barcelona_rain_3h, Valencia_snow_3h all exhibit a positive excess kurtosis, indicating a large number of outliers.      

## Visualizing the outliers

sns.boxplot(x='Barcelona_rain_1h', data=train_data)

sns.boxplot(x='Seville_rain_1h', data=train_data)

sns.boxplot(x='Bilbao_snow_3h', data=train_data)

sns.boxplot(x='Barcelona_pressure', data=train_data)

sns.boxplot(x='Seville_rain_3h', data=train_data)

sns.boxplot(x='Madrid_rain_1h', data=train_data) 

sns.boxplot(x='Barcelona_rain_3h', data=train_data)

sns.boxplot(x='Valencia_snow_3h', data=train_data)

# evaluate correlation
train_data.corr()

plt.figure(figsize=[20,10])
sns.heatmap(train_data.corr(),annot=True )

# have a look at feature distributions

<a id="four"></a>
## 4. Data Engineering
<a class="anchor" id="1.1"></a>
<a href=#cont>Back to Table of Contents</a>

---
    
| ⚡ Description: Data engineering ⚡ |
| :--------------------------- |
| In this section you are required to: clean the dataset, and possibly create new features - as identified in the EDA phase. |

---

# engineer existing features

# remove missing values/ features

#replacing missing values
train_data=train_data.fillna(train_data.mean())

train_data.isnull().sum()

- converting my non-numeric values

train_data['Valencia_wind_deg'] = train_data['Valencia_wind_deg'].str.extract('(\d+)').astype('int64')
train_data['Seville_pressure'] = train_data['Seville_pressure'].str.extract('(\d+)').astype('int64')

# create new features

- creating new columns from time

train_data['Year']  = train_data['time'].astype('datetime64').dt.year
train_data['Month_of_year']  = train_data['time'].astype('datetime64').dt.month
train_data['Week_of_year'] = train_data['time'].astype('datetime64').dt.weekofyear
train_data['Day_of_year']  = train_data['time'].astype('datetime64').dt.dayofyear
train_data['Day_of_month']  = train_data['time'].astype('datetime64').dt.day
train_data['Day_of_week'] = train_data['time'].astype('datetime64').dt.dayofweek
train_data['Hour_of_week'] = ((train_data['time'].astype('datetime64').dt.dayofweek) * 24 + 24) - (24 - train_data['time'].astype('datetime64').dt.hour)
train_data['Hour_of_day']  = train_data['time'].astype('datetime64').dt.hour

train_data = train_data.drop(columns=['Week_of_year','Day_of_year','Hour_of_week', 'Unnamed: 0','time'])

X = train_data.drop(columns = 'load_shortfall_3h')
y = train_data['load_shortfall_3h'].astype('int')

X = X[['Madrid_wind_speed', 'Valencia_wind_deg', 'Bilbao_rain_1h',
       'Valencia_wind_speed', 'Seville_humidity', 'Madrid_humidity',
       'Bilbao_clouds_all', 'Bilbao_wind_speed', 'Seville_clouds_all',
       'Bilbao_wind_deg', 'Barcelona_wind_speed', 'Barcelona_wind_deg',
       'Madrid_clouds_all', 'Seville_wind_speed', 'Barcelona_rain_1h',
       'Seville_pressure', 'Seville_rain_1h', 'Bilbao_snow_3h',
       'Barcelona_pressure', 'Seville_rain_3h', 'Madrid_rain_1h',
       'Barcelona_rain_3h', 'Valencia_snow_3h', 'Madrid_weather_id',
       'Barcelona_weather_id', 'Bilbao_pressure', 'Seville_weather_id',
       'Valencia_pressure', 'Seville_temp_max', 'Bilbao_weather_id', 
        'Valencia_humidity', 'Year', 'Month_of_year', 'Day_of_month', 'Day_of_week', 'Hour_of_day']]

# Creating standardization object
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled,columns=X.columns)
X_scaled.head()

<a id="five"></a>
## 5. Modelling
<a class="anchor" id="1.1"></a>
<a href=#cont>Back to Table of Contents</a>

---
    
| ⚡ Description: Modelling ⚡ |
| :--------------------------- |
| In this section, you are required to create one or more regression models that are able to accurately predict the thee hour load shortfall. |

---

# split data

## Train/test Split:

#Separating our models into training set and testing set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state = 42)

#checking the shape of the training and testing data

print('Training predictor:', X_train.shape)
print('Training target:', y_train.shape)
print('Testing predictor:', X_test.shape)
print('Testing target:', y_test.shape)

# create targets and features dataset

## Declaring the Predictive Models for this project

# create one or more ML models

#Linear Regression model
linear_reg=LinearRegression()

#Lasso Regression model
lasso_reg = Lasso(alpha=0.01)

#Ridge regression model
ridge_reg = Ridge()

#Regression tree model
reg_tree = DecisionTreeRegressor(max_depth=5,random_state=42)

#Random forest regression model
RF = RandomForestRegressor(oob_score= True, n_estimators= 300, min_samples_leaf= 1, max_features= 0.9)

## Fitting the selected models

#Train the linear model
linear_reg.fit(X_train, y_train)

#Train the lasso model
lasso_reg.fit(X_train, y_train)

# Train the RIDGE model
ridge_reg.fit(X_train, y_train)

#Decision tree model
reg_tree.fit(X_train,y_train)

#Random forest model
RF.fit(X_train,y_train)

## Getting predictions

#Getting predictions with the linear model
linear_reg_prediction = linear_reg.predict(X_test)

#Getting predictions withthe lasso model
lasso_reg_prediction = lasso_reg.predict(X_test)

#Getting predictions with the RIDGE model
ridge_reg_prediction = ridge_reg.predict(X_test)

#Getting predictions with tree model
reg_tree_prediction=reg_tree.predict(X_test)

#Getting predictions with the Random forest model
RF_prediction=RF.predict(X_test)

# evaluate one or more ML models

## Assessing the models prediction against the true value:

- Root Mean Square Error (RMSE) will be our standard metric for evalutating performance

#Defining the Root Mean Square Error
def rmse(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))

#Looking at the RMSE within each model
print(f'Linear Model:  {rmse(y_test, linear_reg_prediction)}')
print(f'lasso Model:  {rmse(y_test, lasso_reg_prediction)}')
print(f'Ridge Model:  {rmse(y_test, ridge_reg_prediction)}')
print(f'Decision Tree:  {rmse(y_test, reg_tree_prediction)}')
print(f'Random forest:  {rmse(y_test, RF_prediction)}')

<a id="six"></a>
## 6. Model Performance
<a class="anchor" id="1.1"></a>
<a href=#cont>Back to Table of Contents</a>

---
    
| ⚡ Description: Model performance ⚡ |
| :--------------------------- |
| In this section you are required to compare the relative performance of the various trained ML models on a holdout dataset and comment on what model is the best and why. |

---

# Compare model performance

print(f'Linear Model:  {rmse(y_test, linear_reg_prediction)}')
print(f'lasso Model:  {rmse(y_test, lasso_reg_prediction)}')
print(f'Ridge Model:  {rmse(y_test, ridge_reg_prediction)}')
print(f'Decision Tree:  {rmse(y_test, reg_tree_prediction)}')
print(f'Random forest:  {rmse(y_test, RF_prediction)}')

Model_RMSE_metric = { 'Test RMSE':
                    {"Linear model": np.sqrt(metrics.mean_squared_error(y_test,linear_reg_prediction)),
                        "Lasso": np.sqrt(metrics.mean_squared_error(y_test,lasso_reg_prediction)),
                        "Ridge" : np.sqrt(metrics.mean_squared_error(y_test,ridge_reg_prediction)),
                        "Decision Tree" : np.sqrt(metrics.mean_squared_error(y_test,reg_tree_prediction)),
                        "Random Forest" : np.sqrt(metrics.mean_squared_error(y_test,RF_prediction))}
                    }

# create dataframe from dictionary
Model_RMSE_metric = pd.DataFrame(data=Model_RMSE_metric)
Model_RMSE_metric

## Visualizing each models performance

px.bar(Model_RMSE_metric, y =Model_RMSE_metric['Test RMSE'],
       color = Model_RMSE_metric.index, width =700, height=400)

# Choose best model and motivate why it is the best choice

- Based on the above evaluation metrics and bar graph I can come to the conclusion that the Random Forest model performs better than the others models.

<a id="seven"></a>
## 7. Model Explanations
<a class="anchor" id="1.1"></a>
<a href=#cont>Back to Table of Contents</a>

---
    
| ⚡ Description: Model explanation ⚡ |
| :--------------------------- |
| In this section, you are required to discuss how the best performing model works in a simple way so that both technical and non-technical stakeholders can grasp the intuition behind the model's inner workings. |

---

# discuss chosen methods logic

## Random Forest Logic

What is a Random Forest?
- A random forest is a powerful non-parametric algorithm and as mentioned is an example of an ensemble method built on decision trees, meaning that it relies on aggregating the results of an ensemble of decision trees. The ensembled trees are randomized and the output is mean prediction of the individual trees*



Advantages of Random Forest Model:

- Less overfitting compared to a single tree (i.e. generalizes much better);
- Requires little data preparation - e.g. no real need to standardize features;
- Extremely flexible and usually have high prediction accuracy. 

# Kaggle Shortfall Submission

test_data.head()

## Repeating each engineering step applied to the train data

#Desampling Time
test_data['Year']  = test_data['time'].astype('datetime64').dt.year
test_data['Month_of_year']  = test_data['time'].astype('datetime64').dt.month
test_data['Week_of_year'] = test_data['time'].astype('datetime64').dt.weekofyear
test_data['Day_of_year']  = test_data['time'].astype('datetime64').dt.dayofyear
test_data['Day_of_month']  = test_data['time'].astype('datetime64').dt.day
test_data['Day_of_week'] = test_data['time'].astype('datetime64').dt.dayofweek
test_data['Hour_of_week'] = ((test_data['time'].astype('datetime64').dt.dayofweek) * 24 + 24) - (24 - test_data['time'].astype('datetime64').dt.hour)
test_data['Hour_of_day']  = test_data['time'].astype('datetime64').dt.hour


time = test_data['time']

#Filling missing values
test_data['Valencia_pressure'].fillna(test_data['Valencia_pressure'].mean(), inplace = True)

#Dropping Outliers
test_data = test_data[['Madrid_wind_speed', 'Valencia_wind_deg', 'Bilbao_rain_1h',
       'Valencia_wind_speed', 'Seville_humidity', 'Madrid_humidity',
       'Bilbao_clouds_all', 'Bilbao_wind_speed', 'Seville_clouds_all',
       'Bilbao_wind_deg', 'Barcelona_wind_speed', 'Barcelona_wind_deg',
       'Madrid_clouds_all', 'Seville_wind_speed', 'Barcelona_rain_1h',
       'Seville_pressure', 'Seville_rain_1h', 'Bilbao_snow_3h',
       'Barcelona_pressure', 'Seville_rain_3h', 'Madrid_rain_1h',
       'Barcelona_rain_3h', 'Valencia_snow_3h', 'Madrid_weather_id',
       'Barcelona_weather_id', 'Bilbao_pressure', 'Seville_weather_id',
       'Valencia_pressure', 'Seville_temp_max', 'Bilbao_weather_id', 
        'Valencia_humidity', 'Year', 'Month_of_year', 'Day_of_month', 'Day_of_week', 'Hour_of_day']]

#Converting Valencia_wind_deg to numeric form
test_data['Valencia_wind_deg'] = test_data['Valencia_wind_deg'].str.extract('(\d+)').astype('int64')
test_data['Seville_pressure'] = test_data['Seville_pressure'].str.extract('(\d+)').astype('int64')

#Getting Predictions
test_data['load_shortfall_3h'] = RF.predict(test_data)

test_data['time'] = time
load = test_data[['time','load_shortfall_3h']]
load.to_csv('Kaggle_submission_shortfall.csv', index = False)
load


    # ------------------------------------------------------------------------

    return predict_vector

def load_model(path_to_model:str):
    """Adapter function to load our pretrained model into memory.

    Parameters
    ----------
    path_to_model : str
        The relative path to the model weights/schema to load.
        Note that unless another file format is used, this needs to be a
        .pkl file.

    Returns
    -------
    <class: sklearn.estimator>
        The pretrained model loaded into memory.

    """
    return pickle.load(open(path_to_model, 'rb'))


""" You may use this section (above the make_prediction function) of the python script to implement 
    any auxiliary functions required to process your model's artifacts.
"""

def make_prediction(data, model):
    """Prepare request data for model prediction.

    Parameters
    ----------
    data : str
        The data payload received within POST requests sent to our API.
    model : <class: sklearn.estimator>
        An sklearn model object.

    Returns
    -------
    list
        A 1-D python list containing the model prediction.

    """
    # Data preprocessing.
    prep_data = _preprocess_data(data)
    # Perform prediction with model and preprocessed data.
    prediction = model.predict(prep_data)
    # Format as list for output standardisation.
    return prediction[0].tolist()
