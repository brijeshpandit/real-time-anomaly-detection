import os
import random
import time
from datetime import datetime
from joblib import load
import logging
import matplotlib.pyplot as plt
import numpy as np
from logger import logger

from settings import DELAY, OUTLIERS_GENERATION_PROBABILITY, VISUALIZATION

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger("logs","anomaly")

data_ls = []

def anomaly_dect():
    _id = 0
    
    if VISUALIZATION:
        fig = plt.figure(figsize=(8,4))
        ax = fig.add_subplot()
        ax.set_facecolor('#011627')
        fig.suptitle('Real Time Anomaly Detection')
        fig.show()
    
    while True:
        # Generating some abnormal observations
        if random.random() <= OUTLIERS_GENERATION_PROBABILITY:
            X_test = np.random.uniform(low=-4, high=4, size=(1, 1))
        else:
            X = 0.3 * np.random.randn(1, 1)
            X_test = (X + np.random.choice(a=[2, -2], size=1, p=[0.5, 0.5]))

        X_test = np.round(X_test, 3).tolist()

        current_time = datetime.utcnow().isoformat()

        record = {"id": _id, "data": X_test, "current_time": current_time}
        print(f"Incoming: {record}")

        try:
            model_path = os.path.abspath("isolation_forest.joblib")
            clf = load(model_path)
        except:
            logging.warning(f"Model file not found")
            print(f'Model file not available')
            break

        data = record['data']        
        data_ls.append(data[0][0])
        prediction = clf.predict(data)

        if VISUALIZATION:
            plt_ds = ax.plot(data_ls,color='#41EAD4',label='Data Stream')              
            ax.set_xlabel('Record id')
            ax.set_ylabel('Data')
            ax.grid(True, linestyle='--', alpha=0.2,)                
            if _id==0:
                ax.legend()
            fig.canvas.draw()
            ax.set_xlim(left=0, right=_id+2) 
            
        if prediction[0] == -1:
            score = clf.score_samples(data)
            record["score"] = np.round(score, 3).tolist()
            if VISUALIZATION:
                plt.scatter(_id,data_ls[_id],color='#fc0d1b',linewidth=4, label='Anomaly')
                ax.legend(['Data Stream','Anomaly'],loc='upper left')
            logging.info(f"Anomaly Detected : {record}")
            print(f'Anamoly Detected : {record}')
            
        _id += 1
        plt.pause(DELAY)
        # time.sleep(DELAY)
    plt.show()