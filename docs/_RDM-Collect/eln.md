---
title: Electronic Lab Notebooks (ELNs)
category: RDM-Collect
layout: default
docs_css: markdown
hide: false
authors:
    - nkurtys
    - asmith
    - jdoe
---

## Introduction


An Electronic Lab Notebook (ELN) is a software meant for documenting experiments, resulting research data, and processes. In its most basic form, an ELN replicates an interface similar to a page in a physical lab notebook, that allows input via computer or mobile device. More advanced forms often offer other features such as protocol templates, collaboration tools, support for electronic signatures, and the ability to manage the lab inventory. Ultimately, ELNs will replace physical lab notebooks as part of the digital transformation, {% cite kwok_2018 lindstädt_2019 lma_rdmwg vandendorpe:2024 n4m_wc_elns_2023 vieten_2023 %} as it makes sense to document and handle digital data with a digital tool.

## Uses of ELNs

---

ELNs offer features and functions that can pave the way for significant time savings and knowledge transfer in daily laboratory work. For example, ELNs support the annotation of raw data (e.g. with tags or metadata {% cite rathmann_2021 vandendorpe:2024 %}) without having to switch between different media formats. Annotating data makes it searchable, discoverable, traceable and reusable {% cite vandendorpe:2024 %}. ELNs also bring data and their description closer together through embedded multimedia files (e.g. videos of experimental setups), links to shared resources (e.g. chemical databases or analysis software), links to other experiments, as well as direct links to (raw) data sets and analysis workflows {% cite rehwald_2022 %}. ELNs also allow for the versioning of experiment descriptions {% cite rehwald_2022 %} and the structuring and visualisation of workflows and processes {% cite rathmann_2021 %}. ELNs also have the ability to manage inventories of samples, reagents and other supplies, and track equipment and equipment maintenance schedules {% cite lma_rdmwg %}. ELNs also provide for collaboration {% cite lma_rdmwg %} through a common medium {% cite rehwald_2022 %}. Last but not least, ELNs provide for auditing {% cite lma_rdmwg %}, security and safety. Indeed, ELNs are fireproof, waterproof and cannot be lost, misplaced or stolen. ELNs can also be automatically backed up. They allow timestamping (RFC 3161 using DFN-PKI) and finalisation to prevent further changes {% cite rehwald_2022 %}. They also support electronic signatures {% cite cozatl_2021 %} and require access management {% cite rehwald_2022 %}.

## Benefits and Drawbacks

---

### Benefits
* Boosting efficiency of everyday tasks
* Connecting to a digital research environment and integration into your Research Data Management (RDM) strategy
* Complying to the FAIR data principles
* Contributing to Good Research Practice (GRP)

### Drawbacks
ELNs still have some disadvantages compared to physical lab notebooks, as network interruptions can temporarily limit access to data {% cite kwok_2018 %}. In addition, they may lack chronological continuity, formatting flexibility, haptic perception and resistance to liquids (for end devices). Another major drawback appears to be data security risks, especially when used to collect and document sensitive data. The best solution to this is the use of private servers on site or private, institutionally based cloud services {% cite Guerrero2016 %}.

## Ergonomics

---

Several tools and techniques can be used to overcome the difficulties of using a computer when conducting experiments: tablets in the lab, plug-ins (such as voice input and Optical Character Recognition (OCR) plug-ins), linking experiments to raw data files and results, automatic date and time stamping to prove provenance, and integrating ELNs with other research software to capture data and information {% cite lma_rdmwg %}.

## ELNs’ Role in Data Security and Protection

---

