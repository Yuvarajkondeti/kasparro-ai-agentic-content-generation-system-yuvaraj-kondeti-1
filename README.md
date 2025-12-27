 Kasparro AI Agentic Content Generation System
Overview

This repository implements a modular, agentic content generation system designed to transform a fixed product dataset into structured, machine-readable JSON content pages.

The system is built using a real agent framework (CrewAI) and is architected to demonstrate:

clear agent boundaries

deterministic orchestration

schema-driven outputs

extensibility and maintainability

production-style system thinking

This is a backend / automation system, not a UI or prompt-only project.

 Objective

Given a fixed product dataset as the only source of truth, the system autonomously generates:

faq.json

product_page.json

comparison_page.json

using an agent-orchestrated pipeline.

No external facts or assumptions are introduced.

 High-Level Architecture
System Orchestration Flow

The system follows a step-based orchestration model where a central orchestrator coordinates independent agents.

Flow:

Input Product Data

Product Understanding Agent

FAQ Generation Agent

Content Generation Agent

Comparison Agent

Quality Gate Agent

Structured JSON Outputs

Agents do not call each other directly.
All execution is controlled by the orchestrator.

 Agent Design

Each agent has one clear responsibility, explicit inputs, and no shared global state.

Agents Implemented
Agent	Responsibility
Product Understanding Agent	Normalize and reason over product input
FAQ Generation Agent	Generate categorized FAQs
Content Generation Agent	Generate product page content
Comparison Agent	Compare product with fictional alternative
Quality Gate Agent	Validate structure and constraints
Agent Responsibility Separation

This separation ensures:

modularity

testability

easy extension

 Content Logic & Templates

Business logic is not embedded in templates.

Logic → agents & reusable blocks

Structure → schemas & templates

Content Block Composition

This allows new pages to be added without modifying existing agents.

 Schema-Driven Design

All outputs conform to explicit schemas (Pydantic):

FAQPage

Product

ComparisonPage

Schemas act as:

contracts between agents

validation boundaries

safeguards against malformed outputs

 Execution Modes
Primary Mode — LLM-Backed Agent Execution

Uses CrewAI agents

Backed by OpenAI LLM

Dynamic content generation

Constraint-aware orchestration

Fallback Demo Mode (Explicit)

If LLM execution fails due to external constraints (e.g., API quota):

System switches to explicit fallback demo mode

Outputs are clearly marked:

"mode": "fallback_demo"


Fallback exists only to allow pipeline observability

It does not replace the primary LLM workflow

This design ensures transparency and avoids fake or deceptive outputs.

 Repository Structure
.
├── agents/
│   ├── product_agent.py
│   ├── faq_agent.py
│   ├── content_agent.py
│   ├── comparison_agent.py
│   └── quality_agent.py
│
├── schemas/
│   ├── product_schema.py
│   ├── faq_schema.py
│   └── comparison_schema.py
│
├── data/
│   └── product.json
│
├── outputs/
│   ├── faq.json
│   ├── product_page.json
│   └── comparison_page.json
│
├── crew.py
├── run.py
├── README.md
└── docs/
    ├── projectdocumentation.md
    └── diagrams/

 How to Run
1. Create virtual environment
python -m venv venv
venv\Scripts\activate

2. Install dependencies
pip install crewai crewai-tools openai pydantic python-dotenv

3. Add API key

Create .env:

OPENAI_API_KEY=your_key_here

4. Run
python run.py


Outputs will be generated in the outputs/ directory.

 Outputs

All outputs are:

clean JSON

machine-readable

schema-aligned

No UI, no free-form text.

 What This System Is NOT

 Not a prompt-only script

 Not a UI / frontend app

 Not a hardcoded content generator

 Not a monolithic Python script

This is a system design and agent orchestration exercise.

 Final Notes

This project emphasizes:

correctness over cleverness

architecture over output prettiness

honesty over shortcuts

The system is designed to be reviewed, extended, and maintained — not just executed once.