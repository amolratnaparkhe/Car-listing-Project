#        End-to-end Car listing Data Science Project.
## Objective: To do a comprehensive data analysis on the used car dataset in the Greater Cleveland and predict the prices of a used cars.
**Motivation:** After having looked for a car myself on the websites like Cargurus for some time, I thought of building a model that'd do the price prediction part for me.

> **Note:** As far as this project goes, I'm only interested in predicting the prices for 
>
>> * a used car, a sedan or an suv/crossover 
>> * individual brands are not considered for the project
>> * top 10 car brands for each category are chosen
>> * To maintain zero bias across brands, about 1000 records from each brand are scraped.


## This project is divided into 5 parts:
### 1. Obtain the data
 - To scrape the data,I used the Python library [Scrapy](https://scrapy.org/) and [Cargurus' website](https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?zip=44106&inventorySearchWidgetType=BODYSTYLE&bodyTypeGroup=bg7&showNegotiable=true&sortDir=ASC&sourceContext=carGurusHomePageModel&distance=200&sortType=DEAL_SCORE&endYear=2021&startYear=2005) to get the records for vehicles(Sedan and SUV/Crossover) in the Greater Cleveland area.
 - I'm interested in the cars within a 200 miles radius and between the years 2005-2021.
 
 ### 2. Data cleaning
  - The dataset contains about 20k records with over 20 features equally spread across sedans and suvs.
  - In order to do the analysis on the features, the missing values are either imputed or the corresponding records dropped.
  
 ### 3. Data exploration
  - Data visualization
  - Feature engineering
  - Data analysis
  
 ### 4. Building the Model
 - Two models based on the concept of Decision trees are used.
 - **Random Forest:** Large number of complex and random decision trees(low bias - high variance) in parallel.
 - **Gradient Boosting:** Large number of weak learners(high bias - low variance) which improve upon the errors made by the previous trees.
 
 ### 4. Conlusions/Remarks
 - The two models are compared and the one with the lower RMSE is preferred.
 - **Limitations:** Possible reasons preventing the model from performing better.
 - **Future directions:**  Advanced frameworks like [XgBoost](https://xgboost.readthedocs.io/en/latest/) and Neural Networks using [Tensorflow](https://www.tensorflow.org/) could be employed to see how they perform.
 - **Future directions(contd..):** Planning to scrape more and more data since at the end, good quality data will beat any fancy algorithm.
