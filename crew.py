
# from task import Task

# class Crew:
#     def __init__(self, tasks):
#         self.tasks = tasks
#         self.context = ""
#         self.log = []

#     def run(self, initial_input):
#         self.context = initial_input
#         for task in self.tasks:
#             out = task.run(self.context)
#             self.log.append((task.name, out))
#             self.context += f"\n[{task.name}]: {out}"
#         return self.log


from task import Task

class Crew:
    def __init__(self, agents=None, tasks=None, verbose=False):
        self.agents = agents or []
        self.tasks = tasks or []
        self.context = ""
        self.log = []
        self.verbose = verbose

    def run(self, initial_input):
        self.context = initial_input
        for task in self.tasks:
            if self.verbose:
                print(f"\n🧠 Running task: {task.name}")
            out = task.run(self.context)
            self.log.append((task.name, out))
            self.context = out  # Pass output as new context
        return self.context  # Return final polished post

# crew.py

from task import Task
from agent import Agent
from my_llm import call_llm

# Existing Crew class should be above this

def run_crew(transcript: str) -> str:
    # Step 1: Create agents
    reader = Agent(
        name="TranscriptReader",
        role="Reads the transcript and summarizes the core story",
        goal="Extract the main story or message from a transcript",
        backstory="You help turn raw transcripts into a clear summary.",
        llm_fn=call_llm,
    )

    writer = Agent(
        name="PostWriter",
        role="Writes engaging LinkedIn posts",
        goal="Write a conversational, structured, and professional post for LinkedIn",
        backstory="You are a content writer who crafts posts for social media based on business stories.",
        llm_fn=call_llm,
    )

    reviewer = Agent(
        name="Reviewer",
        role="Reviews and polishes posts",
        goal="Make sure the post is clear, professional, and typo-free",
        backstory="You're a professional editor ensuring quality and tone.",
        llm_fn=call_llm,
    )

    # Step 2: Create tasks
    task1 = Task(
        name="Extract Story",
        agent=reader,
        description="Read the transcript and extract the main story or insight.",
    )

    task2 = Task(
        name="Write Post",
        agent=writer,
        description="Using the extracted story, write a structured LinkedIn post. Structure: Hook, Context, Insight, Conclusion, CTA with hashtags.",
    )

    task3 = Task(
        name="Review & Polish",
        agent=reviewer,
        description="Improve grammar, tone, and clarity of the LinkedIn post.",
    )

    # Step 3: Run the pipeline
    crew = Crew(
        agents=[reader, writer, reviewer],
        tasks=[task1, task2, task3],
        verbose=True,
    )

    final_post = crew.run(transcript)
    return final_post
