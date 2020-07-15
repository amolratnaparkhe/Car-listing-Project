#        End-to-end Car listing Data Science Project.
## Objective: To do a comprehensive data analysis on the used car dataset in the Greater Cleveland area and building a regression model to predict the prices of used cars.
**Motivation:** After having looked for a car myself on the websites like Cargurus for some time, I thought it'd be a good idea to build a model which predicts the prices of the cars I'm interested in.

> **Note:** As far as this project goes, I'm trying to predict the prices for 
>
>> * used cars, in specific, a sedan or an suv/crossover regardless of a particular brand. 
>> * top 10 car brands for each category are chosen.
>> * To maintain zero bias, the samples are scraped and spread equally among the major brands.


## This project is divided into 5 parts:
### 1. Obtain the data
 - I have used the Python library [Scrapy](https://scrapy.org/) and [Cargurus' website](https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?zip=44106&inventorySearchWidgetType=BODYSTYLE&bodyTypeGroup=bg7&showNegotiable=true&sortDir=ASC&sourceContext=carGurusHomePageModel&distance=200&sortType=DEAL_SCORE&endYear=2021&startYear=2005) to scrape the vehicles data within a 200 miles radius and between the years 2005-2021. 
 - I'm building a separate repository on Data mining where I clearly explain how do I use Scrapy to efficiently pull the data from any website.
 
 ### 2. Data cleaning
  - The dataset comprises of about 20k records with over 20 features with many of the columns containing missing values.
  - The dataset is cleaned by using the methods of data imputation and is ready for the next step of data exploration. 
  
 ### 3. Data exploration/visualization/analysis
  - Useful Python libraries like Numpy, Pandas, Matplotlib, Scipy and Seaborn are used to study, visualize and analyze each and every one of the features which could potentially affect the price of the vehicle. The features which statistically hold little/no importance are dropped.
  
 ### 4. Building the Model
 - I have employed two Decision tree based models: Random Forest and GradientBoosting.
 - **Random Forest:** Random forest uses large number of complex and random decision trees(low bias - high variance) in parallel.
 - **Gradient Boosting:**  GradientBoosting also employs large number of weak learners(high bias - low variance) and they improve upon the errors made by the previous weak learners.
 
 ### 5. Conlusions/Remarks/Future 
 - The two models are compared and the one with the lower RMSE is preferred.
 - **Limitations:** Discuss the possible reasons preventing the model from performing better.
 - **Future directions:** I'd like to employ some of the advanced frameworks like [XgBoost](https://xgboost.readthedocs.io/en/latest/) and Neural Networks using the [Tensorflow library](https://www.tensorflow.org/) to see how they perform.
 - **Future directions(contd..):** The goal is to eventually deploy the model on a webpage so that anybody can take advantage of this model. All you got to do is to just feed in the features you're looking for in your dream car and the model will predict its price.
 - **Future directions(contd..):** I'd like to also span not just the area of Cleveland but eventually extend it to all the parts of the US as well as include other  vehicles other than just sedans or suvs. This sort of functionality will require me to scrape more and more data. And as they say, 'large and good quality data always beats any fancy algorithm', I hope to build a robust and accurate ML platform for the users.
