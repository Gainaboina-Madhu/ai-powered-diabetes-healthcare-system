import os
import sys

import logging
from hmac import digest_size

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

from logging_code import setup_logging
logger = setup_logging('Variable')

import seaborn as sns
from scipy import stats
from seaborn import boxplot
from scipy.stats import yeojohnson
from scipy.stats import boxcox

from sklearn.feature_selection import VarianceThreshold
from scipy.stats import pearsonr



def Var_Transform(X_train_nums_cols, X_test_nums_cols, y_train):

    try:

        logger.info(f'===============================  Variable Transformation  ====================================')
        logger.info(f'Before apply Train numerical columns and shapes variable Transformation \n : {X_train_nums_cols.columns} : {X_train_nums_cols.shape}')
        logger.info(f'Before apply Test numerical columns and shapes variable Transformation \n : {X_test_nums_cols.columns} : {X_test_nums_cols.shape}')


        column = ['skin_thickness_mm', 'sbp_mmhg', 'dbp_mmhg','glucose_mg_dl', 'fasting_glucose_mg_dl',
                      'ogtt_2hr_mg_dl', 'hba1c_pct','ldl_mg_dl', 'hdl_mg_dl', 'triglycerides_mg_dl', 'creatinine_mg_dl',
                      'bmi_ran','insulin_mu_l_ran']

        d = []

        for i in column:
            # Train Transformation
            X_train_nums_cols[i+'yeo'], lambda_value = yeojohnson(X_train_nums_cols[i])

            # Test Transformation using same lambda
            X_test_nums_cols[i+'yeo'] = yeojohnson(X_test_nums_cols[i],lmbda=lambda_value)

            d.append(i+'yeo')

            X_train_nums_cols = X_train_nums_cols.drop([i], axis=1)
            X_test_nums_cols = X_test_nums_cols.drop([i], axis=1)

        '''
        
        for i in d:
            plt.figure(figsize=(8, 5))
            plt.subplot(1, 3, 1)
            plt.title('Normal Distribution')
            X_train_nums_cols[i].plot(kind='kde', color='r')

            plt.subplot(1, 3, 2)
            plt.title('BOXPLOT')
            sns.boxplot(x=X_train_nums_cols[i])

            plt.subplot(1, 3, 3)
            plt.title("Probplot - YEO - Tech")
            stats.probplot(X_train_nums_cols[i], dist="norm", plot=plt)
            plt.legend()
            plt.show()
            
        '''

        logger.info(
            f'After apply Train numerical columns and shapes variable Transformation \n : {X_train_nums_cols.columns} : {X_train_nums_cols.shape}')
        logger.info(
            f'After apply Test numerical columns and shapes variable Transformation \n : {X_test_nums_cols.columns} : {X_test_nums_cols.shape}')

        logger.info(f' ================================== Outliers ============================================')

        original_trimming = ['pregnancies', 'family_history_diabetes', 'hypertension',
       'skin_thickness_mmyeo', 'dbp_mmhgyeo',
       'glucose_mg_dlyeo', 'fasting_glucose_mg_dlyeo', 'ogtt_2hr_mg_dlyeo',
       'hba1c_pctyeo', 'ldl_mg_dlyeo', 'hdl_mg_dlyeo',
       'triglycerides_mg_dlyeo']

        f = []

        for col in original_trimming:
            # Applying the Trimming technique
            iqr = X_train_nums_cols[col].quantile(0.75) - X_train_nums_cols[col].quantile(0.25)
            lower_limit = X_train_nums_cols[col].quantile(0.25) - (1.5 * iqr)
            upper_limit = X_train_nums_cols[col].quantile(0.75) + (1.5 * iqr)
            X_train_nums_cols[col+'_tri'] = np.where(X_train_nums_cols[col] < lower_limit, lower_limit,
                                                        np.where(X_train_nums_cols[col] > upper_limit, upper_limit,
                                                                   X_train_nums_cols[col]))
            X_test_nums_cols[col+'_tri'] = np.where(X_test_nums_cols[col] < lower_limit, lower_limit,
                                                        np.where(X_test_nums_cols[col] > upper_limit, upper_limit,
                                                                  X_test_nums_cols[col]))
            f.append(col+'_tri')


            X_train_nums_cols = X_train_nums_cols.drop([col], axis=1)
            X_test_nums_cols = X_test_nums_cols.drop([col], axis=1)


        original_capping = ['age', 'sbp_mmhgyeo', 'creatinine_mg_dlyeo', 'bmi_ranyeo',
                                'insulin_mu_l_ranyeo']

        for col in original_capping:
            # Applying the Capping mean and Standard
            lower = X_train_nums_cols[col].mean() - 3 * X_train_nums_cols[col].std()
            upper = X_train_nums_cols[col].mean() + 3 * X_train_nums_cols[col].std()
            X_train_nums_cols[col+'_CapMS'] = np.where(X_train_nums_cols[col]< lower, lower,
                                                       np.where(X_train_nums_cols[col] > upper, upper,
                                                       X_train_nums_cols[col]))
            X_test_nums_cols[col+'_CapMS'] = np.where(X_test_nums_cols[col] < lower, lower,
                                                       np.where(X_test_nums_cols[col] > upper, upper,
                                                       X_test_nums_cols[col]))

            f.append(col+'CapMS')

            X_train_nums_cols = X_train_nums_cols.drop([col], axis=1)
            X_test_nums_cols = X_test_nums_cols.drop([col], axis=1)


        '''
        for i in f:
        plt.figure(figsize=(5,3))
        plt.title('BOX_PLOT')
        sns.boxplot(x=X_train_nums_cols[i], color='r')
        plt.legend()
        plt.show()
        
        '''

        logger.info(
            f'After apply Train numerical columns and shapes Outliers \n : {X_train_nums_cols.columns} : {X_train_nums_cols.shape}')
        logger.info(
            f'After apply Test numerical columns and shapes Outliters \n : {X_test_nums_cols.columns} : {X_test_nums_cols.shape}')


        logger.info(f'++++++++++++++++++++++++++++  Feature Selection     ++++++++++++++++++++++++')
        logger.info(f'============================   Constant Technique    =============================')

        # Applying the constant technique with threshold = 0
        var = VarianceThreshold(threshold=0)
        var.fit(X_train_nums_cols)
        logger.info(
            f'Checking the Train Good Column {sum(var.get_support())} : {X_train_nums_cols.columns[var.get_support()]}')
        logger.info(
            f'Checking the Train Bad Column {sum(~var.get_support())} : {X_train_nums_cols.columns[~var.get_support()]}')
        logger.info(
            f'Checking the Test Good Column {sum(var.get_support())} : {X_test_nums_cols.columns[var.get_support()]}')
        logger.info(
            f'Checking the Test Bad Column {sum(~var.get_support())} : {X_test_nums_cols.columns[~var.get_support()]}')

        logger.info(f'=================== Quasi Constant Technique ================================')

        # Applying the Quasi Constant technique with threshold = 1(0.01)
        var = VarianceThreshold(threshold=0.01)
        var.fit(X_train_nums_cols)
        logger.info(
            f'Checking the Train Good Column {sum(var.get_support())} : {X_train_nums_cols.columns[var.get_support()]}')
        logger.info(
            f'Checking the Train Bad Column {sum(~var.get_support())} : {X_train_nums_cols.columns[~var.get_support()]}')
        logger.info(
            f'Checking the Test Good Column {sum(var.get_support())} : {X_test_nums_cols.columns[var.get_support()]}')
        logger.info(
            f'Checking the Test Bad Column {sum(~var.get_support())} : {X_test_nums_cols.columns[~var.get_support()]}')

        logger.info(f'=================== Hypothesis Testing Technique =============================')

        # Applying the Hypothesis Testing Technique
        # Applying the pearson Technique
        logger.info(f'the X_train values {X_train_nums_cols.shape}')
        logger.info(f'the y_train values {y_train.shape}')

        c = []
        for i in X_train_nums_cols.columns:
            result = pearsonr(X_train_nums_cols[i], y_train)
            c.append(result)

        t = np.array(c)

        p_values = pd.Series(t[:, 1], index=X_train_nums_cols.columns)

        p = 0
        f = []

        for i in p_values:
            if i < 0.05:
                f.append(X_train_nums_cols.columns[p])
            p = p + 1

        logger.info(f'Checking the Good Columns: {f}')

        '''
        good_columns =['family_history_diabetes_tri', 'glucose_mg_dlyeo_tri', 'fasting_glucose_mg_dlyeo_tri',
                       'ogtt_2hr_mg_dlyeo_tri','hba1c_pctyeo_tri', 'age_CapMS', 'sbp_mmhgyeo_CapMS', 'bmi_ranyeo_CapMS']
        
        
        bad_columns = ['pregnancies_tri',  'hypertension_tri','skin_thickness_mmyeo_tri','dbp_mmhgyeo_tri',
                       'ldl_mg_dlyeo_tri', 'hdl_mg_dlyeo_tri','triglycerides_mg_dlyeo_tri','creatinine_mg_dlyeo_CapMS', 
                       'insulin_mu_l_ranyeo_CapMS']
        '''

        X_train_nums_cols = X_train_nums_cols.drop(['pregnancies_tri',  'hypertension_tri','skin_thickness_mmyeo_tri','dbp_mmhgyeo_tri',
                       'ldl_mg_dlyeo_tri', 'hdl_mg_dlyeo_tri','triglycerides_mg_dlyeo_tri','creatinine_mg_dlyeo_CapMS',
                       'insulin_mu_l_ranyeo_CapMS'], axis=1)
        X_test_nums_cols = X_test_nums_cols.drop( ['pregnancies_tri',  'hypertension_tri','skin_thickness_mmyeo_tri','dbp_mmhgyeo_tri',
                       'ldl_mg_dlyeo_tri', 'hdl_mg_dlyeo_tri','triglycerides_mg_dlyeo_tri','creatinine_mg_dlyeo_CapMS',
                       'insulin_mu_l_ranyeo_CapMS'], axis=1)

        logger.info(
            f'After apply Train numerical columns and shapes Feature_Selection \n : {X_train_nums_cols.columns} : {X_train_nums_cols.shape}')
        logger.info(
            f'After apply Test numerical columns and shapes Feature_Selection \n : {X_test_nums_cols.columns} : {X_test_nums_cols.shape}')



        return X_train_nums_cols,X_test_nums_cols,y_train

    except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in lineno {er_line.tb_lineno} due to {er_type} and Reason {er_msg}')