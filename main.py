import json
from intermine.webservice import Service

service = Service("https://apps.araport.org:443/thalemine/service")
query = service.new_query("Gene")
query.add_view(
    "briefDescription", "computationalDescription", "curatorSummary", "name",
    "length", "primaryIdentifier", "secondaryIdentifier", "symbol"
)

#function used to test code
#python -c 'import main; main.function("<parameter>")'
def search(arg):

    searchInput = arg["Search"]

    prefOutInput = arg["Output"]

    if not searchInput: #empty string
        print returnList()
    elif "*" in searchInput:    #wildcard search
        print wildcardGeneID(searchInput)
    else:   #geneID search
        print returnInfo(searchInput, prefOutInput)

#returns list of all Gene IDs
def returnList():
    geneIDList = []

    for row in query.rows():
        geneIDList.append(str(row["primaryIdentifier"]))

    return geneIDList

#recieves a GeneID - returns briefDescription, easily changeable to any field desired
def returnInfo(id, out):
#this function will look at the geneID from the search and return the basic info of that geneID
    print "Brief Description of %s:" %id

    for row in query.rows():
        if id == row["primaryIdentifier"]:
            return row[out]

def wildcardGeneID(arg):
    #remove * symbol from string
    import re
    arg = re.sub('[*]', '', arg)

    geneIDList = []

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier")

    #searching all the GeneIDs - matches are added to list
    for row in query.rows():
        if arg in str(row["primaryIdentifier"]):
            geneIDList.append(row["primaryIdentifier"])

    return geneIDList
