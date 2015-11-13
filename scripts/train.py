import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split

data = pd.read_hdf('../data/test_train.hdf')

X_train, X_test, y_train, y_test = train_test_split(data.text, data.target,
                                                        test_size=.1, random_state=123)


def make_rf_matrices(data):
    """
    Makes simple tfidf matrices that I used for random forests
    Parameters
    ----------
    data

    Returns
    -------

    """
    vect = TfidfVectorizer()
    X = vect.fit_transform(data.text)


    vect.transform(X_train); vect.transform(X_test)

    return X_train, X_test, y_train, y_test


def train_svc(X, y):
    params = {"tfidf__ngram_range": [(1, 1), (1, 2)],
          "svc__C": [.01, .1, 1, 10, 100]}

    clf = Pipeline([("tfidf", TfidfVectorizer(sublinear_tf=True)),
                ("svc", LinearSVC())])

    gs = GridSearchCV(clf, params, verbose=2, n_jobs=-1)

    gs.fit(X, y)
    print(gs.best_estimator_)
    print(gs.best_score_)


def train_rf_reg(X, y):
    """
    Reason to believe that random forest regressor
    will be the optimal model because it:
        1. Considers that neutral is in the middle ground
        2. Works well for overfitting
        3. Is reasonable to train my huge dataset on.

    Returns
    -------
    """
    rf = RandomForestRegressor(n_estimators=100, max_features='sqrt',
                               n_jobs=-1, min_samples_leaf=4)
    return rf.fit(X, y)