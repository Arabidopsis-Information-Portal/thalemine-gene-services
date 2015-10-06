import json
from intermine.webservice import Service

service = Service("https://apps.araport.org/thalemine/service")

def search(args):
    """
    args contains a dict with one or key:values

    locus is AGI identifier and is mandatory
    """
    locus = args["locus"].upper()

    # get a new query on the class (table) from the model
    query = service.new_query("Gene")

    # views specify the output columns
    query.add_view(
        "primaryIdentifier", "goAnnotation.ontologyTerm.description",
        "goAnnotation.ontologyTerm.name", "goAnnotation.ontologyTerm.namespace",
        "goAnnotation.evidence.code.code", "goAnnotation.dataSets.name",
        "goAnnotation.dataSets.version"
    )

    # set the constraint value(s)
    query.add_constraint("primaryIdentifier", "=", locus, code = "A")

    # print dict of information of matching geneID
    for row in query.rows():
        record = {
            'class': 'locus_property',
            'source_text_description': 'ThaleMine GO record',
            'locus': row["primaryIdentifier"],
            'description': row["goAnnotation.ontologyTerm.description"],
            'name': row["goAnnotation.ontologyTerm.name"],
            'namespace': row["goAnnotation.ontologyTerm.namespace"],
            'evidence_code': row["goAnnotation.evidence.code.code"],
            'dataset_name': row["goAnnotation.dataSets.name"],
            'dataset_version': row["goAnnotation.dataSets.version"]
        }
        print json.dumps(record, indent=2)
        print '---'

def list(args):
    # get a new query on the class (table) from the model
    query = service.new_query("Gene")

    # views specify the output columns
    query.add_view("primaryIdentifier", "chromosomeLocation.end", "chromosomeLocation.start")

    for row in query.rows():
        record = {
            'locus': row['primaryIdentifier']
        }
        print json.dumps(record, indent=2)
        print '---'
