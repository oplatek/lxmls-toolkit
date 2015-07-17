import numpy as np
import scipy as scipy
import lxmls.classifiers.linear_classifier as lc
import sys
from lxmls.distributions.gaussian import *
from itertools import izip

eps = 0.001

class MultinomialNaiveBayes(lc.LinearClassifier):

    def __init__(self,xtype="gaussian"):
        lc.LinearClassifier.__init__(self)
        self.trained = False
        self.likelihood = 0
        self.prior = 0
        self.smooth = False
        self.smooth_param = 1
        
    def train(self,x,y):
        # n_docs = no. of documents
        # n_words = no. of unique words    
        n_docs, n_words = x.shape
        
        # classes = a list of possible classes
        classes = np.unique(y)
        # n_classes = no. of classes
        n_classes = np.unique(y).shape[0]
        
        # prior[0] is the prior probability of a document being of class 0
        prior = np.ones(n_classes)  # add one smoothing
        for c in y:
            prior[c] += 1
        prior = prior / np.sum(prior)
        assert np.abs(np.sum(prior) - 1) < eps

        
        # likelihood[4, 0] is the likelihood of the fifth(*) feature being 
        # active, given that the document is of class 0
        # (*) recall that Python starts indices at 0, so an index of 4 
        # corresponds to the fifth feature!
        likelihood = np.ones((n_words,n_classes))  # add one smoothing
        # compute counts
        for doc_i, [c] in izip(range(n_docs), y):
            for w in x[doc_i]:
                likelihood[w, c] += 1 
        # normalize in respect to class
        for class_i in range(likelihood.shape[1]):
            class_occ = np.sum(likelihood[:, class_i])
            likelihood[:, class_i] /= float(class_occ)

        assert np.abs(np.sum(likelihood[:,0]) - 1) < eps

        params = np.zeros((n_words+1,n_classes))
        for i in xrange(n_classes):
            params[0,i] = np.log(prior[i])
            params[1:,i] = np.nan_to_num(np.log(likelihood[:,i]))
        self.likelihood = likelihood
        self.prior = prior
        self.trained = True
        return params
