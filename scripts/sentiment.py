"""
Sentiment Analysis trainer based on yelp review stars as the target dataset

Methodology:
    1. Create word features
        - Try bag of words first. Move on to tf-idf if that seems to be successful
    2. Label positive and negative reviews
        - 4 or 5 stars positive, 1 or 2 stars negative
    3. Make positive and negative features
    4. Split the dataset
"""
import pandas as pd


def _main():
    """
    Creates the sentiment Analysis model

    """
    reviews = pd.read_hdf('../data/reviews.hdf',)


def bag_of_word_feats(words):
    return {word: True for word in words}


def tf_idf_feats(words):
    pass


def label_reviews(reviews):
    """


    Parameters
    ----------
    df

    Returns
    -------

    """
    negative_reviews = reviews[reviews.stars.isin([1,2])]
    positive_reviews = reviews[reviews.stars.isin([4,5])]
    neutral_reviews = reviews[reviews.stars == 3]


    # Problem: Might be weird for separation purposes here. May want to just keep
    # it in a list.
    positive_text = ' '.join([i for i in positive_reviews.text.values])
    negative_text = ' '.join([i for i in negative_reviews.text.values])
    neutral_reviews = ' '.join([i for i in neutral_reviews.text.values])

    assert type(positive_text) == str

    return positive_text, negative_text, neutral_reviews




def assign_features():
    """
    Given that a review is positive or negative,
    Returns
    -------

    """


def train_model(train_features):
    """

    Parameters
    ----------
    train_features

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