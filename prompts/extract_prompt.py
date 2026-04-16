from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
You are an AI resume parser.

Extract ONLY explicitly mentioned:

1. Skills
2. Tools
3. Years of Experience

Return JSON format:

{{
"skills": [],
"tools": [],
"experience": ""
}}

Resume:
{resume}

IMPORTANT:
Do NOT assume skills not present in the resume.
Only extract what is written.
"""
)