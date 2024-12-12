---
title: Research Data Management (RDM)
category: Research-Data-Management
layout: default
docs_css: markdown
---

## Definition of Research Data Management (RDM)
Research Data Management (RDM) is the care and maintenance required to (1) obtain high-quality data, whether produced or reused, (2) make the data available and usable in the long term, whether produced or reused and (3) make research results reproducible beyond the research project {% cite biernacka:2020 bres_2022 RfII_RD voigt_2022 pauls_2023 bres_2023 %}. It complements research from planning to data reuse and deletion. 

## RDM in microbiology
---
RDM is crucial in microbiology to ensure the integrity and accessibility of data throughout the research process. One essential aspect of RDM is establishing clear protocols for data collection, storage, and analysis. For instance, researchers studying bacterial evolution should document their sampling procedures meticulously, including information on sampling sites, environmental conditions, and sampling techniques, to ensure reproducibility. Additionally, adopting standardized data formats, such as FASTA or GenBank Flat File Format, facilitates data sharing and interoperability across different studies, enhancing collaboration and knowledge exchange within the microbiology research community. Proper metadata annotation is also paramount, as it provides essential context for interpreting the data. Researchers in microbiology should develop comprehensive data management plans (DMPs) outlining how data will be collected, processed, and shared throughout the research data lifecycle. DMPs serve as roadmaps for RDM, ensuring that data handling procedures adhere to ethical, legal, and funder requirements. Moreover, adopting electronic lab notebooks (ELNs) can streamline data organization and collaboration by digitizing research notes, protocols, and experimental results. ELNs enable real-time data capture, version control, and collaboration among team members, facilitating seamless integration with RDM workflows. For example, researchers investigating microbial communities could use ELNs to record observations, generate graphs, and annotate findings collaboratively, ensuring transparency and reproducibility. Researchers working on sensitive information, such as patient data in clinical microbiology studies must take care of data protection and security measures to safeguard this information. Embracing open science practices by depositing data in public repositories like NCBI's GenBank or the European Nucleotide Archive fosters transparency and long-term preservation of microbiological data, ensuring its availability for future research endeavors. Therefore, microbiology researchers should integrate robust RDM practices into their workflows from the outset to maximize the impact and reproducibility of their findings while contributing to the advancement of the field. 

Addtionnaly, researchers should address the management of software tools, including small analysis scripts and machine learning models, within their RDM framework. These tools are integral for processing, analyzing, and interpreting complex microbiological data sets. Therefore, documenting the software environment, version numbers, and dependencies used in data analysis workflows is crucial for ensuring reproducibility and transparency. For instance, a study investigating the taxonomic composition of gut microbiota may rely on custom Python scripts for data preprocessing and statistical analysis. By documenting these scripts along with their parameters and input data, researchers enable others to replicate their analyses and validate their findings. Moreover, utilizing version control systems like Git and hosting repositories on platforms like GitHub or GitLab ensures the traceability and accessibility of software artifacts. By incorporating software management practices into their RDM strategies, microbiology researchers can enhance the reproducibility, transparency, and rigor of their computational analyses, thereby advancing scientific knowledge in the field.

With the growing application of machine learning in microbiology, such as predicting antibiotic resistance or classifying microbial species, it becomes imperative to manage the underlying models transparently. Researchers should document model architectures, training data, and performance metrics to facilitate model validation and comparison across studies. 

## Relevance of RDM
---
Research data are valuable {% cite pauls_2023 %} and therefore need to be managed systematically and responsibly {% cite biernacka:202 0%}. Incorporating robust RDM practices from the outset of a research project helps make research data accessible, reusable, and verifiable throughout the research process and in the long term, regardless of the data producer {% cite pauls_2023 %}. Such practices also ensure integrity and help maximize the impact, reproducibility, transparency, and rigor of researchers' analyses and findings. Finally, robust RDM practices enhance collaboration and knowledge sharing and help preserve the scientific record, and advance scientific knowledge.

