from crewai import Agent, Task

def quality_agent(llm):
    agent = Agent(
        role="Quality Gate Agent",
        goal="Validate generated content against constraints",
        backstory=(
            "You act as the final gatekeeper. "
            "If content violates any rule, you must FAIL the system."
        ),
        llm=llm,
        verbose=True
    )

    task = Task(
        agent=agent,  # ✅ REQUIRED
        description=(
            "Validate the generated content. Enforce the following:\n"
            "- FAQ count must be >= 15\n"
            "- No duplicate questions\n"
            "- All required fields must be non-empty\n"
            "If ANY rule fails, respond with an error and DO NOT approve."
        ),
        expected_output="Validation approval or failure message"
    )

    return agent, task
