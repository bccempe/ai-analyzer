from pydantic import BaseModel

class App(BaseModel):
    id: int
    name: str

class LLM(BaseModel):
    id: int
    name: str

class Evaluator(BaseModel):
    id: int
    type: str
    llm_id: int
    system_prompt: str

class AppEvaluator(BaseModel):
    id: int
    app_id: int
    evaluator_id: int

class RawPrompt(BaseModel):
    id: int
    app_id: int
    question: str
    response: str
    temperature: int

class MetricResponse(BaseModel):
    score: int