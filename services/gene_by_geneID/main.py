import json

#intermine search common algorithms
from services.common.searchFunctions import returnList
from services.common.searchFunctions import wildcardGeneID
from services.common.searchFunctions import returnInfo

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
