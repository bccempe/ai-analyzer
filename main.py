from typing import List
from fastapi import FastAPI
from externals.openai import client, model_name
from azure.ai.inference.models import SystemMessage, UserMessage
from models import App, LLM, Evaluator, AppEvaluator, RawPrompt
from repositories.json_repo import REPO

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/generate-debate")
def generate_debate(question: str):
    macro_system_prompt = "Eres un asistente técnico experto. Responde de forma concisa."

    response = client.complete(
        messages=[
            SystemMessage(content=macro_system_prompt),
            UserMessage(content=question),
        ],
        model=model_name,
        temperature=0.7,
        max_tokens=1000
    )

    # 4. Extracción de datos para tu Framework
    print(f"Respuesta de la IA: {response.choices[0].message.content}")
    print(f"Tokens usados: {response.usage.total_tokens}")
    return {"response": response.choices[0].message.content}

# JSON repository-backed endpoints
@app.get("/apps", response_model=List[App])
def list_apps():
    return REPO.list_apps()


@app.get("/llms", response_model=List[LLM])
def list_llms():
    return REPO.list_llms()


@app.get("/evaluators", response_model=List[Evaluator])
def list_evaluators():
    return REPO.list_evaluators()


@app.get("/app-evaluators", response_model=List[AppEvaluator])
def list_app_evaluators():
    return REPO.list_app_evaluators()


@app.get("/raw-prompts", response_model=List[RawPrompt])
def list_raw_prompts():
    return REPO.list_raw_prompts()