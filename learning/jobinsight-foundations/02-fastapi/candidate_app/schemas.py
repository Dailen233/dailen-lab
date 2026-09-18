from pydantic import BaseModel, Field

class CandidateInput(BaseModel):
    name: str = Field(min_length=1, max_length=30)
    target_job: str = Field(min_length=1, max_length=50)


class CandidateResponse(BaseModel):
    id: int
    name: str
    target_job: str


class CandidateListResponse(BaseModel):
    total: int
    data: list[CandidateResponse]


class CandidateDeleteResponse(BaseModel):
    message: str
    data: CandidateResponse


class StudyAdviceInput(BaseModel):
    target_job: str = Field(min_length=1, max_length=50)


class StudyAdviceResponse(BaseModel):
    target_job: str
    advice: str

