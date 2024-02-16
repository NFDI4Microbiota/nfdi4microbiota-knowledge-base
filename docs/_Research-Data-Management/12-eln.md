---
title: Electronic Lab Notebooks (ELNs)
category: Research-Data-Management
layout: default
docs_css: markdown
hide: true
---
# Definition of Electronic Lab Notebooks (ELNs)
An Electronic Lab Notebook (ELN) is a software meant for documenting experiments, resulting research data and processes. In its most basic form, an ELN replicates an interface similar to a page in a physical lab notebook. More advanced forms often offer features such as protocol templates, collaboration tools, support for electronic signatures and the ability to manage the lab inventory. Ultimately, ELNs will replace physical lab notebooks as part of the digital transformation {% cite kwok_2018 lindstädt_2019 lma_rdmwg vandendorpe_nd vieten_2023 %}.

# Uses of lab notebooks

## Physical lab notebooks
As well as documenting your experiments, resulting research data and processes, a physical lab notebook is also intended to communicate your work (e.g. why experiments were initiated?). It also serves as a legal document to prove patents and defend your data against accusations of misconduct. Finally, it is your scientific legacy in the laboratory {% cite n4m_wc_elns_2023 %}.

## Additional uses of ELNs
ELNs offer features and functions that can pave the way for significant time savings and knowledge transfer in daily laboratory work. For example, ELNs support the annotation of raw data (e.g. with tags or metadata {% cite vandendorpe_nd rathmann_2021 %} without having to switch between different media formats. Annotating data makes it searchable, discoverable, traceable and reusable {% cite vandendorpe_nd %}. ELNs also bring data and their description closer together through embedded multimedia files (e.g. videos of experimental setups), links to shared resources (e.g. chemical databases or analysis software), links to other experiments, and direct links to (raw) data sets and analysis workflows {% cite rehwald_2022 %}. ELNs also allow for the versioning of experiment descriptions {% cite rehwald_2022 %} and the structuring and visualisation of workflows and processes {% cite rathmann_2021 %}. ELNs also have the ability to manage inventories of samples, reagents and other supplies, and track equipment and equipment maintenance schedules {% cite lma_rdmwg %}. ELNs also provide for collaboration {% cite lma_rdmwg %} through a common medium {% cite rehwald_2022 %}. Last but not least, ELNs provide for auditing {% cite lma_rdmwg %}, security and safety. Indeed, ELNs are fireproof, waterproof and cannot be lost, misplaced or stolen. ELNs can also be automatically backed up. They allow timestamping (RFC 3161 using DFN-PKI) and finalisation to prevent further changes {% cite rehwald_2022 %}. They also support electronic signatures {% cite cozatl_2021 %} and require access management {% cite rehwald_2022 %}.

## What ELNs should not be used for
ELNs are not data publishing platforms and are not suitable for storing large files. Large files require special technology for secure storage (e.g. Object Store, Nextcloud), but can still be linked in the ELN {% cite rehwald_2022 %}.

# Benefits and drawbacks
## Pros & Cons of Physical Lab Notebooks

Historically, documentation of experiments have been done in a physical, paper and pen notebook. For some researchers this is still a preferred method of documentation. It’s easy and inexpensive to use as it does not require computers nor internet access. However, with the technological advancement in data collection and processing there is a greater amount of data produced than ever before and with it there is a need for data to be digitized and managed electronically. 

Also with advances in communication and travel it is even easier to work collaboratively with researchers at different institutes around the world. This collaboration would be difficult or hindered if scans of physical lab notebooks would need to be shared. Of course, this also does not take into consideration the legibility of the experiment notes or the ability to make general sense of it.

These drawbacks outweigh the benefits of a physical laboratory notebook. Adoption of an ELN is one of the essential steps needed in making research data FAIR. The purpose of adherence to the FAIR principles is so that the data can continue to be reused, validated, and expanded by researchers in the future. The data life cycle starts with planning and goes through the production and analysis followed by storage and access and ideally ends with data re-use. 

In order for data to be re-used it needs to meet the criteria of the FAIR principles. This is where the largest drawback of physical laboratory notebooks lies. Data in a physical notebook cannot be found, accessed, or reused by other researchers. Data in an ELN can be extracted, downloaded, shared, and stored in a FAIR capacity. This data can also be described with metadata which gives more context needed to make sense of the data and ensure it can be reused.

Unfortunately, the major drawback to the wide use of ELNs in all areas of research appears to be data security risks, specifically when used in medical research. There is still an ongoing discussion on how to best securely manage patient research data in an ELN. However, according to Guerrero the best solutions involve using private servers on site or private institutionally based cloud services {% cite Guerrero2016 %}.

## Boosting efficiency of everyday tasks
ELNs increase the efficiency of everyday tasks by providing time-saving features and functions such as search and filtering {% cite vandendorpe_nd %}. ELNs also take advantage of standardisation {% cite rathmann_2021 %}: they have the ability to create templates such as protocols, Standard Operating Procedures (SOPs) and workflows. This facilitates data documentation with metadata {% cite vandendorpe_nd %} and supports clarity and organisation of data and protocols {% cite n4m_wc_elns_2023 %}. ELNs also provide ubiquitous access {% cite vandendorpe_nd %}: protocols, observations, notes and other data can be entered using a computer or mobile device {% cite lma_rdmwg %}.

## Connection to a digital research environment
ELNs are linked to a digital research environment {% cite vandendorpe_nd %}, for example through their import and export capabilities {% cite bobrov_2021 %}. ELNs can also provide seamless interfaces to other programmes, such as Application Programming Interfaces (APIs) {% cite bobrov_2021 %}. This networked aspect of ELNs enables them to play a central role in an institution's [Research Data Management](https://nfdi4microbiota.github.io/nfdi4microbiota-knowledge-base/Research-Data-Management/02-rdm) (RDM) strategy. Indeed, ELNs can be linked and contribute to almost each step of the research data lifecycle:

* **Data collection:** ELNs can automatically record results from measuring instruments {% cite rathmann_2021 vandendorpe_2020 %} and retrieve data from databases for actively used data {% cite assmann_2022 Krause_2016 %}.

* **Data processing:** As we have seen, ELNs facilitate the documentation of data with metadata. They also allow data to be captured as early as possible and fed directly into an analysis pipeline {% cite vandendorpe_nd %}.

* **Data sharing and publishing:** ELNs facilitate collaboration by allowing data already in digital form to be used directly in the ELN {% cite vandendorpe_nd %}. ELNs also make it easy to share information about the project, data and documentation with collaborators {% cite lma_rdmwg %}, for example via the cloud {% cite n4m_wc_elns_2023 %}. All this also facilitates collaboration with the institutional library, research data centre and IT centre {% cite vandendorpe_nd %}.
ELNs also facilitate publishing by providing a means to prepare research data for publication {% cite vandendorpe_2020 %} and by integrating with other applications such as Mendeley, Dataverse and PubMed {% cite n4m_wc_elns_2023 lma_rdmwg %}.

* **Digital preservation:** ELNs facilitate the creation of backups {% cite rathmann_2021 %} and can include links to the location of large amounts of data {% cite bobrov_2021 %}. They also facilitate the archiving of data and its documentation {% cite vandendorpe_nd n4m_wc_elns_2023 %} by providing a means to prepare research data for digital preservation {% cite vandendorpe_2020 %} and by being linked to digital preservation systems.

* **Data discovery and reuse:** ELNs can prove provenance {% cite lma_rdmwg %}.

## Complying to the FAIR Data Principles
ELNs support the [FAIR Data Principles](https://nfdi4microbiota.github.io/nfdi4microbiota-knowledge-base/Research-Data-Management/04-fair) {% cite lma_rdmwg %}:

* **Findability:** ELNs support findability by providing comprehensive search capabilities (e.g. database search, full-text search, conditional search), by supporting the assignment of metadata and tags (e.g. through extraction from documents), by assigning persistent identifiers such as the Digital Object Identifier (DOI) and by linking to data repositories and digital preservation systems {% cite bobrov_2021 %}.

* **Accessibility:** ELNs support accessibility by storing data in a fixed and accessible location, rather than on the researcher's USB stick or portable hard drive {% cite bobrov_2021 %}.

* **Interoperability:** ELNs support interoperability by supporting the use of controlled vocabularies in metadata and allowing export to standard formats {% cite bobrov_2021 %}.

* **Reusability:** ELNs support reusability by providing detailed provenance information through audit trails and documentation of both data generation (e.g. method logs) and equipment used {% cite bobrov_2021 %}.

## Contributing to Good Scientific Practice (GSP)
ELNs make an important contribution to Good Scientific Practice (GSP) by facilitating the tracking, tracing and documentation of research processes and results over time {% cite vandendorpe_nd %}. They enable this by providing functions and features such as electronic signatures, version control {% cite vandendorpe_2020 %}, authentication, 'freezing' of work status, searchability and tagging of entries, and audit trail {% cite bobrov_2021 %}.

ELNs also prevent data loss by eliminating problems with data deletion {% cite bobrov_2021 %}, illegible handwriting, media discontinuities between handwritten and digital entries {% cite vandendorpe_nd %}, damaged paper notebooks, and researchers moving on {% cite lma_rdmwg %}.

Finally, ELNs contribute to GSP by providing for data security and collaboration (see Data sharing and publishing) {% cite lma_rdmwg %}.

# Criteria to select an ELN
## Basic systems
Basic systems allow for traditional text entry, which can be searched and made available on multiple devices via the cloud. They also allow files (e.g. images, spreadsheets) to be attached to text and the attachments to be viewed, annotated and searched. Such systems include Word, Evernote and Dropbox. Basic systems have the advantage of being inexpensive, easily accessible and already familiar to many researchers. However, considerable effort is required to achieve the functionality of a traditional ELN with such a system {% cite bobrov_2021 vandendorpe_2020 %}.

## Specialised systems
Specialised systems have all the features of basic systems and more. They have the ability to capture freehand and chemical drawings {% cite lma_rdmwg %}. They also offer subject-specific features/editors and templates. They also allow task assignment between colleagues, complex rights management (i.e. with roles and individual rights), basic inventory management (i.e. allowing the quantity and location of samples and reagents to be managed) and extensions/APIs for customisation {% cite bobrov_2021 vandendorpe_2020 %}. Last but not least, they comply with the [Code of Federal Regulations Title 21 Part 11](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/CFRSearch.cfm?CFRPart=11). This part requires full audit trails (i.e. all previous versions of a note are stored and changes are logged), electronic signatures on completed records, witnessing and freezing (i.e. making a note immutable after the author and a witness have signed it), and prevents the deletion of records by their author. Such systems include Arxspan, Biovia, eCat, eLabJournal, eLabFTW, iLabber, Labfolder and RSpace. Specialised systems have the advantage of offering easy entry through free online versions and the possibility of local installation and data storage. They can also be integrated into your own IT environment via APIs {% cite bobrov_2021 vandendorpe_2020 %}.

## High-end systems
High-end systems have all the features of specialised systems and more. High-end ELNs integrate a Laboratory Information Management System (LIMS) (e.g. IBDS E-WORKBOOK, iLAB Laboratory Execution System) that allows complete tracking of samples and reagents through all experiments. They are also directly linked to laboratory equipment such as microscopes, spectrometers and sequencers. High-end systems provide workflows for specific samples, experiments and tasks. They can automatically deliver raw data and metadata (e.g. date of last calibration) from laboratory equipment. Finally, they allow data mining (aggregation and clustering of structured data) and analysis of raw data within the system. Such systems include Hivebench and Limsophy. High-end systems have the advantage of completeness of features and all their components fit together seamlessly, making them easy to use. However, they are often cloud-hosted solutions, which means that data control and security remain in the hands of the ELN provider {% cite bobrov_2021 vandendorpe_2020 %}, and they are more expensive {% cite higgins_2022 %}. They also use proprietary formats, which can increase the risk of vendor lock-in (i.e. making users dependent on the ELN and unable to use their data with another ELN without significant switching costs {% cite vendor_lock_in %}) {% cite bobrov_2021 vandendorpe_2020 %}.

## Electronic Lab Notebooks *vs.* Laboratory Information Management System (LIMS)
ELNs are sometimes confused with Laboratory Information Management Systems (LIMS). They both streamline laboratory workflow and data management and are complementary, but they have different functionalities and features. A LIMS is a comprehensive software for managing and tracking laboratory operations and data. A LIMS covers sample management, workflow management and automation, quality control and sample tracking throughout the laboratory. On the other hand, an ELN focuses on experimental data acquisition, experiment documentation and (real-time) collaboration {% cite eln_lims_linkedin eln_lims_sapio %}.

# Implementing an ELN
## Changing Culture
A cultural change is needed in order to transition researchers not only to ELNs from physical notebooks but to adhere to FAIR principles thus working towards open science. According to Nosek's [Strategy for Culture Change](https://www.cos.io/blog/strategy-for-culture-change), at the Center for Open Science there are “five levels of intervention” which starts at the bottom with infrastructure. 

Changes to infrastructure would help ease the transition to an ELN by making such it possible to adopt. Covering costs for the use of an ELN at the institutional level, rather than leaving it up to individually funded research projects, would make it possible for groups to justify their use. The next step would be to ensure a good experience with ELNs through a user-friendly interface, training researchers how to use the ELN, and incorporating it into existing workflows.

A community of researchers will begin to form who use ELNs as a common practice. Provide incentives to researchers in order to ensure the continued use of the ELN. According to the Center for Open Science there are over 100 journals which offer badges that indicate when there is data or materials available to the reader. These badges incentivize researchers to share data as it adds more credibility to their findings. After moving through the bottom four levels of infrastructure, experience, community, and incentives the top level policy change will be possible. At the policy level the institution can now make the transition to ELN a requirement for its affiliated researchers.

While there are still researchers who may be apprehensive regarding sharing their data this will change as the culture surrounding research transitions to more transparency.


# Further resources
* [ELN Finder - Demo](https://eln-finder.ulb.tu-darmstadt.de/home) - Tool to help researchers searching and selecting a suitable ELN thanks to more than 40 filter criteria.
* ELN Filter - Selection of ELNs that are suitable for the life sciences and that can be filtered out according to criteria ([English](https://www.publisso.de/fileadmin/user_upload/PUBLISSO/PUBLISSO_ELN-Filter_2021-06_english.xlsx), [German](https://www.publisso.de/fileadmin/user_upload/PUBLISSO/PUBLISSO_ELN-Filter_2020-12-01.xlsx)).
* ELN Guide - ELNs in the context of research data management and good research practice – a guide for the life sciences ([English](https://dx.doi.org/10.4126/FRL01-006425772), [German](https://dx.doi.org/10.4126/FRL01-006422868)).
* Free consultation sessions to get advice on the selection and introduction of an ELN (<forschungsdaten@zbmed.de>).
* [Video tutorial series](https://www.youtube.com/playlist?list=PLJYlS0FDTMq17tvYMeuI2Ct5XtykRFy0K) (only in German).
* Working groups on ELNs (e.g. in [North Rhine-Westphalia](https://wiki.hhu.de/display/ELB/) in German).

# References
{% bibliography --cited_in_order %}
