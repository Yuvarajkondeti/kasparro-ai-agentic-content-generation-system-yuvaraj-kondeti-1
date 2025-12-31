from crewai import Crew, Process
from agents.faq_agent import faq_agent
from agents.comparison_agent import comparison_agent
from agents.quality_agent import quality_agent

def create_crew(llm, product_data):
    faq_a, faq_t = faq_agent(llm, product_data)
    comp_a, comp_t = comparison_agent(llm, product_data)
    qual_a, qual_t = quality_agent(llm)

    crew = Crew(
        agents=[faq_a, comp_a, qual_a],
        tasks=[faq_t, comp_t, qual_t],
        process=Process.sequential
    )

    return crew
