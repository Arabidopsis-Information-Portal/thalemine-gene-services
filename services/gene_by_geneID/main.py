import json

#intermine is data service used by thalemine
#generated python code for query
from intermine.webservice import Service
service = Service("https://apps.araport.org/thalemine/service")
query = service.new_query("Gene")

#TODO: Move this to inside the functions
query.add_view(
    "primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start"
)

#operation
def search(parameter):
    #store input as variables
    searchInput = parameter["Identifier"]
    prefOutInput = parameter["Output"]

    #determine what to return
    if prefOutInput is 'All':
        print json.dumps(returnAllInfo(searchInput))
    else:
        print json.dumps(returnInfo(searchInput,prefOutInput))

#operation
def list():
    query.add_view("primaryIdentifier")

    results = {}


    for row in query.rows():
        print json.dumps({"primaryIdentifier" : row["primaryIdentifier"]})
        print '---'
        #results["primaryIdentifier"+str(row)] = row["primaryIdentifier"]
        #results[row] = row["primaryIdentifier"]


    #return results

#returns information for all fields
def returnAllInfo(id):
    #query search thalemine
    query.add_constraint("primaryIdentifier", "=", id, code = "A")

    #return dict of information of matching geneID
    for row in query.rows():
        return {"primaryIdentifier": row["primaryIdentifier"],
                "results" :
                    {"chromosomeLocation.end" : row["chromosomeLocation.end"],
                        "chromosomeLocation.start" : row["chromosomeLocation.start"]
                    }
        }
#returns specific info about specific geneID
def returnInfo(id, out):
    #query search thalemine
    query.add_constraint("primaryIdentifier", "=", str(id), code = "A")

    #return dict of information of matching geneID
    for row in query.rows():
        return {"primaryIdentifier": row["primaryIdentifier"], out : row[out]}
