from unittest.mock import Mock, MagicMock

def mock_built_in_fn(methods):
    fields = MagicMock()
    call   = Mock(return_value=fields)
    return call, fields

# Mock Open Function
open_mock, open_mock_ = mock_built_in_fn(["write"])