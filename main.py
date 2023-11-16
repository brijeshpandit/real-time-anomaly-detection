from model_prod import model
from anomaly import anomaly_dect

if __name__ == '__main__':
    model()             # Training the model first
    anomaly_dect()      # Running the anomayl.py script for anomaly detection
    