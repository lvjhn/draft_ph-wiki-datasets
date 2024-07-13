from core.helpers import flatten

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
    }, 
}

print(list(flatten(tree)))