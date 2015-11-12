import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix

data = pd.read_hdf('../data/test_train.hdf')


def make_matrix(ser):
    vect = TfidfVectorizer()
    X = vect.fit_transform(ser)
    return X


def train_svc(X, y):
    params = {"tfidf__ngram_range": [(1, 1), (1, 2)],
          "svc__C": [.01, .1, 1, 10, 100]}

    clf = Pipeline([("tfidf", TfidfVectorizer(sublinear_tf=True)),
                ("svc", LinearSVC())])

    gs = GridSearchCV(clf, params, verbose=2, n_jobs=-1)

    gs.fit(X, y)
    print(gs.best_estimator_)
    print(gs.best_score_)


def train_random_forest_reg(X, y):
    """
    Reason to believe that random forest regressor
    will be the optimal model because it:
        1. Considers that neutral is in the middle ground
        2. Works well for overfitting
        3. Is reasonable to train my huge dataset on.

    Returns
    -------

    """
    params =  {"tfidf__ngram_range": [(1, 1), (1, 2)],
          "rf__n_estimators": [100, 500, 1000]}

    clf = Pipeline([('tfidf', TfidfVectorizer(sublinear_tf=True)),
                    'rf', RandomForestRegressor])

    gs = GridSearchCV(clf, params, oob_score=True, max_features='sqrt')

    gs.fit(X, y)