Some ELNs can help you keep your data secure by meeting the trustworthiness criteria defined in [FDA 21 CFR Part 11](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application) (USA) and [EU Annex 11](https://www.gmp-compliance.org/guidelines/gmp-guideline/eu-gmp-annex-11-computerised-systems) (EU), including the provision of audit capabilities. ELNs can also provide two-factor authentication and unique credentials. Another way to address data security risks is to use of private servers on site or private, institutionally based cloud services {% cite Guerrero2016 %}. If you are setting up an ELN at your institution, you should also develop a data security plan {% cite lma_rdmwg %}. 
If you intend to collect sensitive data (e.g. sensitive personal data, sensitive environmental data) with the ELN, you should involve your institution's data protection officer (i.e. the person who oversees the application of and compliance with regulations designed to protect important information from corruption, compromise or loss within an organisation {% cite data_protection_officer:2023 crocetti:2021 %}) in the implementation process to ensure compliance with your institution's data protection regulations and the General Data Protection Regulation (GDPR) (i.e. the regulation “on the protection of natural persons with regard to the processing of personal data and on the free movement of such data” {% cite EU:n.d. %}). These regulations may restrict the physical location and transfer of data, excluding the use of cloud-hosted ELNs {% cite kwok_2018 higgins_2022 %}. You can also contact your RDM support team or relevant initiatives (e.g. the National Research Data Infrastructure for Personal Health Data ([NFDI4Health](https://www.nfdi4health.de/en/))) to find out more about anonymisation and pseudonymisation services, as well as your organisation's existing policies and procedures for handling sensitive data and how an ELN might fit into this picture. Ideally, this should be done at the stage of writing your [Data Management Plan (DMP)]({% link _RDM-Plan/dmp.md %}). It is important to note that privacy issues are not addressed by the ELN itself, but rather by how you set it up and store your data {% cite vandendorpe:2024 %}. 

## Selecting an ELN

---

To select an ELN, we recommend that you define selection criteria that reflect the needs of your institution and labs. You can then use these criteria in a matrix to compare them with the features offered by available ELNs {% cite vandendorpe:2024 %}, or enter these criteria into the [ELN Finder](https://eln-finder.ulb.tu-darmstadt.de/home). The ELN Finder is a tool developed together by the University and State Library Darmstadt and the ZB MED - Information Centre for Life Sciences. It is an interactive tool for filtering ELNs based on 40 filter criteria {% cite vandendorpe:2024 %}.

### Important criteria
* **Discipline**
* **Proprietary *vs.* open-source**
* **Software as a Service (SaaS) *vs.* on-premises**
* **Performance and stability**
* **ELN *vs.* LIMS:** ELNs are sometimes confused with Laboratory Information Management Systems (LIMS). They both streamline laboratory workflow and data management and are complementary, but they have different functionalities and features. A LIMS is a comprehensive software for managing and tracking laboratory operations and data. A LIMS covers sample management and tracking, workflow management and automation and quality control throughout the laboratory. On the other hand, an ELN focuses on experimental data acquisition, experiment documentation and (real-time) collaboration {% cite Integrated_software_solutions:2023 Halton:2024 %}.

### Features Based on System Complexity

#### Basic Systems
Basic systems are tools used as ELNs that were not originally designed for this purpose {% cite Dirnagl:2016 %}. They allow traditional text entry, which can be searched and made available on multiple devices via the cloud. They also allow files (e.g. images, spreadsheets) to be attached to text and the attachments to be viewed, annotated and searched. Such systems include Word, Evernote and Dropbox. Basic systems have the advantage of being inexpensive, easily accessible and already familiar to many researchers. However, considerable effort is required to achieve the functionality of a traditional ELN with such a system {% cite vandendorpe_2020 bobrov_2021 %}. They typically do not include any kind of audit trail (i.e. saving all previous versions of a note and logging changes), certification {% cite Dirnagl:2016 %}, or the ability to digitally sign or timestamp entries, with workarounds such as signing exported files required {% cite higgins_2022 %}.

#### Specialised Systems
Specialised systems are ELNs that allow unstructured data entry and offer a wide range of functionalities {% cite Dirnagl:2016 %}. These specialised systems have all the features of basic systems and more; including the ability to integrate original data {% cite Dirnagl:2016 %} and capture freehand and chemical drawings {% cite lma_rdmwg %}. Specialized systems also provide subject-specific features/editors and templates, task allocation between colleagues, complex rights management (i.e. with roles and individual rights) within institutes and workgroups {% cite Dirnagl:2016 %}, basic inventory management (i.e. the ability to manage the quantity and location of samples and reagents) and extensions/APIs for customisation {% cite vandendorpe_2020 bobrov_2021 %}. 

Finally, they comply with the [FDA 21 CFR Part 11](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application). This part requires version control {% cite Dirnagl:2016 %}, full audit trails, electronic signatures on completed records, witnessing and freezing (i.e., making a record immutable after the author and a witness have signed it), and prevents the author from deleting records. Examples of specialised systems: include Arxspan, Biovia, eCat, eLabJournal, eLabFTW, iLabber, Labfolder, and RSpace. 

Specialised systems have the advantage of offering easy entry through free online versions and the ability to install and store data locally. They can also be integrated into your own IT environment via Application Programming Interfaces (APIs) {% cite vandendorpe_2020 bobrov_2021 %}.

#### High-End Systems
High-end systems are ELNs that are offered as a module of a comprehensive laboratory management system {% cite Dirnagl:2016 %}. They have all the features of specialised systems and more. High-end ELNs integrate a LIMS (e.g. IBDS E-WORKBOOK, iLAB Laboratory Execution System) that allows complete tracking of samples and reagents through all experiments. They are also directly linked to laboratory equipment such as microscopes, spectrometers and sequencers. High-end systems provide workflows for specific samples, experiments and tasks. They can automatically provide raw data and metadata (e.g. date of last calibration) from laboratory instruments. Finally, high-end systems allow data mining (i.e. the aggregation and clustering of structured data) and analysis of raw data within the system. Such systems include Hivebench and Limsophy. High-end systems have the advantage of completeness of functionality and all their components fit together seamlessly. However, they can be complex to use and few allow users to use a language other than English (by 2020) {% cite Dirnagl:2016 %}. In addition, they are often cloud-hosted solutions, which means that data control and security remain in the hands of the ELN provider {% cite vandendorpe_2020 bobrov_2021 %}, and that they are more expensive {% cite higgins_2022 %}. They also use proprietary formats, which can increase the risk of vendor lock-in (i.e. making users dependent on the ELN and unable to use their data with another ELN without significant switching costs {% cite vendor_lock_in %}) {% cite vandendorpe_2020 bobrov_2021 %}.


## Implementing the ELN

---

### Steps
To successfully select and maintain an ELN, you must first analyse the current situation and assess your institution's needs. You will then need to define selection criteria against which you will test pre-selected ELNs to choose the one that best meets your needs. Once you have selected an ELN, you need to licence it and then introduce it to your institution's research groups. The introduction phase consists of ensuring that all technical requirements (such as a stable wireless connection) are met, creating and implementing a distribution plan, training users and setting up support services. Finally, you will need to monitor the application {% cite Adam:2021 vandendorpe:2024 %}.

### Timeframe
Testing pre-selected ELNs takes three to six months, depending on when sufficient knowledge of the products’ suitability has been acquired {% cite vandendorpe:2024 %}. Setting up an ELN (especially the inventory functions) initially takes time. However, having an ELN saves time in the long term, e.g. by linking experiments to samples and by managing and ordering supplies {% cite lma_rdmwg %}.

## eLabFTW

---

eLabFTW is a free and open-source {% cite rathmann_2021 %} ELN developed by Deltablot (France) {% cite cozatl_2021 %}. eLabFTW is a web-based application that runs on all major operating systems. It can be used in research and teaching (e.g. for laboratory exercises) {% cite cozatl_2021 %}. In addition to a search function {% cite rathmann_2021 %} and the ability to take notes, eLabFTW allows you to create experiments and collections of experiments {% cite cozatl_2021 %}, log work steps, document data and results {% cite rathmann_2021 %} with metadata, and create a database for a variety of objects (e.g. lab materials, lab equipment). It is also a good collaborative tool with which you can manage the lab {% cite cozatl_2021 %}. eLabFTW will also help you comply with GRP as it prevents data deletion and provides immutability through timestamps {% cite rathmann_2021 %}. Being open source, it is freely modifiable and highly customisable. It also benefits from community development, by scientists for scientists  {% cite cozatl_2021 %}. Its interface has been translated into 17 languages as of June 2024 {% cite Carpi:2021 %}. To see what it looks like, watch this [video tutorial]((https://www.youtube.com/playlist?list=PLJYlS0FDTMq17tvYMeuI2Ct5XtykRFy0K)) with eLabFTW and Labfolder from ZB MED on YouTube.

## Resources

---

* [ELN Material Collection](https://elb-materialsammlung.gitlab.io/sammlung/)


* **Best practice examples** (see in {% cite Adam:2021 %})
    * ETH Zürich with openBIS
    * NFDI4Chem with Chemotion
    * University Medicine Göttingen with RSpace
    * University of Edinburgh with RSpace


* **Consortium:** [The ELN Consortium](https://github.com/TheELNConsortium)


* **ELN comparison matrix:** the ELN comparison matrix was created by the Longwood Medical Area Research Data Management Working Group (LMA RDMWG) in 2018, with the last snapshot taken on 2021-04-19. The aim of this matrix is to help researchers identify practical ELN tools to meet their specific needs. It covers 33 ELNs and was compiled through a survey sent to 26 ELN vendors. It is aimed at researchers in the LMA biomedical research community, other researchers and librarians {% cite lma_rdmwg %}.


* **ELN Finder:** the ELN Finder is a tool developed together by the University and State Library Darmstadt and the ZB MED - Information Centre for Life Sciences. It is an interactive tool for filtering ELNs based on 40 filter criteria {% cite vandendorpe:2024 %}.


* **Guides**
    * [Labfolder guide](https://labfolder.com/electronic-lab-notebook-eln-research-guide/)
    * [SciNote guide](https://www.scinote.net/blog/electronic-lab-notebook-guide/)
    * [Uncountable guide](https://www.uncountable.com/try/free-guide-electronic-laboratory-notebooks-eln-guide)
    * [University of Cambridge guide](https://www.data.cam.ac.uk/data-management-guide/electronic-research-notebooks)
    * ZB MED guide {% cite Adam:2021 %}: the ZB MED ELN Guide is intended to help researchers and information infrastructures choose an ELN. It also contains useful references and is available in both English and German.


* **Mailing lists**
    * [Elabnotebook](https://listserv.gwdg.de/mailman/listinfo/elabnotebook)
    * [German Research Network](eln@listserv.dfn.de)
    * [UK Education and Research communities](https://www.jiscmail.ac.uk/cgi-bin/webadmin?A0=RESEARCHNOTEBOOKS)


* **Network:** [Research Data Alliance (RDA) - Research Data Architectures in Research Institutions IG](https://www.rd-alliance.org/groups/research-data-architectures-research-institutions-ig/members/all-members/)


* **Working groups**
    * [ELB.nrw](https://wiki.hhu.de/display/ELB/ELB.nrw+Startseite)
    * National Research Data Infrastructure (NFDI) working group on ELN
    * [Ouvrir la science - Cahiers de laboratoire électroniques](https://www.ouvrirlascience.fr/cahiers-de-laboratoire-electroniques/)


It is also advisable to talk to other members of your research community to find out about their experiences with ELNs (e.g. advantages and disadvantages of different tools, selection process).


If you have any further questions about the management and analysis of your microbial research data, please contact us: [helpdesk@nfdi4microbiota.de](mailto:helpdesk@nfdi4microbiota.de) (by emailing us you agree to the privacy policy on our website: [Contact](https://nfdi4microbiota.de/contact-form.html))

