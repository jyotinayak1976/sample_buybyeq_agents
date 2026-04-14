from agents.base_agent import Agent

class DataProcessingAgent(Agent):
    def __init__(self, name, fields):
        super().__init__(name)
        self.fields = fields

    def execute(self, data):
        if "error" in data:
            return data

        return {
            "processed": {k: data.get(k) for k in self.fields}
        }
