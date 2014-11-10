#!/usr/bin/python
'''
Pre-process the training sets and test sets.

Input
------
train_rev2.csv: original sub-training sets.
test_rev2.csv: original test set.

Output
-------
ptrain.csv: preprocessed training set.
ptest.csv: preprocessed test set.
'''

import pandas as pd

# numerical columns
NUMCOLS = ("click","day","short_hour","C1","C17",
           "C18","C19","C20","C21","C22","C23","C24")
# categorical columns
CATCOLS = ("banner_pos","site_id","site_domain","site_category",
           "app_id","app_domain","app_category","device_os","device_make",
           "device_model","device_type","device_conn_type")
# charcteristic columns
CHACOLS = ("site_id","site_domain","site_category","app_id","app_domain",
           "app_category","device_os","device_make","device_model")

def extract_hour(data):
    '''Extact from the raw and add two attributes, i.e. day and short_hour'''
    data_str = data['hour'].apply(str)
    data['day'] = data_str.apply(lambda x: x[4:6])
    data['short_hour'] = data_str.apply(lambda x: x[6:])
    return data

def preprocess(data):
    '''Pre-process the dataset'''
    data = extract_hour(data) # add 'day' and 'short_hour'

    # hash tricks
    from sklearn.feature_extraction import FeatureHasher



if __name__ == "__main__":
    random.seed(3)
    test = pd.read_csv('data/test_rev2.csv')
    test = preprocess(test)
    test.to_csv('data/ptest.csv')
    del test
    train = pd.read_csv('data/train_rev2.csv')
    train = preprocess(train)
    train.to_csv('data/ptest_rev2.csv')
