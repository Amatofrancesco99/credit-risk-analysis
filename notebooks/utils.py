from sklearn.metrics import  accuracy_score, classification_report


# Function that takes a MScore and cast it into an integer value (0 means a low credit risk, 1 an high credit risk)
def MScore_to_int(x):
    return 0 if (str(x[0]).lower() in ['a', 'b']) else 1


# Function to print the overall performance metrics of a model
def print_performances(name, classifier, X_train, y_train, X_test, y_test):
    y_predict_train = classifier.predict(X_train)
    y_predict_test = classifier.predict(X_test)
    print(name + '\n - Train accuracy: ' + str(round(accuracy_score(y_train, y_predict_train) * 100, 1)) + '%')
    print(' - Test accuracy: '+ str(round(accuracy_score(y_test, y_predict_test) * 100, 1)) + '%')
    print('\nTest '+str(classification_report(y_test, y_predict_test)))