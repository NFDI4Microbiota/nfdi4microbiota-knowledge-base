---
title: Data Management Plans (DMPs)
category: RDM-Plan
layout: default
docs_css: markdown
---

# Introduction
A Data Management Plan (DMP) is a formal and living document that defines responsibilities and provides guidance. It describes data and data management during the project and measures for archiving and making data and research results available, usable and understandable after the project has ended. 

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
When implemented correctly, a DMP can [benefit all stakeholders](https://doi.org/10.1371/journal.pcbi.1006750) of a research project despite the initial overhead of creating the DMP itself.

## Saving time and nerves
A DMP can save time and nerves for yourself and others by planning ahead. DMPs define roles, responsibilities and efforts regarding the data and its management. Writing a DMP will also get you in touch with IT staff and your institution's data protection officer at an early stage. Writing a DMP also ensures data quality and allows you to easily trace your processing steps, making your analysis and results reproducible. Writing a DMP also allows you to manage access rights and prevent security breaches. Finally, by writing your DMP, you may be able to identify gaps and vulnerabilities in your current data management strategy at an early stage and outline solutions to fill them.

## Harmonise the shared use of data
A DMP can also facilitate and harmonise the coordination and shared use of data by multiple project partners, as well as improve knowledge management (even when staff change). A DMP provides the project team with an overview and control of the data, its use and storage, and all data management activities, enabling process optimisation and facilitating organisation and work. A DMP will also help you to establish project-wide standards and a common vocabulary. It will also allow you to keep track of data by knowing where it is stored during and after the project, making it easily retrievable and reducing the risk of data duplication and loss (some data, such as excavation data and textual annotations, are not reproducible) due to technical or human error. Finally, writing a DMP gives you a clear organisation of the data and its handling, which helps you to understand your own data (e.g. through documentation) and makes your work more efficient.

## Further benefits
DMPs offer other benefits, such as enabling verification and control: researchers are accountable for how their data are managed during their research project. They also help to identify - and potentially minimise - time and money costs that need to be included in the proposal, such as for RDM activities. They also help to comply with Good Research Practice (GRP), support research integrity and ensure that ethical and legal requirements are met. DMPs also help to meet institutional and funder requirements: funding agencies increasingly require information on the management of research data, and a DMP allows you to structure and formalise this information. Last but not least, DMPs facilitate data reuse, thereby increasing data citation and advancing scientific progress.

# Writing a DMP

## Who is involved in the creation of the DMP?
Entities involved in the creation of a DMP are researchers, RDM staff (check your institution's [research data policy](https://www.forschungsdaten.org/index.php/Forschungsdaten-Policies) and ask for [local support](https://www.forschungsdaten.org/index.php/FDM-Kontakte)) and central infrastructure (e.g. computer centre, library).

## When to set up a DMP?
A DMP can be set up before the project starts or at the beginning of the project. Ensure that there are no inconsistencies with time and cost schedules.

## Length & level of details
The length of a DMP can vary from a few paragraphs to several pages (about 2 to 15 pages). It is better to be realistic; be as informative as possible and as detailed as necessary. At the beginning of the research project (e.g. when you have to submit your DMP together with the proposal), the DMP is quite short and provides basic information. As the project progresses, the DMP contains more and more information, the answers become more detailed and the functions of the DMP increase until it becomes a project management tool.

## DMP quality check
A good DMP is well structured and distinguishes between actions to be taken during and after the project. It is a living document that needs to be updated regularly and is for the use of all project stakeholders. It should be started as early as possible, be as concise as possible, as long as necessary, and contain sufficient detail without being redundant. Ideally, the DMP will be published with the research data at the end of the project.

# DMP tools
Even though, it is generally possible to formulate a DMP in an office document, the use of more dynamic and machine-readable formats finally enables the full anticipated potential.
In Germany the [Research Data Management Organiser (RDMO)](https://rdmorganiser.github.io/) has gained widespread adoption among institutes and consortia.
This web-tool is used to create institute-wide templates and organize DMPs in different versions and share them with all stakeholders.

## DMP templates in RDMO
RDMO organizes individual plans around predefined templates that reflect the requirements of the respective institution, discipline or funder.
This ensures machine-actionable compatibility for administrative stakeholders and re-usability for researchers in following projects.
These templates usually contain much more aspects that do not have to be answered right from the start of a project, but can be completed as the research progresses.

# Further resources

## Machine-actionable DMPs (maDMPs)
* Data Stewardship Wizard (DSW) - [Machine-Actionability](https://ds-wizard.org/machine-actionability)
* Michener, W. K. (2015). Ten Simple Rules for Creating a Good Data Management Plan. In P. E. Bourne (Ed.), PLOS Computational Biology (Vol. 11, Issue 10, p. e1004525). Public Library of Science (PLoS). [https://doi.org/10.1371/journal.pcbi.1004525](https://doi.org/10.1371/journal.pcbi.1004525)
* Miksa, T., Simms, S., Mietchen, D., & Jones, S. (2019). Ten principles for machine-actionable data management plans. In F. Ouellette (Ed.), PLOS Computational Biology (Vol. 15, Issue 3, p. e1006750). Public Library of Science (PLoS). [https://doi.org/10.1371/journal.pcbi.1006750](https://doi.org/10.1371/journal.pcbi.1006750)

## Software Management (SM) Plans
* [SM Wizard](https://smw.ds-wizard.org/)
* [Writing and using a software management plan](https://www.software.ac.uk/guide/writing-and-using-software-management-plan)

# References
{% bibliography --cited_in_order %}
