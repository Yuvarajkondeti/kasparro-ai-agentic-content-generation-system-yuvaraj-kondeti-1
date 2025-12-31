import os
import json
import time
from dotenv import load_dotenv
from crewai import LLM
from crew import create_crew

load_dotenv()

MAX_RETRIES = 2


def run_with_llm_or_fail():
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY not found. System cannot run without LLM.")

    with open("data/product.json") as f:
        product_data = json.load(f)

    llm = LLM(model="gpt-4o-mini")

    last_error = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"Attempt {attempt}: Executing agent pipeline with LLM...")
            crew = create_crew(llm, product_data)
            result = crew.kickoff()

            if not result:
                raise RuntimeError("LLM returned empty result")

            return result

        except Exception as e:
            last_error = e
            print(f"LLM execution failed on attempt {attempt}: {e}")
            time.sleep(2)

    raise RuntimeError(
        f"System aborted after {MAX_RETRIES} failed LLM attempts. "
        f"No outputs were generated. Last error: {last_error}"
    )


if __name__ == "__main__":
    output = run_with_llm_or_fail()

    # Outputs must ONLY be written after successful LLM execution
    os.makedirs("outputs", exist_ok=True)

    with open("outputs/final_output.json", "w") as f:
        f.write(output)

    print("Pipeline executed successfully with LLM.")
