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
    # store input as variables
    searchInput = parameter["Identifier"]
    prefOutInput = parameter["Output"]

    # auto-generated query code
    # query search thalemine
    query = service.new_query("Gene")
    # adding views to the query
    query.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")
    query.add_constraint("primaryIdentifier", "=", searchInput, code = "A")

    # print dict of information of matching geneID
    for row in query.rows():
        if prefOutInput == "all":
            record = {
                "locus_id": row["primaryIdentifier"],
                "chromosomeLocation.end": row["chromosomeLocation.end"],
                "chromosomeLocation.start": row["chromosomeLocation.start"]
            }
        else:
            record = {
                "locus_id": row["primaryIdentifier"],
                prefOutInput: row[prefOutInput]
            }
        print json.dumps(record, indent=2)
        print '---'

#function that responds when the URL ends in /list
#this list operation is supported by the Adama middleware on Araport
#endpoints of this name are to return a list of values that can be used as parameters for the /search endpoint
def list(parameter):
    #auto-generated query code
    queryList = service.new_query("Gene")
    queryList.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")

    for row in queryList.rows():
        org = {
            'locus_id': row['primaryIdentifier']
        }
        print json.dumps(org, indent=2)
        print '---'
