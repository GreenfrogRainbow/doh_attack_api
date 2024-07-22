import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import pickle
import joblib

file = "..csv"   #此处为输入数据的路径

df = pd.read_csv(file)

# 删除缺失值和重复值
df = df.dropna()
df = df.drop_duplicates()
# 删除指定列
df = df.drop(['SourceIP', 'DestinationIP', 'TimeStamp'], axis=1)
feature_names = df.columns

# 提取特征和标签
X = df.drop('Label',axis=1)

y = df.Label
# 标签编码
label_encoder = joblib.load('label_encoder.pkl')
y = label_encoder.transform(y)

# # 假设 y 是编码前的原始标签
# original_labels = label_encoder.inverse_transform(y)
with open('./StandardScaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
X = scaler.transform(X)


X_test,y_test=X,y

# 定义加载路径
load_path = "./stacking_classifier_model_new.pkl"

# 加载模型
with open(load_path, 'rb') as f:
    loaded_model = pickle.load(f)

y_pred = loaded_model.predict(X_test)


# 评估模型
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f'Precision: {precision:.5f}')
print(f'Recall: {recall:.5f}')
print(f'F1-score: {f1:.5f}')
print('Confusion Matrix:')
print(conf_matrix)
print('Classification Report:')
print(class_report)


import seaborn as sns
from sklearn.metrics import confusion_matrix

# 计算混淆矩阵
cm = confusion_matrix(y_test, y_pred)

# 可视化混淆矩阵
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='d',
            xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()
