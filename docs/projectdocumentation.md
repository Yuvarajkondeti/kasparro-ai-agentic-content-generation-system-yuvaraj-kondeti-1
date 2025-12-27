# Project Documentation  
## Multi-Agent Content Generation System

---

## 1. Problem Statement

The objective of this assignment is to design and implement a **production-style agentic automation system** that converts a fixed product dataset into multiple structured, machine-readable content artifacts.

The challenge is not content writing, but **system design**:
- defining meaningful agents
- orchestrating them correctly
- enforcing structure and determinism
- avoiding monolithic or prompt-only solutions

The system must operate strictly on the provided product data and must not introduce external facts.

---

## 2. Solution Overview

This project implements a **CrewAI-based multi-agent system** where independent agents are coordinated by a central orchestrator to generate structured JSON outputs.

Key design principles:
- agent isolation
- schema-driven outputs
- deterministic orchestration
- transparency over execution failures
- extensibility without refactoring core logic

The system produces:
- FAQ Page
- Product Page
- Comparison Page

All outputs are machine-readable JSON.

---

## 3. Scope & Assumptions

### In Scope
- Backend-only automation system
- Agent-based content generation
- Structured JSON outputs
- Clear documentation and diagrams

### Out of Scope
- UI / frontend
- Databases
- External APIs beyond LLM
- Free-form text or markdown outputs

---

## 4. System Design (MOST IMPORTANT)

### 4.1 High-Level Orchestration

The system follows a **step-based orchestration pipeline**.

![System Orchestration Flow](diagrams/orchestration_flow.png)

Execution flow:
1. Load product data (single source of truth)
2. Initialize CrewAI agents
3. Execute tasks in a controlled sequence
4. Validate outputs structurally
5. Persist JSON artifacts

Agents do not communicate directly.  
All execution is mediated by the orchestrator.

This avoids hidden state and implicit dependencies.

---

### 4.2 Agent Responsibility Model

![Agent Responsibilities](diagrams/agent_responsibilities.png)

Each agent has:
- a single responsibility
- explicit inputs and outputs
- no shared mutable state

| Agent | Responsibility |
|-----|---------------|
| Product Understanding Agent | Interprets and normalizes product data |
| FAQ Generation Agent | Generates categorized FAQs |
| Content Agent | Produces product page content |
| Comparison Agent | Generates structured comparison |
| Quality Gate Agent | Validates structure and constraints |

This separation allows:
- easy replacement of agents
- independent testing
- future extension without refactoring

---

### 4.3 Content Logic, Templates, and Schemas

![Content Blocks and Templates](diagrams/content_blocks_templates.png)

The system explicitly separates:
- **logic** (agents)
- **structure** (schemas)
- **assembly** (orchestration)

Schemas act as contracts:
- enforcing JSON shape
- preventing malformed output
- enabling deterministic validation

Templates are structural definitions, not logic containers.

---

## 5. Execution Modes

### 5.1 Primary Mode — LLM-backed Agent Execution

In normal operation:
- CrewAI agents are backed by an OpenAI LLM
- Content is dynamically generated
- Constraints such as FAQ count and schema shape are enforced

This mode represents the intended production behavior.

---

### 5.2 Fallback Demo Mode (Explicit & Honest)

If LLM execution fails due to **external constraints** (e.g., API quota):

- The system switches to an explicit fallback mode
- Outputs are marked:
  ```json
  "mode": "fallback_demo"
  Data Flow Summary
Input Data
   ↓
Agent Reasoning
   ↓
Schema Validation
   ↓
JSON Output