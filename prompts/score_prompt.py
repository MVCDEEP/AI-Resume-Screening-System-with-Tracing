from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match_data"],
    template="""
Based on matching results:

{match_data}

Return:

{
"score": "",
"explanation": ""
}

Rules:

80-100 strong
50-79 average
0-49 weak
"""
)