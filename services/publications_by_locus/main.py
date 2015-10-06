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
        "primaryIdentifier", "publications.firstAuthor", "publications.title",
        "publications.year", "publications.journal", "publications.volume",
        "publications.pages", "publications.pubMedId", "publications.issue"
    )

    # set the constraint value(s)
    query.add_constraint("primaryIdentifier", "=", locus, code = "A")

    # print dict of information of matching geneID
    for row in query.rows():
        record = {
            'class': 'locus_property',
            'source_text_description': 'ThaleMine publication record',
            'locus': row["primaryIdentifier"],
            'first_author': row["publications.firstAuthor"],
            'title': row["publications.title"],
            'year': row["publications.year"],
            'journal': row["publications.journal"],
            'volume': row["publications.volume"],
            'pages': row["publications.pages"],
            'pubmed_id': row["publications.pubMedId"],
            'issue': row["publications.issue"]
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
