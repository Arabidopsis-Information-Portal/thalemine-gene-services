#go_by_geneid_v1.0

## Synopsis

###Araport API that serves GO information about genes.

The main goal for this API was to have a search function for a specific geneID and return GO information.

Another function, list, would be used to list all 30000+ geneIDs that have GO information.

Genes have many IDs, but this service utilizes the Locus ID.

The Locus ID follows the format: ATXgYYYYY. The AT refers to Arabidopsis thaliana, the X number corresponds to the chromosome number, the g refers to gene, and the 5 following Ys correspond to the five-digit code, numbered from top to bottom of the chromosome.

Example Locus ID: AT4G34260

## Notes

v1.0 is the final version.

## Contributors

*Iniyan Chezhian - JCVI
