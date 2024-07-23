import pandas as pd
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
source_path = os.path.join(BASE_DIR, 'static')
pkls_path = os.path.join(source_path, 'pkls')


def doh_predict(file_path):
    df = pd.read_csv(file_path)

    # 删除缺失值和重复值
    df = df.dropna()
    df = df.drop_duplicates()
    # 删除指定列
    df = df.drop(['SourceIP', 'DestinationIP', 'TimeStamp'], axis=1)
    feature_names = df.columns
    # 提取特征和标签
    X = df.drop('Doh', axis=1)

    with open(os.path.join(pkls_path, 'StandardScaler.pkl'), 'rb') as f:
        scaler = pickle.load(f)

    X = scaler.transform(X)
    X_test = X

    # 定义加载路径
    load_path = "stacking_classifier_model_new.pkl"

    # 加载模型
    with open(os.path.join(pkls_path, load_path), 'rb') as f:
        loaded_model = pickle.load(f)

    y_pred = loaded_model.predict_proba(X_test)
    return y_pred