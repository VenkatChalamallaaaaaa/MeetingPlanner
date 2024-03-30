from crewai import Crew
from tasks import MeetingPreparationTasks
from agents import MeetingPreparationAgents
from getpass import getpass
import os
from openai import OpenAI

OpenAI_API_KEY = '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'
os.environ["OPENAI_API_KEY"] = OpenAI_API_KEY


tasks = MeetingPreparationTasks()
agents = MeetingPreparationAgents()




print("## Welcome to Student Meeting Scheduler")
print("------------------------------------")

participants = input("What are the emails for the participants (other than you) in the meeting?\n")

emails_array = participants.split(',')

# all the emails
emails_array = [email.strip() for email in emails_array]

##context
context = input("What is the context of the meeting?\n")

#objective
objective = input("What is your objective for this meeting?\n")


print(f"participants: {participants} | context: {context} | objective: {objective}")

researcher_agent = agents.research_agent()
industry_analyst_agent = agents.industry_analysis_agent()
meeting_strategy_agent = agents.meeting_strategy_agent()
summary_and_briefing_agent = agents.summary_and_briefing_agent()

research = tasks.research_task(researcher_agent, participants, context)
industry_analysis = tasks.industry_analysis_task(industry_analyst_agent, participants, context)
meeting_strategy = tasks.meeting_strategy_task(meeting_strategy_agent, context, objective)
summary_and_briefing = tasks.summary_and_briefing_task(summary_and_briefing_agent, context, objective)

crew = Crew(
    agents=[
        researcher_agent, 
        industry_analyst_agent,
        meeting_strategy_agent, 
        summary_and_briefing_agent
    ], 
    tasks=[
        research, 
        industry_analysis,
        meeting_strategy,
        summary_and_briefing
    ]
)

game = crew.kickoff()

print("## Here is the result ##")
print(game)