from flask import Blueprint, render_template, request
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.linear_model import LinearRegression

pd.options.mode.chained_assignment = None  # default='warn'

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/form', methods = ['get', 'post'])
def form():
    from ucimlrepo import fetch_ucirepo

    # fetch dataset
    heart_disease = fetch_ucirepo(id=45)

    # data (as pandas dataframes)
    X = heart_disease.data.features
    y = heart_disease.data.targets

    # # metadata
    # print(heart_disease.metadata)

    # # variable information
    # print(heart_disease.variables)

    # print(X.head())

    # print(X['sex'].value_counts())

    # print(y.head())

    # print(y.value_counts())

    # X.shape

    # y.shape

    # print(X.info())

    X['ca'] = X['ca'].fillna(value = X['ca'].mode()[0])

    X['thal'] = X['thal'].fillna(value = X['thal'].mode()[0])

    # print(X.info())

    X_np = X.to_numpy()
    # print(type(X_np[0][0]))
    y_np = y['num'].to_numpy()

    X_train, X_test, y_train, y_test = train_test_split(X_np, y_np, test_size = 0.2)

    knn = KNeighborsClassifier(n_neighbors = 7)

    knn.fit(X_train, y_train)
    # print(knn.score(X_test, y_test))

    if request.method == 'POST':
        data = np.array(list(request.form.to_dict().values())).astype(np.float64)
        data_shaped = np.reshape(data, (1, -1))
        pred = knn.predict(data_shaped)

        temp = "hello"        
        if pred == 0:
            temp = "You're good!"
        else:
            temp = "You should see a doctor."

        return render_template('result.html', content = temp) 
        
    return render_template('form.html')

@views.route('/result')
def result():
    return render_template('result.html')