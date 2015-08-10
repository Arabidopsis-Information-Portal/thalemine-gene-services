import json

#InterMine is a software on Araport that was used to generate the ThaleMine database
#InterMine documentation: intermine.readthedocs.org
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
        returnAllInfo(searchInput)
    else:
        returnInfo(searchInput,prefOutInput)

#operation
def list(parameter):
    #auto-generated query code
    queryList = service.new_query("Gene")
    queryList.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")

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
    query.add_view(
    "goAnnotation.subject.primaryIdentifier",
    "goAnnotation.ontologyTerm.name",
    "goAnnotation.ontologyTerm.description",
    "goAnnotation.ontologyTerm.namespace",
    "goAnnotation.evidence.code.code"
    )
    #manipulate the auto-generated code to constrain to a variable
    query.add_constraint("goAnnotation.subject.primaryIdentifier", "=", id, code = "B")


    #return dict of information of matching geneID
    for row in query.rows():
        print json.dumps(
                {"locus_id" : row["goAnnotation.subject.primaryIdentifier"],
                "name" : row["goAnnotation.ontologyTerm.name"],
                "def" : row["goAnnotation.ontologyTerm.description"],
                "namespace" : row["goAnnotation.ontologyTerm.namespace"],
                "evidence_code" : row["goAnnotation.evidence.code.code"],
                }
        )
        print '---'

#returns specific info about specific geneID
def returnInfo(id, out):
    #auto-generated query code
    #query search thalemine
    query = service.new_query("Gene")
    #adding views to the query
    query.add_view(
    "goAnnotation.subject.primaryIdentifier",
    "goAnnotation.ontologyTerm.name",
    "goAnnotation.ontologyTerm.description",
    "goAnnotation.ontologyTerm.namespace",
    "goAnnotation.evidence.code.code"
    )
    #manipulate the auto-generated code to constrain to a variable
    query.add_constraint("goAnnotation.subject.primaryIdentifier", "=", id, code = "B")

    #return dict of information of matching geneID
    for row in query.rows():
        print json.dumps(
                {"goAnnotation.subject.primaryIdentifier": row["goAnnotation.subject.primaryIdentifier"],
                out : row[out]}
        )
        print '---'
