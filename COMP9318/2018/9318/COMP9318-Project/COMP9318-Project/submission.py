import helper
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report


def fool_classifier(test_data):  ## Please do not change the function defination...
    ## Read the test data file, i.e., 'test_data.txt' from Present Working Directory...

    ## You are supposed to use pre-defined class: 'strategy()' in the file `helper.py` for model training (if any),
    #  and modifications limit checking
    strategy_instance = helper.strategy()
    parameters = {}

    x = []
    for sentence in strategy_instance.class0:
        x.append(' '.join(word for word in sentence))
    for sentence in strategy_instance.class1:
        x.append(' '.join(word for word in sentence))
    x_1 = np.array(strategy_instance.class0)
    x_2 = np.array(strategy_instance.class1)
    y_1 = np.zeros(x_1.shape)
    y_2 = np.ones(x_2.shape)
    y = np.concatenate((y_1, y_2))
    Y = list(y)

    def my_tokenizer(s):
        return s.split()

    cv = CountVectorizer(tokenizer=my_tokenizer, binary=True)
    X1 = cv.fit_transform(x).toarray()
    tf = TfidfTransformer().fit(X1)
    X = tf.transform(X1)

    features = cv.get_feature_names()

    parameters = {'gamma': 'auto', 'C': 2, 'kernel': 'linear', 'degree': 3, 'coef0': 0.0}

    clf = strategy_instance.train_svm(parameters, X, Y)

    # clf = grid.best_estimator_
    clf.fit(X, Y)
    with open(test_data, 'r') as test:
        test_list = [line.strip().split(' ') for line in test]
    x_test_list = []
    for sentence in test_list:
        x_test_list.append(' '.join(word for word in sentence))
    x_count = cv.transform(x_test_list).toarray()
    # tf1 = TfidfTransformer().fit(x_count)
    x_tfidf = tf.transform(x_count).toarray().tolist()
    idf = list(tf.idf_)

    dic = {}
    theta = list(clf.coef_.toarray()[0])
    for i in range(len(features)):
        dic[features[i]] = (theta[i], idf[i])

    order1 = []

    for x in dic:
        if dic[x][0] < 0:
            order1.append((x, dic[x][0] * dic[x][1]))
    order2 = tuple(order1)
    for i in range(len(test_list)):
        order = list(order2)
        for j in range(len(test_list[i])):
            if test_list[i][j] in features:
                order.append((test_list[i][j], dic[test_list[i][j]][0] * dic[test_list[i][j]][1]))
        order.sort(key=lambda x: abs(x[1]), reverse=True)

        count = 0

        for x in order:
            if x[1] > 0:
                # print(x[1])
                while True:
                    if x[0] not in test_list[i]:
                        break
                    test_list[i].remove(x[0])
                    if x[0] not in test_list[i]:
                        count += 1
                        break
            if count >= 20:
                break
        if count < 20:
            for x in order:
                if x[1] < 0:
                    if x[0] not in test_list[i]:
                        test_list[i].append(x[0])
                        count += 1
                if count == 20:
                    break

    with open('./modified_data.txt', 'w') as f:
        for x in test_list:
            f.writelines(' '.join(y for y in x) + ' ' + '\n')
    ##..................................#
    #
    #
    #
    ## Your implementation goes here....#
    #
    #
    #
    ##..................................#

    ## Write out the modified file, i.e., 'modified_data.txt' in Present Working Directory...

    ## You can check that the modified text is within the modification limits.
    modified_data = './modified_data.txt'
    assert strategy_instance.check_data(test_data, modified_data)
    return (clf, cv, tf)  ## NOTE: You are required to return the instance of this class.
