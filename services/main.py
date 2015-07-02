import json
from intermine.webservice import Service

service = Service("https://apps.araport.org:443/thalemine/service")
query = service.new_query("Gene")
query.add_view(
    "briefDescription", "computationalDescription", "curatorSummary", "name",
    "length", "primaryIdentifier", "secondaryIdentifier", "symbol"
)

def search(parameter):
    searchInput = parameter["Identifier"]
    prefOutInput = parameter["Output"]

    if not searchInput: #empty string
        result = {"list" : returnList()}
    elif "*" in searchInput:    #wildcard search
        result = {"list" : wildcardGeneID(searchInput)}
    else:   #geneID search
        result = {"gene_info" : returnInfo(searchInput, prefOutInput)}

    print json.dumps(result)

#returns list of all Gene IDs
def returnList():
    geneIDList = []

    for row in query.rows():
        geneIDList.append(str(row["primaryIdentifier"]))

    return geneIDList

def returnInfo(id, out):
    query.add_constraint("primaryIdentifier", "CONTAINS", id)
    for row in query.rows():
        if id == row["primaryIdentifier"]:
            return row[out]

def wildcardGeneID(arg):
    #remove * symbol from string
    import re
    arg = re.sub('[*]', '', arg)

    geneIDList = []

    query.add_constraint("primaryIdentifier", "CONTAINS", arg)

    #searching all the GeneIDs - matches are added to list
    for row in query.rows():
        if arg in str(row["primaryIdentifier"]):
            geneIDList.append(row["primaryIdentifier"])

    return geneIDList
