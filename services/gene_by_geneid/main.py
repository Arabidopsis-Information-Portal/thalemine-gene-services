import json

#InterMine is a software on Araport that was used to generate the ThaleMine database
#InterMine documentation: intermine.readthedocs.org
#auto-generated service code
from intermine.webservice import Service
service = Service("https://apps.araport.org/thalemine/service")

#function that responds when the URL ends in /search
#this search operation is supported by the Adama middleware on Araport
#endpoints of this name are to return certain data of a gene search
def search(parameter):
    #store input as variables
    searchInput = parameter["Identifier"]
    prefOutInput = parameter["Output"]

    #determine what to return
    if prefOutInput == "all":
        print json.dumps(returnAllInfo(searchInput))
    else:
        print json.dumps(returnInfo(searchInput,prefOutInput))

#function that responds when the URL ends in /list
#this list operation is supported by the Adama middleware on Araport
#endpoints of this name are to return a list of values that can be used as parameters for the /search endpoint
def list(parameter):
    #auto-generated query code
    queryList = service.new_query("Gene")
    queryList.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")
    
    queryList.add_constraint("chromosome.primaryIdentifier", "IS NOT NULL", code = "A")

    for row in queryList.rows():
        org = {}
        org['locus_id'] = row["primaryIdentifier"]
        print json.dumps(org)
        print '---'
    return

#returns information for all fields for specfic geneID
def returnAllInfo(id):
    #auto-generated query code
    #query search thalemine
    query = service.new_query("Gene")
    #adding views to the query
    query.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")
    query.add_constraint("primaryIdentifier", "=", id, code = "A")

    #return dict of information of matching geneID
    for row in query.rows():
        return {"locus_id": row["primaryIdentifier"],
                "chromosomeLocation.end" : row["chromosomeLocation.end"],
                "chromosomeLocation.start" : row["chromosomeLocation.start"]
                }

#returns specific info about specific geneID
def returnInfo(id, out):
    #auto-generated query code
    #query search thalemine
    query = service.new_query("Gene")
    #adding views to the query
    query.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")
    query.add_constraint("primaryIdentifier", "=", id, code = "A")

    #return dict of information of matching geneID
    for row in query.rows():
        return {"locus_id": row["primaryIdentifier"], out : row[out]}
