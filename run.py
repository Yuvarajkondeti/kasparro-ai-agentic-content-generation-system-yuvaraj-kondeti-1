from dotenv import load_dotenv
load_dotenv()

import json
from crewai import LLM
from crew import create_crew

with open("data/product.json") as f:
    product_data = json.load(f)

llm = LLM(model="gpt-4o-mini")

output = None
execution_mode = "llm"

try:
    crew = create_crew(llm, product_data)
    output = crew.kickoff()
except Exception as e:
    print("⚠️ LLM execution failed. Switching to fallback demo mode.")
    print(f"Reason: {e}")
    execution_mode = "fallback"

if execution_mode == "llm":
    with open("outputs/faq.json", "w") as f:
        f.write(output)
else:
    # ---------------- FALLBACK MODE ----------------
    print("⚠️ Running in fallback demo mode (LLM quota unavailable)")

    # FAQ PAGE (fallback)
    faq_output = {
        "mode": "fallback_demo",
        "reason": "LLM quota unavailable",
        "product_name": product_data["product_name"],
        "faqs": [
            {
                "question": f"What is {product_data['product_name']}?",
                "answer": "This product information is derived strictly from the provided dataset.",
                "category": "informational"
            },
            {
                "question": "What is the concentration of Vitamin C?",
                "answer": product_data["concentration"],
                "category": "informational"
            },
            {
                "question": "Which skin types is it suitable for?",
                "answer": ", ".join(product_data["skin_type"]),
                "category": "safety"
            },
            {
                "question": "How should the product be used?",
                "answer": product_data["how_to_use"],
                "category": "usage"
            },
            {
                "question": "What is the price of the product?",
                "answer": f"₹{product_data['price']}",
                "category": "pricing"
            }
        ]
    }

    with open("outputs/faq.json", "w") as f:
        json.dump(faq_output, f, indent=2)

    # PRODUCT PAGE (fallback)
    product_page_output = {
        "mode": "fallback_demo",
        "reason": "LLM quota unavailable",
        "product_name": product_data["product_name"],
        "concentration": product_data["concentration"],
        "key_ingredients": product_data["key_ingredients"],
        "benefits": product_data["benefits"],
        "how_to_use": product_data["how_to_use"],
        "side_effects": product_data["side_effects"],
        "skin_type": product_data["skin_type"],
        "price": product_data["price"]
    }

    with open("outputs/product_page.json", "w") as f:
        json.dump(product_page_output, f, indent=2)

    # COMPARISON PAGE (fallback)
    comparison_output = {
        "mode": "fallback_demo",
        "reason": "LLM quota unavailable",
        "product_a": {
            "name": product_data["product_name"],
            "ingredients": product_data["key_ingredients"],
            "benefits": product_data["benefits"],
            "price": product_data["price"]
        },
        "product_b": {
            "name": "RadiantC Serum X (Fictional)",
            "ingredients": ["Vitamin C"],
            "benefits": ["Brightening"],
            "price": 799
        }
    }

    with open("outputs/comparison_page.json", "w") as f:
        json.dump(comparison_output, f, indent=2)