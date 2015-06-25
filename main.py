# file: main.py
import json

from intermine.webservice import Service
service = Service("https://apps.araport.org:443/thalemine/service")

#recieves a GeneID from the search and returns a briefDescription
def returnInfo(id):
#this function will look at the geneID from the search and return the basic info of that geneID

    query = service.new_query("Gene")

    # The view specifies the output columns
    query.add_view("primaryIdentifier", "briefDescription")

    print "Brief Description of %s:" %id

    for row in query.rows():
        if id == "0":
            print "There is no such Gene ID."
        elif id == row["primaryIdentifier"]:
            print row["briefDescription"]

#ID Search - Gene ID
def searchGeneID(arg):

    text = str(arg)

    #default value if there is no match
    geneID = "0"

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier")
    query.add_sort_order("Gene.primaryIdentifier", "ASC")

    for row in query.rows():
        if text == row["primaryIdentifier"]:
            geneID = text

    returnInfo(geneID)

#TODO
#Keyword Search
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
        if (text in row["briefDescription"]) or (text in row["symbol"]) or
        (text in row["secondaryIdentifier"]) or (text in row["primaryIdentifier"])or
        (text in row["name"]) or (text in row["length"]) or (text in row["curatorSummary"]) or
        (text in row["computationalDescription"]):
            results.extend(row["primaryIdentifier"])

    #TODO
    #keyword search code...

    return geneID

    #have this function make a list of the geneid. then use a for loop to send each value to the return info function

#return json.dumps(variable)
