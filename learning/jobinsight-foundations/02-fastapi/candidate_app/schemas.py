from pydantic import BaseModel, Field, ConfigDict

class CandidateInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

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
    model_config = ConfigDict(str_strip_whitespace=True)

    target_job: str = Field(min_length=1, max_length=50)


class StudyAdviceResponse(BaseModel):
    target_job: str
    advice: str

