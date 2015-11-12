"""
Very basic preprocessing of the review text

"""

import pandas as pd
import sys
import os



def _main():
    data = pd.read_hdf('../data/restaurant_reviews.hdf')
    data = get_text_and_labels(data)

    data.text = data.text.str.lower()

    data.to_hdf('../data/test_train.hdf', 'df', mode='w', format='f')


def get_text_and_labels(data):
    """

    Returns
    -------

    """
    data.loc[data.stars.isin([1,2]), 'target'] = -1
    data.loc[data.stars.isin([4,5]), 'target'] = 1
    data.loc[data.stars.isin([3]), 'target'] = 0
    data = data[['text', 'target']]

    return data



if __name__ == '__main__':
    sys.exit(_main())