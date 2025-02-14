from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
from utils.prompt_templates import COVER_LETTER_USER_PROMPT

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Use the updated ChatOpenAI class
llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=api_key)

def generate_cover_letter(job_description, candidate_info,key_details):
    cover_letter_prompt = PromptTemplate.from_template(COVER_LETTER_USER_PROMPT)
    cover_letter_chain = LLMChain(llm=llm, prompt=cover_letter_prompt)
    
    cover_letter = cover_letter_chain.run(job_description=job_description, candidate_info=candidate_info,key_details = key_details)
    return cover_letter
