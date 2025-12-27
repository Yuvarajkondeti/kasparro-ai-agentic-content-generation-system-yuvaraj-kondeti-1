from crewai import Agent

def create_comparison_agent(llm):
    return Agent(
        role="Product Comparison Agent",
        goal="Generate a structured comparison between the given product and a fictional alternative",
        backstory=(
            "You compare two products using the same schema. "
            "The second product must be fictional but logically structured."
        ),
        llm=llm,
        verbose=True
    )