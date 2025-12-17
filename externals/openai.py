import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

# 1. Configuración (Usa tu token de GitHub)
token = ""
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o" # Puedes usar "Llama-3-70b", "Phi-3-mini", etc.

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)