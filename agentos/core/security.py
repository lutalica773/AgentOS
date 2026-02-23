class SecurityManager:

        def check_permission(self, agent_name, action):

                permissions = {
                            "research_agent": ["read"],
                                        "finance_agent": ["read", "write"]
                                                }

                                                        allowed = permissions.get(agent_name, [])

                                                                return action in allowed