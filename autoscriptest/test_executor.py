from unittest.mock import MagicMock
from autoscriptest.script_executor import ScriptExecutor

class TestExecutor:
    def __init__(self, config: 'Config'):
        self.config = config

    def test_script(self, script: 'Script') -> None:
        executor = ScriptExecutor(self.config)
        executor.execute_script(script)