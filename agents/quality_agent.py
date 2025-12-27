from crewai import Agent

def create_quality_agent(llm):
    return Agent(
        role="Quality Gate Agent",
        goal="Validate generated outputs against structural and content constraints",
        backstory=(
            "You ensure outputs meet minimum requirements such as FAQ count, "
            "schema validity, and category coverage."
        ),
        llm=llm,
        verbose=True
    )