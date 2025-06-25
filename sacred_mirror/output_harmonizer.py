class OutputHarmonizer:
    def harmonize(self, llm_response: str, mirror_data: dict) -> str:
        reflection = mirror_data.get("emotional_reflection", "")
        structure = mirror_data.get("structure", "")
        ethics = mirror_data.get("ethical_frame", "")

        summary = f"[Tone Insight] {reflection}\n[Structural Insight] {structure}\n[Ethical Insight] {ethics}\n"
        return summary + "\n\nLLM Response: " + llm_response
