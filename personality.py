import json
import os

PERSONALITY_FILE = "personality.json"


def init_personality():

    if not os.path.exists(PERSONALITY_FILE):

            data = {
                        "interests": {},
                                    "goals": [],
                                                "traits": {}
                                                        }

                                                                json.dump(data, open(PERSONALITY_FILE, "w"), indent=2)


                                                                def load_personality():
                                                                    return json.load(open(PERSONALITY_FILE))


                                                                    def save_personality(data):
                                                                        json.dump(data, open(PERSONALITY_FILE, "w"), indent=2)


                                                                        # ======================
                                                                        # LEARN FROM USER
                                                                        # ======================

                                                                        def learn_from_intent(intent):

                                                                            personality = load_personality()

                                                                                personality["interests"][intent] = \
                                                                                        personality["interests"].get(intent, 0) + 1

                                                                                            save_personality(personality)


                                                                                            # ======================
                                                                                            # ANALYZE USER
                                                                                            # ======================

                                                                                            def analyze_personality():

                                                                                                personality = load_personality()

                                                                                                    print("\n🧠 Prime Personality")

                                                                                                        interests = personality["interests"]

                                                                                                            if not interests:
                                                                                                                    print("Learning user...")
                                                                                                                            return

                                                                                                                                sorted_data = sorted(
                                                                                                                                        interests.items(),
                                                                                                                                                key=lambda x: x[1],
                                                                                                                                                        reverse=True
                                                                                                                                                            )

                                                                                                                                                                for k, v in sorted_data:
                                                                                                                                                                        print(f"{k}: {v}")

                                                                                                                                                                            print(f"\n⭐ Main focus → {sorted_data[0][0]}")