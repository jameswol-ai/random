import json
import os

def load_workflow(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def load_all_workflows(directory):
    workflows = {}

    for file in os.listdir(directory):
        if file.endswith(".json"):
            path = os.path.join(directory, file)
            wf = load_workflow(path)

            workflows[wf["name"]] = wf["stages"]

    return workflows
