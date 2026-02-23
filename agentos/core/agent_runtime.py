import importlib

class AgentRuntime:

    def load_agent(self, agent_name: str):
            try:
                        module = importlib.import_module(f"agents.{agent_name}")
                                    agent_class = getattr(module, "Agent")
                                                return agent_class()
                                                        except Exception:
                                                                    return None