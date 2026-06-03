import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

from logging_code import setup_logging
logger = setup_logging('Balancing')

from imblearn.over_sampling import SMOTE

def Data_Balancer(Training_data, Testing_data,y_train,y_test):
    try:
        logger.info(f'====================== Applying the SMOTE (over sampling the data) =============================')
        logger.info(f'Total Training Data {Training_data.columns} and shape {Training_data.shape}')
        logger.info(f'Total Testing Data {Testing_data.columns} and shape {Testing_data.shape}')
        logger.info(f' Checking how many are Good rows : {sum(y_train == 1)}')
        logger.info(f'Chacking how many  pre to diabiates: {sum(y_train == 2)}')
        logger.info(f' Checking how many are Bad rows : {sum(y_train == 0)} ')

        sm = SMOTE(sampling_strategy='auto', random_state=42)

        Training_data_bal, y_train_bal = sm.fit_resample(Training_data, y_train)


        logger.info(f'Total Training Data {Training_data_bal.columns} and shape {Training_data_bal.shape}')
        logger.info(f'Total Testing Data shape {y_train_bal.shape}')
        logger.info(f' Checking how many are Good rows : {sum(y_train_bal == 1)}')
        logger.info(f'Chacking how many  pre to diabiates: {sum(y_train_bal == 2)}')
        logger.info(f' Checking how many are Bad rows : {sum(y_train_bal == 0)} ')

        return Training_data_bal,y_train_bal


    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        logger.info(f'Error in lineno {er_line.tb_lineno} due to {er_type} and Reason {er_msg}')
