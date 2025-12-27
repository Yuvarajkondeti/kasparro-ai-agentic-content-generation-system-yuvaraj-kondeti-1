from crewai import Agent

def create_product_agent(llm):
    return Agent(
        role="Product Understanding Agent",
        goal="Understand and normalize the input product data into a clean internal representation",
        backstory=(
            "You analyze raw product input data and ensure it is logically consistent, "
            "well-structured, and suitable for downstream content generation agents."
        ),
        llm=llm,
        verbose=True
    )