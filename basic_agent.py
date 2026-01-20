from typing import TypedDict, Optional


class AgentState(TypedDict):
    weight: Optional[float]
    height: Optional[float]
    bmi: Optional[float]


class BMIAgent:
    def __init__(self) -> None:
        self.state: AgentState = {
            "weight": None,
            "height": None,
            "bmi": None,
        }

    def run(self, weight: float, height: float) -> None:
        self.state["weight"] = weight
        self.state["height"] = height
        self.state["bmi"] = weight / (height ** 2)


def main() -> None:
    agent = BMIAgent()

    while True:
        weight = input("Enter weight (kg): ")
        if weight == "exit":
            break

        height = input("Enter height (meters): ")

        agent.run(float(weight), float(height))

        print("BMI =", agent.state["bmi"])


if __name__ == "__main__":
    main()
