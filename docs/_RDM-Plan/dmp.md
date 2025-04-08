---
title: Data Management Plans (DMPs)
category: RDM-Plan
layout: default
docs_css: markdown
---

## Introduction
A Data Management Plan (DMP) is a formal and living document that defines responsibilities and provides guidance. It describes data and data management during the project and measures for archiving and making data and research results available, usable, and understandable after the project has ended. 

DMPs are required in [DFG funding proposals since 2022](https://www.dfg.de/en/research_funding/announcements_proposals/2022/info_wissenschaft_22_25/index.html) and in [EU Funding Programs 2021-2027](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/common/guidance/aga_en.pdf). For funders, DMPs serve as a reporting tool to hold grantees accountable for conducting good and open science, with regular updates or in case of changes. For researchers and other stakeholders, DMPs are meant to be a living document that accompanies them from proposal writing or project start to the sharing of their data and results.

## Content of DMPs

---



DMPs typically include the following information:
* Administrative project-specific information (including a description of the research project)
* Roles, responsibilities and obligations
* Budget, costs and resources
* Description of the data to be collected and shared (including types, organization, quality and use)
* Data documentation and standards
* Data access and publishing (including referencing and data citation)
* Data security, storage (during and after the project), backup and digital preservation
* Further points: ethical and legal aspects (e.g. anonymization), data deletion

**Digital preservation in DMPs:** DMPs usually ask for “long-term archiving” or “long-term preservation”, “data preservation”, “long-term data accessibility” or sometimes “data sharing”  of research data. The exact terminology varies according to different funders and their DMP templates and research data policies. For long-term archiving, preservation, and accessibility/sharing, the publication of research data in a Trusted Digital Repository (TDR) is recommended {% cite OpenAIRE_2024 england_2023_10125224 %}. TDRs typically fall into one of two categories:
1. a repository that has a CoreTrustSeal, Nestor seal (DIN 31644), or ISO 16363 certification
2. a repository that is widely used and supported by the international research community

To find a TDR, see the [Data Repositories page of the Knowledge Base]({% link _RDM-Share/data-repositories.md %}).

## DMP Templates and Examples

---

**Templates**
* [NFDI4Microbiota's template](https://doi.org/10.5281/zenodo.13628589)
* Portage Network's template for [advanced research computing](https://doi.org/10.5281/zenodo.4573539)
* Portage Network's template for [molecular interactions](https://doi.org/10.5281/zenodo.4683647)

**Omics-specific examples**
* [DD-DeCaF Bioinformatics Services for Data-Driven Design of Cell Factories and Communities](https://phaidra.univie.ac.at/o:1139495)
* [METASTAVA](https://doi.org/10.5281/zenodo.5841166)


## Benefits of a DMP

---

If implemented correctly, a DMP can [benefit all stakeholders](https://doi.org/10.1371/journal.pcbi.1006750) in a research project, despite the initial cost of creating the DMP itself.

A DMP can **save time and nerves** for yourself and others by planning ahead. DMPs define roles, responsibilities, and efforts regarding the data and its management. Writing a DMP will also get you in touch with IT staff and your institution's data protection officer at an early stage. Writing a DMP also ensures data quality and allows you to easily trace your processing steps, making your analysis and results reproducible. Writing a DMP also allows you to manage access rights and prevent security breaches. Finally, by writing your DMP, you may be able to identify gaps and vulnerabilities in your current data management strategy at an early stage and outline solutions to fill them.

A DMP can also facilitate and **harmonize the coordination and shared use of data** by multiple project partners, as well as improve knowledge management (even when staff change). A DMP provides the project team with an overview and control of the data, its use and storage, and all data management activities, enabling process optimization and facilitating organization and work. A DMP will also help you to establish project-wide standards and a common vocabulary. It will also allow you to keep track of data by knowing where it is stored during and after the project, making it easily retrievable and reducing the risk of data duplication and loss due to technical or human error (some data, such as excavation data and textual annotations, are not reproducible). Finally, writing a DMP gives you a clear organization of the data and its handling, which helps you to understand your own data (e.g. through documentation) and makes your work more efficient.

DMPs offer **other benefits**, such as enabling verification and control: researchers are accountable for how their data are managed during their research project. They also help to identify - and potentially minimize - time and money costs that need to be included in the proposal, such as for Research Data Management (RDM) activities. They also help to comply with Good Research Practice (GRP), support research integrity, and ensure that ethical and legal requirements are met. DMPs also help to meet institutional and funder requirements: funding agencies increasingly require information on the management of research data, and a DMP allows you to structure and formalize this information. Last but not least, DMPs facilitate data reuse, thereby increasing data citation and advancing scientific progress.

## Writing a DMP

---

**Who is involved in the creation of the DMP?** Entities involved in the creation of a DMP are researchers, RDM staff (check your institution's [research data policy](https://www.forschungsdaten.org/index.php/Forschungsdaten-Policies) and ask for [local support](https://www.forschungsdaten.org/index.php/FDM-Kontakte)) and central infrastructure (e.g. computer center, library).

**When to set up a DMP?** A DMP can be set up before the project starts or at the beginning of the project.

**Length & level of details of the DMP:** The length of a DMP can vary from a few paragraphs to several pages (about 2 to 15 pages). It is better to be realistic; be as informative as possible and as detailed as necessary. At the beginning of the research project (e.g. when you have to submit your DMP together with the proposal), the DMP is quite short and provides basic information. As the project progresses, the DMP contains more and more information, the answers become more detailed, and the functions of the DMP increase.

**DMP quality check:** A good DMP is well structured and distinguishes between actions to be taken during and after the project. It is a living document that needs to be updated regularly and is for the use of all project stakeholders. It should be started as early as possible, be as concise as possible, as long as necessary, and contain sufficient detail without being redundant. Ideally, the DMP will be published with the research data at the end of the project.

## DMP Tools

---

Although it is generally possible to formulate a DMP in a text document, the use of more dynamic and machine-readable formats finally unlocks its full potential.

* **[Research Data Management Organizer](https://rdmorganiser.github.io/) (RDMO)** is an open-source web application that has been widely adopted by institutes and consortia in Germany. RDMO supports the structured and collaborative planning and implementation of RDM and also enables the textual output of a DMP. 
RDMO organizes individual DMPs around predefined templates that reflect the requirements of the respective institution, discipline, or funder. This ensures machine-actionable compatibility for administrative stakeholders and reusability for researchers in subsequent projects.

* **[Data Stewardship Wizard](https://ds-wizard.org/) (DSW)** was developed by ELIXIR Netherlands and ELIXIR Czech Republic and is recommended by the [Horizon Europe Programme Guide](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/guidance/programme-guide_horizon_en.pdf). DSW is an open-source dynamic web form system. It has been designed as an expert system and is intended for data stewards to assist researchers in creating machine-actionable DMPs. It offers user-friendly questionnaires and many different templates (it is also possible to create your own template). Training on DSW is organized by different ELIXIR nodes.

* **[DMPonline](https://dmponline.dcc.ac.uk/)** was developed by the [Digital Curation Center](https://www.dcc.ac.uk/) (DCC) for the UK funding context but has also been used elsewhere. It is an open-source, web-based tool for researchers. It enables the creation, review, and sharing of DMPs that meet institutional and funder requirements.

## Further Resources

---

* Cessda - [Data Management Expert Guide](https://dmeg.cessda.eu/Data-Management-Expert-Guide)
* [Content of a Data Management Plan](https://doi.org/10.18154/RWTH-2019-10064)
* [Data Management Plan — the Turing Way - Data Management Plan](https://the-turing-way.netlify.app/reproducible-research/rdm/rdm-dmp.html)
* [DMP course for librarians]([https://librarycarpentry.org/lc-dmp101/dmp.html))
* OpenAIRE - [How to create a Data Management Plan](https://www.openaire.eu/how-to-create-a-data-management-plan)
* [Research data management and Data Management Plans](https://doi.org/10.5281/zenodo.4587426)
* [Research Data Management Workflows and maDMPs (Version 1.0.0)](https://doi.org/10.5281/zenodo.3944468)
* Research Data Netherlands - [The what, why, and how of data management planning](https://www.youtube.com/watch?v=gYDb-GP1CA4)
* RDMkit - [Data management plan](https://rdmkit.elixir-europe.org/data_management_plan)
* [Ten Simple Rules for Creating a Good Data Management Plan](https://doi.org/10.1371/journal.pcbi.1004525)
* [What will it cost to manage and share my data?](https://doi.org/10.5281/zenodo.4548344)

**Machine-actionable DMPs (maDMPs)**
* Data Stewardship Wizard (DSW) - [Machine-Actionability](https://ds-wizard.org/machine-actionability)
* [Ten principles for machine-actionable data management plans](https://doi.org/10.1371/journal.pcbi.1006750)

**Software Management (SM) Plans**
* [SM Wizard](https://smw.ds-wizard.org/)
* [Writing and using a software management plan](https://www.software.ac.uk/guide/writing-and-using-software-management-plan)

