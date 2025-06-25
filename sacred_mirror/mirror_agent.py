class MirrorAgent:
    def __init__(self, mcp=None):
        self.mcp = mcp

    def interpret(self, user_input: str, user_profile: dict) -> dict:
        tone = "neutral"
        sentiment_keywords = {
            "anger": ["hate", "stupid", "sucks", "can’t stand"],
            "sadness": ["tired", "lonely", "lost", "worthless"],
            "hope": ["maybe", "hope", "trying", "working on"],
            "joy": ["grateful", "love", "excited", "happy"],
        }

        for label, keywords in sentiment_keywords.items():
            if any(kw in user_input.lower() for kw in keywords):
                tone = label
                break

        reflection = f"Detected emotional tone: {tone}."
        return {"emotional_reflection": reflection}
