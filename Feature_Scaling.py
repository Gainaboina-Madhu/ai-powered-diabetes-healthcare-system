import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import os
import sys
import seaborn as sns
import logging

import pickle

import warnings
warnings.filterwarnings('ignore')


#modularization

from logging_code import setup_logging
logger = setup_logging('Feature_Scaling')


from sklearn.preprocessing import StandardScaler #Z_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score


def feature_scale(Training_data_bal, Testing_data,y_train_bal,y_test):
    try:
        logger.info(f' Before applying the feature scaling Training data {Training_data_bal.columns} and its shape {Training_data_bal.shape}')
        logger.info(f' Before applying the feature scaling Testing data {Testing_data}')

        sc = StandardScaler()
        sc.fit(Training_data_bal)

        Training_data_bal_sc = pd.DataFrame(sc.transform(Training_data_bal),columns=Training_data_bal.columns)

        Testing_data_sc = pd.DataFrame(sc.transform(Testing_data),columns=Testing_data.columns)

        with open('standard_scaler.pkl', 'wb') as f:
            pickle.dump(sc, f)

        dt_reg = DecisionTreeClassifier(
            criterion='entropy',
            max_depth=20,
            max_features='sqrt',
            min_samples_leaf=2,
            min_samples_split=5,
            random_state=42
        )

        dt_reg.fit(Training_data_bal_sc, y_train_bal)

        predictions = dt_reg.predict(Testing_data_sc)

        logger.info(f'The Confusion Matrix \n {confusion_matrix(y_test, predictions)}')

        logger.info(f'The Accuracy is : {accuracy_score(y_test, predictions)}')

        logger.info(f'The Classification Report is : \n {classification_report(y_test, predictions)}')

        with open('Model.pkl', 'wb') as t:
            pickle.dump(dt_reg, t)





    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        logger.info(f'Error in lineno {er_line.tb_lineno} due to {er_type} and Reason {er_msg}')