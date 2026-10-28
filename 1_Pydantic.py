from pydantic import BaseModel, AnyUrl, EmailStr,  Field
from typing import List, Dict ,Optional

class Patient(BaseModel):
    name: str
    age: int = Field(gt=0, lt=100)
    weight: float = Field(gt=1)
    married: bool
    allergies: List[str]
    site: AnyUrl
    email: Optional[EmailStr] 

def Insert_Patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.site)
    print(patient.email)

    print('insert data')

def Update_Patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Update data')

patient_info = {'name': 'ayan', 'age': 13, 'weight': 45.6, 'married': False, 'allergies': ['Dust', 'chest', 'polen'],
                 'site': "https://fast.com/", 'email': "abc123@gmail.com"}

pat_1 = Patient(**patient_info)

Insert_Patient_data(pat_1)