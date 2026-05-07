from datapizza.agents import Agent
from datapizza.memory import Memory
from .config import WikiConfig
from .schemas import ORCHESTRATOR_PROMPT


class OrchestratorAgent:
    """Interactive chatbot that routes user requests to specialized sub-agents via can_call."""

    def __init__(self, config: WikiConfig):
        self.config = config

    def start(self, ingest_agent=None, query_agent=None, lint_agent=None):
        """Initialize the orchestrator with available sub-agents."""
        can_call = []
        for agent in [ingest_agent, query_agent, lint_agent]:
            if agent is not None:
                can_call.append(agent.agent)

        self._agent = Agent(
            name="wiki_orchestrator",
            client=self.config.create_client(),
            system_prompt=ORCHESTRATOR_PROMPT,
            can_call=can_call,
            stateless=False,
            memory=Memory(),
        )

    def chat(self, message: str) -> str:
        """Send a message to the orchestrator and get the response."""
        if not hasattr(self, "_agent"):
            return "Error: orchestrator not started. Call start() first."
        result = self._agent.run(message)
        if result is None:
            return ""
        if hasattr(result, "text"):
            return result.text
        return str(result)
