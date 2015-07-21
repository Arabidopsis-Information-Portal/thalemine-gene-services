import json
#service to access thalemine database
from intermine.webservice import Service
service = Service("https://apps.araport.org/thalemine/service")

#operation to print the last ~20 locus ids
def search(parameter):

    querySearch = service.new_query("Gene")
    querySearch.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")
    cnt = 0
    for row in querySearch.rows():
        org = {}
        org['locus_id'] = row["primaryIdentifier"]
        if (cnt > 33590):
            print json.dumps(org)
            print '---'
        cnt += 1
    return

#operation to print the first 30000 locus ids
def list(parameter):

    querySearch = service.new_query("Gene")
    querySearch.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")
    cnt = 0
    for row in querySearch.rows():
        org = {}
        org['locus_id'] = row["primaryIdentifier"]
        print json.dumps(org)
        print '---'
        cnt += 1
        if (cnt > 30000):
            break
    return
