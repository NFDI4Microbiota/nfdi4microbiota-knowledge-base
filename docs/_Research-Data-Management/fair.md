---
title: FAIR data principles
category: Research-Data-Management
layout: default
docs_css: markdown
authors:
   - jvandendorpe

---

## Why the FAIR data principles matter in microbiology

Microbes exhibit remarkable versatility, thriving in environments as varied as the human body, plants and soils, and extreme habitats such as deep-sea vents. Microbes' interactions within these environments have significant implications for fields such as medicine, biotechnology and agriculture, to name just a few.

As microbiology research becomes increasingly data-driven and leverages technologies such as advanced multi-omics, it holds great promise but also presents certain challenges. In order to fully leverage extensive microbial data, these data must be well-organized and carefully annotated. This involves adhering to best practices for documenting data with metadata, conducting data analysis, and ensuring that data are shared in ways that support reusability, reproducibility of results and research transparency. The FAIR (Findable, Accessible, Interoperable and Reusable) data principles offer guidelines for effective data management, with the aim of making data easier to discover and map within the scientific community.

## What are the FAIR data principles?
---
The FAIR data principles are a concise and measurable set of principles that may act as a guideline for those wishing to enhance the reusability of their data holdings. FAIR stands for Findable, Accessible, Interoperable and Reusable {% cite wilkinson_2016  %}. The FAIR data principles aims at {% cite wilkinson_2016 lowenberg_2021 %}:

* Improving the infrastructure supporting the reuse of scholarly data.
* Enhancing the ability of machines to automatically find and use data.
* Supporting the reuse of data by individuals, which “is essential to the advancement of research and clinical practice”.

![FAIR Data Principles]({{ '/assets/img/fair_principles_cropped.png' | relative_url }})

The principles {% cite wilkinson_2016 go_fair_2022 %} are reproduced below:

### Findable

* (Meta)data are assigned a globally unique and persistent identifier.
* Data are described with rich metadata.
* Metadata clearly and explicitly include the identifier of the data it describes.
* (Meta)data are registered or indexed in a searchable resource (e.g. data repository).

### Accessible

* (Meta)data are retrievable by their identifier using a standardized communications protocol (e.g. http(s)).
* The protocol is open, free, and universally implementable.
* The protocol allows for an authentication and authorization procedure, where necessary.
* Metadata are accessible, even when the data are no longer available.

### Interoperable 

Data interoperability is the ability of a dataset to work with other datasets or systems without special effort on the part of the user {% cite godan_action_2019_3588148 %}.

