import json

#intermine is data service used by thalemine
#generated python code for query
from intermine.webservice import Service
service = Service("https://apps.araport.org/thalemine/service")


#query = service.new_query("Gene")
#adding views to the query
#query.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")

#operation
def search(parameter):

    querySearch = service.new_query("Gene")
    querySearch.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")
    cnt = 0
    for row in querySearch.rows():
        org = {}
        org['locus_id'] = row["primaryIdentifier"]
        print json.dumps(org)
        print '---'
        cnt += 1
        if (cnt > 10):
            break

    return


    """
    #store input as variables
    searchInput = parameter["Identifier"]
    prefOutInput = parameter["Output"]

    #determine what to return
    if prefOutInput == "both":
        print json.dumps(returnAllInfo(searchInput))
    else:
        #print json.dumps(returnInfo(searchInput,prefOutInput))
        print "test123"
    """

#operation
def list(parameter):

    querySearch = service.new_query("Gene")
    querySearch.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")
    cnt = 0
    for row in querySearch.rows():
        org = {}
        org['locus_id'] = row["primaryIdentifier"]
        print json.dumps(org)
        print '---'
        cnt += 1
        if (cnt > 30000):
            break

    return
        #the at num is this ... ->>   row["primaryIdentifier"]


        #print json.dumps({"primaryIdentifier" : row["primaryIdentifier"]})
        #test = row["primaryIdentifier"]
        #x=1
        #print "---"

    #print "done"
    #print "---"


#returns information for all fields for specfic geneID
def returnAllInfo(id):
    #query search thalemine
    query = service.new_query("Gene")
    #adding views to the query
    query.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")
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
    query = service.new_query("Gene")
    #adding views to the query
    query.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")
    query.add_constraint("primaryIdentifier", "=", id, code = "A")

    #return dict of information of matching geneID
    for row in query.rows():
        return {"primaryIdentifier": row["primaryIdentifier"], out : row[out]}
