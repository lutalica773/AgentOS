class AgentBuilder:

        def generate_agent_code(self, name: str, purpose: str):

                code = f'''
                class Agent:
                    def run(self, intent: str):
                            return "AI-generated agent {name} handling: " + intent
                            '''
                                    return code