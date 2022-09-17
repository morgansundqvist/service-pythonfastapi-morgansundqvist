from typing import Union

from fastapi import FastAPI

from crud import get_skills, get_work_experiences
from schemas import Skill, WorkExperience

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/work-experience", response_model=list[WorkExperience])
def read_work_experience():
    """Controller for the REST API end point of getting work experience for Morgan Sundqvist

    Returns:
        _type_: _description_
    """
    return get_work_experiences()

@app.get("/skill", response_model=list[Skill])
def read_skills():
    """Controller for REST API end point of getting skills for Morgan Sundqvist

    Returns:
        _type_: _description_
    """
    return get_skills()