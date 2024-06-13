from dataclasses import dataclass
from typing import List

@dataclass
class Script:
    name: str
    commands: List[str]

class ScriptExecutor:
    def __init__(self, config: 'Config'):
        self.config = config

    def execute_script(self, script: Script) -> None:
        # execute script commands
        for command in script.commands:
            print(f"Executing command: {command}")