# Industrial-Copper-Modelling
This project is about to build Regression Model to predict the selling price of copper and to build Classification Model to predict the leads conversion.

**Copper - A Brief Overview**

Copper is a reddish-brown metal known for its high electrical and thermal conductivity.
It is one of the oldest metals used by humans, with historical evidence dating back thousands of years. Copper is malleable, ductile, and resistant to corrosion, making it useful in various industries, especially in electrical wiring, plumbing, and electronics.
Due to its excellent conductivity, copper is a critical component in power generation and transmission systems.
It is also used in alloys like bronze (copper and tin) and brass (copper and zinc) for various mechanical and aesthetic applications.
Copper is widely mined across the world, with major producers including Chile, the U.S., and Peru.

**Copper Usage:**

Copper is widely used across multiple industries due to its excellent electrical and thermal conductivity, corrosion resistance, and malleability.
Copper is used across various industries in the following approximate percentages:
1.Electrical and Electronics Industry - 40%: This includes electrical wiring, power generation, transmission systems, and electronic components.
2.Construction Industry - 30%: Copper is used in plumbing, roofing, cladding, and building infrastructure.
3.Transportation Industry - 12%: Used in automobiles (wiring, radiators, motors), aircraft, and trains.
4.Consumer Products - 12%: Includes appliances, cookware, and other household goods.
5.Industrial Machinery - 6%: Used in machinery, heat exchangers, and industrial equipment.

**Problem Statement**

The copper industry deals with less complex data related to sales and pricing.The data may suffer from issues of skewness and noisy.
Due to these challenges,manual predictions of selling price is not optimal and time consuming too.
A machine learning regression model can address these issues by utilizing advanced techniques such as data normalization,
feature scaling, and outlier detection, and leveraging algorithms that are robust to skewed and noisy data.

Another area where the copper industry faces challenges is in capturing the leads. 
A lead classification model is a system for evaluating and classifying leads based on how likely they are to become a customer.

**Approach:**

**1. Data Understanding:**

Identify the types of variables (continuous, categorical) and their distributions.

If any rubbish values found such as '0000',it should be converted into null.

**2. Data Preprocessing:**

  * Handle missing values with mean/median/mode.
  * Treat Outliers using IQR
  * Identify Skewness in the dataset and treat skewness with appropriate data transformations, such as log transformation.
  * Encode categorical variables using suitable techniques, such as one-hot encoding, label encoding, or ordinal encoding, based on their nature and relationship with the target variable.





