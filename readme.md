# Recommending Bars based on implicit tastes
This web app recommends restaurants to users based on their latent processes. 
For example, users who prioritize a cheap bar and don't particularly care about atmosphere will be served
with recommendations that users with similar tastes liked. 

// Screenshot here
 
# An Example


# Methodology
## New Sentiment Analysis
I train a new model to estimate the sentiment of each word based on 

The results of my training set are as follows:

// Training table here

## Latent Topic Modeling

## Finding 'Friends'


## Recommending Bars based on friends
Given the friends

## Solving the Cold Start Problem

# Tools Used
1. Sentiment Analysis with Spacy
2. Latent Dirchlet Analysis
3. KNN
4. Flask
5. D3 and Tableau for visualization
6. Spark to demonstrate the scalability of this model


# Scaling
I implement the heart of the recommender system such that it will work on both a single system
 (Python) as well as a 

When dealing with a single city, which makes sense for most use cases, using a distributed solution such as Spark
should be unneccessary for most use cases.

However, if we were to use this strategy for a larger dataset such as all Amazon reviews, using a distributed solution 
would likely be necessary to achieve decent performance.

# Visualizations
A map is available of the top 10 recommended items based on the input given.