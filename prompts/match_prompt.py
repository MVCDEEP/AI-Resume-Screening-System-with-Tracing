from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["resume_data","job_description"],
    template="""
Compare resume with job description.

Return JSON:

{
"matched_skills": [],
"missing_skills": []
}

Resume:
{resume_data}

Job:
{job_description}

Do NOT assume skills.
"""
)