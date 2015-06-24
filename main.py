# file: main.py
import json

from intermine.webservice import Service
service = Service("https://apps.araport.org:443/thalemine/service")

#TODO
#The genes will be indexed and referenced with Gene ID

#ID Search
def returnInfo():
    #TODO
    #this function will look at the geneID from the search and return the basic info of that geneID


#ID Search Functions
#ID Search - Gene ID
def searchGeneID(arg):

    text = str(arg)

    #defalt value if there is no match
    geneID = "0"

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier")
    query.add_sort_order("Gene.primaryIdentifier", "ASC")

    for row in query.rows():
        #print row["primaryIdentifier"]
        if text == row["primaryIdentifier"]:
            geneID = text

    return geneID


#TODO
#Keyword Search
def searchKeyword(arg):

    text = str(arg)

    #defalt value if there is no match
    geneID = "0"

    #TODO
    #keyword search code...

    return geneID
