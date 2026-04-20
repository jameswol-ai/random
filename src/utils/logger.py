import datetime

class Logger:
    def log(self, stage, message):
        time = datetime.datetime.now().isoformat()
        print(f"[{time}] [{stage}] {message}")
