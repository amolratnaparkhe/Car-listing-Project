#        End-to-end Car listing Data Science Project.
## Objective: To do a comprehensive data analysis and predict the price of a used car(Sedan or SUV) in the Greater Cleveland area.
**Motivation:** After having looked for a car for myself on the websites like Cargurus for long, I thought of building a model that'd do the price prediction part for me.
> **Note:** I'm interested in predicting the prices for 
>
>> * a used car
>> * a sedan or an suv/crossover
>> * brands are not so important for the project
>> * top 10 car brands for each category are chosen
>> * To maintain zero bias across brands, about 1000 records from each brand are scraped.


## This project is divided into 5 parts:
### 1. Obtain the data
 - To obtain the records, I used the Python library [Scrapy](https://scrapy.org/).
 - I used [Cargurus' website](https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?zip=44106&inventorySearchWidgetType=BODYSTYLE&bodyTypeGroup=bg7&showNegotiable=true&sortDir=ASC&sourceContext=carGurusHomePageModel&distance=200&sortType=DEAL_SCORE&endYear=2021&startYear=2005) to scrape the records for vehicles(Sedan and SUV/Crossover) in the Greater Cleveland area.
 - I'm interested in the cars within a 200 miles radius and between the years 2005-2021.
 
 ### 2. Data cleaning
  - The dataset contains about 20k records equally distributed across sedans and suvs.
  - There are over 20 features which include things like mileage, engine, transmission, trim, etc.
  - In order to do the analysis on the features, the missing values are either imputed or the corresponding records dropped.
  
 ### 3. Data exploration
  - The features are visualized and divided into 2 categories, numerical and categorical.
  - Each of the categorical features are analyzed and turned into appropriate numerical values using feature engineering.
  - All of the numerical features are studied to understand which features are statistically more important/correlated with our target variable, i.e. Price.
  - Features with little/no correlation with the Price are dropped.
 
 ### 4. Building the Model
 - The feature set contains a large number of categorical features as well as distinctly separated numerical features.
 - To make use of this knowledge, two models based on the concept of Decision trees are used.
 - **Random Forest:** Starting with a large number of complex and random decision trees(low bias - high variance) in parallel, the first model is built.
 - **Gradient Boosting:** This one starts with a large number of weak learners(high bias - low variance) and improves upon the errors(in residuals) made by the previous trees to eventually build the second model.
