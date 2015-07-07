import json

#intermine is data service used by thalemine
#generated python code for query
from intermine.webservice import Service
service = Service("https://apps.araport.org:443/thalemine/service")
query = service.new_query("Gene")
query.add_view(
    "briefDescription", "computationalDescription", "curatorSummary", "name", "length", "primaryIdentifier", "secondaryIdentifier", "symbol")

#operation
def search(parameter):
    #store input as variables
    searchInput = parameter["Identifier"]
    prefOutInput = parameter["Output"]

    #searchInput is null or just * - return list of all geneIDs
    if not searchInput or searchInput is'*':
        result = {"list" : returnList()}
    #searchInput has a * - return list of wildcard search matches
    elif "*" in searchInput:
        result = {"list" : wildcardGeneID(searchInput)}
    #searchInput is a specific geneID - return requested information
    else:
        result = {"gene_info" : returnInfo(searchInput, prefOutInput)}

    print json.dumps(result)

#returns list of all Gene IDs
def returnList():
    geneIDList = []

    #add each geneID to list
    for row in query.rows():
        geneIDList.append(str(row["primaryIdentifier"]))

    return geneIDList

#returns specific info about specific geneID
def returnInfo(id, out):
    #query search thalemine
    query.add_constraint("primaryIdentifier", "CONTAINS", id)

    #return information about matched geneID
    for row in query.rows():
        if id == row["primaryIdentifier"]:
            return row[out]

#returns list of matches from wildcard search
def wildcardGeneID(arg):
    #remove * symbol from string
    import re
    arg = re.sub('[*]', '', arg)

    geneIDList = []

    #query search thalemine
    query.add_constraint("primaryIdentifier", "CONTAINS", arg)

    #add wildcard matches to list
    for row in query.rows():
        if arg in str(row["primaryIdentifier"]):
            geneIDList.append(row["primaryIdentifier"])

    return geneIDList
