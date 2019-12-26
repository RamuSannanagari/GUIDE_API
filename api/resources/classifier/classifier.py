import io, os, sys

from .base import BaseClassifier
from api.errors import RaiseError
from api import log

from collections import OrderedDict

"""get the logger"""
log = log.get_logger()

class FidBobClassifier(BaseClassifier):
    """name of the classifier"""
    name = "fid_intent_classifier"

    def __init__(self, t_vector=None, lr_model=None, ncf=None):
        """constructor to init the fid classifier"""
        self.ncf = ncf

    def predict(self, expression=None):
        """expression for which we run the model against to derive the intent"""
        confidence_score = 0
        intent = None

        #intent, confidence_score = self.ncf(expression)
        intent, confidence_score = "Test",100
        l_msg = "model found : {} and score is {}".format(intent, confidence_score)
        log.debug(l_msg)

        return intent, confidence_score