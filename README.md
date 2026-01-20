# BMI Calculator Agent

This project demonstrates a basic Agentic AI system implemented in Python without using any Large Language Model (LLM).
The agent maintains internal state, performs calculations, makes decisions, and resets itself after each execution.

---

## Overview

The BMI Calculator Agent:
- Accepts user weight and height
- Calculates Body Mass Index (BMI)
- Determines fitness category
- Stores data inside agent state
- Resets state after each run

This project is designed to teach agent-based thinking and state management before moving to LLM or Google ADK agents.

---

## Agent State

The agent uses a structured state defined with TypedDict.

AgentState structure:

- weight: float or None
- height: float or None
- bmi: float or None
- fitness: string or None

The state represents the agent’s internal memory during execution.

---

## Agent Logic

### BMI Calculation

BMI is calculated using the formula:

BMI = weight / (height * height)

---

### Fitness Classification Rules

- BMI < 18.5        → Underweight
- 18.5 ≤ BMI < 25  → Healthy
- 25 ≤ BMI < 30    → Overweight
- BMI ≥ 30         → Obese

---

## Code Structure

BMI Calculator/

│

├── basic_agent.py

├── fitness_check_BMI.py

└── README.md

---

## How to Run

Activate the virtual environment (if applicable):

source .venv/bin/activate

Run the program:

python basic_agent.py

---

## Sample Input and Output

Input:

Enter weight (kg): 70  
Enter height (meters): 1.75  

Output:

BMI = 22.857142857142858  
Fitness = Healthy  

Exit the program:

Enter weight (kg): exit

---

## Why This Is Agentic AI

- The agent owns and manages its internal state
- Decisions are made using deterministic logic
- No external AI or LLM is involved
- The agent can be reused and reset
- The structure is production-ready

---

## Possible Future Enhancements

- Store agent state in a database
- Add BMI history tracking
- Convert agent to asynchronous execution
- Integrate Google ADK
- Expand into multi-agent systems

---

## Author

Aniket Yalmalwar
