import json

def search(parameters):
    print json.dumps({'Name': 'Zara', 'Age': 7, 'Class': 'First'})
    print '---'

#operation
def list():
    print json.dumps({"primaryIdentifier": "AT12345",
                "results" :
                    {"chromosomeLocation.end" : "12",
                        "chromosomeLocation.start" : 34}
        })

    print '---'
