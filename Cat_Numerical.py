import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

from logging_code import setup_logging
logger = setup_logging('Cat_to_NUmerical_col')

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder


def Cat_Num_cols(X_train_cat_cols, X_test_cat_cols):
    try:
        logger.info(f'Before doing Train Categorical to numerical : {X_train_cat_cols.columns} \n : and its shape {X_train_cat_cols.shape}')
        logger.info(f'Before doing Test Categorical to numerical : {X_test_cat_cols.columns} \n : and its shape {X_test_cat_cols.shape}')

        # drooping the customer id
        X_train_cat_cols = X_train_cat_cols.drop(['diagnosis'], axis=1)
        X_test_cat_cols = X_test_cat_cols.drop(['diagnosis'], axis=1)

        # Applying the nominal encoder(OneHotEncoder)
        # Columns are ('gender')

        logger.info(f'============= Applying the nominal encoder(OneHotEncoder) ========================= ')
        logger.info(f' Columns are gender ')

        one_hot = OneHotEncoder(drop='first')
        one_hot.fit(X_train_cat_cols[['gender']])
        val_train = one_hot.transform(X_train_cat_cols[['gender']]).toarray()
        val_test = one_hot.transform(X_test_cat_cols[['gender']]).toarray()

        t1 = pd.DataFrame(val_train)
        t2 = pd.DataFrame(val_test)

        t1.columns = one_hot.get_feature_names_out()
        t2.columns = one_hot.get_feature_names_out()

        X_train_cat_cols.reset_index(drop=True, inplace=True)
        X_test_cat_cols.reset_index(drop=True, inplace=True)

        t1.reset_index(drop=True, inplace=True)
        t2.reset_index(drop=True, inplace=True)

        X_train_cat_cols = pd.concat([X_train_cat_cols, t1], axis=1)
        X_test_cat_cols = pd.concat([X_test_cat_cols, t2], axis=1)

        X_train_cat_cols = X_train_cat_cols.drop(['gender'], axis=1)
        X_test_cat_cols = X_test_cat_cols.drop(['gender'], axis=1)

        logger.info(
            f'Before doing Train Categorical to numerical : {X_train_cat_cols.columns} \n : and its shape {X_train_cat_cols.shape}')
        logger.info(
            f'Before doing Test Categorical to numerical : {X_test_cat_cols.columns} \n : and its shape {X_test_cat_cols.shape}')

        # applying the OrdinalEncoder
        logger.info(f'====================  OrdinalEncoder  =======================')

        ordinal_cols = ['physical_activity', 'smoking_status']

        od = OrdinalEncoder()
        od.fit(X_train_cat_cols[['physical_activity', 'smoking_status']])

        results_train = od.transform(X_train_cat_cols[['physical_activity', 'smoking_status']])
        results_test = od.transform(X_test_cat_cols[['physical_activity', 'smoking_status']])

        p1 = pd.DataFrame(results_train, columns=[c+"_ordinal" for c in ordinal_cols])
        p2 = pd.DataFrame(results_test, columns=[c+"_ordinal" for c in ordinal_cols])

        # p1.columns = od.get_feature_names_out()+"_ordinal"
        # p2.columns = od.get_feature_names_out()+"_ordinal"

        p1.reset_index(drop=True, inplace=True)
        p2.reset_index(drop=True, inplace=True)

        X_train_cat_cols = pd.concat([X_train_cat_cols, p1], axis=1)
        X_test_cat_cols = pd.concat([X_test_cat_cols, p2], axis=1)

        X_train_cat_cols = X_train_cat_cols.drop(['physical_activity', 'smoking_status'], axis=1)
        X_test_cat_cols = X_test_cat_cols.drop(['physical_activity', 'smoking_status'], axis=1)
        logger.info(f"After Ordinal X_train_cat Column : {X_train_cat_cols.shape} : \n : {X_train_cat_cols.columns}")
        logger.info(f"After Ordinal X_test_cat Column : {X_test_cat_cols.shape} : \n : {X_test_cat_cols.columns}")
        logger.info(f'Checking the Data {X_train_cat_cols}')

        return X_train_cat_cols, X_test_cat_cols

    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        logger.info(f'Error in lineno {er_line.tb_lineno} due to {er_type} and Reason {er_msg}')