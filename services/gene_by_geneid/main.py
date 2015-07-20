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

    queryAll1 = service.new_query("Gene")
    queryAll1.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")

    for row in queryAll1.rows():
        org = {}
        org['locus_id'] = row["primaryIdentifier"]
        break

    print json.dumps(org)
    print '---'
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

    queryAll = service.new_query("Gene")
    queryAll.add_view("primaryIdentifier")

    for row in queryAll.rows():
        org = {}

        org['locus_id'] = row["primaryIdentifier"]

        #org['locus_id'] = "text"

        print json.dumps(org)
        print '---'

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
