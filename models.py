from pydantic import BaseModel

class App(BaseModel):
    id: str
    name: str