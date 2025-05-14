import vertexai
from vertexai import agent_engines

# Assuming you have already deployed your agent and have its resource name
AGENT_ENGINE_RESOURCE_NAME = "projects/986247448338/locations/us-central1/reasoningEngines/480134737617223680"

# Get the agent from the resource name
remote_agent = agent_engines.get(AGENT_ENGINE_RESOURCE_NAME)
print(remote_agent)
# Now you can query the agent
# response = remote_agent.stream_query(input={"messages": [
#     ("user", "I feel panic")
# ]})

# for chunk in response:
#     candidates = chunk.get("candidates", [])
#     for candidate in candidates:
#         content = candidate.get("content", {})
#         parts = content.get("parts", [])
#         for part in parts:
#             print(part.get("text", ""), end="", flush=True)

# response = remote_agent.stream_query(input={
#     "messages": [{"role": "user", "content": "Hello"}]
# })

# for chunk in response:
#     print(chunk)

response = remote_agent.query(
    input={"messages": [{"role": "user", "content": "I feel panic"}]}
)
# for chunk in response:
#     content = chunk.get("content", {})
#     parts = content.get("parts", [])
#     for part in parts:
#         print(part.get("text", ""))
print(response.candidates[0].content.parts[0].text)
# for chunk in response:
#     print(chunk)

# View progress and logs at https://console.cloud.google.com/logs/query?project=hackathon-att-2025-lf


# {'content': {'parts': [{'function_call': {'id': 'adk-cdedfac3-95a0-4719-96c1-3229e3cd5aa1', 'args': {}, 'name': 'on_overwhelm_tapped'}}], 'role': 'model'}, 'invocation_id': 'e-16a67f14-e7e3-40cd-936e-9bf49c220357', 'author': 'input_and_state', 'actions': {'state_delta': {}, 'artifact_delta': {}, 'requested_auth_configs': {}}, 'long_running_tool_ids': [], 'id': 'TH151XNp', 'timestamp': 1747251646.432744}
# {'content': {'parts': [{'function_response': {'id': 'adk-cdedfac3-95a0-4719-96c1-3229e3cd5aa1', 'name': 'on_overwhelm_tapped', 'response': {'event': 'OVERWHELM_TRIGGERED', 'timestamp': 'auto', 'source': 'calm_beacon_button'}}}], 'role': 'user'}, 'invocation_id': 'e-16a67f14-e7e3-40cd-936e-9bf49c220357', 'author': 'input_and_state', 'actions': {'state_delta': {}, 'artifact_delta': {}, 'requested_auth_configs': {}}, 'id': 'ECgQecap', 'timestamp': 1747251646.977418}       
# {'content': {'parts': [{'text': "OK. I've notified the system that you're feeling overwhelmed.\n"}], 'role': 'model'}, 'invocation_id': 'e-16a67f14-e7e3-40cd-936e-9bf49c220357', 'author': 'input_and_state', 'actions': {'state_delta': {}, 'artifact_delta': {}, 'requested_auth_configs': {}}, 'id': 's0FZh34A', 'timestamp': 1747251647.059114}




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
