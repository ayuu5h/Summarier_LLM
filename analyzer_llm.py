from langchain_community.llms import Ollama
from prompt_template import prompt

llm = Ollama(model="llama3.2", temperature=0)

def analyze_with_llm(summary):
    try:
        final_prompt = prompt.format(summary=summary)
        response = llm.invoke(final_prompt)

        return response.strip()

    except Exception:
        return "Error generating insights"