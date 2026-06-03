from os.path import split

import numpy as np
import pandas as pd
import sklearn
import os
import sys
import warnings
warnings.filterwarnings('ignore')

from logging_code import setup_logging
logger = setup_logging('main')

from Variable_Transformation import Var_Transform
from Cat_Numerical import Cat_Num_cols
from Balancing import Data_Balancer
from Feature_Scaling import feature_scale
from ALL_MODELS import common
from hyperparameter_tuning import tuning


from sklearn.model_selection import train_test_split



class DIABETES:

    def __init__(self, path):

        self.path = path

        self.df = pd.read_csv(self.path)
        # showing the data set
        logger.info(f'Total Dataset {self.df}')

        # checking the dataset information
        for i in self.df.columns:
            logger.info(f'{i} -> {self.df[i].isnull().sum()}')
        #logger.info(f'Checking the DataSet {self.df.info()}')

        self.df = self.df.drop({'patient_id'}, axis=1)

        self.X = self.df.iloc[:, :-1]
        self.y = self.df.iloc[:, -1]
        logger.info(f'checking the X columns {self.X.columns}')
        logger.info(f'checking the y columns {self.y}')

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        for i in self.X_train.columns:
            logger.info(f'================  Train ==============')
            logger.info(f'{i} -> {self.X_train[i].isnull().sum()}')
            logger.info(f'================= Test ====================')
            logger.info(f'{i} -> {self.X_test[i].isnull().sum()}')

    def handling_null_values(self):
        try:
            for i in self.X_train.columns:
                if self.X_train[i].isnull().sum() > 0:
                    # creating duplicate column
                    self.X_train[i+'_ran'] = self.X_train[i]
                    self.X_test[i + '_ran'] = self.X_test[i]
                    # random sample values
                    s = self.X_train[i].dropna().sample(self.X_train[i].isnull().sum(), random_state=42)
                    s_test = self.X_test[i].dropna().sample(self.X_test[i].isnull().sum(), random_state=42)
                    # assigning null index
                    s.index = self.X_train[self.X_train[i].isnull()].index
                    s_test.index = self.X_test[self.X_test[i].isnull()].index
                    # replacing null values
                    self.X_train.loc[self.X_train[i].isnull(),i+'_ran'] = s
                    self.X_test.loc[self.X_test[i].isnull(),i + '_ran'] = s_test

                    self.X_train = self.X_train.drop([i], axis=1)
                    self.X_test = self.X_test.drop([i], axis=1)

            logger.info(f'After applying the random sample imputation for Train Checking')
            for i in self.X_train.columns:
                logger.info(f'{i} -> {self.X_train[i].isnull().sum()}')

            logger.info(f'After applying the random sample imputation for Test Checking')
            for i in self.X_train.columns:
                logger.info(f'{i} -> {self.X_test[i].isnull().sum()}')



        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in lineno {er_line.tb_lineno} due to {er_type} and Reason {er_msg}')

    def data_seperation(self):
        try:
            logger.info(f'================ Data Splitting =======================================')
            logger.info(f'Before splitting the Train columns {self.X_train.columns}')
            logger.info(f'Before splitting the Test columns {self.X_test.columns}')

            self.X_train_nums_cols = self.X_train.select_dtypes(exclude=object)
            self.X_train_cats_cols = self.X_train.select_dtypes(include=object)

            self.X_test_nums_cols = self.X_test.select_dtypes(exclude=object)
            self.X_test_cats_cols = self.X_test.select_dtypes(include=object)

            logger.info(f'After splitting the Train numerical columns {self.X_train_nums_cols.columns} : \n {self.X_train_nums_cols.shape}')
            logger.info(f'After splitting the Train categorical  columns {self.X_train_cats_cols.columns} : \n {self.X_train_cats_cols.shape}')
            logger.info(f'After splitting the Test numerical columns {self.X_test_nums_cols.columns} : \n {self.X_test_nums_cols.shape}')
            logger.info(f'After splitting the Test categorical  columns {self.X_test_cats_cols.columns} : \n {self.X_test_cats_cols.shape}')
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in lineno {er_line.tb_lineno} due to {er_type} and Reason {er_msg}')

    def Transformation(self):
        try:
            logger.info(f'================ Variable & Outlier & Feature Selection =======================================')
            logger.info(f'Before apply Train numerical columns and shapes \n : {self.X_train_nums_cols.columns} : {self.X_train_nums_cols.shape}')
            logger.info(f'Before apply Test numerical columns and shapes  \n : {self.X_test_nums_cols.columns} : {self.X_test_nums_cols.shape}')

            self.X_train_nums_cols, self.X_test_nums_cols, self.y_train = Var_Transform(self.X_train_nums_cols,self.X_test_nums_cols,self.y_train)

            logger.info(f'After apply Train numerical columns and shapes variable Transformation \n : {self.X_train_nums_cols.columns} : {self.X_train_nums_cols.shape}')
            logger.info(f'After apply Test numerical columns and shapes variable Transformation \n : {self.X_test_nums_cols.columns} : {self.X_test_nums_cols.shape}')

        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in lineno {er_line.tb_lineno} due to {er_type} and Reason {er_msg}')

    def Cat_to_Num(self):
        try:
            logger.info(f'================  Cat to NUmerical Columns =======================================')
            logger.info(f'Before apply Cat to Numerical Train numerical columns and shapes \n : {self.X_train_cats_cols.columns} : {self.X_train_cats_cols.shape}')
            logger.info(f'Before apply Cat to Numerical Test numerical columns and shapes  \n : {self.X_test_cats_cols.columns} : {self.X_test_cats_cols.shape}')

            self.X_train_cats_cols, self.X_test_cats_cols = Cat_Num_cols(self.X_train_cats_cols, self.X_test_cats_cols)

            self.X_train_nums_cols.reset_index(drop=True, inplace=True)
            self.X_train_cats_cols.reset_index(drop=True, inplace=True)
            self.X_test_nums_cols.reset_index(drop=True, inplace=True)
            self.X_test_cats_cols.reset_index(drop=True, inplace=True)

            self.Training_data = pd.concat([self.X_train_nums_cols, self.X_train_cats_cols], axis=1)
            self.Testing_data = pd.concat([self.X_test_nums_cols, self.X_test_cats_cols], axis=1)

            logger.info(
                f'Total Training Data is : {self.Training_data.columns} \n and it shape : {self.Training_data.shape} ')
            logger.info(
                f'Total Testing Data is : {self.Testing_data.columns} \n and it shape : {self.Testing_data.shape}')


        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in lineno {er_line.tb_lineno} due to {er_type} and Reason {er_msg}')

    def Data_Balancing(self):
        try:
            logger.info(f'========================= Data Balancing ================================')

            logger.info(
                f'Before Data Balanced the {self.Training_data.columns} and it is shape {self.Training_data.shape}')
            self.Training_data_bal, self.y_train_bal = Data_Balancer(self.Training_data, self.Testing_data,
                                                                     self.y_train, self.y_test)
            logger.info(
                f'After balancing the data {self.Training_data_bal.columns} and it is shape : {self.Training_data_bal.shape}')
            logger.info(f' After balancing the data {self.y_train_bal.shape}')


        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in lineno {er_line.tb_lineno} due to {er_type} and Reason {er_msg}')

    def feature_scaler(self):
        try:
            logger.info(
                f' Before applying the feature scaling Training data {self.Training_data_bal.columns} and its shape {self.Training_data_bal.shape}')
            logger.info(
                f' Before applying the feature scaling Testing data {self.Testing_data} and its shape {self.Testing_data.shape} ')

            feature_scale(self.Training_data_bal, self.Testing_data, self.y_train_bal,self.y_test)

            logger.info(f' After applying the feature scaling Training data {self.Training_data_bal_sc} {self.Training_data_bal_sc.shape}')
            logger.info(f' After applying the feature scaling Testing data {self.Testing_data_sc.shape}')


        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in lineno {er_line.tb_lineno} due to {er_type} and Reason {er_msg}')

    def all_models(self):
        try:
            self.Training_data_bal_sc,self.y_train_bal,self.Testing_data_sc,self.y_test = common(self.Training_data_bal_sc,self.y_train_bal,self.Testing_data_sc,self.y_test)
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in lineno {er_line.tb_lineno} due to {er_type} and Reason {er_msg}')

    def hyperparameter(self):
        try:
            tuning(self.Training_data_bal_sc, self.y_train_bal, self.Testing_data_sc, self.y_test)

        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in lineno {er_line.tb_lineno} due to {er_type} and Reason {er_msg}')


if __name__ == "__main__":
    obj = DIABETES('diabetes_dataset.csv')
    obj.handling_null_values()
    obj.data_seperation()
    obj.Transformation()
    obj.Cat_to_Num()
    obj.Data_Balancing()
    obj.feature_scaler()
    obj.all_models()
    obj.hyperparameter()