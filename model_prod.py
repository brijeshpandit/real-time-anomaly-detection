import random
from joblib import dump

import numpy as np
from sklearn.ensemble import IsolationForest

def model():    
    rng = np.random.RandomState(100)

    # Generating random train data
    X = 0.3 * rng.randn(500, 1)
    X_train = np.r_[X + 2]
    X_train = np.round(X_train, 3)

    # fit the model
    clf = IsolationForest(n_estimators=50, max_samples=500, random_state=rng, contamination=0.01)
    clf.fit(X_train)

    # saving the trained model file
    dump(clf, './model_isolation_forest.joblib')