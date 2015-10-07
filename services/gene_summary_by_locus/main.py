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
    query.add_view("primaryIdentifier", "symbol", "name", "briefDescription",
                   "computationalDescription", "curatorSummary", "length",
                   "chromosome.primaryIdentifier", "chromosomeLocation.end",
                   "chromosomeLocation.start", "chromosomeLocation.strand", "synonyms.value")

    # set the constraint value(s)
    query.add_constraint("primaryIdentifier", "=", locus, code = "A")

    # outer join on synonyms
    query.outerjoin("synonyms")

    # loop over rows of data to build the JSON object
    synonyms = []
    found = False
    for row in query.rows():
        gene_id = row["primaryIdentifier"]
        symbol = row["symbol"]
        name = row["name"]
        brief_description = row["briefDescription"]
        computational_description = row["computationalDescription"]
        curator_summary = row["curatorSummary"]
        length = row["length"]
        location = row["chromosome.primaryIdentifier"]
        chromosome_start = row["chromosomeLocation.start"]
        chromosome_end = row["chromosomeLocation.end"]
        strand = row["chromosomeLocation.strand"]
        synonyms.append(row["synonyms.value"])
        found = True

    if found:
        record = {
            'class': 'locus_property',
            'source_text_description': 'ThaleMine Gene Summary',
            'locus': gene_id,
            'symbol': symbol,
            'name': name,
            'brief_description': brief_description,
            'computational_description': computational_description,
            'curator_summary': curator_summary,
            'length': length,
            'location': location,
            'chromosome_start': chromosome_start,
            'chromosome_end': chromosome_end,
            'strand': strand,
            'synonyms': synonyms
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
