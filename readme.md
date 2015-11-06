# Building a better recommender system
When different people go to a restaurant they have different priorities. Some people prioritize cost. Others prioritize 
the atmosphere. Current recommender systems don't take this into account. 

This web app recommends restaurants to users based on users' preferences. Preferences are obtained in one of two ways.
The first method is to infer the preferences of users based on their reviews. The second method is to allow users to specify 
their preferences manually. This latter method is a solution to the cold-start problem. 

For example, users who prioritize a cheap restaurant and don't particularly care about atmosphere will be served
with recommendations that users with similar priorities liked. 

// Screenshot here
 
# An Example
When Sue goes a restaurant, the most important thing to her is the quality of the food. She is particularly apathetic 
 to atmosphere. Sue has also never given a review before
 
Sue has never used our website before so she opts manually select her preferences. She gives quality of food a 5
on the important scale and the quality of waitors as a 3. She doesn't care about the other factors so she gives them
a 1. 


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

# Resources
This project was inspired by the following papers:

1. 