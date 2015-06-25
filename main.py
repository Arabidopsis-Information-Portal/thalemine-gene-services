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

    text = str(arg)

    #default value if there is no match
    geneID = "0"

    #TODO
    #keyword search code...

    return geneID
