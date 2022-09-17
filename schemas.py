from pydantic import BaseModel

class WorkExperience(BaseModel):
    id: str
    startDate: str
    endDate: str
    company: str
    role: str
    keyFacts: list[str]


class Skill(BaseModel):
    id: str
    category: str
    skill: str