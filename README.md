# ThaleMine Gene Webservices

These are [Araport](http://www.araport.org) API wrappers around various ThaleMine webservices for retrieving information about genes. The list endpoint in all services returns a list a valid AGI locus identifiers.

## gene_summary_by_locus
Given an AGI locus identifier return summary information about a gene from ThaleMine.
```
$ http "https://api.araport.org/community/v0.3/araport/gene_summary_by_locus_v0.1/search?locus=AT1G65480" Authorization:"Bearer $TOKEN"
{
    "metadata": {
        "time_in_main": 0.37862300872802734
    },
    "result": [
        {
            "brief_description": "PEBP (phosphatidylethanolamine-binding protein) family protein",
            "chromosome_end": 24333934,
            "chromosome_start": 24331428,
            "class": "locus_property",
            "computational_description": "FLOWERING LOCUS T (FT); FUNCTIONS IN: phosphatidylethanolamine binding, protein binding; INVOLVED IN: photoperiodism, flowering, positive regulation of flower development, regulation of flower development; LOCATED IN: nucleus, cytoplasm; EXPRESSED IN: 14 plant structures; EXPRESSED DURING: 7 growth stages; CONTAINS InterPro DOMAIN/s: Phosphatidylethanolamine-binding, conserved site (InterPro:IPR001858), Phosphatidylethanolamine-binding protein PEBP (InterPro:IPR008914); BEST Arabidopsis thaliana protein match is: PEBP (phosphatidylethanolamine-binding protein) family protein (TAIR:AT4G20370.1); Has 2182 Blast hits to 2182 proteins in 306 species: Archae - 0; Bacteria - 0; Metazoa - 594; Fungi - 140; Plants - 1404; Viruses - 3; Other Eukaryotes - 41 (source: NCBI BLink).",
            "curator_summary": "FT, together with LFY, promotes flowering and is antagonistic with its homologous gene, TERMINAL FLOWER1 (TFL1). FT is expressed in leaves and is induced by long day treatment. Either the FT mRNA or protein is translocated to the shoot apex where it induces its own expression. Recent data suggests that FT protein acts as a long-range signal. FT is a target of CO and acts upstream of SOC1.",
            "length": 2507,
            "location": "Chr1",
            "locus": "AT1G65480",
            "name": "FLOWERING LOCUS T",
            "source_text_description": "ThaleMine Gene Summary",
            "strand": "1",
            "symbol": "FT",
            "synonyms": [
                "RSB8"
            ]
        }
    ],
    "status": "success"
}
```

## gene_history_by_locus
Given an AGI locus identifier return history information about a gene from ThaleMine.
```
$ http "https://api.araport.org/community/v0.3/araport/gene_history_by_locus_v0.1/search?locus=AT1G65480" Authorization:"Bearer $TOKEN"
{
    "metadata": {
        "time_in_main": 0.4304320812225342
    },
    "result": [
        {
            "class": "locus_property",
            "date": "20010104",
            "loci_involved": [],
            "locus": "AT1G65480",
            "operation": "new",
            "source": "TIGR",
            "source_description": null,
            "source_text_description": "ThaleMine Gene History",
            "source_url": null
        },
        {
            "class": "locus_property",
            "date": "20020419",
            "loci_involved": [],
            "locus": "AT1G65480",
            "operation": "new",
            "source": "MIPS",
            "source_description": null,
            "source_text_description": "ThaleMine Gene History",
            "source_url": null
        }
    ],
    "status": "success"
}
```

## gene_features_by_locus
Given an AGI locus identifier return the overlapping features of a gene from ThaleMine.
```
$ http "https://api.araport.org/community/v0.3/araport/gene_features_by_locus_v0.2/search?locus=AT1G65480" Authorization:"Bearer $TOKEN"
{
    "metadata": {
        "time_in_main": 0.45671606063842773
    },
    "result": [
        {
            "chromosome_end": 24334499,
            "chromosome_start": 24331373,
            "class": "locus_property",
            "feature_id": "AT1G65480 0.5kb downstream",
            "feature_type": "",
            "length": 3127,
            "location": "Chr1",
            "locus": "AT1G65480",
            "source_text_description": "ThaleMine Gene Feature",
            "strand": "+"
        },
        {
            "chromosome_end": 24333999,
            "chromosome_start": 24330873,
            "class": "locus_property",
            "feature_id": "AT1G65480 0.5kb upstream",
            "feature_type": "",
            "length": 3127,
            "location": "Chr1",
            "locus": "AT1G65480",
            "source_text_description": "ThaleMine Gene Feature",
            "strand": "+"
        },
        ...
    ],
    "status": "success"
}
```

## gene_ontology_by_locus
Given an AGI locus identifier return Gene ontology information from ThaleMine.
```
$ http "https://api.araport.org/community/v0.3/araport/gene_ontology_by_locus_v0.2/search?locus=AT1G65480" Authorization:"Bearer $TOKEN"
{
    "metadata": {
        "time_in_main": 0.45537710189819336
    },
    "result": [
        {
            "class": "locus_property",
            "dataset_name": "GO Annotation from UniProt",
            "dataset_version": "06/30/2015",
            "description": "The process whose specific outcome is the progression of the flower over time, from its formation to the mature structure. The flower is the reproductive structure in a plant, and its development begins with the transition of the vegetative or inflorescence meristem into a floral meristem.",
            "evidence_codes": [
                "IEA"
            ],
            "locus": "AT1G65480",
            "name": "flower development",
            "namespace": "biological_process",
            "source_text_description": "ThaleMine GO record"
        },
        {
            "class": "locus_property",
            "dataset_name": "GO Annotation from UniProt",
            "dataset_version": "06/30/2015",
            "description": "The process in which relatively unspecialized cells, e.g. embryonic or regenerative cells, acquire specialized structural and/or functional features that characterize the cells, tissues, or organs of the mature organism or some other relatively stable phase of the organism's life history. Differentiation includes the processes involved in commitment of a cell to a specific fate and its subsequent development to the mature state.",
            "evidence_codes": [
                "IEA"
            ],
            "locus": "AT1G65480",
            "name": "cell differentiation",
            "namespace": "biological_process",
            "source_text_description": "ThaleMine GO record"
        },
        ...
    ],
    "status": "success"
}
```

## generifs_by_locus
Given an AGI locus identifier return GeneRIF information from ThaleMine.
```
$ http "https://api.araport.org/community/v0.3/araport/generifs_by_locus_v0.1/search?locus=AT1G65480" Authorization:"Bearer $TOKEN"
{
    "metadata": {
        "time_in_main": 0.5702738761901855
    },
    "result": [
        {
            "annotation": "A region important in vivo localizes to a 14-amino-acid segment that evolves very rapidly in TFL1 orthologs, but is almost invariant in FT orthologs.",
            "class": "locus_property",
            "last_updated": "Wed Jan 20 19:00:00 EST 2010",
            "locus": "AT1G65480",
            "publication": {
                "first_author": "Ahn JH",
                "issue": "3",
                "journal": "EMBO J",
                "pages": "605-14",
                "pubmed_id": "16424903",
                "title": "A divergent external loop confers antagonistic activity on floral regulators FT and TFL1.",
                "volume": "25",
                "year": 2006
            },
            "source_text_description": "ThaleMine GeneRIF record"
        },
        {
            "annotation": "Antagonistic roles of SEPALLATA3, FT and FLC genes as targets of the polycomb group gene CURLY LEAF",
            "class": "locus_property",
            "last_updated": "Fri Jun 29 20:00:00 EDT 2012",
            "locus": "AT1G65480",
            "publication": {
                "first_author": "Lopez-Vernaza M",
                "issue": "2",
                "journal": "PLoS One",
                "pages": "e30715",
                "pubmed_id": "22363474",
                "title": "Antagonistic roles of SEPALLATA3, FT and FLC genes as targets of the polycomb group gene CURLY LEAF.",
                "volume": "7",
                "year": 2012
            },
            "source_text_description": "ThaleMine GeneRIF record"
        },
        ...
    ],
    "status": "success"
}
```

## publications_by_locus
Given an AGI locus identifier return publication information from ThaleMine.
```
$ http "https://api.araport.org/community/v0.3/araport/publications_by_locus_v0.1/search?locus=AT1G65480" Authorization:"Bearer $TOKEN"
{
    "metadata": {
        "time_in_main": 0.5910820960998535
    },
    "result": [
        {
            "class": "locus_property",
            "first_author": "Abe M",
            "issue": "5737",
            "journal": "Science",
            "locus": "AT1G65480",
            "pages": "1052-6",
            "pubmed_id": "16099979",
            "source_text_description": "ThaleMine publication record",
            "title": "FD, a bZIP protein mediating signals from the floral pathway integrator FT at the shoot apex.",
            "volume": "309",
            "year": 2005
        },
        {
            "class": "locus_property",
            "first_author": "Adams S",
            "issue": "2",
            "journal": "Plant J",
            "locus": "AT1G65480",
            "pages": "257-67",
            "pubmed_id": "19563438",
            "source_text_description": "ThaleMine publication record",
            "title": "Interaction between the light quality and flowering time pathways in Arabidopsis.",
            "volume": "60",
            "year": 2009
        },
        ...
    ],
    "status": "success"
}
```

## Contributors
  * Erik Ferlanti - JCVI
  * Iniyan Chezhian - JCVI
