import json
from intermine.webservice import Service

service = Service("https://apps.araport.org:443/thalemine/service")
query = service.new_query("Gene")
query.add_view(
    "briefDescription", "computationalDescription", "curatorSummary", "name", "length", "primaryIdentifier", "secondaryIdentifier", "symbol")

def search(parameter):
    searchInput = parameter["Identifier"]
    prefOutInput = parameter["Output"]

    if not searchInput or searchInput is'*':
        result = {"list" : returnList()}
    elif "*" in searchInput:
        result = {"list" : wildcardGeneID(searchInput)}
    else:
        result = {"gene_info" : returnInfo(searchInput, prefOutInput)}

    print json.dumps(result)

#returns list of all Gene IDs
def returnList():
    geneIDList = []

    for row in query.rows():
        geneIDList.append(str(row["primaryIdentifier"]))

    return geneIDList

#returns specific info about specific geneID
def returnInfo(id, out):
    query.add_constraint("primaryIdentifier", "CONTAINS", id)
    for row in query.rows():
        if id == row["primaryIdentifier"]:
            return row[out]

#returns list of matches from wildcard search
def wildcardGeneID(arg):
    #remove * symbol from string
    import re
    arg = re.sub('[*]', '', arg)

    geneIDList = []

    query.add_constraint("primaryIdentifier", "CONTAINS", arg)

    for row in query.rows():
        if arg in str(row["primaryIdentifier"]):
            geneIDList.append(row["primaryIdentifier"])

    return geneIDList
