## Medical Cost Prediction

### Overview

This project predicts individual medical insurance costs using a trained machine learning model. It includes data, training notebooks, and a simple Flask app to expose predictions.

### Repository structure (key files)

- app.py - Flask application to serve predictions
- requirements.txt - Python dependencies for the server
- model/ - trained model and related artifacts
- training/ - notebooks and scripts used to prepare data and train the model

### Prerequisites

- Python 3.8 or newer
- pip

### Quick setup

1. (Optional) Create and activate a virtual environment

   python -m venv myvenv
   # Windows PowerShell
   .\myvenv\Scripts\Activate.ps1

2. Install dependencies

   pip install -r requirements.txt

3. Verify model artifacts

   Ensure the trained model files exist in the `model/` directory. If they are not present, run the training notebook in `training/` to produce them.

#### Run the server

1. From the `Medical-Cost-Prediction` directory, run:

```
   uvicorn app:app --reload
```

2. The Flask app will start and expose an endpoint for predictions (refer to `app.py` for the exact route and payload format).

Usage

- Send a POST request with the expected JSON payload to the prediction endpoint. See `app.py` for the input fields and response format.

*Notes*


- If you update model or preprocessing code, retrain and export artifacts to the `model/` directory before running the server.
