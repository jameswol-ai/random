class MemoryStore:
    def __init__(self):
        # format: {stage_name: {"success": int, "count": int}}
        self.stats = {}

    def record(self, stage_name, success=True):
        if stage_name not in self.stats:
            self.stats[stage_name] = {"success": 0, "count": 0}

        self.stats[stage_name]["count"] += 1
        if success:
            self.stats[stage_name]["success"] += 1

    def score(self, stage_name):
        data = self.stats.get(stage_name)
        if not data or data["count"] == 0:
            return 0.5  # neutral prior

        return data["success"] / data["count"]
