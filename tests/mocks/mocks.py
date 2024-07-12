from unittest.mock import Mock 

# Mock Open Function
class OpenMock: 
    def __init__(self, *args):
        self.write = Mock()

open_mock = Mock(
    return_value=OpenMock()
)