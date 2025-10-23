import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import OneHotEncoder
from numpy.linalg import inv



# Please replace "MatricNumber" with your actual matric number here and in the filename
def A2_A02xxxxxN(N):
    """
    Input type
    :N type: int

    Return type
    :X_train type: numpy.ndarray of size (number_of_training_samples, 4)
    :y_train type: numpy.ndarray of size (number_of_training_samples,)
    :X_test type: numpy.ndarray of size (number_of_test_samples, 4)
    :y_test type: numpy.ndarray of size (number_of_test_samples,)
    :Ytr type: numpy.ndarray of size (number_of_training_samples, 3)
    :Yts type: numpy.ndarray of size (number_of_test_samples, 3)
    :Ptrain_list type: List[numpy.ndarray]
    :Ptest_list type: List[numpy.ndarray]
    :w_list type: List[numpy.ndarray]
    :error_train_array type: numpy.ndarray
    :error_test_array type: numpy.ndarray
    """
    # your code goes here
    random_state = N
    test_size = 0.6
    lamdaa = 0.0001

    iris_data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris_data['data'], iris_data['target'], test_size = test_size, random_state = random_state)
    one_hot_encoder = OneHotEncoder(sparse_output = False)

    reshaped_training = y_train.reshape(len(y_train),1)
    Ytr = one_hot_encoder.fit_transform(reshaped_training)
    reshaped_testing = y_test.reshape(len(y_test),1)
    Yts = one_hot_encoder.fit_transform(reshaped_testing)

    Ptrain_list = CreateRegressor(X_train, 8)
    Ptest_list = CreateRegressor(X_train, 8)

    w_list = []

    for i in Ptrain_list: 
        if i.shape[0] >= i.shape[1]:
            w = inv(i.T @ i + lamdaa*np.identity(i.shape[1])) @ i.T @ Ytr
            w_list.append(w)
        else:
            w = i.T @ inv(i @ i.T + lamdaa*np.identity(i.shape[0])) @ Ytr
            w_list.append(w)
    
    y_training_argmax = [] 
    y_test_argmax = [] 
    for i in range(0,8):
        y_training_est_p = Ptrain_list[i] @ w_list [i]
        y_training_cls_p = y_training_est_p.argmax(axis = 1)
        y_training_argmax.append(y_training_cls_p)

        y_test_est_p = Ptest_list[i] @ w_list[i]
        y_test_cls_p = y_test_est_p.argmax(axis = 1)
        y_test_argmax.append(y_test_cls_p)

    
    error_train_array = [] 
    for j in y_training_argmax: 
        error_train_array.append(sum(j !=j))    

    error_test_array = [] 
    for k in y_test_argmax:
        error_test_array.append(sum(y_test != y_test))
    
    error_train_array = np.array(error_train_array)
    error_test_array = np.array(error_test_array)

    # return in this order
    return X_train, y_train, X_test, y_test, Ytr, Yts, Ptrain_list, Ptest_list, w_list, error_train_array, error_test_array

def CreateRegressor (x, max_ord):
    P = []
    
    for ord in range (1, max_ord + 1):
        P_current_regressors = PolynomialFeatures(ord).fit_transform(x)
        P.append(P_current_regressors)

    return P


#print(A2_A0282042N(5))
