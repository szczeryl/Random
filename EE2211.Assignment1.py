import numpy as np

# I blurred out the last 4 numbers of my matric number for privacy purposes
# Please replace "MatricNumber" with your actual matric number here and in the filename
def A1_A028xxxxN(X, y):
    """
    Input type
    :X type: numpy.ndarray
    :y type: numpy.ndarray

    Return type
    :InvXTX type: numpy.ndarray
    :w type: numpy.ndarray

    """
    XT = np.transpose(X)
    XTX = XT @ X
    InvXTX = np.linalg.inv(XTX)
    w = InvXTX @ XT @ y

    pass

    # return in this order
    return InvXTX, w





   
