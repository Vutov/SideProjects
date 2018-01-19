import numpy as np
import pandas as pd

def setup_data():
    file = 'titanic_data.csv'
    full_data = pd.read_csv(file)
    survived = full_data['Survived']
    data = full_data.drop('Survived', axis=1)

    print(full_data)

    return {'survived': survived, 'full_data': data}


def accuracy_score(truth, pred):
    if len(truth) == len(pred):
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean() * 100)

    else:
        return "Number of predictions does not match number of outcomes!"


def prediction_0(data):
    """ Model with no features. Always predicts a passenger did not survive. """

    predictions = []
    for _, passanger in data.iterrows():
        predictions.append(0)

    return pd.Series(predictions)


def prediction_1(data):
    """ Model with one feature:
            - Predict a passenger survived if they are female. """

    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'female':
            predictions.append(1)
        else:
            predictions.append(0)

    return pd.Series(predictions)


def prediction_2(data):
    """ Model with two features:
                - Predict a passenger survived if they are female.
                - Predict a passenger survived if they are male and younger than 10. """

    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'female':
            predictions.append(1)
        else:
            if passenger['Age'] < 10:
                predictions.append(1)
            else:
                predictions.append(0)

    return pd.Series(predictions)


def prediction_3(data):
    """ Model with multiple features. Makes a prediction with an accuracy of at least 80%. """

    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'female':
            if passenger['Pclass'] != 3 or passenger['Age'] > 48 or passenger['Fare'] <= 23:
                predictions.append(1)
                continue
        else:
            if passenger['Age'] < 10 or passenger['Fare'] >= 500:
                predictions.append(1)
                continue

        predictions.append(0)

    return pd.Series(predictions)


data = setup_data()
prediction_data = prediction_3(data['full_data'])
print(accuracy_score(data['survived'], prediction_data))