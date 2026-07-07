import os
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.workflow import Context
import asyncio

# Core engine execution
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
Settings.llm = GoogleGenAI(model="gemini-2.5-flash", temperature=0.1)

print("[✓] RAG Agent infrastructure compiled successfully.")
