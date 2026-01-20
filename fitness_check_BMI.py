from typing import TypedDict, Optional


class AgentState(TypedDict):
    weight: Optional[float]
    height: Optional[float]
    bmi: Optional[float]
    fitness: Optional[str]


class BMIAgent:
    def __init__(self) -> None:
        self.state: AgentState = {
            "weight": None,
            "height": None,
            "bmi": None,
            "fitness": None,
        }

    def reset(self) -> None:
        self.state["weight"] = None
        self.state["height"] = None
        self.state["bmi"] = None
        self.state["fitness"] = None

    def calculate(self, weight: float, height: float) -> None:
        self.state["weight"] = weight
        self.state["height"] = height
        self.state["bmi"] = weight / (height ** 2)
        self.fit_check()

    def fit_check(self) -> None:
        bmi = self.state["bmi"]

        if bmi < 18.5:
            self.state["fitness"] = "Underweight"
        elif bmi < 25:
            self.state["fitness"] = "Healthy"
        elif bmi < 30:
            self.state["fitness"] = "Overweight"
        else:
            self.state["fitness"] = "Obese"

def main() -> None:
    agent = BMIAgent()

    while True:
        weight = input("Enter weight (kg): ")
        if weight == "exit":
            break

        height = input("Enter height (meters): ")

        agent.calculate(float(weight), float(height))

        print("BMI =", agent.state["bmi"],"\nFitness = ",agent.state["fitness"])
        agent.reset()


if __name__ == "__main__":
    main()

