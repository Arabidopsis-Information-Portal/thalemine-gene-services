import json

#InterMine is a software on Araport that was used to generate the ThaleMine database
#InterMine documentation: intermine.readthedocs.org
#auto-generated service code
from intermine.webservice import Service
service = Service("https://apps.araport.org/thalemine/service")
GO_FIELDS_MAP = {
    'locus_id': 'goAnnotation.subject.primaryIdentifier',
    'name': 'goAnnotation.ontologyTerm.name',
    'def': 'goAnnotation.ontologyTerm.description',
    'namespace': 'goAnnotation.ontologyTerm.namespace',
    'evidence_code': 'goAnnotation.evidence.code.code'
}

#operation
def search(parameter):
    #store input as variables
    searchInput = parameter["Identifier"]
    prefOutInput = parameter["Output"]

    # auto-generated query code
    # query search thalemine
    query = service.new_query("Gene")
    # adding views to the query
    query.add_view(
        GO_FIELDS_MAP['locus_id'],
        GO_FIELDS_MAP['name'],
        GO_FIELDS_MAP['def'],
        GO_FIELDS_MAP['namespace'],
        GO_FIELDS_MAP['evidence_code']
    )
    # manipulate the auto-generated code to constrain to a variable
    query.add_constraint(GO_FIELDS_MAP['locus_id'], "=", searchInput, code = "B")

    # print dict of information of matching geneID
    for row in query.rows():
        if prefOutInput == "all":
            record = {
                'locus_id' : row[GO_FIELDS_MAP['locus_id']],
                'name' : row[GO_FIELDS_MAP['name']],
                'def': row[GO_FIELDS_MAP['def']],
                'namespace' : row[GO_FIELDS_MAP['namespace']],
                'evidence_code' : row[GO_FIELDS_MAP['evidence_code']]
            }
        else:
            gKey = [key for key, value in GO_FIELDS_MAP.iteritems() if value == prefOutInput][0]
            record = {
                'locus_id': row[GO_FIELDS_MAP['locus_id']],
                gKey : row[prefOutInput]
            }
        print json.dumps(record, indent=2)
        print '---'

def list(parameter):
    #auto-generated query code
    queryList = service.new_query("Gene")
    queryList.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")

    for row in queryList.rows():
        org = {
            'locus_id': row['primaryIdentifier']
        }
        print json.dumps(org, indent=2)
        print '---'
