#gene_by_geneid_v0.1

## Synopsis

###Araport API that serves basic information about genes.

The main goal for this API was to search for a specific geneID and return chromosome information.
Another function, list, would be used to list all 30000+ geneIDs.

I was experiencing issues with the list function, so I tested the list code by having two very similar list codes: one in the list function and another in the search function.

Both functions seem to run fine on the command line. However, running them on araport.org, using Adama seems to result in a 30 second timeout for the code under the search function.

## Notes

Since this release is mainly a test, the actual search function code has been redacted. However, the parameters and other information for search remain in the metadata.yml.

Please ignore these parameters and other information, as they are not used/applicable.

## Contributors

*Iniyan Chezhian - JCVI
