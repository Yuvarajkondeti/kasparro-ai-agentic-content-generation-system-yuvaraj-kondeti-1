from crewai import Agent

def create_content_agent(llm):
    return Agent(
        role="Product Content Generation Agent",
        goal="Generate structured product page content strictly from validated product data",
        backstory=(
            "You generate structured, machine-readable product descriptions "
            "without adding external information or assumptions."
        ),
        llm=llm,
        verbose=True
    )