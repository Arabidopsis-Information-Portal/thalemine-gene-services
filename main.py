# file: main.py
import json

from intermine.webservice import Service
service = Service("https://apps.araport.org:443/thalemine/service")



#TODO
#The genes will be indexed and referenced with Gene ID

#ID Search
def idSearch():

    geneID =

    #adding the ID search to this list of Gene IDs
    geneIDList = searchGeneID()


    print geneIDList



    print "END NOW"

    #TODO
    #Make sure duplicates in the list are removed.
    #maybe use the count() method?





#TODO
#make this method return the list, and send it to a print method
#share the print method with the keyword search


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