## Advantages and drawbacks of RDM
---
As noted above, there are many benefits to incorporating robust RDM practices from the outset of a research project. For researchers, good RDM enhances visibility, reputation (by ensuring the quality of research), data ownership (i.e. "the possession of and responsibility for information" [NCATS Toolkit](https://toolkit.ncats.nih.gov/)) {% cite bres_2022 jacob_2022 %} and helps them to meet formal requirements from third parties (e.g. research funders, institutions and publishers). For the project, good RDM brings clarity and findability, supports coordination, data security and good storage practices, helps to keep track of the project and deal with legal aspects, and increases eligibility for funding {% cite assmann_2022 bres_2022 bres_2023 %}. For the research group, good RDM enables knowledge management, transfer and preservation, while improving teamwork and saving time, money and resources {% cite assmann_2022 bobrov_2021 bres_2022 %}. For third parties, good RDM practices increase transparency, make data FAIR (i.e. findable, accessible, interoperable and reusable (no need for unnecessary duplication)) and increase collaboration {% cite assmann_2022 bobrov_2021 bres_2022 jacob_2022 voigt_2022 assmann:2022-08 %}. Last but not least, good RDM practices help to address societal challenges by ensuring reproducibility, availability and verifiability, preventing data loss and preserving the scientific record, ensuring good research practice (GRP) and supporting open science (i.e. open transfer of research knowledge, open access to research data) {% cite assmann_2022 bobrov_2021 engelhardt_2022 jacob_2022 lindstädt_2019 voigt_2022 bres_2023 %}.

There are also consequences of poor RDM practices, such as retractions of papers. For example, Dan Ariely, a professor of psychology and behavioural economics at Duke University, had one of his papers on dishonesty retracted. He could not remember in what year and in what form he had received the data from the company he was working with. Nor did he check the data for irregularities. The company could not find the data either {% cite bartlett:2021 %}. 

## Problems in RDM
---
Current issues and challenges in RDM can be classified by stakeholder, as individual researchers, research funders, research organisations, librarians and reviewers have different needs {% cite science_europe:2024 %}. 

For individual researchers, the different organisational requirements can be confusing, especially if they work with different organisations, change their home institution or collaborate with researchers from other organisations where different rules apply  {% cite science_europe:2024 sheikh:2023 %}. The lack of connectivity between tools used at different stages of the research data lifecycle can also be a barrier to the proper management of their data.

For research funders, the development of technological infrastructure can be difficult {% cite sheikh:2023 %}. 

For research organisations, the institutional commitment and academic engagement required can be overwhelming. The lack of policy, funding and storage also hinders progress in RDM {% cite sheikh:2023 %}.

For librarians and RDM staff, raising awareness among researchers of the benefits of data sharing remains a challenge. On another note, librarians need (discipline-specific) skills and competencies to provide RDM-based services {% cite sheikh:2023 %}.


## Research data life cycle
---
The research data life cycle is a model that illustrates the steps of RDM and describes how data should ideally flow through a research project to ensure successful data curation and preservation {% cite NTU_LibGuides_RD_life_cycle princeton:2024 %}. It is intended to help researchers understand the scope and importance of data management {% cite sheikh:2023 %}. The research data life cycle can be illustrated as follow {% cite RDMkit:2021 %}: 

![Research data life cycle]({{ '/assets/img/research_data_life_cycle_elixir.png' | relative_url }})

NFDI4Microbiota offers dedicated services and tools along the research data life cycle: 
* **Plan:** a [DMP template](https://doi.org/10.5281/zenodo.13628589).
* **Collect:**
    * Protocols on [protocols.io](https://www.protocols.io/researchers/sarah-schulz). 
    * 2- to 3-hour workshops on ELNs (see example slides [here](https://doi.org/10.5281/zenodo.11578583)).
    * Training with eLabFTW (see example demo [here](https://doi.org/10.5446/68306)).
    * Annual seminar on ELNs.
* **Process:** metadata (standards):
    * On this [Knowledge Base](https://nfdi4microbiota.github.io/nfdi4microbiota-knowledge-base/Research-Data-Management/03-md.html)
    * On [GitHub](https://github.com/NFDI4Microbiota/MetadataStandards)
* **Analyse:** the Cloud-based Workflow Manager ([CloWM](https://clowm.bi.denbi.de/login?next=/dashboard)) (15 Nextflow workflows in production, more than 20 available soon).
* **Preserve:** the [ARUNA](https://aruna-storage.org/) data orchestration engine, an open-source data management platform that allows scientists and industry partners to store, annotate and share their data according to the FAIR data principles.
* **Reuse:** 
    * [StrainInfo](https://straininfo.dsmz.de/), a service developed to provide a resolution of microbial strain identifiers by storing culture collection numbers, their relations, and culture-associated data.
    * [VirJenDB](https://www.virjendb.org/), a central hub connecting virus researchers to publicly available virus resources, metadata and sequences.

If the steps of the research data life cycle are not completed, data and results may be lost, or they may be preserved but without the necessary metadata to reuse them or make the research process reproducible (see Lost Data Map below). It is important to note that the research data life cycle is a model whose steps do not necessarily have to be followed in strict order, but they should all be completed.

![Lost Data Map]({{ '/assets/img/lost_data_map_rfii_Mau_CC-BY.png' | relative_url }})

## Current developments and initiatives
---
Internationally, the increasingly frequent requirement to produce a DMP has stimulated interest in RDM {% cite yamaji:2024 %} and encouraged libraries to take an active role in RDM through advocacy, policy development, and advisory and consultancy services {% cite cox:2017 %}. Some institutions, such as KU Leuven, have also developed a dashboard to review datasets to meet funder requirements {% cite yamaji:2024 %}.

In Germany, the National Research Data Infrastructure (NFDI) funds nearly 30 discipline-specific consortia to help researchers make their data reusable in the long term.

## Further resources
---
* General resources:
    * Brief Guide - Research Data Management: [Training Expert Group 2020](https://doi.org/10.5281/zenodo.4000989)
    * The Research Data Management toolkit for Life Sciences [RDMkit](https://rdmkit.elixir-europe.org) by [ELIXIR](https://elixir-europe.org)
* Essential scientific and technical information about software tools, databases and services for bioinformatics and the life sciences: [bio.tools](https://bio.tools/)
* Research data management platforms:
    * [Coscine](https://coscine.de/) by [RWTH Aachen](https://www.rwth-aachen.de)
    * [BEXIS2](https://demo.bexis2.uni-jena.de) by [NFDI4Biodiversity](https://www.nfdi4biodiversity.org/en/) at [FSU Jena](https://www.uni-jena.de)
    * [GfBio](https://www.gfbio.org) consortium services

