import pytest
from autoscriptest.script_executor import ScriptExecutor
from autoscriptest.config import Config

@pytest.fixture
def config():
    return Config("scripts", "tests")

def test_execute_script(config):
    executor = ScriptExecutor(config)
    script = Script("test_script", ["command1", "command2"])
    executor.execute_script(script)