from typing import List

class ScriptParser:
    def __init__(self, config: 'Config'):
        self.config = config

    def parse_script(self, script_file: str) -> 'Script':
        # parse script file and return Script object
        with open(script_file, 'r') as f:
            lines = f.readlines()
            commands = [line.strip() for line in lines]
            return Script(script_file, commands)