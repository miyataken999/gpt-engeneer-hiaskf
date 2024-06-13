import pytest
from autoscriptest.script_parser import ScriptParser
from autoscriptest.config import Config

@pytest.fixture
def config():
    return Config("scripts", "tests")

def test_parse_script(config):
    parser = ScriptParser(config)
    script = parser.parse_script("test_script.txt")
    assert script.name == "test_script.txt"
    assert script.commands == ["command1", "command2"]