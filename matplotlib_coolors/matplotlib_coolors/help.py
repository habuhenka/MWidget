def imp(void=0):
  if void == 90811:
    print(
"""from sklearn.metrics import r2_score

from sklearn.svm import SVR
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor"""
    )

def imp2(void=0):
  if void == 90811:
    print(
"""from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from sklearn.svm import SVC
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier"""
    )

def imp3(void=0):
  if void == 90811:
    print(
"""from sklearn.metrics import calinski_harabasz_score, silhouette_score

from sklearn.cluster import KMeans, AgglomerativeClustering"""
    )

def hypr(void=0):
  if void == 90811:
    print(
"""grid = {
    'depth'         : [4,5,6,7,8,9,10],
    'learning_rate' : [0.01,0.02,0.03,0.04],
    'iterations'    : [10,20,30,40,50,60,70,80,90,100]}

grid2 = {
    'max_depth': [3, 6, 9],
    'max_leaf_nodes': [3, 6, 9],
    'n_estimators': [25, 50, 100, 150],
    'max_features': ['sqrt', 'log2', None]}

RandomizedSearchCV(rfr, grid2, n_jobs=-1)
GridSearchCV(estimator=model, param_grid=grid, cv=5, n_jobs=-1)
"""
    )