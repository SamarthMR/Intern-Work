import pandas as pd
df=pd.read_csv("Iris.csv").drop(columns=['Id'])

from sklearn.preprocessing import LabelEncoder
df['Species'] = LabelEncoder().fit_transform(df['Species'])

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=['Species']), df['Species'], test_size=0.3)

from sklearn.svm import SVC
SVM = SVC(kernel = 'linear').fit(x_train, y_train)

import pickle
pickle.dump(SVM, open("Iris.pkl", "wb"))