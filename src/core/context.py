# src/core/context.py

from models.design_schema import create_empty_design

class Context:
    def __init__(self, data=None):
        self.data = data or {}
        self.data["design"] = create_empty_design()

    def update(self, key, value):
        self.data[key] = value

    def update_design(self, key, value):
        self.data["design"][key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def get_design(self):
        return self.data["design"]