* (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation (e.g. controlled vocabularies/ontologies/thesauri, a good data model).
* (Meta)data use vocabularies that follow the FAIR principles (e.g. using FAIR Data Point).
* (Meta)data include qualified references to other (meta)data (e.g. specifying if one dataset builds on another one, properly citing all datasets).

### Reusable

* Meta(data) are richly described with a plurality of accurate and relevant attributes (i.e. metadata that richly describes the context under which the data was generated such as the experimental protocols, the species used).
* (Meta)data are released with a clear and accessible data usage license.
* (Meta)data are associated with detailed provenance.


## Challenges in adopting the FAIR data principles in microbiology research
---
Despite their benefits, some challenges remain in adopting the FAIR data principles in microbiology. These include varying levels of researcher awareness of data standards and data deposition practices, especially when it comes to complex and large microbial datasets. Additionally, inconsistent reporting practices across the field can pose challenges. Data-sharing requirements (e.g. from publishers and funding agencies) are not always comprehensive and sometimes focus on specific data types, which can lead to discrepancies in what is shared. The diversity of metadata requirements, including those relating to environmental and experimental conditions, can further complicate standardization efforts. Finally, technical challenges related to data quality control and version management, combined with limited incentives for adhering to the FAIR data principles, may hinder their adoption {% cite huttenhower_2023 %}.

## 12 actionable ways to make your data FAIR
---
 1. Write a Data Management Plan (DMP) using our [DMP template](https://doi.org/10.5281/zenodo.13628589).
 2. Learn how to document your data collection with eLabFTW by watching our [demo](https://doi.org/10.5446/68306) (and if you get excited - talk to our [Helpdesk](https://www.nfdi4microbiota.de/support/helpdesk/) regarding how to set it up)
 3. Purify viral particles from bacterial liquid culture using our protocol in our [protocols.io workspace](https://protocols.io/workspaces/nfdi4microbiota) or contribute more protocol to it to make it citable.
 4. Refer to cultivation media using [MediaDive](https://mediadive.dsmz.de/) in you next publication.
 5. Document your data early using microbiology's metadata standards and controlled vocabularies, which we compiled [here](https://github.com/NFDI4Microbiota/MetadataStandards).
 6. Analyse your data with end-to-end workflows using our workflow execution platform CloWM ([Cloud-based Workflow Manager](https://clowm.bi.denbi.de/login)).
 7. Save your raw data in original format and use acceptable file formats.
    - FASTA (\*.fasta, .fas, .fa, .fna, .ffn, .faa, .mpfa, \*.frn) for nucleotide and protein sequences.
    - FASTQ (\*.fq, \*.fastq) for raw biological sequence and its corresponding quality score.
    - General Feature Format (GFF) (\*.gff, \*.gff3) for genes and other features of DNA, RNA and protein sequences.
    - Sequence Alignment Map (SAM) (\*.sam) and Binary Alignement Map (BAM)  (\*. bam) for biological sequences aligned to a reference sequence.
    - Variant Call Format (VCF) (\*.vcf) for gene sequence variations.
 8. Organise your data following our [lesson plan on data organisation](https://doi.org/10.4126/FRL01-006484175).
 9. Store your data and metadata files in our data orchestration engine [ARUNA](https://aruna-engine.org/).
10. Submit final data files to a repository following the recommendations on the [Data repositories page](https://knowledgebase.nfdi4microbiota.de/RDM-Share/data-repositories.html) of our Knowledge Base.
11. Refer to your microbial strains using identifiers which you can find in our service [StrainInfo](https://straininfo.dsmz.de/about).
12. Search for data in our central hub for virus resources [VirJenDB](https://virjendb.org/).

## Further resources
---
* Introducing the FAIR Principles for research software: [Barker *et al.* 2022](https://doi.org/10.1038/s41597-022-01710-x)

### Learning resources
* Course on FAIR in (biological) practice: [The Carpentries Incubator](https://carpentries-incubator.github.io/fair-bio-practice/)
* How to be FAIR with your data. A teaching and training handbook for higher education institutions: [Engelhardt *et al.* 2022](https://doi.org/10.5281/zenodo.6674301)
* Unit on the benefits and challenges associated with sharing research data openly: [The University of Edinburgh](https://mantra.ed.ac.uk/fairsharingandaccess/)

### How to make data FAIR?
* Guidelines to FAIRify data management and make data reusable: [PARTHENOS](https://doi.org/10.5281/zenodo.2668479)
* Preparing data for sharing: [Knight 2015](https://www.slideshare.net/lshtm/preparing-data-for-sharing-the-fair-principles)
* Recipes that help you to make and keep data FAIR: [FAIR Cookbook](https://faircookbook.elixir-europe.org/content/home.html)
* Top 10 FAIR Data & Software Things: [Martinez *et al.* 2019](https://doi.org/10.5281/zenodo.3409968)

### How to assess the FAIRness of your datasets?
* FAIR data maturity model indicators: [Bahim *et al.* 2020](https://doi.org/10.5334/dsj-2020-041), Table 1
* FAIR evaluator service: [Fraunhofer FIT](https://gitlab.fit.fraunhofer.de/abu.ibne.bayazid/fairevaluator)
* How FAIR are your data? [Jones and Grootveld 2017](https://doi.org/10.5281/zenodo.5111307)
* Self-Assessment Tool to Improve the FAIRness of Your Dataset ([SATIFYD](https://satifyd.dans.knaw.nl/)) 

