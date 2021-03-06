import numpy as np
from typing import List
from classifier import Classifier

class DecisionStump(Classifier):
    def __init__(self, s:int, b:float, d:float):
        self.clf_name = "Decision_stump"
        self.s = s
        self.b = b
        self.d = d

    def train(self, features: List[List[float]], labels: List[int]):
        pass
        
    def predict(self, features: List[List[float]]) -> List[int]:
        ##################################################
        # TODO: implement "predict"
        ##################################################
        a=[]
        for X in features:
            if X[self.d]>self.b:
                a.append(self.s)
            else:
                a.append(-1*self.s)
        return a