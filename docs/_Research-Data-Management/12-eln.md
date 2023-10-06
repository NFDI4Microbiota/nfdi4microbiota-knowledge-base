---
title: Electronic Lab Notebooks (ELNs)
category: Research-Data-Management
layout: default
docs_css: markdown
---
# Definition of Electronic Lab Notebooks (ELNs)
An Electronic Lab Notebook (ELN) is a software meant for documenting experiments, resulting research data and processes. In its most basic form, an ELN replicates an interface similar to a page in a physical lab notebook. More advanced forms often offer features such as protocol templates, collaboration tools, support for electronic signatures and the ability to manage the lab inventory. Ultimately, ELNs will replace physical lab notebooks as part of the digital transformation {% cite kwok_2018 lindstädt_2019 lma_rdmwg vandendorpe_nd vieten_2023 %}.

# Uses of lab notebooks

## Physical lab notebooks
As well as documenting your experiments, resulting research data and processes, a physical lab notebook is also intended to communicate your work (e.g. why experiments were initiated?). It also serves as a legal document to prove patents and defend your data against accusations of misconduct. Finally, it is your scientific legacy in the laboratory {% cite n4m_wc_elns_2023 %}.

## Additional uses of ELNs
ELNs offer features and functions that can pave the way for significant time savings and knowledge transfer in daily laboratory work. For example, ELNs support the annotation of raw data (e.g. with tags or metadata {% cite rathmann_2021 vandendorpe_nd %} without having to switch between different media formats. Annotating data makes it searchable, discoverable, traceable and reusable {% cite vandendorpe_nd %}. ELNs also bring data and their description closer together through embedded multimedia files (e.g. videos of experimental setups), links to shared resources (e.g. chemical databases or analysis software), links to other experiments, and direct links to (raw) data sets and analysis workflows {% cite rehwald_2022 %}. ELNs also allow for the versioning of experiment descriptions  {% cite rehwald_2022 %} and the structuring and visualisation of workflows and processes {% cite rathmann_2021 %}. ELNs also have the ability to manage inventories of samples, reagents and other supplies, and track equipment and equipment maintenance schedules {% cite lma_rdmwg %}. ELNs also provide for collaboration {% cite lma_rdmwg %} through a common medium  {% cite rehwald_2022 %}. Last but not least, ELNs provide for auditing {% cite lma_rdmwg %}, security and safety. Indeed, ELNs are fireproof, waterproof and cannot be lost, misplaced or stolen. ELNs can also be automatically backed up. They allow timestamping (RFC 3161 using DFN-PKI) and finalisation to prevent further changes  {% cite rehwald_2022 %}. They also support electronic signatures {% cite cozatl_2021 %} and require access management {% cite rehwald_2022 %}.

## What ELNs should not be used for
ELNs are not data publishing platforms and are not suitable for storing large files. Large files require special technology for secure storage (e.g. Object Store, Nextcloud), but can still be linked in the ELN {% cite rehwald_2022 %}.

# Benefits and drawbacks

## Boosting efficiency of everyday tasks
ELNs increase the efficiency of everyday tasks by providing time-saving features and functions such as search and filtering {% cite vandendorpe_nd %}. ELNs also take advantage of standardisation {% cite rathmann_2021 %}: they have the ability to create templates such as protocols, Standard Operating Procedures (SOPs) and workflows. This facilitates data documentation with metadata {% cite vandendorpe_nd %} and supports clarity and organisation of data and protocols {% cite n4m_wc_elns_2023 %}. ELNs also provide ubiquitous access {% cite vandendorpe_nd %}: protocols, observations, notes and other data can be entered using a computer or mobile device {% cite lma_rdmwg %}.

## Connection to a digital research environment
ELNs can be integrated into a networked research environment {% cite vandendorpe_nd %}, for example through their import and export capabilities {% cite bobrov_2021 %}. ELNs can also automatically record results from measuring instruments {% cite vandendorpe_2020 rathmann_2021 %} and provide seamless interfaces to other programs such as application programming interfaces (APIs) {% cite bobrov_2021 %}. All of this ensures that everything is connected and that research data is captured as early as possible and fed directly into an analysis pipeline {% cite vandendorpe_nd %}.

# Further resources
* [ELN Finder - Demo](https://eln-finder.ulb.tu-darmstadt.de/home) -  Tool to help researchers searching and selecting a suitable ELN thanks to more than 40 filter criteria.
* ELN Filter - Selection of ELNs that are suitable for the life sciences and that can be filtered out according to criteria ([English](https://www.publisso.de/fileadmin/user_upload/PUBLISSO/PUBLISSO_ELN-Filter_2021-06_english.xlsx), [German](https://www.publisso.de/fileadmin/user_upload/PUBLISSO/PUBLISSO_ELN-Filter_2020-12-01.xlsx)).
* ELN Guide - ELNs in the context of research data management and good research practice – a guide for the life sciences ([English](https://dx.doi.org/10.4126/FRL01-006425772), [German](https://dx.doi.org/10.4126/FRL01-006422868)).
* Free consultation sessions to get advice on the selection and introduction of an ELN (<forschungsdaten@zbmed.de>).
* [Video tutorial series](https://www.youtube.com/playlist?list=PLJYlS0FDTMq17tvYMeuI2Ct5XtykRFy0K) (only in German).
* Working groups on ELNs (e.g. in [North Rhine-Westphalia](https://www.fdm.nrw/index.php/fdm-nrw/elb/), Germany).

# References
{% bibliography --cited_in_order %}
