from Researcher_and_Writer import agents
from Researcher_and_Writer import tasks
from crewai import Crew

crew = Crew(
    agents=[agents.planner, agents.writer, agents.editor],
    tasks=[tasks.plan, tasks.write, tasks.edit],
    verbose=True
)

result = crew.kickoff(inputs={"topic": "Artificial Intelligence"})