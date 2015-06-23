# file: main.py
import json

from intermine.webservice import Service
service = Service("http://apps.araport.org:443/thalemine/service")



#TODO
#The genes will be indexed and referenced with Gene ID

#ID Search
def IDsearch(args):

    geneIDList = []

#adding the ID search to this list of Gene IDs
    geneIDList.extend(searchGeneID(args))



#TODO
#Make sure duplicates in the list are removed.
#maybe use the count() method?


#      for p in geneIDList: print p

#TODO
#make this method return the list, and send it to a print method
#share the print method with the keyword search


#ID Search Functions
#ID Search - Gene ID
def searchGeneID(args):

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier")
    query.add_sort_order("Gene.primaryIdentifier", "ASC")

    for row in query.rows():
        return row["primaryIdentifier"]

#
def search(args):



#
def search(args):


#TODO
#Keyword Search
