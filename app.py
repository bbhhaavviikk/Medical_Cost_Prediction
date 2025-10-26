from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import joblib

app = FastAPI()
model = joblib.load('./model/insurance_model.pkl')


def preprocess_input(data):
    sex_map = {"male": 1, "female": 0}
    smoker_map = {"yes": 1, "no": 0}
    region_map = {"southeast": 0, "southwest": 1, "northeast": 2, "northwest": 3}

    try:
        sex = sex_map[data["sex"].lower()]
        smoker = smoker_map[data["smoker"].lower()]
        region = region_map[data["region"].lower()]
    except KeyError as e:
        raise ValueError(f"Invalid categorical value: {e}")

    return [[
        data["age"],
        sex,
        data["bmi"],
        data["children"],
        smoker,
        region
    ]]

@app.get("/")
async def hey():
    return "Hey"


@app.get("/health")
async def health():
    """Health check route to verify the server is running."""
    return {"status": "ok"}

@app.post("/api/predict")
async def predict_cost(request: Request):
    try:
        data = await request.json()
        required_fields = ["age", "sex", "bmi", "children", "smoker", "region"]
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return JSONResponse(
                status_code=400,
                content={"error": f"Missing fields: {', '.join(missing_fields)}"}
            )

        # Preprocess input before prediction
        features = preprocess_input(data)
        prediction = model.predict(features)[0]

        return {
            "message": "Prediction made successfully",
            "predicted_cost": float(prediction)
        }

    except ValueError as ve:
        return JSONResponse(
            status_code=400,
            content={"error": f"Invalid input: {str(ve)}"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Something went wrong: {str(e)}"}
        )