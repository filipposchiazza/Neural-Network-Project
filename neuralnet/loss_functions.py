#Define different types of Loss functions
import numpy as np


clip_value = 1e-15
###############################################################################

# Binary Cross Entropy is used for binary classification tasks

def binary_cross_entropy(prediction, target):
    "Binary Cross Entropy loss function"
    # Use np.clip in order to avoid nan problems when evaluating np.log()
    prediction = np.clip(prediction, a_min=clip_value, a_max=1-clip_value)
    term_1 = target * np.log(prediction)
    term_2 = (1 - target) * np.log(1 - prediction)
    return -(term_1 + term_2)


def binary_cross_entropy_deriv(prediction, target):
    "Derivative of the Binary Cross Entropy"
    # Use np.clip in order to avoid nan problems when evaluating the fraction target/prediction
    prediction = np.clip(prediction, a_min=clip_value, a_max=1-clip_value)
    term_1 = target / prediction 
    term_2 = (1 - target) / (1 - prediction)
    return term_2 - term_1

###############################################################################

# Cross entropy is used for multiple-class classification tasks

def cross_entropy(prediction, target):
    "Cross Entropy loss function"
    # Use np.clip in order to avoid nan problems when evaluating np.log()
    prediction = np.clip(prediction, a_min=clip_value, a_max=1)
    log = np.log(prediction)
    ylog = target * log
    return -np.sum(ylog)


def cross_entropy_deriv(prediction, target):
    "Derivative of the Cross Entropy"
    # Use np.clip in order to avoid nan problems when evaluating the fraction target/prediction
    prediction = np.clip(prediction, a_min=clip_value, a_max=1)
    return - target/prediction

###############################################################################
