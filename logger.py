import os
import time
from datetime import datetime
import logging 

def logger(fold, name):
    
    log_folder = fold
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    current_time = datetime.utcnow().isoformat().replace(":","_")

    log_file_path = os.path.join(log_folder, f'{name}_{current_time}.log')
    file_handler = logging.FileHandler(log_file_path)

    logging.getLogger('').addHandler(file_handler)