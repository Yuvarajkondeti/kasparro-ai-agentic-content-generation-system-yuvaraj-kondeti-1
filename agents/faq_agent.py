from crewai import Agent

def create_faq_agent(llm):
    return Agent(
        role="FAQ Generation Agent",
        goal="Generate at least 15 high-quality, categorized FAQs strictly from the given product data",
        backstory=(
            "You are a reliable AI agent responsible for generating structured FAQ content. "
            "You must not hallucinate or add external information. "
            "All questions and answers must be derived strictly from the provided product data."
        ),
        llm=llm,
        verbose=True
    )