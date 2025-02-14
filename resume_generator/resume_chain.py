from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
from utils.prompt_templates import RESUME_USER_PROMPT

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Use the updated ChatOpenAI class
llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=api_key)

def generate_resume(job_description, candidate_info, template,key_details):
    resume_prompt = PromptTemplate.from_template(RESUME_USER_PROMPT)
    resume_chain = LLMChain(llm=llm, prompt=resume_prompt)
    
    resume = resume_chain.run(job_description=job_description, candidate_info=candidate_info, template=template,key_details = key_details)
    return resume
