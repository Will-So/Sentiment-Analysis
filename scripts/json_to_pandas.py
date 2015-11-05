"""
Loads yelp data into a Pandas Dataframe.


"""

import pandas as pd
import sys
import logging

DATA_DIR = '/Users/Will/Data/newest_yelp/'

HDF = False


def _main():
    """

    Returns
    -------

    """
    reviews = reviews_to_pandas(DATA_DIR)

    if HDF:
        reviews.to_hdf('../data/df.hdf', 'df', mode='w', format='f')

    print(reviews.head(2))

    businesses = businesses_to_pandas(DATA_DIR)
    businesses.to_hdf('..data/df.hdf', 'businesses', mode='w', format='f')


def reviews_to_pandas(dir):
    """

    Parameters
    ----------
    dir

    Returns
    -------

    Examples
    ----
    >>> df = reviews_to_pandas(DATA_DIR)
    >>> df.head(2)

    """



    data = load_json_file(dir + 'yelp_academic_dataset_review.json')
    df = parse_large_df(data)

    return df


def businesses_to_pandas(dir):
    """

    Parameters
    ----------
    dir

    Returns
    -------

    """
    data = load_json_file(dir + 'yelp_academic_dataset_business.json')
    df = parse_large_df(data)

    return df


def parse_large_df(data):
    """
    Hacky way to deal with dataframes that are large quickly from a json file.

    Parameters
    ----------
    data: A list of the json files

    Returns
    -------
    df: dataframe
    """
    minis = {}
    for i in range(1, (len(data)), 10000):
        j = i + 10000
        data_json_str = "[" + ','.join(data[i:j]) + "]"
        temp = pd.read_json(data_json_str)
        minis[i] = temp
        print(str(j) + ' rows in a df')

    df = pd.read_json(data[0])
    for i in range(1, (len(data)), 10000):
        df = pd.concat([df, minis[i]], ignore_index=True, axis=0)
        print('appending {}'.format(i))

    return df


def load_json_file(json_dir):
    """
    Loads a json file with the directory

    Returns
    -------

    """
    with open(json_dir) as jsonfile:
        data = jsonfile.readlines()
        # remove the trailing "\n" from each line
        data = list(map(lambda x: x.rstrip(), data))

    return data


if __name__ == '__main__':
    sys.exit(_main())
