import numpy as np

# Please replace "StudentMatriculationNumber" with your actual matric number here and in the filename
def A3_AxxxxxxxN(learning_rate, num_iters):
    """
    Input type
    :learning_rate type: float
    :num_iters type: int

    Return type
    :a_out type: numpy array of length num_iters
    :f1_out type: numpy array of length num_iters
    :b_out type: numpy array of length num_iters
    :f2_out type: numpy array of length num_iters
    :c_out type: numpy array of length num_iters
    :d_out type: numpy array of length num_iters
    :f3_out type: numpy array of length num_iters
    """
    # your code goes here
    a = 2.5
    b = 0.5
    c = 2.0 
    d = 4.0 

    #a^5; sin^2 b; c^3 + d^2 sin d

    a_out = np.zeros(num_iters)
    f1_out = np.zeros(num_iters)
    b_out = np.zeros(num_iters)
    f2_out = np.zeros(num_iters)
    c_out = np.zeros(num_iters)
    d_out = np.zeros(num_iters)
    f3_out= np.zeros(num_iters)

    for i in range(num_iters):
        grad_a = 5*a*a*a*a
        a = a - learning_rate * grad_a
        a_out[i] = a
        f1_out[i] = a*a*a*a*a

        grad_b = 2 * np.sin(b) * np.cos(b)
        b = b - learning_rate * grad_b
        b_out[i] = b
        f2_out[i] = np.sin(b)**2

        grad_c = 3*c **2 
        grad_d = d**2 * np.cos(d) + 2*d * np.sin(d)
        c = c - learning_rate * grad_c
        d = d - learning_rate * grad_d 
        c_out[i] = c
        d_out[i] = d
        f3_out[i] = c**3 + d**2 * np.sin(d)

    # return in this order
    return a_out, f1_out, b_out, f2_out, c_out, d_out, f3_out 

print(A3_AxxxxxxxN(0.1, 10))
