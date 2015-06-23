# file: main.py
import json

#TODO
#The genes will be indexed and referenced with Gene ID



from intermine.webservice import Service
service = Service("http://apps.araport.org:443/thalemine/service")


#ID Search
def IDsearch(args):

    geneIDList = []

    geneIDList.append()



#TODO
#Make sure duplicates in the list are removed.
#maybe use the count() method?


#    for p in geneIDList: print p

#TODO
#make this method return the list, and send it to a print method
#share the print method with the keyword search


#ID Search Functions
#ID Search - Gene ID
def searchGeneID(args):

#START COPIED CODE

    # Get a new query on the class (table) you will be querying:
    query = service.new_query("Gene")

    # The view specifies the output columns
    query.add_view("primaryIdentifier")

    # Uncomment and edit the line below (the default) to select a custom sort order:
    # query.add_sort_order("Gene.primaryIdentifier", "ASC")

    for row in query.rows():
        print row["primaryIdentifier"]

#END COPIED CODE


#
def search(args):



#
def search(args):


#TODO
#Keyword Search
