# memory.py
import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"


# =============================
# INIT MEMORY
# =============================

def load_memory():
    if not os.path.exists(MEMORY_FILE):
            return {
                        "profile": {},
                                    "stats": {},
                                                "preferences": {},
                                                            "agents": {},
                                                                        "suggestions": [],
                                                                                    "privacy": {
                                                                                                    "allow_learning": True,
                                                                                                                    "store_history": True
                                                                                                                                },
                                                                                                                                            "last_updated": str(datetime.now())
                                                                                                                                                    }

                                                                                                                                                        with open(MEMORY_FILE, "r") as f:
                                                                                                                                                                return json.load(f)


                                                                                                                                                                def save_memory(memory):
                                                                                                                                                                    memory["last_updated"] = str(datetime.now())

                                                                                                                                                                        with open(MEMORY_FILE, "w") as f:
                                                                                                                                                                                json.dump(memory, f, indent=2)


                                                                                                                                                                                memory = load_memory()


                                                                                                                                                                                # =============================
                                                                                                                                                                                # PROFILE MEMORY
                                                                                                                                                                                # =============================

                                                                                                                                                                                def update_profile(key, value):
                                                                                                                                                                                    memory["profile"][key] = value
                                                                                                                                                                                        save_memory(memory)


                                                                                                                                                                                        def get_profile(key):
                                                                                                                                                                                            return memory["profile"].get(key)


                                                                                                                                                                                            # =============================
                                                                                                                                                                                            # USAGE STATS
                                                                                                                                                                                            # =============================

                                                                                                                                                                                            def log_usage(category):
                                                                                                                                                                                                stats = memory["stats"]

                                                                                                                                                                                                    if category not in stats:
                                                                                                                                                                                                            stats[category] = 0

                                                                                                                                                                                                                stats[category] += 1

                                                                                                                                                                                                                    check_suggestions(category)

                                                                                                                                                                                                                        save_memory(memory)


                                                                                                                                                                                                                        def get_stats():
                                                                                                                                                                                                                            return memory["stats"]


                                                                                                                                                                                                                            # =============================
                                                                                                                                                                                                                            # PREFERENCES
                                                                                                                                                                                                                            # =============================

                                                                                                                                                                                                                            def set_preference(key, value):
                                                                                                                                                                                                                                memory["preferences"][key] = value
                                                                                                                                                                                                                                    save_memory(memory)


                                                                                                                                                                                                                                    def get_preference(key):
                                                                                                                                                                                                                                        return memory["preferences"].get(key)


                                                                                                                                                                                                                                        # =============================
                                                                                                                                                                                                                                        # AGENT REGISTRY
                                                                                                                                                                                                                                        # =============================

                                                                                                                                                                                                                                        def register_agent(name, config=None):
                                                                                                                                                                                                                                            memory["agents"][name] = config or {}
                                                                                                                                                                                                                                                save_memory(memory)


                                                                                                                                                                                                                                                def remove_agent(name):
                                                                                                                                                                                                                                                    if name in memory["agents"]:
                                                                                                                                                                                                                                                            del memory["agents"][name]
                                                                                                                                                                                                                                                                    save_memory(memory)


                                                                                                                                                                                                                                                                    def get_agents():
                                                                                                                                                                                                                                                                        return memory["agents"]


                                                                                                                                                                                                                                                                        # =============================
                                                                                                                                                                                                                                                                        # PRIVACY CONTROL
                                                                                                                                                                                                                                                                        # =============================

                                                                                                                                                                                                                                                                        def privacy_allowed():
                                                                                                                                                                                                                                                                            return memory["privacy"].get("allow_learning", True)


                                                                                                                                                                                                                                                                            def set_privacy(key, value):
                                                                                                                                                                                                                                                                                memory["privacy"][key] = value
                                                                                                                                                                                                                                                                                    save_memory(memory)


                                                                                                                                                                                                                                                                                    # =============================
                                                                                                                                                                                                                                                                                    # PRIME AGENT SUGGESTIONS
                                                                                                                                                                                                                                                                                    # =============================

                                                                                                                                                                                                                                                                                    def add_suggestion(text):
                                                                                                                                                                                                                                                                                        suggestions = memory["suggestions"]

                                                                                                                                                                                                                                                                                            if text not in suggestions:
                                                                                                                                                                                                                                                                                                    suggestions.append(text)

                                                                                                                                                                                                                                                                                                        save_memory(memory)


                                                                                                                                                                                                                                                                                                        def get_suggestions():
                                                                                                                                                                                                                                                                                                            return memory["suggestions"]


                                                                                                                                                                                                                                                                                                            def clear_suggestions():
                                                                                                                                                                                                                                                                                                                memory["suggestions"] = []
                                                                                                                                                                                                                                                                                                                    save_memory(memory)


                                                                                                                                                                                                                                                                                                                    # =============================
                                                                                                                                                                                                                                                                                                                    # INTELLIGENCE (Prime Agent Brain)
                                                                                                                                                                                                                                                                                                                    # =============================

                                                                                                                                                                                                                                                                                                                    def check_suggestions(category):

                                                                                                                                                                                                                                                                                                                        stats = memory["stats"]

                                                                                                                                                                                                                                                                                                                            # Research workflow suggestion
                                                                                                                                                                                                                                                                                                                                if stats.get("research", 0) >= 5:
                                                                                                                                                                                                                                                                                                                                        add_suggestion("Create Research Workflow Agent?")

                                                                                                                                                                                                                                                                                                                                            # Finance automation
                                                                                                                                                                                                                                                                                                                                                if stats.get("finance", 0) >= 5:
                                                                                                                                                                                                                                                                                                                                                        add_suggestion("Enable Monthly Finance Automation?")

                                                                                                                                                                                                                                                                                                                                                            # Productivity mode
                                                                                                                                                                                                                                                                                                                                                                if stats.get("planning", 0) >= 5:
                                                                                                                                                                                                                                                                                                                                                                        add_suggestion("Enable Focus Productivity Mode?")

                                                                                                                                                                                                                                                                                                                                                                            # Too many agents cleanup
                                                                                                                                                                                                                                                                                                                                                                                if len(memory["agents"]) >= 6:
                                                                                                                                                                                                                                                                                                                                                                                        add_suggestion("You have many agents. Merge similar agents?")


                                                                                                                                                                                                                                                                                                                                                                                        # =============================
                                                                                                                                                                                                                                                                                                                                                                                        # DEBUG
                                                                                                                                                                                                                                                                                                                                                                                        # =============================

                                                                                                                                                                                                                                                                                                                                                                                        def reset_memory():
                                                                                                                                                                                                                                                                                                                                                                                            global memory
                                                                                                                                                                                                                                                                                                                                                                                                memory = load_memory()
                                                                                                                                                                                                                                                                                                                                                                                                    save_memory(memory)