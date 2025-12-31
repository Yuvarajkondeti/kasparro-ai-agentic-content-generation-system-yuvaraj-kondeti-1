from crewai import Agent, Task

def faq_agent(llm, product_data):
    agent = Agent(
        role="FAQ Reasoning Agent",
        goal="Generate and reason over user FAQs from product data",
        backstory=(
            "You analyze product attributes and generate meaningful user questions. "
            "You must ensure sufficient coverage and avoid duplication."
        ),
        llm=llm,
        verbose=True
    )

    task = Task(
        agent=agent,  # ✅ BIND AGENT HERE
        description=(
            "Generate AT LEAST 15 unique FAQs based ONLY on the product data. "
            "Each FAQ must include a question, answer, and category. "
            "If you cannot generate 15, FAIL."
        ),
        expected_output=(
            "Valid JSON with structure: "
            "{ product_name: string, faqs: [ {question, answer, category} ] }"
        )
    )

    return agent, task
