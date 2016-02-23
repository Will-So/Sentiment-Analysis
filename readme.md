# Yelp Sentiment Analysis
This is the first part in a project that will provide a more sophisiticated recommendation system than is currently found in industry.
When different people go to a restaurant they have different priorities. Some people prioritize cost. Others prioritize
the atmosphere. Current recommender systems don't take this into account.

![](https://dl.dropboxusercontent.com/u/97258109/Screens/S3588.png)
 
# Methodology
I train a new model to estimate the sentiment of each word using the star ratings of the review as whether the sentiment should 
 be positive or negative. In accordance with [1] I include a neutral category in the training. 


# Tools Used
1. Sentiment Analysis with Spacy and Sci-kit learn for the machine learning and tf-idf processing. 

# Resources
This project was inspired by the following papers:

1. Koppel, Moshe, and Jonathan Schler. "The importance of neutral examples for learning sentiment."
2. http://harshtechtalk.com/get-informative-features-scikit-learn/
3. [Proof](http://axon.cs.byu.edu/Dan/778/papers/Feature%20Selection/guyon2.pdf) that we can use SVM coefficients to 
 get the relatively important coefficients. 