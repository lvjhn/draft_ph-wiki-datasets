import pytest 
import shutil 
import os 

class BaseTest: 
    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        shutil.rmtree("./tests/temp")
        os.mkdir("./tests/temp")
        yield
        shutil.rmtree("./tests/temp")
        os.mkdir("./tests/temp")

