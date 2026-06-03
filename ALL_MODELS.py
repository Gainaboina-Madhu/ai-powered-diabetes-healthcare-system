import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import os
import seaborn as sns
import logging
from logging_code import setup_logging
logger = setup_logging("All_Models_code")
import sys
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.metrics import roc_auc_score,roc_curve

def knn(X_train,y_train,X_test,y_test):
    global knn_reg
    knn_reg = KNeighborsClassifier(n_neighbors=5)
    knn_reg.fit(X_train, y_train)
    predictions = knn_reg.predict(X_test)
    logger.info(confusion_matrix(y_test, predictions))
    logger.info(accuracy_score(y_test, predictions))
    logger.info(classification_report(y_test, predictions))
    global knn_predictions
    knn_predictions = knn_reg.predict(X_test)


def nb(X_train,y_train,X_test,y_test):
    global nb_reg
    global nb_reg
    nb_reg = GaussianNB()
    nb_reg.fit(X_train, y_train)
    predictions = nb_reg.predict(X_test)
    logger.info(confusion_matrix(y_test, predictions))
    logger.info(accuracy_score(y_test, predictions))
    logger.info(classification_report(y_test, predictions))
    global nb_predictions
    nb_predictions = nb_reg.predict(X_test)

def lr(X_train,y_train,X_test,y_test):
    global lr_reg
    lr_reg = LogisticRegression()
    lr_reg.fit(X_train,y_train)
    predictions = lr_reg.predict(X_test)
    logger.info(confusion_matrix(y_test,predictions))
    logger.info(accuracy_score(y_test,predictions))
    logger.info(classification_report(y_test,predictions))
    global lr_predictions
    lr_predictions = lr_reg.predict(X_test)


def dt(X_train,y_train,X_test,y_test):
    global dt_reg
    dt_reg = DecisionTreeClassifier(criterion='entropy')
    dt_reg.fit(X_train,y_train)
    predictions = dt_reg.predict(X_test)
    logger.info(confusion_matrix(y_test,predictions))
    logger.info(accuracy_score(y_test,predictions))
    logger.info(classification_report(y_test,predictions))
    global dt_predictions
    dt_predictions = dt_reg.predict(X_test)

def rf(X_train,y_train,X_test,y_test):
    global rf_reg
    rf_reg = RandomForestClassifier(criterion='entropy',n_estimators=5)
    rf_reg.fit(X_train,y_train)
    predictions = rf_reg.predict(X_test)
    logger.info(confusion_matrix(y_test,predictions))
    logger.info(accuracy_score(y_test,predictions))
    logger.info(classification_report(y_test,predictions))
    global rf_predictions
    rf_predictions = rf_reg.predict(X_test)

def adab(X_train,y_train,X_test,y_test):
    global ada_reg
    lr = LogisticRegression()
    ada_reg = AdaBoostClassifier(n_estimators=5)
    ada_reg.fit(X_train,y_train)
    predictions = ada_reg.predict(X_test)
    logger.info(confusion_matrix(y_test,predictions))
    logger.info(accuracy_score(y_test,predictions))
    logger.info(classification_report(y_test,predictions))
    global ada_predictions
    ada_predictions = ada_reg.predict(X_test)

def gb(X_train,y_train,X_test,y_test):
    global gr_reg
    gr_reg = GradientBoostingClassifier(n_estimators=5)
    gr_reg.fit(X_train,y_train)
    predictions = gr_reg.predict(X_test)
    logger.info(confusion_matrix(y_test,predictions))
    logger.info(accuracy_score(y_test,predictions))
    logger.info(classification_report(y_test,predictions))
    global gb_predictions
    gb_predictions = gr_reg.predict(X_test)

def xgb(X_train,y_train,X_test,y_test):
    global xgb_reg
    xgb_reg = XGBClassifier(n_estimators = 5)
    xgb_reg.fit(X_train,y_train)
    predictions = xgb_reg.predict(X_test)
    logger.info(confusion_matrix(y_test,predictions))
    logger.info(accuracy_score(y_test,predictions))
    logger.info(classification_report(y_test,predictions))
    global xgb_predictions
    xgb_predictions = xgb_reg.predict(X_test)

def svm(X_train,y_train,X_test,y_test):
  global sv_reg
  sv_reg = SVC(kernel = 'rbf')
  sv_reg.fit(X_train,y_train)
  predictions = sv_reg.predict(X_test)
  logger.info(confusion_matrix(y_test,predictions))
  logger.info(accuracy_score(y_test,predictions))
  logger.info(classification_report(y_test,predictions))
  global svm_predictions
  svm_predictions = sv_reg.predict(X_test)

from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc


def auc_roc_tech(X_train, y_train, X_test, y_test):

    # ===================== Binarize Output ======================

    classes = np.unique(y_test)

    y_test_bin = label_binarize(y_test, classes=classes)

    n_classes = y_test_bin.shape[1]


    models = {

        'KNN': knn_reg,
        'NB': nb_reg,
        'LR': lr_reg,
        'DT': dt_reg,
        'RF': rf_reg,
        'ADA': ada_reg,
        'GB': gr_reg,
        'XGB': xgb_reg

    }


    plt.figure(figsize=(10, 7))


    for model_name, model in models.items():

        # probability prediction
        y_prob = model.predict_proba(X_test)

        # micro-average ROC curve
        fpr, tpr, _ = roc_curve(
            y_test_bin.ravel(),
            y_prob.ravel()
        )

        roc_auc = auc(fpr, tpr)

        plt.plot(
            fpr,
            tpr,
            label=f'{model_name} AUC = {roc_auc:.3f}'
        )


    plt.plot([0, 1], [0, 1], 'k--')

    plt.xlabel("False Positive Rate")

    plt.ylabel("True Positive Rate")

    plt.title("Multi-Class ROC-AUC Curve")

    plt.legend(loc='lower right')

    plt.show()

def common(X_train,y_train,X_test,y_test):
    try:
        logger.info('-----------knn----------------')
        knn(X_train, y_train, X_test, y_test)
        logger.info('-----------Naive Bayes----------------')
        nb(X_train, y_train, X_test, y_test)
        logger.info('-----------LR----------------')
        lr(X_train, y_train, X_test, y_test)
        logger.info('-----------dt----------------')
        dt(X_train, y_train, X_test, y_test)
        logger.info('-----------rf----------------')
        rf(X_train, y_train, X_test, y_test)
        logger.info('-----------adaboost----------------')
        adab(X_train, y_train, X_test, y_test)
        logger.info('-----------gradient boosting----------------')
        gb(X_train, y_train, X_test, y_test)
        logger.info('-----------xtreme GB----------------')
        xgb(X_train, y_train, X_test, y_test)
        # logger.info('-----------SVM----------------')
        # svm(X_train, y_train, X_test, y_test)
        logger.info('------------AUC and ROC-----------------')
        auc_roc_tech(X_train,y_train,X_test,y_test)

        return X_train,y_train,X_test,y_test



    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        logger.info(f"Error in line no : {er_line.tb_lineno} due to : {er_msg}")