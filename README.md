# Efficient Data Stream Anomaly Detection

This Python project focuses on developing a robust script for detecting anomalies in continuous data streams, simulating real-time sequences of floating-point numbers with visualization and logging. The data stream could represent diverse metrics, such as financial transactions or system performance metrics.


## Process

**Train Unsupervised Anomaly Detection Model:**
   - Develop a machine learning model for anomaly detection without labeled data.
   - Save the model for real-time predictions.

**Generate Fake Streaming Data:**
   - Simulate a continuous data stream with synthetic data.
   - Send the data for real-time analysis.

**Real-time Anomaly Detection:**
   - Analyze the streaming data using the pre-trained model.
   - Identify anomalies in the data stream.

**Real-time Visualization:**
   - Implement a real-time visualization tool to display the data stream and detected anomalies.
   - Enhances monitoring and understanding of patterns within the data.

**Print Anomalies to Console:**
   - Display detected anomalies directly in the console.
   - Simplifies the process for quick observation and debugging.


## Model Selection


For the anomaly detection tasks in this project, Isolation Forest has been selected as the primary algorithm due to its specific advantages:

- **Unsupervised Learning:** Isolation Forest excels in anomaly detection without the need for labeled data, making it suitable for scenarios with limited labeled instances.

- **Scalability:** Known for its scalability, Isolation Forest efficiently handles large datasets and performs well in high-dimensional spaces, crucial for processing continuous data streams.

- **Tree-Based Efficiency:** Isolation Forest's tree-based approach, constructing a random forest of isolation trees, is effective in capturing irregularities and isolating anomalies efficiently.

- **Adaptability to Concept Drift:** The algorithm adapts well to concept drift, accommodating changes in the statistical properties of data over time, a critical factor in real-time applications.

- **Efficiency in Anomaly Detection:** Isolation Forest's ability to identify anomalies with shorter paths in trees contributes to its efficiency, making it a practical choice for real-time detection where speed is essential.

## Usage

- Adjust the parameters in the **settings.py** file according to the project specifications. Presently, three configurable parameters are available:
  - `DELAY`: Time interval for the generation of random data.
  - `OUTLIERS_GEN_PROB`: Probability of outlier generation.
  - `VISUALIZATION`: Set to True if visualization is desired.

- Install project dependencies
    ```bash
    pip install -r requirements.txt
    ```

- Execute the **main.py** script to initiate model training and anomaly detection.
    ```bash
    python main.py
    ```
  - By default, **model_prod.py** and **anomaly.py** are invoked from **main.py**.
## Dependencies

- Python 3.x
- joblib
- matplotlib
- numpy
- scikit-learn