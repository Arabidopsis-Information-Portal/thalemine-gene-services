import json

#intermine is data service used by thalemine
#auto-generated service code
from intermine.webservice import Service
service = Service("https://apps.araport.org/thalemine/service")

#operation
def search(parameter):
    #store input as variables
    searchInput = parameter["Identifier"]
    prefOutInput = parameter["Output"]

    #determine what to return
    if prefOutInput == "all":
        print json.dumps(returnAllInfo(searchInput))
    else:
        print json.dumps(returnInfo(searchInput,prefOutInput))

#operation
def list(parameter):
    #auto-generated service code
    queryList = service.new_query("Gene")
    queryList.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")
    queryList.add_constraint("chromosome.primaryIdentifier", "IS NOT NULL", code = "A")
    for row in queryList.rows():
        org = {}
        org['locus_id'] = row["primaryIdentifier"]
        print json.dumps(org)
        print '---'

    return

#TODO
#returns information for all fields for specfic geneID
def returnAllInfo(id):
    #auto-generated query code
    #query search thalemine
    query = service.new_query("Gene")
    #adding views to the query
    query.add_view(
    "goAnnotation.subject.primaryIdentifier", "goAnnotation.ontologyTerm.name",
    "goAnnotation.ontologyTerm.description",
    "goAnnotation.ontologyTerm.namespace", "goAnnotation.evidence.code.code"
    )
    #adding a constraint to limit the results
    query.add_constraint("goAnnotation.subject.primaryIdentifier", "=", id, code = "B")

    #return dict of information of matching geneID
    for row in query.rows():
        return {"primaryIdentifier": row["goAnnotation.subject.primaryIdentifier"],
                "chromosomeLocation.end" : row["chromosomeLocation.end"],
                "chromosomeLocation.start" : row["chromosomeLocation.start"]
        }

#TODO
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
        return {"primaryIdentifier": row["primaryIdentifier"], out : row[out]}
