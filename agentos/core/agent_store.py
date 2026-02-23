from core.agent_builder import AgentBuilder

class AgentStore:

    def __init__(self):
            self.builder = AgentBuilder()

                def install_agent(self, name: str, purpose: str):

                        agent_code = self.builder.generate_agent_code(name, purpose)

                                path = f"agents/{name}.py"

                                        with open(path, "w") as f:
                                                    f.write(agent_code)

                                                            return f"{name} installed by AgentOS AI"