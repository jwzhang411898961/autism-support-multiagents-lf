from google.adk.agents import Agent
from google.adk.tools.toolbox_tool import ToolboxTool
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts.in_memory_artifact_service import InMemoryArtifactService
from google.genai import types

import os
from dotenv import load_dotenv


# TODO(developer): replace this with your Google API key

load_dotenv()  # Load environment variables from .env
api_key = os.getenv('GOOGLE_API_KEY')
# api_key = ""
# print(api_key)
os.environ['GOOGLE_API_KEY'] = api_key


toolbox_tools = ToolboxTool("http://127.0.0.1:5000")

prompt = """
  You are a helpful text log assistant that specializes in retrieving and analyzing user conversation logs. 
  You can efficiently search through conversation history using user IDs (uid) and session IDs (session_id).
  When retrieving logs, you can:
  - Show specific conversations by user ID
  - Display conversations from particular sessions
  - Summarize the key points of conversations
  - Show the most recent messages
  Always provide clear, organized responses and highlight important information from the logs.
  If summarizing conversations, focus on the main topics, decisions, and action items.
"""

root_agent = Agent(
    model='gemini-2.0-flash',
    name='text_log_agent',
    description='A helpful AI assistant.',
    instruction=prompt,
    tools=toolbox_tools.get_toolset("my-toolset"),
)

session_service = InMemorySessionService()
artifacts_service = InMemoryArtifactService()
session = session_service.create_session(
    state={}, app_name='text_log_agent', user_id='DDeNcLqfYySaVL8SUfwnE2PYb4A2'
)
runner = Runner(
    app_name='text_log_agent',
    agent=root_agent,
    artifact_service=artifacts_service,
    session_service=session_service,
)

queries = [
    "What's the last 5 sentences of the text log of my uid, regardless of session id",
    "you should have my uid, it is the same uid as this session",
    "ok my uid is HHlaD2KY6ibqNflPS61cDUCRAw93",
    "Show me all the sentences in my conversation with session id IFDfZ9wC",
    "Summarize the key points of my conversation with session id muUL1S9g",
]

for query in queries:
    print('Question:', query)
    content = types.Content(role='user', parts=[types.Part(text=query)])
    events = runner.run(session_id=session.id,
                        user_id='DDeNcLqfYySaVL8SUfwnE2PYb4A2', new_message=content)

    responses = (
      part.text
      for event in events
      for part in event.content.parts
      if part.text is not None 
    )

    print('Responses:')
    i=0
    for text in responses:
      print('#',i,' ', text)
      i+=1