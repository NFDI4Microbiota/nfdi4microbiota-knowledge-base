---
title: Research Data Management (RDM)
category: Research-Data-Management
layout: default
docs_css: markdown
---

## Definition of Research Data Management (RDM)
Research Data Management (RDM) is the care and maintenance required to (1) obtain high-quality data (whether produced or reused), (2) make the data available and usable in the long term (whether produced or reused) and (3) make research results reproducible beyond the research project {% cite biernacka:2020 bres_2022 RfII_RD voigt_2022 pauls_2023 bres_2023 %}. It complements research from planning to data reuse and deletion. 

## Relevance of RDM
---
Research data are valuable {% cite pauls_2023 %} and therefore need to be managed systematically and responsibly {% cite biernacka:2020 %}. Incorporating robust RDM practices from the outset of a research project helps make research data accessible, reusable and verifiable throughout the research process and in the long term, regardless of the data producer {% cite pauls_2023 %}. Such practices also ensure integrity and help maximise the impact, reproducibility, transparency and rigour of researchers' analyses and findings. Finally, robust RDM practices enhance collaboration and knowledge sharing and help preserve the scientific record and advance scientific knowledge.

## Benefits and Drawbacks of RDM
---
As noted above, there are many benefits to incorporating robust RDM practices from the outset of a research project. For researchers, good RDM enhances visibility, reputation (by ensuring the quality of research), data ownership (i.e. "the possession of and responsibility for information" [NCATS Toolkit](https://toolkit.ncats.nih.gov/)) {% cite bres_2022 jacob_2022 %} and helps them to meet formal requirements from third parties (e.g. research funders, institutions and publishers). For the project, good RDM brings clarity and findability, supports coordination, data security and good storage practices, helps to keep track of the project and deal with legal aspects, and increases eligibility for funding {% cite assmann_2022 bres_2022 bres_2023 %}. For the research group, good RDM enables knowledge management, transfer and preservation, while improving teamwork and saving time, money and resources {% cite assmann_2022 bobrov_2021 bres_2022 %}. For third parties, good RDM practices increase transparency, make data FAIR (i.e. findable, accessible, interoperable and reusable (no need for unnecessary duplication)) and increase collaboration {% cite assmann_2022 bobrov_2021 bres_2022 jacob_2022 voigt_2022 assmann:2022-08 %}. Last but not least, good RDM practices help to address societal challenges by ensuring reproducibility, availability and verifiability, preventing data loss and preserving the scientific record, ensuring good research practice (GRP) and supporting open science (i.e. open transfer of research knowledge, open access to research data) {% cite assmann_2022 bobrov_2021 engelhardt_2022 jacob_2022 lindstädt_2019 voigt_2022 bres_2023 %}.

There are also consequences of poor RDM practices, such as retractions of papers. For example, Dan Ariely, a professor of psychology and behavioural economics at Duke University, had one of his papers on dishonesty retracted. He could not remember in what year and in what form he had received the data from the company he was working with. Nor did he check the data for irregularities. The company could not find the data either {% cite bartlett:2021 %}. 
Another consequence might be that a paper, or in this case a book, has to be corrected and submitted again for review: Eliran Bar-El, a sociologist at the University of York had to correct his book “How Slavoj Became Žižek - The Digital Making of a Public Intellectual” because of “[several insufficient, missing, or erroneous citations of source material upon which the author builds his argument](https://web.archive.org/web/20231109095858/https:/press.uchicago.edu/books/Book-Pages/9780226823508.html)” {% cite joelving:2023 %}. 

## Research Data Life Cycle
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
    * On this [Knowledge Base]({% link _Research-Data-Management/md.md %}).
    * On [GitHub](https://github.com/NFDI4Microbiota/MetadataStandards).
* **Analyse:** the Cloud-based Workflow Manager ([CloWM](https://clowm.bi.denbi.de/login?next=/dashboard)).
* **Preserve:** the [ARUNA](https://aruna-storage.org/) data orchestration engine, an open-source data management platform that allows scientists and industry partners to store, annotate and share their data according to the FAIR data principles.
* **Reuse:** 
    * [StrainInfo](https://straininfo.dsmz.de/), a service developed to provide a resolution of microbial strain identifiers by storing culture collection numbers, their relations, and culture-associated data.
    * [VirJenDB](https://www.virjendb.org/), a central hub connecting virus researchers to publicly available virus resources, metadata and sequences.

If the steps of the research data life cycle are not completed, data and results may be lost, or they may be preserved but without the necessary metadata to reuse them or make the research process reproducible (see Lost Data Map {% cite mau:2019 %} below).

![Lost Data Map]({{ '/assets/img/lost_data_map_rfii_Mau_CC-BY.png' | relative_url }}){:width="70%"}

## Measures of Good RDM
---

Below are measures of good RDM, grouped according to the steps in the research data life cycle. These measures are largely based on {% cite biernacka:2020 pauls_2023 steen:2022 %}, and some are explained in more detail on other pages of this Knowledge Base.

### Plan
Planning a research project includes creating a research design, planning for data management (i.e. creating an initial DMP that outlines how data will be collected, processed and shared), exploring existing data sources and planning for consent to share data.

### Collect
Even before the collection of research data, adopting an Electronic Lab Notebook (ELN) may be a good measure to take. By digitising research notes, protocols and experimental results, an ELN can streamline data organisation and collaboration between team members. In addition, ELNs provide version control and real-time data capture, enabling seamless integration with RDM workflows. For example, researchers studying microbial communities could use an ELN to record observations, generate graphs and annotate results, all collaboratively, ensuring transparency and reproducibility.
Collecting primary research data requires the creation of clear protocols for data collection, whereas collecting secondary data, i.e. the acquisition of existing third-party data, may require obtaining permission to reuse the data. 
Collecting research data also involves capturing data with metadata. For example, researchers studying bacterial evolution should carefully document their sampling procedures, including information on sampling sites, environmental conditions and sampling techniques to ensure reproducibility. 
Finally, collecting research data includes data validation (i.e. data cleaning and quality control), the use of acceptable file formats, and data check.

### Process and Analyse
Processing research data begins with the proper documentation/description of the data. In terms of documenting scripts, code and software, software tools (from small analysis scripts to machine learning models) are integral to the processing, analysis and interpretation of complex microbiology data sets. Therefore, documenting the software environment, version numbers and dependencies used in data analysis workflows is critical to ensure reproducibility and transparency. For example, a study investigating the taxonomic composition of the gut microbiota may rely on custom Python scripts for data pre-processing and statistical analysis. By documenting these scripts, along with the parameters and input data used, researchers can enable others to replicate their analyses and validate their findings. In addition, the use of version control systems (VCS) such as Git, and the hosting of Git repositories on platforms such as GitHub or GitLab, ensures the traceability and accessibility of software artefacts. By incorporating such software management practices into their RDM strategy, microbiology researchers can improve the reproducibility, transparency and rigour of their computational analyses, thereby advancing scientific knowledge in the field. When it comes to documenting models, with the increasing use of machine learning in microbiology (e.g. to predict antibiotic resistance or classify microbial species), it is imperative that the underlying models are managed transparently. Researchers should document model architectures, training data and performance metrics to facilitate model validation and comparison across studies.
Before research data can be analysed, it needs to be digitised, transcribed, translated and possibly anonymised. Clear protocols for data analysis must then be established. Finally, the data can be interpreted and research findings produced.

### Preserve
Preserving research data requires establishing clear protocols for data storage and migrating data to appropriate media and formats. Adopting standardised formats, such as FASTA or the GenBank flat file format, facilitates interoperability and data sharing between studies, thereby enhancing collaboration and knowledge sharing with the microbiology research community. Data preservation also requires the creation of preservation documentation prior to the actual long-term preservation of data. 

### Share
Data sharing requires access control (i.e. selecting appropriate access to data) and data security. Researchers working with sensitive data, such as sensitive personal data (e.g. in clinical microbiology studies) or sensitive environmental data, need to consider protection and security measures to safeguard this information. Data sharing also requires that copyright be established before the data is actually shared and published. 
Microbiology researchers can embrace open-science practices by depositing their research data in public repositories such as NCBI's GenBank or EMBL-EBI's European Nucleotide Archive (ENA), thereby promoting transparency and long-term preservation of microbial data and ensuring its availability for future research.

### Reuse
Reusing data includes reviewing results and previous research, conducting follow-up research, and using data for teaching and learning.

## Issues and Challenges in RDM
---
Current issues and challenges in RDM can be classified by stakeholder, as individual researchers, research funders, research organisations, librarians and reviewers have different needs {% cite science_europe:2024 %}. 

For individual researchers, the different organisational requirements can be confusing, especially if they work with different organisations, change their home institution or collaborate with researchers from other organisations where different rules apply  {% cite science_europe:2024 sheikh:2023 %}. The lack of connectivity between tools used at different steps in the research data lifecycle can also be a barrier to the proper management of their data.

For research funders, the development of technological infrastructure can be difficult {% cite sheikh:2023 %}. 

For research organisations, the institutional commitment and academic engagement required can be overwhelming. The lack of policy, funding and storage also hinders progress in RDM {% cite sheikh:2023 %}.

For librarians and RDM staff, raising awareness among researchers of the benefits of data sharing remains a challenge. On another note, librarians need (discipline-specific) skills and competencies to provide RDM-based services {% cite sheikh:2023 %}.

## Developments and Initiatives in RDM
---
Internationally, the increasingly frequent requirement to produce a DMP has stimulated interest in RDM {% cite yamaji:2024 %} and encouraged libraries to take an active role in RDM through advocacy, policy development, and advisory and consultancy services {% cite cox:2017 %}. Some institutions, such as KU Leuven, have also developed a dashboard to review datasets to meet funder requirements {% cite yamaji:2024 %}.

In Germany, the National Research Data Infrastructure (NFDI) funds nearly 30 discipline-specific consortia to help researchers make their data reusable in the long term.

## Resources
---

### General Resources
* [Brief Guide - Research Data Management](https://doi.org/10.5281/zenodo.4000989) by Training Expert Group.
* The Research Data Management toolkit for Life Sciences [RDMkit](https://rdmkit.elixir-europe.org/) by ELIXIR
* Virtual Research Environment ([VRE](https://vre.charite.de/vre/))

#### Platforms
* [BExIS2](https://demo.bexis2.uni-jena.de/) by NFDI4Biodiversity at FSU Jena
* [Coscine](https://www.coscine.de/en/) by RWTH aachen
* [GfBio](https://www.gfbio.org/) consortium services
* Research Data Management Competence Base ([RDM Compas](https://rdm-compas.org/en/homepage)) by KonsortSWD (social, behavioural, educational and economic sciences)

### Bioinformatics and Life-science Resources
* [Bio.tools](https://bio.tools/): essential scientific and technical information on software tools, databases and services for bioinformatics and the life sciences.
* G-Node infrastructure ([GIN](https://gin.g-node.org/)): GIN offers modern RDM for neuroscience. It is based on Gogs, git and git-annex technologies. GIN features include project management/coordination, large file support and data publishing. It also allows subfolders to be synchronised, shared and published independently of other subfolders. GIN also supports Markdown and LaTeX for manuscript writing. 
To use GIN, you must first create a new project repository and clone the research folder structure. You can then add a script that synchronises the repository and its submodules on double-click. You can also add submodules to a lab-wide repository. 

* TMF-Portal [ToolPool Gesundheitsforschung](https://www.toolpool-gesundheitsforschung.de/): The TMF-Portal was launched in 2017 and is operated by the Technologie- und Methodenplattform für die vernetzte medizinische Forschung e.V. (TMF). It provides a collection of IT infrastructure-related products for networked medical research. There are products from the TMF and from other providers such as companies and research institutions. There are over 80 products, more than half of which are software tools. Other product categories include eServices, reports and expert opinions, working materials and checklists, consultancy services and training courses. Products can be filtered by category, topic, project phase, keywords, provider and year. Similar products can also be compared using a feature matrix. On each product page you will find information about the use of the product in projects, testimonials from other users and references. New products can be submitted by anyone. Each product is then reviewed by a team of TMF members against a set of criteria before being added to the portal.
To use the portal, follow this link. Many offerings are free and can be accessed directly from the portal. Software products usually require local installation and configuration {% cite steen:2022 %}.

#### Standard Operating Procedures (SOPs)
* [SOP: Data management in clinical trials](https://khpcto.co.uk/SOPs/18_DataSOP.php)
* [SOP: Data Management in the National Institute of Neurological Disorders and Stroke](https://research.ninds.nih.gov/sites/default/files/documents/SOP18_Cinical_Data_Management_508C.pdf)
