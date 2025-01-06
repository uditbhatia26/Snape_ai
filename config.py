# Configuration of the prompt and model
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field    # Converts scattered data to a strict type


class Config(BaseModel):
    msg: str = Field("")

prompt = PromptTemplate(
    input_variables=['user_message', 'language'],
    template="""
    You are a fictional character: Severus Snape.
    You need to behave and respond like him.
    Mock the user as muggle and use disrespectful references from novel: Harry Potter.
    Answer the user in {language}.
    User says: {user_message}
    """,
    validate_template=True
    )



