---
title: Resources
category: Reproducible-Data-Analysis
layout: default
docs_css: markdown
---


# Metainformation Template

## CV terms

| Issue 84 metadata key           | Corresponding bio.tools CV term                                                                  | Type of value or list of values   |
|---------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------|
| Homepage                        |                                                                                                  |                                   |
| Developmental stage of the tool | maturity                                                                                         | (Emerging, Mature , Legacy)       |
| Topic                           | (could be ELIXIR Community)                                                                      |                                   |
| Software or data license        | license                                                                                          | string                            |
| Description                     |                                                                                                  | multiline varchar (max. 50 lines) |
| Input format                    | see [EBI](https://www.ebi.ac.uk/ols4/ontologies/edam/classes/http%253A%252F%252Fedamontology.org%252Fformat_1915?lang=en)  | [^2]               |
| Tool operation (function)       | see [link](https://bioportal.bioontology.org/ontologies/EDAM?p=classes&conceptid=operation_0004) | [^1]                              |
| Output data                     | see [EBI](https://www.ebi.ac.uk/ols4/ontologies/edam/classes/http%253A%252F%252Fedamontology.org%252Fformat_1915?lang=en)  |                    |
| Credits and support             | entity type, entity role                                                                         |                                   |

[^1]: Alignment, Analysis, Annotation, Calculation, Classification, Clustering, Comparison, Conversion, Correlation, Data handling, Design, Generation, Indexing, Mapping,
Modelling and simulation, Optimisation and refinement, Prediction and recognition, Quantification, Service management, Validation, Visualisation

[^2]: FASTA, SAM, TSV, CSV, XLSX, Image

---

## Template
### Homepage
### Maturity
### Topic
### License
### Description
### Input format
### Tool operation
### Output data
### Credits, support
  - code: github/gitlab/sourceforge link
  - doi: [10.XXXX/YYYYYY](doi.org/10.xxxx/YYYYYYYY)


# Bioinformatic tools

---

## Disclaimer: Changes in the tool display

We recently created a [NFDI4Microbiota domain](https://nfdi4microbiota.bio.tools) on [the life sciences software registry bio.tools](https://bio.tools) and we will soon be displaying all the tools that NFDI4Microbiota created as well as the ones that NFDI4Microbiota consortium members endorse and highly recommend.

Thank you for your patience while we sort out editing rights and collection labels.
Below you can browse tool recommendations from our consortium members.


## bakta
### Homepage
https://github.com/oschwengers/bakta
### maturity
Mature
### topic
nnotation of bacterial genomes and plasmids
### license
[GPL-3.0](https://opensource.org/license/gpl-3-0/)
### Description
Bakta is a tool for the rapid & standardized annotation of bacterial genomes and plasmids from both isolates and MAGs. It provides dbxref-rich, sORF-including and taxon-independent annotations in machine-readable JSON & bioinformatics standard file formats for automated downstream analysis.
### Input format
(zipped) fasta
### Tool operation
annotation
### Output data
.tsv: annotations as simple human readble TSV
.gff3: annotations & sequences in GFF3 format
.gbff: annotations & sequences in (multi) GenBank format
.embl: annotations & sequences in (multi) EMBL format
.fna: replicon/contig DNA sequences as FASTA
.ffn: feature nucleotide sequences as FASTA
.faa: CDS/sORF amino acid sequences as FASTA
.hypotheticals.tsv: further information on hypothetical protein CDS as simple human readble tab separated values
.hypotheticals.faa: hypothetical protein CDS amino acid sequences as FASTA
.json: all (internal) annotation & sequence information as JSON
.txt: summary as TXT
.png: circular genome annotation plot as PNG
.svg: circular genome annotation plot as SVG
### Credits, support
  - code: [oschwengers@github](https://github.com/oschwengers/bakta)
  - doi: [10.1099/mgen.0.000685](https://doi.org/10.1099/mgen.0.000685)


---

## andi
### Homepage
http://github.com/evolbioinf/andi/
### maturity
Mature
### topic
Phylogenetic analysis
### license
[GPL-v3](https://opensource.org/license/gpl-3-0/)
### Description
Andi estimates the evolutionary distance between closely related genomes.
These distances can be used to rapidly infer phylogenies for big sets of genomes. Because andi does not compute full alignments, it is so efficient that it scales even up to thousands of bacterial genomes.
### Input
2 fasta files
### Tool operation
Calculation
### Output data
txt (distance matrix)
### Credits, support
 - github: @haubold
 - doi: [10.1093/bioinformatics/btu815](https://doi.org/10.1093/bioinformatics/btu815)


---

## xenoseq
### Homepage
https://github.com/bramvandijk88/xenoseq
### maturity
Mature
### topic
Metagenomics, horizontal gene transfer
### license
[GPL-3.0](https://opensource.org/license/gpl-3-0/)
### Description
Pipeline to automate the comparison between short-read libraries to detect foreign ("xenotypic") sequences.
### Input format
fastq, tsv
### Tool operation
Sequence analysis
### Output data
fasta, tsv
### Credits, support
  - github: @bramvandijk88


---

## syntenet
### Homepage
<https://doi.org/doi:10.18129/B9.bioc.syntenet>
### maturity
Mature
### topic
Inference And Analysis Of Synteny Networks
### license
[GPL-3.0](https://opensource.org/license/gpl-3-0/)
### Description
syntenet can be used to infer synteny networks from whole-genome protein sequences and analyze them. Anchor pairs are detected with the MCScanX algorithm, which was ported to this package with the Rcpp framework for R and C++ integration. Anchor pairs from synteny analyses are treated as an undirected unweighted graph (i.e., a synteny network), and users can perform: i. network clustering; ii. phylogenomic profiling (by identifying which species contain which clusters) and; iii. microsynteny-based phylogeny reconstruction with maximum likelihood.
### Input format
fasta, gff, gtf
### Tool operation
Phylogenetic Inference
### Output data
R data.frame
### Credits, support
  - github: @almeidasilvaf
  - doi:10.1093/bioinformatics/btac806


---

## DeLTA2
### Homepage
https://gitlab.com/dunloplab/delta
### maturity
Mature
### topic
Bioimage segmentation and tracking
### license
[MIT](https://opensource.org/license/mit/)
### Description
DeLTA (Deep Learning for Time-lapse Analysis) is a deep learning-based image processing pipeline for segmenting and tracking single cells in time-lapse microscopy movies.
### Input format
czi, tiff, png, jpg
### Tool operation
Classication
### Output data
tiff, tsv
### Credits, support
  - gitlab: @jblugagne
  - doi:10.1371/journal.pcbi.1009797


---

## Omnipose
### Homepage
https://github.com/kevinjohncutler/omnipose
### maturity
Mature
### topic
Bioimage segmentation
### license
[Omnipose NonCommercial License](https://github.com/kevinjohncutler/omnipose?tab=License-1-ov-file#readme)
### Description
Omnipose is a general image segmentation tool that builds on Cellpose in a number of ways described in our paper. It works for both 2D and 3D images and on any imaging modality or cell shape, so long as you train it on representative images.
### Input format
czi, tiff, png, jpg
### Tool operation
Classification
### Output data
tiff, hdf5
### Credits, support
  - github: @kevinjohncutler
  - doi:10.1038/s41592-022-01639-4


---

## RAREFAN
### Homepage
http://rarefan.evolbio.mpg.de
### maturity
Mature
### topic
Genome sequence analysis
### license
[MIT](https://opensource.org/license/mit/)
### Description
The RAREFAN webserver aims to identify and analyze RAYT transposases and their associated REPIN (Repetitive Extragenic PalINdromic sequences) in bacterial species. The input to the server is a selection of closely related strains (less than 5% divergence). Our service provides an analysis of REPIN population size, how it relates to REPIN replication rate and the presence and absence of RAYTs across all submitted genomes.
### Input
fasta
### Tool operation
Genome annotation
### Output data
gff3, html, R
### Credits, support
  - github: @CFGrote
  - doi:10.24072/pcjournal.244


---

## ProteinOrtho
### Homepage
https://gitlab.com/paulklemm_PHD/proteinortho
### maturity
Mature
### topic
Comparative Genomics, Orthology
### license
[GPL-3.0](https://opensource.org/license/gpl-3-0/)
### Description
Proteinortho is a tool to detect orthologous genes within different species.
For doing so, it compares similarities of given gene sequences and clusters them to find significant groups.
Input: Multiple fasta files (orange boxes) with many proteins/genes (circles).
Output: Groups (*.proteinortho) and pairs (*.proteinortho-graph) of orthologs proteins/genes.
The algorithm was designed to handle large-scale data and can be applied to hundreds of species at one.
To enhance the prediction accuracy, the relative order of genes (synteny) can be used as additional feature for the discrimination of orthologs. The corresponding extension, namely PoFF (doi:10.1371/journal.pone.0105015), is already build in Proteinortho.
### Input
FASTA
### Tool operation
Analysis, Clustering
### Output data
tsv, graph, html, xml
### Credits, support
 - gitlab: @paulklemm_PHD
 - doi:10.1186/1471-2105-12-124


---

## vConTACT
### Homepage
 ### maturity
Mature
### topic
Taxonomy
### license
[GPL-3.0](https://opensource.org/license/gpl-3-0/)
### Description
vConTACT2 is a tool to perform guilt-by-contig-association classification of viral genomic sequence data. It's designed to cluster and provide taxonomic context of viral metagenomic sequencing data.
### Input
FASTA
### Tool operation
classification
### Output data
TSV,  network file, annotation file
### Credits, support
 - code: https://bitbucket.org/MAVERICLab/vcontact2/src/master/
 - doi: [10.1038/s41587-019-0100-8](10.1038/s41587-019-0100-8)


---

## VirFinder
### Homepage
https://github.com/jessieren/VirFinder
### maturity
Mature
### topic
Prediction of viral sequences
### license
USC-RL v1.0
### Description
The package provides functions to predict viral sequences in a fasta file, such as the assembled contigs from metagenomic data. The method has good prediction accuracy for short (~1kb) and noval viral sequences.
The prediction method is based on the sequence signatures (k-tuple word frequencies) that distinguish virus from host sequences. The model was trained using equal number of known viral and host sequences. For a query sequence, the number of occurrences of k-tuple words are first counted by a c++ program using a hash table. Then the sequence is predicted based on the k-tuple word frequencies using a logistic regression model trained with previously known sequences.
### Input
FASTA
### Tool operation
R
### Output data
TSV
### Credits, support
 - code: https://github.com/jessieren/VirFinder
 - doi:


---

## deepARG
### Homepage
[https://github.com/gaarangoa/deeparg](https://github.com/gaarangoa/deeparg)
### Maturity
Mature
### Topic
Antibiotic Resistance Genes Prediction from metagenomes
### License
[MIT](https://opensource.org/license/mit/)
The databases used may have commercial restrictions
### Description
The deepARG tool leverages deep learning techniques to predict antibiotic resistance genes (ARGs) from genetic sequences. It is designed to handle both DNA and protein sequences, making it versatile for various research applications. By using advanced machine learning algorithms, deepARG can accurately identify and categorize ARGs. Detailed documentation and usage instructions are provided in the GitHub repository, including how to install, run the tool, and interpret its outputs.
### Input
- DNA sequences (fasta)
- Protein sequences (faa)
- Short reads (fast)
### Tool Operation
- Genome annotation
### Output Data
- tsv
- Predictions of antibiotic resistance genes with associated metadata
### Credits, Support
- Creator: Gustavo Arango-Argoty
- github: @gaarangoa
- doi: [10.1186/s40168-018-0401-z](https://doi.org/10.1186/s40168-018-0401-z)


---

## Qiita
### Homepage
[https://qiita.ucsd.edu/](https://qiita.ucsd.edu/)
### maturity
Mature
### topic
Multiomics databasing analysis
### license
[BSD 3-Clause](https://opensource.org/license/bsd-3-clause/)
### Description
Qiita (canonically pronounced cheetah) is an entirely open-source microbial study management platform. It allows users to keep track of multiple studies with multiple ‘omics data. Additionally, Qiita is capable of supporting multiple analytical pipelines through a 3rd-party plugin system, allowing the user to have a single entry point for all of their analyses.
Qiita provides database and compute resources to the global community, alleviating the technical burdens that are typically limiting for researchers studying microbial ecology (e.g. familiarity with the command line or access to compute power).
Qiita’s platform allows for quick reanalysis of the datasets that have been deposited using the latest analytical technologies. This means that Qiita’s internal datasets are living data that is periodically re-annotated according to current best practices.
### Input format
FASTQ, SAM
### Tool operation
Analysis, Data handling
### Output data
SAM, Tables, visualizations
### Credits, support
  - code: [github.com/qiita-spots/qiita](https://github.com/qiita-spots/qiita)
  - doi: [10.1038/s41592-018-0141-9](https://doi.org/10.1038/s41592-018-0141-9)


---

## GTDBTk
### Homepage
[https://github.com/Ecogenomics/GTDBTk](https://github.com/Ecogenomics/GTDBTk)
[https://ecogenomics.github.io/GTDBTk/](https://ecogenomics.github.io/GTDBTk/)
### Maturity
Mature and under constant development
### Topic
Bacterial and Archaeal Genome Taxonomic classification, Phylogenetic Analysis
### License
[GPL-3.0](https://opensource.org/license/gpl-3-0/)
### Description
GTDBTk (Genome Taxonomy Database Toolkit) is a software toolkit designed to classify bacterial and archaeal genomes based on the Genome Taxonomy Database (GTDB). It is designed to work with recent advances that allow hundreds or thousands of metagenome-assembled genomes (MAGs) to be obtained directly from environmental samples. It can also be applied to isolate and single-cell genomes. GTDBTk aims to standardize microbial taxonomy, facilitating consistent and reproducible microbial diversity studies.
### Input
- Genomic sequences (fasta, both complete and draft genomes)
### Tool Operation
- Taxonomic classification based on the Genome Taxonomy Database
- Phylogenetic tree construction
### Output Data
- tsv, fasta, tree
### Credits, Support
- Chaumeil PA, et al. 2022. GTDB-Tk v2: memory friendly classification with the Genome Taxonomy Database. Bioinformatics, btac672.
- doi: [10.1093/bioinformatics/btac672](https://doi.org/10.1093/bioinformatics/btac672)


---

## PlasFlow
### Homepage
[https://github.com/smaegol/PlasFlow](https://github.com/smaegol/PlasFlow)
### Maturity
Mature
### Topic
Plasmid Prediction in Metagenomics contigs
### License
[GPL-3.0](https://opensource.org/license/gpl-3-0/)
### Description
PlasFlow is a set of scripts used for prediction of plasmid sequences in metagenomic contigs. It relies on the neural network models trained on full genome and plasmid sequences and is able to differentiate between plasmids and chromosomes with accuracy reaching 96%. It outperforms other available solutions for plasmids recovery from metagenomes and incorporates the thresholding which allows for exclusion of incertain predictions. PlasFlow has been published in Nucleic Acids Research (https://doi.org/10.1093/nar/gkx1321).
### Input
- Nucleotide sequences (fasta format)
### Tool Operation
- Sequence Classification
### Output Data
- tsv (Classification results indicating plasmid or chromosomal origin)
### Credits, Support
- Created by S. Maegol
- Krawczyk PS, Lipinski L, Dziembowski A. Nucleic Acids Res. 2018 Apr 6;46(6):e35.
- doi: [10.1093/nar/gkx1321](https://doi.org/10.1093/nar/gkx1321)
