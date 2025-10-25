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

## Example Request

Below are example requests showing how to call the prediction endpoint (`/api/predict`) with JSON input. The server (when started with the command above) listens by default at `http://127.0.0.1:8000`.

### curl

Replace values in the JSON with the person you want to predict for. Make sure the server is running.

```bash
curl -X POST "http://127.0.0.1:8000/api/predict" \
   -H "Content-Type: application/json" \
   -d '{
      "age": 29,
      "sex": "female",
      "bmi": 27.9,
      "children": 1,
      "smoker": "no",
      "region": "northeast"
   }'
```

### Postman (or any HTTP client)

In Postman, create a new POST request to `http://127.0.0.1:8000/api/predict` and set the request body type to `raw` -> `JSON`. Use the same JSON payload as above:

```json
{
   "age": 29,
   "sex": "female",
   "bmi": 27.9,
   "children": 1,
   "smoker": "no",
   "region": "northeast"
}
```

### Example response

On success the endpoint returns JSON with the predicted cost, for example:

```json
{
   "message": "Prediction made successfully",
   "predicted_cost": 4235.72
}
```

If required fields are missing or invalid, the API returns a 400 error with an explanation. For unexpected server errors a 500 response is returned.

*Notes*


- If you update model or preprocessing code, retrain and export artifacts to the `model/` directory before running the server.
