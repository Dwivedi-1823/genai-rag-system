# import os
# from dotenv import load_dotenv
# from langchain_openai import OpenAIEmbeddings

# load_dotenv() # Manually pull variables from .env

# def get_embeddings():
#     api_key = os.getenv("OPENAI_API_KEY")
#     return OpenAIEmbeddings(api_key=api_key)
#     # return OpenAIEmbeddings(
#     #     openai_api_key=os.getenv("OPENAI_API_KEY")
#     # )
# import os
# from langchain_google_genai import GoogleGenerativeAIEmbeddings

# def get_embeddings():
#     return GoogleGenerativeAIEmbeddings(
#         model="models/embedding-001",
#         google_api_key=os.getenv("GOOGLE_API_KEY")
#     )
from langchain_community.embeddings import FakeEmbeddings


def get_embeddings():
    return FakeEmbeddings(size=1536)