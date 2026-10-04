from pathlib import Path
import pickle

MODEL_PATH = Path(__file__).with_name("pipeline.bin")

CLIENT = {
    "lead_source": "paid_ads",
    "industry": "technology",
    "employment_status": "employed",
    "location": "north_america",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
    "interaction_count": 4,
    "lead_score": 0.41,
}

with MODEL_PATH.open("rb") as f_in:
    dv, model = pickle.load(f_in)

X = dv.transform([CLIENT])

prob = float(model.predict_proba(X)[0, 1])

print(f"Conversion probability: {prob:.3f}")
