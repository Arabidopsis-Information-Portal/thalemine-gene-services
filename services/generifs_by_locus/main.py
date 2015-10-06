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
        "primaryIdentifier", "geneRifs.annotation", "geneRifs.timeStamp",
        "geneRifs.publication.firstAuthor", "geneRifs.publication.title",
        "geneRifs.publication.year", "geneRifs.publication.journal",
        "geneRifs.publication.volume", "geneRifs.publication.pages",
        "geneRifs.publication.pubMedId", "geneRifs.publication.issue"
    )

    # set the constraint value(s)
    query.add_constraint("primaryIdentifier", "=", locus, code = "A")

    # print dict of information of matching geneID
    for row in query.rows():
        record = {
            'class': 'locus_property',
            'source_text_description': 'ThaleMine GeneRIF record',
            'locus': row["primaryIdentifier"],
            'annotation': row["geneRifs.annotation"],
            'last_updated': row["geneRifs.timeStamp"],
            'publication': {
                'first_author': row["geneRifs.publication.firstAuthor"],
                'title': row["geneRifs.publication.title"],
                'year': row["geneRifs.publication.year"],
                'journal': row["geneRifs.publication.journal"],
                'volume': row["geneRifs.publication.volume"],
                'pages': row["geneRifs.publication.pages"],
                'pubmed_id': row["geneRifs.publication.pubMedId"],
                'issue': row["geneRifs.publication.issue"]
            },
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
