
class Agent:
    def __init__(self, name, role, goal, backstory, llm_fn):
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.llm_fn = llm_fn

    def run(self, prompt):
        full = f"""
You are {self.name}, a {self.role}.
Goal: {self.goal}
Backstory: {self.backstory}

Task:
{prompt}
"""
        return self.llm_fn(full)
