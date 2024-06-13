from autoscriptest.config import Config
from autoscriptest.script import Script
from autoscriptest.test import Test
from autoscriptest.utils import get_script_path, get_test_path

def main():
    script_path = get_script_path()
    test_path = get_test_path()
    config = Config(script_path, test_path)
    script = Script(script_path)
    test = Test(test_path)
    script.run()
    test.run()

if __name__ == "__main__":
    main()