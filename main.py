#import json
from intermine.webservice import Service

service = Service("https://apps.araport.org:443/thalemine/service")

#function used to test code
#python -c 'import main; print main.function("<parameter>")'
def function(arg):
    if not arg: #empty string
        return returnList()
    elif "*" in arg:    #wildcard search
        return wildcardGeneID(arg)
    else:   #geneID search
        return returnInfo(arg)

#returns list of all Gene IDs
def returnList():
    geneIDList = []

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier")

    for row in query.rows():
        geneIDList.append(str(row["primaryIdentifier"]))

    return geneIDList

#recieves a GeneID - returns briefDescription, easily changeable to any field desired
def returnInfo(id):
#this function will look at the geneID from the search and return the basic info of that geneID

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "briefDescription")

    print "Brief Description of %s:" %id

    for row in query.rows():
        if id == row["primaryIdentifier"]:
            return row["briefDescription"]

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

#ignore below code
"""
#TODO
#Keyword Search - like Google
def searchKeyword(arg):

    results = []

    text = str(arg)

    #default value if there is no match
    geneID = "0"

    query = service.new_query("Gene")

    # The view specifies the output columns
    query.add_view(
        "briefDescription", "symbol", "secondaryIdentifier", "primaryIdentifier",
        "name", "length", "curatorSummary", "computationalDescription"
    )

    for row in query.rows():
        if (text in row["briefDescription"]) or (text in row["symbol"])                 \
        or (text in row["secondaryIdentifier"]) or (text in row["primaryIdentifier"])   \
        or (text in row["name"]) or (text in row["curatorSummary"])                     \
        or (text in row["computationalDescription"]):
            results.extend(row["primaryIdentifier"])

    #should return an array of geneID
    return geneID
"""
#return json.dumps(variable)
