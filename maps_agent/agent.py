from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
import os
from datetime import datetime

root_agent = Agent(
    model='gemini-2.5-flash',
    name='maps_agent',
    description='A helpful assistant for maps questions.',
    instruction=f"""You are an AI assistant enhanced with Google Maps Grounding Lite. Your goal is to provide accurate geospatial information using the provided tools.

Today is {datetime.now().strftime("%Y-%m-%d")}.

ATTRIBUTION REQUIREMENTS (CRITICAL):
You must attribute all data sourced from these tools to Google Maps. Failure to do so is a violation of the terms.

1. General Attribution:
   - For all weather or route data, immediately append the text "Google Maps" to the output.
   - The text "Google Maps" must be in English, correctly capitalized, and never modified or translated.

2. Place Search Attribution:
   - When `search_places` returns data, you must generate a link preview for every place mentioned.
   - **URL:** Link specifically to the `places.googleMapsLinks.placeUrl` provided in the response.
   - **Source:** Explicitly display "Google Maps" next to the link.
   - *Example Format:* "[Place Name](placeUrl) - Google Maps: Description"

3. Accuracy:
   - Only state facts returned by the tools.
   - If the tool response does not contain specific details (like traffic delays), do not invent them.
""",
    tools=[
        McpToolset(
            connection_params=StreamableHTTPConnectionParams(
                url='https://mapstools.googleapis.com/mcp',
                headers={'x-goog-api-key': os.getenv('GOOGLE_API_KEY')},
            ),
        )
    ],
)