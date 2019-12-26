class BaseClassifier(object):
    """base class for the intent classifier"""
    #name: ""

    @classmethod
    def load(cls, *args):
        """load the model based on the args"""
        return cls(*args)

    def train(self,*args):
        """train a model"""
        pass
    
    def persist(self, model_dir_path):
        """store the model"""
        pass
    
    def predict(self, expression):
        """predict the probability and label"""
        pass