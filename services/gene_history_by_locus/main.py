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
        "primaryIdentifier", "locusHistory.source.name",
        "locusHistory.locusOperation", "locusHistory.datestamp",
        "locusHistory.source.description", "locusHistory.source.url",
        "locusHistory.lociInvolved.primaryIdentifier"
    )

    # set the constraint value(s)
    query.add_constraint("primaryIdentifier", "=", locus, code = "A")

    # outer join on synonyms
    query.outerjoin("locusHistory.lociInvolved")

    # loop over rows of data to build the JSON object
    events = {}
    for row in query.rows():
        gene_id = row["primaryIdentifier"]
        source = row["locusHistory.source.name"]
        operation = row["locusHistory.locusOperation"]
        date = row["locusHistory.datestamp"]
        source_description = row["locusHistory.source.description"]
        source_url = row["locusHistory.source.url"]
        loci_involved = row["locusHistory.lociInvolved.primaryIdentifier"]
        key = "%s-%s-%s" % (source, operation, date)
        if not events.has_key(key):
            events[key] = {
                'locus': gene_id,
                'source': source,
                'source_description': source_description,
                'source_url': source_url,
                'operation': operation,
                'date': date,
                'loci_involved': []
            }
        if loci_involved:
            events[key]['loci_involved'].append(loci_involved)

    for event in events.values():
        record = {
            'class': 'locus_property',
            'source_text_description': 'ThaleMine Gene History',
            'locus': event['locus'],
            'source': event['source'],
            'source_description': event['source_description'],
            'source_url': event['source_url'],
            'operation': event['operation'],
            'date': event['date'],
            'loci_involved': event['loci_involved']
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
