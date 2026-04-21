from langchain.prompts import PromptTemplate

template = """
You are a quality inspection expert.

Given the following defect summary:

{summary}

Identify:
1. Critical issues
2. Recommendations

Return in this EXACT format:

Critical Issues:
- point 1
- point 2

Recommendations:
- point 1
- point 2
"""

prompt = PromptTemplate(
    input_variables=["summary"],
    template=template
)