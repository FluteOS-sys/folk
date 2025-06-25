class GuideAgent:
    def __init__(self, mcp=None):
        self.mcp = mcp

    def interpret(self, user_input: str, ethics_profile: dict) -> dict:
        # Look for core ethical or epistemic patterns
        values = ethics_profile.get("core_values", [])
        philosophy = ethics_profile.get("epistemology", "pragmatic")

        alignment = []
        for v in values:
            if v.lower() in user_input.lower():
                alignment.append(v)

        summary = ""
        if alignment:
            summary += f"Input reflects alignment with: {', '.join(alignment)}. "
        else:
            summary += "No strong value alignment detected. "

        summary += f"Epistemic lens: {philosophy}."

        return {"ethical_frame": summary}
