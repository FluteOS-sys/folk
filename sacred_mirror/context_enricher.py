class ContextEnricher:
    def enrich(self, user_input: str, interpretation: dict) -> str:
        context_summary = " | ".join([f"{k}: {v}" for k, v in interpretation.items()])
        enriched_prompt = f"Context: {context_summary}\n\nUser Input: {user_input}"
        return enriched_prompt
