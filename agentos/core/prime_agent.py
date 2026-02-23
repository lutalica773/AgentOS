# prime_agent.py

from memory import (
    log_usage,
        get_suggestions,
            get_agents,
                register_agent
                )


                class PrimeAgent:

                    def __init__(self):
                            print("🧠 Prime Agent initialized")

                                # =============================
                                    # MAIN THINK LOOP
                                        # =============================

                                            def think(self, user_input):

                                                    intent = self.detect_intent(user_input)

                                                            if intent:
                                                                        log_usage(intent)

                                                                                response = self.generate_response(intent, user_input)

                                                                                        return response

                                                                                            # =============================
                                                                                                # INTENT DETECTION
                                                                                                    # =============================

                                                                                                        def detect_intent(self, text):

                                                                                                                text = text.lower()

                                                                                                                        if any(x in text for x in ["research", "learn", "search"]):
                                                                                                                                    return "research"

                                                                                                                                            if any(x in text for x in ["money", "finance", "budget"]):
                                                                                                                                                        return "finance"

                                                                                                                                                                if any(x in text for x in ["plan", "schedule", "todo"]):
                                                                                                                                                                            return "planning"

                                                                                                                                                                                    if any(x in text for x in ["build", "code", "program"]):
                                                                                                                                                                                                return "development"

                                                                                                                                                                                                        return "general"

                                                                                                                                                                                                            # =============================
                                                                                                                                                                                                                # RESPONSE GENERATION
                                                                                                                                                                                                                    # =============================

                                                                                                                                                                                                                        def generate_response(self, intent, text):

                                                                                                                                                                                                                                if intent == "research":
                                                                                                                                                                                                                                            return "🔎 Research mode activated"

                                                                                                                                                                                                                                                    if intent == "finance":
                                                                                                                                                                                                                                                                return "💰 Finance assistant ready"

                                                                                                                                                                                                                                                                        if intent == "planning":
                                                                                                                                                                                                                                                                                    return "📅 Planning assistant ready"

                                                                                                                                                                                                                                                                                            if intent == "development":
                                                                                                                                                                                                                                                                                                        return "⚙️ Developer agent ready"

                                                                                                                                                                                                                                                                                                                return "🤖 I am learning your workflow..."

                                                                                                                                                                                                                                                                                                                    # =============================
                                                                                                                                                                                                                                                                                                                        # SUGGESTIONS SYSTEM
                                                                                                                                                                                                                                                                                                                            # =============================

                                                                                                                                                                                                                                                                                                                                def show_suggestions(self):

                                                                                                                                                                                                                                                                                                                                        suggestions = get_suggestions()

                                                                                                                                                                                                                                                                                                                                                if not suggestions:
                                                                                                                                                                                                                                                                                                                                                            print("No suggestions yet.")
                                                                                                                                                                                                                                                                                                                                                                        return

                                                                                                                                                                                                                                                                                                                                                                                print("\n🧠 Prime Suggestions:")
                                                                                                                                                                                                                                                                                                                                                                                        for s in suggestions:
                                                                                                                                                                                                                                                                                                                                                                                                    print(f"- {s}")

                                                                                                                                                                                                                                                                                                                                                                                                        # =============================
                                                                                                                                                                                                                                                                                                                                                                                                            # AGENT CREATION
                                                                                                                                                                                                                                                                                                                                                                                                                # =============================

                                                                                                                                                                                                                                                                                                                                                                                                                    def create_agent(self, name):

                                                                                                                                                                                                                                                                                                                                                                                                                            register_agent(name, {
                                                                                                                                                                                                                                                                                                                                                                                                                                        "created_by": "PrimeAgent"
                                                                                                                                                                                                                                                                                                                                                                                                                                                })

                                                                                                                                                                                                                                                                                                                                                                                                                                                        print(f"✅ Agent '{name}' created")


                                                                                                                                                                                                                                                                                                                                                                                                                                                        # =============================
                                                                                                                                                                                                                                                                                                                                                                                                                                                        # TEST MODE
                                                                                                                                                                                                                                                                                                                                                                                                                                                        # =============================

                                                                                                                                                                                                                                                                                                                                                                                                                                                        if __name__ == "__main__":

                                                                                                                                                                                                                                                                                                                                                                                                                                                            prime = PrimeAgent()

                                                                                                                                                                                                                                                                                                                                                                                                                                                                while True:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        user = input("\nYou: ")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if user == "exit":
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            break

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    response = prime.think(user)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            print("AgentOS:", response)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    prime.show_suggestions()