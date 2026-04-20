import unittest
from core.engine import WorkflowEngine

class DummyEngineTest(unittest.TestCase):

    def setUp(self):
        self.workflow = {
            "test_flow": [
                {"name": "stage_one"},
                {"name": "stage_two"}
            ]
        }

        self.engine = WorkflowEngine(self.workflow)

    def test_context_setting(self):
        self.engine.set_context("input", "test building")
        self.assertEqual(self.engine.context["input"], "test building")

    def test_workflow_execution(self):
        self.engine.set_context("input", "simple test")

        result = self.engine.run_workflow("test_flow")

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()
