---
title: Available NFDI4Microbiota Tools
category: Software Development
layout: default
docs_css: markdown
---

The following data is compiled from a questionnaire of Q4 2022 and is targeted at groups funded under NFDI4Microbiota, that have a particular application/pipeline/database (henceforth referred to just as "tool") already implemented or in inception that should be integrated and endorsed by the NFDI4Microbiota umbrella.

The goal is to gather this information centrally in NFDI4Microbiota to assess the span of tools and derive consortium-wide guidelines for the tightest integration possible.

## Disclaimer: Changes in the tool display
---
We recently created a [NFDI4Microbiota domain](https://bio.tools/t?domain=nfdi4microbiota) on [the life sciences software registry bio.tools](https://bio.tools) and we will soon be displaying all the tools that NFDI4Microbiota created as well as the ones that NFDI4Microbiota consortium members endorse and highly recommend.

Thank you for your patience while we sort out editing rights and collection labels.  
In the meantime, browse our tools below and find more [recommendations for resources on reproducible data analysis]({% link _Reproducible-Data-Analysis/resources.md %}).

## Applications
---

### checkM2 (EMBL) 

Assessing the quality of metagenome-derived genome bins using machine learning

operating system: Linux

License: [GPL 3.0](https://opensource.org/license/gpl-3-0/)

Link: [https://github.com/chklovski/CheckM2](https://github.com/chklovski/CheckM2)

### The Cloud-based Workflow Manager - CloWM (BIBI)
The Cloud-based Workflow Manager (CloWM /klaʊm/) offers the seamless integration of (1) curated, scientific workflows written in the Nextflow DSL, (2) robust data storage, (3) a highly scalable compute layer for data-intensive analysis tasks and a (4) user-friendly interface. The CloWM platform is completely open-source and can be used free-of-charge.
The CloWM platform already contains several curated, best-practice workflows that cover a broad range of research fields/tasks, such as metagenomics (WGS and 16S), human-variation-analysis, infectious diseases (SARS-CoV2, Mpox, Influenza A+B), meta-barcoding, genome assembly, transcriptomics, basecalling, phylogenomics, …
Some of these workflows are exclusively available on CloWM.

operating system: Platform independent

License: [Apache 2](https://www.apache.org/licenses/LICENSE-2.0.txt)

Link: [https://clowm.bi.denbi.de](https://clowm.bi.denbi.de)

### Eggnog mapper (EMBL) 

Fast genome-wide functional annotation through orthology assignment

operating system: Linux, MacOS, Windows

License: [AGPL 3.0](https://opensource.org/license/agpl-v3/) 

Link: [https://github.com/eggnogdb/eggnog-mapper](https://github.com/eggnogdb/eggnog-mapper)

### GUNC (EMBL) 

Python package for detection of chimerism and contamination in prokaryotic genomes.

operating system: Linux, MacOS, Windows

License: [GPL 3.0](https://opensource.org/license/gpl-3-0/) 

Link: [https://github.com/grp-bork/gunc](https://github.com/grp-bork/gunc)

### mOTUs (EMBL) 

A computational tool that estimates relative taxonomic abundance of known and currently unknown microbial community members using metagenomic shotgun sequencing data.

operating system: Linux

License: [GPL 3.0](https://opensource.org/license/gpl-3-0/)  

Link: [https://github.com/motu-tool/mOTUs](https://github.com/motu-tool/mOTUs)

### Proteinortho (UMR) 

Proteinortho is a tool to detect orthologous genes within different species.

operating system: Linux, MacOS

License: [LGPL 3.0](https://opensource.org/license/lgpl-3-0/)

Link: [https://gitlab.com/paulklemm_PHD/proteinortho](https://gitlab.com/paulklemm_PHD/proteinortho)

## Benchmarks
---
### AMBER (Helmholtz-HZI) 

Assessment of Metagenome BinnERs

operating system: Linux

License: [GPL 3.0](https://opensource.org/license/gpl-3-0/)

Link: [https://github.com/CAMI-challenge/AMBER](https://github.com/CAMI-challenge/AMBER)

## Databases
---
### BacDive (DSMZ) 

"BacDive is the worldwide largest database for standardized bacterial information.

operating system: Linux

License: [CC BY](http://creativecommons.org/licenses/by/4.0/)

Link: [https://bacdive.dsmz.de/](https://bacdive.dsmz.de/)

### EggNOG Database (EMBL) 

"A database of orthology relationships, functional annotation,

operating system: Linux

License: unknown 

Link: [http://eggnog5.embl.de/#/app/home](http://eggnog5.embl.de/#/app/home)

### MediaDive (DSMZ) 

Standardized cultivation media database

operating system: Linux, MacOS, Windows

License: [CC BY](http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1) 

Link: [https://mediadive.dsmz.de](https://mediadive.dsmz.de)

### HumanMetagenomeDB (UFZ)

"Explore and download curated human metagenome metadata. HumanMetagenomeDB (version 1.0) contains metadata of 69,822 metagenome samples.

operating system: Platform independent

License: [CC BY](http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1)

Link: [https://web.app.ufz.de/hmgdb/](https://web.app.ufz.de/hmgdb/)

### MarineMetagenomeDB (UFZ)

"Explore and download curated marine metagenome metadata. MarineMetagenomeDB (Release 1.0) contains standardized metadata of 11,449 marine metagenome samples.

operating system: Platform independent

License: [GPL 3.0](https://opensource.org/license/gpl-3-0/)

Link: [https://web.app.ufz.de/marmdb/](https://web.app.ufz.de/marmdb/)

### AnimalAssociatedMetagenomeDB (UFZ)

"Explore and download curated animal-associated metagnome metadata. The AnimalAssociatedMetagenomeDB (version 1.0) contains 10,885 metagenome samples.

operating system: Platform independent

License: [GPL 3.0](https://opensource.org/license/gpl-3-0/)

Link: [https://webapp.ufz.de/aamdb/](https://webapp.ufz.de/aamdb/)

### TerrestrialMetagenomeDB (UFZ)

"Explore and download curated terrestrial metagenome metadata. TerrestrialMetagenomeDB (release 1.0) includes 15,022 terrestrial metagenome samples.

operating system: Platform independent

License: [CC BY](http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1)

Link: [https://webapp.ufz.de/tmdb](https://webapp.ufz.de/tmdb)

## Pipelines
---
### BioAutoML (UFZ) 

BioAutoML: Automated Feature Engineering and Metalearning for Classification of Biological Sequences

operating system: Linux, MacOS

License: [BSD3](https://opensource.org/license/bsd-3-clause/)

Link: [https://github.com/Bonidia/BioAutoML](https://github.com/Bonidia/BioAutoML)

### CAMISIM (Helmholtz-HZI) 

Model abundance distributions of microbial communities and simulate metagenome datasets

operating system: Linux

License: [Apache 2](https://opensource.org/license/apache-2-0/)

Link: [https://github.com/CAMI-challenge/CAMISIM](https://github.com/CAMI-challenge/CAMISIM)

### MetaProteomeAnalyzer (ISAS) 

Workflow for metaproteomics anaylysis of microbiomes

operating system: Linux, Windows

License: [Apache 2](https://opensource.org/license/apache-2-0/)

Link: [https://github.com/compomics/meta-proteome-analyzer](https://github.com/compomics/meta-proteome-analyzer)

### Multi-Domain Genome Recovery (MuDoGeR) (UFZ)

The Multi-Domain Genome Recovery v1.0.1 (MuDoGeR v1.0.1) framework is a tool developed to help recover Metagenome-Assembled Genomes (MAGs) - from prokaryotes and eukaryotes - and Uncultivated Viral Genomes (UViGs) from whole-genome sequence (WGS) samples simultaneously.

The MuDoGeR v1.0.1 framework act as a wrapper of several tools. Available as a singularity container of via conda installation.

It was designed to be an easy-to-use tool that outputs ready-to-use comprehensive files.

operating system: Linux

License: [GPL 3.0](https://opensource.org/license/gpl-3-0/)

Link: [https://github.com/mdsufz/MuDoGeR](https://github.com/mdsufz/MuDoGeR)

### OrtSuite (UFZ) 

Flexible pipeline for annotation of ecosystem processes and prediction of putative microbial interactions

operating system: Linux

License: [CC BY](http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1) 

Link: [https://github.com/mdsufz/OrtSuite](https://github.com/mdsufz/OrtSuite)

### PredicTF (UFZ) 

Tool to predict bacterial transcription factors in complex microbial communities

operating system: Linux

License: [CC BY](http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1)  

Link: [https://github.com/mdsufz/PredicTF](https://github.com/mdsufz/PredicTF)

### Protologger (UKAachen) 

Protologger is a bioinformatic tool that automatically generates all the necessary readouts for writing a detailed protologue.

By producing multiple taxonomic outputs, functional features and ecological analysis using the 16S rRNA gene and genome sequences from a single species, the time needed to gather the information for describing novel taxa is substantially reduced.

operating system: Linux

License: [CC BY](http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1) 

Link: [http://protologger.de/](http://protologger.de/)

### Qiita (JLU) 

Best practice microbiome analysis suite

operating system: Linux

License: [BSD3](https://opensource.org/license/bsd-3-clause/)

Link: [https://qiita.ucsd.edu/](https://qiita.ucsd.edu/)

## Webservices
---
### iPath (EMBL) 

Interactive Pathways Explorer (iPath) is a web-based tool for the visualization, analysis and customization of various pathway maps.

operating system: Linux

License: [GPL](https://opensource.org/license/gpl-3-0/) 

Link: [https://pathways.embl.de/](https://pathways.embl.de/)

### iTOL (EMBL) 

Interactive Tree Of Life is an online tool for the display, annotation and management of phylogenetic and other trees.

operating system: Linux

License: paid 

Link: [https://itol.embl.de/](https://itol.embl.de/)

### Help Desk (ZBMED) 

Utility flask app for contact notification on the NFDI4Microbiota homepage

operating system: Linux

License: NA 

Link: [https://nfdi4microbiota.de/contact-form.html](https://nfdi4microbiota.de/contact-form.html)
