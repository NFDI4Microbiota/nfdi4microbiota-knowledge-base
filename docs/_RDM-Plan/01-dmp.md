---
title: Data Management Plans (DMPs)
category: RDM-Plan
layout: default
docs_css: markdown
---

# Introduction
A Data Management Plan (DMP) is a formal and living document that defines responsibilities and provides guidance. It describes data and data management during the project and measures for archiving and making data and research results available, usable and understandable after the project has ended {% cite lindstädt_2019 vandendorpe_2020 cozatl_2021 assmann_2022-03 %}. 

DMPs are required in [DFG funding proposals since 2022](https://www.dfg.de/en/research_funding/announcements_proposals/2022/info_wissenschaft_22_25/index.html) and in [EU Funding Programmes 2021-2027](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/common/guidance/aga_en.pdf). For funders, DMPs serve as a reporting tool to hold grantees accountable for conducting good and open science, with regular updates or in case of changes. For researchers and other stakeholders, DMPs are meant to be a living document that accompanies them from proposal writing or project start to the sharing of their data and results.

# Content of DMPs
DMPs usually contain the following information:
* Administrative project-specific information (including a description of the research project)
* Roles, responsibilities and obligations
* Budget, costs and resources
* Description of the data to be collected and shared (including types, organisation, quality and usage)
* Data documentation and standards
* Data access and publishing (including referenceability and data citation)
* Data security
* Data storage during and after the project
* Data backup and digital preservation
* Further points: ethical and legal aspects (e.g. anonymisation, data deletion)

## Digital Preservation in DMPs
DMPs usually ask for “long-term archiving” or “long-term preservation”, “data preservation”, “long-term data accessibility” or sometimes “data sharing”  of research data. The exact terminology varies according to different funders and their DMP templates and research data policies. For long-term archiving, preservation and accessibility/sharing, the publication of research data in a Trusted Digital Repository (TDR) is recommended {% cite OpenAIRE_2024 england_2023_10125224 %}. TDRs typically fall into two categories:
1. a repository that has a CoreTrustSeal, nestor seal (DIN 31644) or ISO 16363 certification
2. a repository that is widely used and supported by the international research community

To find a TDR, see the [Data Repositories page of the Knowledge Base](https://nfdi4microbiota.github.io/nfdi4microbiota-knowledge-base/Research-Data-Management/22-data-repositories).

# Templates and examples
* Templates
    * [NFDI4Microbiota's template](https://doi.org/10.5281/zenodo.13628589)
    * Portage Network's template for [advanced research computing](https://doi.org/10.5281/zenodo.4573539)
    * Portage Network's template for [molecular interactions](https://doi.org/10.5281/zenodo.4683647)
* Omics-specific examples
    * [DD-DeCaF Bioinformatics Services for Data-Driven Designof Cell Factories and Communities](https://phaidra.univie.ac.at/o:1139495)
    * [METASTAVA](https://doi.org/10.5281/zenodo.5841166)

# Benefits
When implemented correctly, a DMP can [benefit all stakeholders](https://doi.org/10.1371/journal.pcbi.1006750) of a research project despite the initial overhead of creating the DMP itself:

- **Transparency and reproducibility:** besides serving as a reporting tool for funders and governing institutions, a DMP can be handed to new collaborators of a project to convey a short description, experimental design, methodological spectrum, proposed hypotheses and general progress. This way, all stakeholders can quickly look up the state of data, find the responsible person for questions and document their own contribution.
- **Resource management:** including a timeline of personal and lab resource availability can enable service facilities (e.g. sequencing or IT) to more accurately schedule their resources/capacity and project costs.
- **Standardize processes:** DMPs can easily be adapted to similar projects by researchers in the same field/institute to reduce the effort for new proposals and resort to fixed entities (e.g. ethical board).

# DMP tools
Even though, it is generally possible to formulate a DMP in an office document, the use of more dynamic and machine-readable formats finally enables the full anticipated potential.
In Germany the [Research Data Management Organiser (RDMO)](https://rdmorganiser.github.io/) has gained widespread adoption among institutes and consortia.
This web-tool is used to create institute-wide templates and organize DMPs in different versions and share them with all stakeholders.

## DMP templates in RDMO
RDMO organizes individual plans around predefined templates that reflect the requirements of the respective institution, discipline or funder.
This ensures machine-actionable compatibility for administrative stakeholders and re-usability for researchers in following projects.
These templates usually contain much more aspects that do not have to be answered right from the start of a project, but can be completed as the research progresses.

# Further resources
* **Example of a good DMP**: Molin, E. (2018). Behave Working Data-Management-Plan. Zenodo. [https://doi.org/10.5281/ZENODO.1243717](https://doi.org/10.5281/ZENODO.1243717)

## DMP templates
* **Biological & Environmental Sciences**
    * German Federation for Biological Data (GFBio): [web page](https://dmp.gfbio.org/)
    * DataPlant: [web page](https://nfdi4plants.de/dataplan/)

* **Health Sciences**
    * University of Minnesota (incl. School of Public Health): [web page](https://www.lib.umn.edu/services/data/dmp-examples)
    * Clinical trials
        * National Institutes of Health (NIH): [download](https://www.nidcr.nih.gov/sites/default/files/2018-03/clinical-data-management-plan-template_0.docx)
        * PAPA-ARTiS: [download](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5b6899b9b&appId=PPGMS)
        * European Clinical Research Infrastructure Network (ECRIN): [pdf (p. 48)](https://ecrin.org/sites/default/files/Data%20centre%20certification/Standards%20v4%20201804.pdf)

## Machine-actionable DMPs (maDMPs)
* Michener, W. K. (2015). Ten Simple Rules for Creating a Good Data Management Plan. In P. E. Bourne (Ed.), PLOS Computational Biology (Vol. 11, Issue 10, p. e1004525). Public Library of Science (PLoS). [https://doi.org/10.1371/journal.pcbi.1004525](https://doi.org/10.1371/journal.pcbi.1004525)
* Miksa, T., Simms, S., Mietchen, D., & Jones, S. (2019). Ten principles for machine-actionable data management plans. In F. Ouellette (Ed.), PLOS Computational Biology (Vol. 15, Issue 3, p. e1006750). Public Library of Science (PLoS). [https://doi.org/10.1371/journal.pcbi.1006750](https://doi.org/10.1371/journal.pcbi.1006750)

## Software Management (SM) Plans
* [SM Wizard](https://smw.ds-wizard.org/)

# References
{% bibliography --cited_in_order %}
