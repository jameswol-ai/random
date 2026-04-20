import unittest

from workflows.basic_workflow import architectural_workflow

class WorkflowStructureTests(unittest.TestCase):

    def test_workflow_exists(self):
        self.assertIn("basic_design", architectural_workflow)

    def test_workflow_is_list(self):
        flow = architectural_workflow["basic_design"]
        self.assertIsInstance(flow, list)

    def test_stages_have_names(self):
        flow = architectural_workflow["basic_design"]

        for stage in flow:
            self.assertIn("name", stage)

if __name__ == "__main__":
    unittest.main()
