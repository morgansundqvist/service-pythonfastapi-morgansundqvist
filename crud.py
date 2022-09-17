import json

from schemas import Skill, WorkExperience

WORK_EXPERIENCE_JSON = """
[
  {
    "id": "4741e341-c368-487f-b9bb-b2963b729049",
    "startDate": "2006-06",
    "endDate": "2007-10",
    "company": "Software Innovation AB",
    "role": "Developer",
    "keyFacts": [
      "Developer within CRM domain worked with large clients such as H&M"
    ]
  },
  {
    "id": "f8cd529e-6b0e-446c-aac0-bcd00bd6967e",
    "startDate": "2007-10",
    "endDate": "2012-12",
    "company": "Annata AB",
    "role": "Development team lead / ERP Specialist",
    "keyFacts": [
      "Development team lead, onboarding and mentoring new developer",
      "Functonal ERP specialist within Automotive, Logistics, Inventory management and Financials"
    ]
  },
  {
    "id": "2790b8bf-72c5-45af-a6e5-d5aaf0053f4f",
    "startDate": "2012-12",
    "endDate": "2014-07",
    "company": "Pingdom (pingdom.com)",
    "role": "CTO",
    "keyFacts": [
      "Reponsible for development and operation of Pingdom",
      "Inventor of patents within monitoring analytics",
      "Responsible for 20+ DevOps fantastic colleagues",
      "Journey from 30 000 to 600 000 customers"
    ]
  },
  {
    "id": "0eab7d44-e54b-4247-9bbf-541a15320aa4",
    "startDate": "2014-07",
    "endDate": "2017-09",
    "company": "Orango AB / Annata AB",
    "role": "Microsoft Dynamics 365 F&O ERP Specialist",
    "keyFacts": [
      "Responsible for complete ERP projects",
      "Technical lead",
      "Certified in Dynamics Ax 3, Dynamics Ax 2009 and Dynamics 365 F&O",
      "Financial, Logistics, Inventory Management ,Automotive, Accounts Recievable, Accounts Payable domains"
    ]
  },
  {
    "id": "92cdeaa1-ef45-4f39-90a5-eb84f721c2a0",
    "startDate": "2017-09",
    "endDate": "2021-06",
    "company": "Dooer AB (dooer.com, voitto.se)",
    "role": "CTO",
    "keyFacts": [
      "Product owner and architect for Saas platform, 150+ micro services, CI/CD, GDPR",
      "Product owner for bookkeeping service",
      "Product owner for backoffice system",
      "Manager for 30+ fantastic DevOps colleagues"
    ]
  },
  {
    "id": "21666b47-1e86-4372-86cb-28d6f055b6d3",
    "startDate": "2021-07",
    "endDate": "Present",
    "company": "Volvo Construction Equipment AB",
    "role": "Senior IT Solution Architect / Product owner",
    "keyFacts": [
      "Architect within Connected Services domain",
      "Working with digital services for IOT data from all connected machines",
      "Product owner and architect for creating a micro service architectural pattern and platform"
    ]
  }
]
"""

SKILLS_JSON = """
[
  {
    "id": "72787bb9-c5db-42b5-ba4b-5b0efeaa1b09",
    "category": "Business",
    "skill": "Leadership"
  },
  {
    "id": "4135c021-bf68-463c-b08a-d70d7075e4ef",
    "category": "Business",
    "skill": "Financial"
  },
  {
    "id": "4c299720-54c6-46c4-8922-108e055bfb80",
    "category": "Business",
    "skill": "Accounting"
  },
  {
    "id": "f515a5df-b81c-4241-9a69-58937bb9a515",
    "category": "Business",
    "skill": "Logistics"
  },
  {
    "id": "2cdf3448-6c94-4cc8-b61c-dc298bd84e63",
    "category": "Business",
    "skill": "Project management"
  },
  {
    "id": "9ff7fcea-d1fc-44f3-af97-f802e722da74",
    "category": "Business",
    "skill": "Stakeholder management"
  },
  {
    "id": "478b9287-a377-4bcf-b8f7-e4939e708ea0",
    "category": "IT",
    "skill": "ERP implementation"
  },
  {
    "id": "f69818ea-1d04-4712-808d-81d0bde5e85d",
    "category": "IT",
    "skill": "TOGAF"
  },
  {
    "id": "e4766c92-873f-4819-bee2-87aee317b572",
    "category": "IT",
    "skill": "Software Architecture"
  },
  {
    "id": "b9402181-6135-4d3c-ad67-758336af0f8b",
    "category": "IT",
    "skill": "SCRUM"
  },
  {
    "id": "b9402181-6135-4d3c-ad67-758336af0f8b",
    "category": "IT",
    "skill": "Agile Kanban"
  },
  {
    "id": "c09393f4-ac3b-41d5-8337-26d90675c4fb",
    "category": "Programming languages",
    "skill": ".Net C#"
  },
  {
    "id": "f8b0c228-86b6-4ba4-9efe-cd035b898aa2",
    "category": "Programming languages",
    "skill": "Python"
  },
  {
    "id": "97c6ab7a-3f9a-44ac-82b6-5b5cf33f1d46",
    "category": "Programming languages",
    "skill": "JavaScript (TypeScript, React, NodeJS)"
  },
  {
    "id": "e1085582-8a47-45e6-8230-9034295390ee",
    "category": "Programming languages",
    "skill": "Go"
  }
]
"""


def get_work_experiences()-> list[WorkExperience]:
    """Returns all of Morgans work experience in a very condenced format

    Returns:
        list[schemas.WorkExperience]: WorkExperience type as list
    """

    response_dict = json.loads(WORK_EXPERIENCE_JSON)
    return response_dict

def get_skills() -> list[Skill]:
    """Reurns some of Morgans skills he has aquired over his working life

    Returns:
        list[Skill]: _description_
    """

    respose_dict = json.loads(SKILLS_JSON)
    return respose_dict
