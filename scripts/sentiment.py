"""
Sentiment Analysis trainer based on yelp review stars as the target dataset

Methodology:
    1. Create word features
        - Try bag of words first. Move on to tf-idf if that seems to be successful
    2. Label positive and negative reviews
        - 4 or 5 stars positive, 1 or 2 stars negative
    3. Make positive and negative features
    4. Split the dataset into train_test_split
    5. Validate dataset using cross validation
    6.
"""
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import Pipeline


def _main():
    """
    Creates the sentiment Analysis model

    """
    reviews = pd.read_hdf('../data/reviews.hdf',)
    X_train, X_test, y_train, y_test = train_test_split(reviews.text, reviews.stars,
                                                        train_size=0.8, random_state=188)


def count_vect_nb(words):
    """
    The simplest baseline model that uses multinomial NB
    Parameters
    ----------
    words

    Returns
    -------

    """
    vect = CountVectorizer()
    params = {'count_vect__ngram_range': [(1, 1), (1, 2)]}

    X = vect.fit_transform(words)

    clf = Pipeline([('count_vect')])


def tfidf(words):
    vect = TfidfVectorizer()



#
# def label_reviews(reviews):
#     """
#     # TODO: Things should be sentence tokenized
#
#     Parameters
#     ----------
#     df
#
#     Returns
#     -------
#
#     """
#     negative_reviews = reviews[reviews.stars.isin([1,2])]
#     positive_reviews = reviews[reviews.stars.isin([4,5])]
#     neutral_reviews = reviews[reviews.stars == 3]
#
#
#     # Problem: Might be weird for separation purposes here. May want to just keep
#     # it in a list.
#     positive_text = ' '.join([i for i in positive_reviews.text.values])
#     negative_text = ' '.join([i for i in negative_reviews.text.values])
#     neutral_reviews = ' '.join([i for i in neutral_reviews.text.values])
#
#     assert type(positive_text) == str
#
#     return positive_text, negative_text, neutral_reviews
#



def assign_features():
    """
    Given that a review is positive or negative,
    Returns
    -------

    """


def train_svm(train_features):
    """

    Parameters
    ----------
    train_features

    Returns
    -------

    """


def train_linear_model(train_features, targets):
    """
    Tends to perform better than SVM in the case of three-way classification between neutral
     and non-neutral things

    I also binarize the feature count as suggested by //

    Parameters
    ----------
    train_features
    targets

    Returns
    -------

    Notes
    ----


    """


def train_nb(train_features, targets):
    """
    Trains the sentiment of the reviews based

    Parameters
    ----------
    train_features
    targets

    Returns
    -------

    """
    clf = MultinomialNB()
    model = clf.fit(train_features, targets)
    return model


def predict_sentiment():
    """

    Returns
    -------

    """


def eval_model(model, test_features):
    """

    Parameters
    ----------
    model
    test_features

    Returns
    -------

    """