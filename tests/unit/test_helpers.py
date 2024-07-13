from core.helpers import flatten 

class TestHelpers: 
    def test_flatten(self):
        tree = {
            "1" : {
                "1" : {
                    "1" : {}, 
                    "2" : {}
                },
                "2" : {}
            }, 
            "2" : {
                "1" : {
                    "1" : {}, 
                    "2" : {}
                },
                "2" : {
                    "1" : {}
                }
            }
        }

        items = list(flatten(tree, mode="dfs"))
        assert len(items) == 11
        assert type(items[0]) is str

        items = list(flatten(tree, mode="bfs"))
        assert len(items) == 11
        assert type(items[0]) is str

        items = list(flatten(tree, mode="dfs", as_tuple=True))
        assert len(items) == 11
        assert type(items[0]) is tuple

        items = list(flatten(tree, mode="bfs", as_tuple=True))
        assert len(items) == 11
        assert type(items[0]) is tuple
