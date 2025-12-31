from crewai import Agent, Task

def comparison_agent(llm, product_data):
    agent = Agent(
        role="Comparison Reasoning Agent",
        goal="Generate a logical fictional comparison product and compare it",
        backstory=(
            "You generate a fictional but logically consistent alternative product "
            "using the same schema as the original."
        ),
        llm=llm,
        verbose=True
    )

    task = Task(
        agent=agent,  # ✅ REQUIRED
        description=(
            "Create a fictional Product B logically comparable to the given product. "
            "Then produce a structured comparison using the same schema for both products. "
            "Product B must NOT be hardcoded."
        ),
        expected_output=(
            "Valid JSON with structure: "
            "{ product_a: {...}, product_b: {...} }"
        )
    )

    return agent, task
