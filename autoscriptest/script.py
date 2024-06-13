from dataclasses import dataclass

@dataclass
class Script:
    def __init__(self, script_path):
        self.script_path = script_path

    def run(self):
        # implement script running logic here
        print("Running script...")