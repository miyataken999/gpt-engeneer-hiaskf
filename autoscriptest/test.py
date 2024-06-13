from dataclasses import dataclass

@dataclass
class Test:
    def __init__(self, test_path):
        self.test_path = test_path

    def run(self):
        # implement test running logic here
        print("Running test...")