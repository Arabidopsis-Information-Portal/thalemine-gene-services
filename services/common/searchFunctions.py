#returns list of all Gene IDs
def returnList():
    geneIDList = []

    #add each geneID to list
    for row in query.rows():
        geneIDList.append(str(row["primaryIdentifier"]))

    return geneIDList

#returns specific info about specific geneID
def returnInfo(id, out):
    #query search thalemine
    query.add_constraint("primaryIdentifier", "=", id, code = "A")

    #return information about matched geneID
    for row in query.rows():
        if id == row["primaryIdentifier"]:
            return row[out]

#returns list of matches from wildcard search
def wildcardGeneID(arg):
    #remove * symbol from string
    import re
    arg = re.sub('[*]', '', arg)

    geneIDList = []

    #query search thalemine
    query.add_constraint("primaryIdentifier", "CONTAINS", arg, code = "A")

    #add wildcard matches to list
    for row in query.rows():
        geneIDList.append(row["primaryIdentifier"])

    return geneIDList
