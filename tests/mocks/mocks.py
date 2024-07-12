from unittest.mock import Mock 

def mock_built_in_fn(methods):
    class FunctionMock: 
        def __init__(self, *args):
            for method in methods: 
                setattr(self, method, Mock())

    fields = FunctionMock()
    call   = Mock(return_value=fields)

    return call, fields

# Mock Open Function
open_mock, open_mock_ = mock_built_in_fn(["write"])