class SacredRouter:
    def __init__(self, architect, mirror, guide):
        self.architect = architect
        self.mirror = mirror
        self.guide = guide

    def process(self, user_input: str, context: dict) -> dict:
        architect_output = self.architect.interpret(user_input, context)
        mirror_output = self.mirror.interpret(user_input, context.get("user_profile", {}))
        guide_output = self.guide.interpret(user_input, context.get("ethics_profile", {}))

        return {
            **architect_output,
            **mirror_output,
            **guide_output
        }
