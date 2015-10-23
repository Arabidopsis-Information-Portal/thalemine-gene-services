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
        "primaryIdentifier", "overlappingFeatures.primaryIdentifier",
        "overlappingFeatures.chromosomeLocation.start",
        "overlappingFeatures.chromosomeLocation.end",
        "overlappingFeatures.chromosomeLocation.strand",
        "overlappingFeatures.sequenceOntologyTerm.name",
        "overlappingFeatures.length",
        "overlappingFeatures.chromosome.primaryIdentifier"
    )

    # set the constraint value(s)
    query.add_constraint("primaryIdentifier", "=", locus, code = "A")

    # outer join on synonyms
    query.outerjoin("overlappingFeatures.sequenceOntologyTerm")

    # loop over rows of data to build the JSON object
    for row in query.rows():
        strand = ''
        if row["overlappingFeatures.chromosomeLocation.strand"]:
            if int(row["overlappingFeatures.chromosomeLocation.strand"]) > 0:
                strand = '+'
            else:
                strand = '-'

        feature_type = row["overlappingFeatures.sequenceOntologyTerm.name"]
        record = {
            'class': 'locus_property',
            'source_text_description': 'ThaleMine Gene Feature',
            'locus': row["primaryIdentifier"],
            'feature_id': row["overlappingFeatures.primaryIdentifier"],
            'length': row["overlappingFeatures.length"],
            'location': row["overlappingFeatures.chromosome.primaryIdentifier"],
            'chromosome_start': row["overlappingFeatures.chromosomeLocation.start"],
            'chromosome_end': row["overlappingFeatures.chromosomeLocation.end"],
            'strand': strand,
            'feature_type': feature_type if feature_type else ''
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
