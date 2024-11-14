from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

class Input(BaseModel):
    city: str
    city_development_index: float
    gender: str
    relevent_experience: str
    enrolled_university: str
    education_level: str
    major_discipline: str
    experience: str
    company_size: str
    company_type: str
    last_new_job: str
    training_hours: int

class Output(BaseModel):
    target: int

@app.post("/predict", response_model=Output)
def predict(data_input: Input) -> Output:
    x_input = pd.DataFrame([{
        'city': data_input.city,
        'city_development_index': data_input.city_development_index,
        'gender': data_input.gender,
        'relevent_experience': data_input.relevent_experience,
        'enrolled_university': data_input.enrolled_university,
        'education_level': data_input.education_level,
        'major_discipline': data_input.major_discipline,
        'experience': data_input.experience,
        'company_size': data_input.company_size,
        'company_type': data_input.company_type,
        'last_new_job': data_input.last_new_job,
        'training_hours': data_input.training_hours,
    }])
    
    model = joblib.load('jobchg_pipeline_model.pkl')
    prediction = model.predict(x_input)[0]  # Get the single prediction value
    return Output(target=int(prediction))
