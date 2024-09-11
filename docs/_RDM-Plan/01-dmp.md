---
title: Data Management Plans (DMPs)
category: RDM-Plan
layout: default
docs_css: markdown
---


# Introduction
Data Management Plans (DMPs) are required in [DFG funding proposals since 2022](https://www.dfg.de/en/research_funding/announcements_proposals/2022/info_wissenschaft_22_25/index.html) as well as for [EU Funding Programmes 2021-2027](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/common/guidance/aga_en.pdf). DMPs act as a reporting tool for funders to hold grant recipients accountable to conduct good and open science with periodic updates or upon changes. For researchers and other stakeholders, DMPs are meant as a living document that accompanies them from proposal writing or project start to the sharing of their data and findings.

# Definition
A Data Management Plan (DMP) is a formal and living document that defines responsibilities and provides guidance. It describes data and data management during the project and measures for archiving and making data and research results available, usable and understandable after the project has ended {% cite lindstädt_2019 vandendorpe_2020 cozatl_2021 assmann_2022-03 %}.

# Content of DMPs
In a DMP, researchers usually describe the data, their generation and processing during the project, as well as how the data and research results will be archived afterwards to remain available, usable and comprehensible. DMPs usually contain the following information:
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
Data Management Plans usually ask for “long-term archiving” or “long-term preservation” of research data, “data preservation”, “long-term data accessibility” or sometimes “data sharing”. Exact terminology varies according to the different funders and their DMP templates and research data guidelines.
For long-term archiving, preservation and accessibility/sharing, publication of research data in a Trusted Digital Repository (TDR) / trustworthy repository is recommended {% cite OpenAIRE_2024 england_2023_10125224 %}. TDR fall usually into two categories:
* a repository that has a CoreTrustSeal, nestor seal (DIN 31644) or ISO 16363 certification
* a repository that is commonly used and endorsed by the international research communities

For finding a TDR, check the [Data Repository page of the Knowledge Base](https://nfdi4microbiota.github.io/nfdi4microbiota-knowledge-base/Research-Data-Management/22-data-repositories).

# Benefits
When implemented correctly, a DMP can [benefit all stakeholders](https://doi.org/10.1371/journal.pcbi.1006750) of a research project despite the initial overhead of creating the DMP itself:

- **Transparency and reproducibility:** besides serving as a reporting tool for funders and governing institutions, a DMP can be handed to new collaborators of a project to convey a short description, experimental design, methodological spectrum, proposed hypotheses and general progress. This way, all stakeholders can quickly look up the state of data, find the responsible person for questions and document their own contribution.
- **Resource management:** including a timeline of personal and lab resource availability can enable service facilities (e.g. sequencing or IT) to more accurately schedule their resources/capacity and project costs.
- **Standardize processes:** DMPs can easily be adapted to similar projects by researchers in the same field/institute to reduce the effort for new proposals and resort to fixed entities (e.g. ethical board).

# DMP tools
Even though, it is generally possible to formulate a DMP in an office document, the use of more dynamic and machine-readable formats finally enables the full anticipated potential.
In Germany the [Research Data Management Organiser (RDMO)](https://rdmorganiser.github.io/) has gained widespread adoption among institutes and consortia.
This web-tool is used to create institute-wide templates and organize DMPs in different versions and share them with all stakeholders.

# DMP templates
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
