import vertexai
from vertexai import agent_engines

# Assuming you have already deployed your agent and have its resource name
AGENT_ENGINE_RESOURCE_NAME = "projects/986247448338/locations/us-central1/reasoningEngines/480134737617223680"

# Get the agent from the resource name
remote_agent = agent_engines.get(AGENT_ENGINE_RESOURCE_NAME)
print(remote_agent)
# Now you can query the agent
response = remote_agent.stream_query(input={"messages": [
    ("user", "I feel panic")
]})
print(response)

# View progress and logs at https://console.cloud.google.com/logs/query?project=hackathon-att-2025-lf







# (manager-py3.12) PS C:\Users\jwzha\autism-support-multiagents-lf> poetry run deploy-remote --create
# Identified the following requirements: {'google-cloud-aiplatform': '1.89.0', 'cloudpickle': '3.1.1'}
# The following requirements are missing: {'cloudpickle'}
# The following requirements are appended: {'cloudpickle==3.1.1'}
# The final list of requirements: ['google-cloud-aiplatform[adk,agent_engines]', 'cloudpickle==3.1.1']
# Using bucket hackathon-att-2025
# Wrote to gs://hackathon-att-2025/agent_engine/agent_engine.pkl
# Writing to gs://hackathon-att-2025/agent_engine/requirements.txt
# Creating in-memory tarfile of extra_packages
# Writing to gs://hackathon-att-2025/agent_engine/dependencies.tar.gz
# Creating AgentEngine
# Create AgentEngine backing LRO: projects/986247448338/locations/us-central1/reasoningEngines/480134737617223680/operations/2138963910353485824
# View progress and logs at https://console.cloud.google.com/logs/query?project=hackathon-att-2025-lf
# AgentEngine created. Resource name: projects/986247448338/locations/us-central1/reasoningEngines/480134737617223680
# To use this AgentEngine in another session:
# agent_engine = vertexai.agent_engines.get('projects/986247448338/locations/us-central1/reasoningEngines/480134737617223680')
# Created remote app: projects/986247448338/locations/us-central1/reasoningEngines/480134737617223680
