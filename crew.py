import json
from crewai import Crew, Task
from agents.faq_agent import create_faq_agent
from schemas.faq_schema import FAQPage

def create_crew(llm, product_data):
    faq_agent = create_faq_agent(llm)

    faq_task = Task(
        description=f"""
        You are given the following product data.

        Your task:
        1. Generate AT LEAST 15 FAQs.
        2. Categorize each FAQ into one of the following:
           - informational
           - usage
           - safety
           - pricing
           - comparison
        3. Do NOT add external facts.
        4. Output MUST be valid JSON matching this schema:
           {FAQPage.schema_json()}

        Product Data:
        {json.dumps(product_data)}
        """,
        expected_output="Valid JSON matching FAQPage schema with at least 15 FAQs",
        agent=faq_agent
    )

    return Crew(
        agents=[faq_agent],
        tasks=[faq_task],
        verbose=True
    )