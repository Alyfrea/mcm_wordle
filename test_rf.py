from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import explained_variance_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('question2.csv')
# y = df.drop(columns=['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'ex_1'])
y = df['ex'].values
x = df.drop(columns=['ex', 'dx', 'ex_1'])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)
rfc = RandomForestRegressor(n_estimators=100).fit(x_train, y_train)
y_pre = rfc.predict(x_test)
# print(explained_variance_score(y_pre, y_test))
# print(rfc.score(x_test, y_test))
plt.figure(figsize=(20, 8))
plt.plot(list(range(y_train.size)), y_train)
plt.plot([item * 4 for item in range(y_test.size)], y_test)
plt.savefig('./ans.png')
# importances = rfc.feature_importances_
# feat_labels = x.columns[::-1]
# indices = np.argsort(importances)[::-1]
# for ind in indices:
#     print(f'{feat_labels[ind]:<25s}{importances[ind]:.6f}')
# frac = importances[indices[:5]]
# labels = feat_labels[indices[:5]]
# frac = np.append(frac, 1 - np.sum(frac))
# labels = np.append(labels, 'others')
# colors = np.array(['black'] + ['grey'] * 5)
# explode = np.array([0.1] + [0] * 5)
# plt.pie(frac, labels=labels, colors=colors, explode=explode)
# plt.show()
# drops = ['DX_bl', 'Month']
# xd = df.drop(columns=drops)
# xd_train, xd_test, y_train, y_test = train_test_split(xd, y, test_size=.2)
# rfcd = RandomForestClassifier().fit(xd_train, y_train)
# y_pre = rfcd.predict(xd_test)
# print(classification_report(y_pre, y_test))
# importances = rfcd.feature_importances_
# feat_labels = xd.columns[::-1]
# indices = np.argsort(importances)[::-1]
# for ind in indices:
#     print(f'{feat_labels[ind]:<25s}{importances[ind]:.6f}')
# y_pre = rfcd.predict_proba(xd_test)
# fig, axs = plt.subplots(2, 3, figsize=(60, 40))
# dg_line = np.array([0, 1])
# for i in range(5):
#     ax = axs[i // 3, i % 3]
#     y_true = np.array([int(item == i + 1) for item in y_test])
#     fpr, tpr, threshold = roc_curve(y_true, y_score=y_pre[:, i])
#     ax.plot(fpr, tpr, color='black', label=f'AUC={auc(fpr, tpr):.3f}')
#     ax.plot(dg_line, dg_line, linestyle='--', color='grey')
#     ax.set_facecolor('white')
#     ax.legend(loc='lower right', fontsize=45, facecolor='white')
#     ax.spines[:].set_color('black')
# axs[1, 2].axis('off')
