import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import sys
import os
import seaborn as sns
import logging

from logging_code import setup_logging
logger = setup_logging("RandomForest_Hyperparameter_Tuning")

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import GridSearchCV


def tuning(Training_data_bal_sc, y_train_bal, Testing_data_Zscore, y_test):

    try:
        logger.info(f'Applying the Tuning Test')

        # ================= GridSearchCV ======================

        parameters_list = {

            'n_estimators': [100, 200, 300],

            'criterion': ['gini', 'entropy'],

            'max_depth': [None, 5, 10, 20],

            'min_samples_split': [2, 5, 10],

            'min_samples_leaf': [1, 2, 4],

            'max_features': ['sqrt', 'log2'],

            'bootstrap': [True, False]

        }


        grid_rf = GridSearchCV(
            estimator=RandomForestClassifier(random_state=42),
            param_grid=parameters_list,
            scoring='accuracy',
            cv=5,
            n_jobs=-1
        )


        grid_result = grid_rf.fit(Training_data_bal_sc, y_train_bal)


        logger.info(f'Grid Search Result : {grid_result}')

        logger.info(f'Best Parameters : {grid_result.best_params_}')

        logger.info(f'Best Accuracy Score : {grid_result.best_score_}')



    except Exception as e:

        er_type, er_msg, er_line = sys.exc_info()

        logger.info(f'Error in lineno {er_line.tb_lineno} due to {er_type} and Reason {er_msg}')