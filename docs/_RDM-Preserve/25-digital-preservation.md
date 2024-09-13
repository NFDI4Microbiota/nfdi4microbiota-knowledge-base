---
title: Digital Preservation
category: RDM-Preserve
layout: default
docs_css: markdown
---

## Definition
Digital preservation means taking certain measures to ensure that digital material can be found and can be accessed in the long term ("long-term accessibility of data"). It aims to preserve information in a way that is understandable and reusable for a specific community and to prove its authenticity. 

## Digital preservation for researchers
The sustainable handling of data by researchers naturally facilitates the long-term accessibility of data. Best practice methods are:
* Cleaning data / data structures - see also: [Data Organisation](https://knowledgebase.nfdi4microbiota.de/RDM-Process/14-data-organization.html)
* Validating data - see also: [Data Quality Control](https://knowledgebase.nfdi4microbiota.de/RDM-Collect/13-data-qc.html)
* Documenting data with metadata and context information to ensure reusability: commenting, adding descriptive, administrative and technical metadata, asigning user license.
* Using well-known open file formats during the project phase - see below - or transfering data into reusable file formats (needs documenting: original file or derivative)
* Storing data following the 3-2-1 rule:
    * Keeping 3 copies of any important file
    * Storing files on 2 different media types
    * Keeping at least 1 copy off site.

### Data selection
To decide well-founded on data selection we recommend reading the how-to guide of the Edinburgh Digital Curation Centre {% cite dcc_five_2014 %}. The suggested steps are:
* **Step 1:** Identify purposes that the data could fulfill: consider the purpose or ‘reuse case’ of your data, including reuse outside your research group.
* **Step 2:** Identify data that **must** be kept: consider legal or policy compliance risks, as well as funder requirements. 
* **Step 3:** Identify data that **should** be kept: as it may have long-term value. 
* **Step 4:** Weigh up the costs and identify any need for external advice in case of shortfall in the budget. 
* **Step 5:** Complete the data appraisal, i.e. list what data must, should or could be kept to fulfill which potential reuse purposes. Summarize any actions needed to prepare the data for deposit - or justification for not keeping it.


### Recommended file formats for preservation
Making your research available in recommended file formats additional to the original software format supports highly the reusability and long-term accessibility of your data.
Attributes of those file formats are: 
* Open rather than proprietary (examples for [open files formats](https://en.wikipedia.org/wiki/List_of_open_file_formats))
* Well-documented
* In widespread use
* Simple (e.g. csv rather than xlsx)
* Text-based (i.e. any file you can open with a text editor and read) rather than binary (e.g. txt files rather than doc files)
* Exportable to / unpackable into an open format (e.g. xlsx, docx, etc. can be unpacked into folders of xml files)
* Machine-readable
  
For biomaterial data, recommended formats are CSV, TXT and XML.

## Digital preservation for repository operators

Specific preservation measures depend on the digital objects, needs of the user community, and various other conditions. Repositories usually contain publications as files, making file format identification and validation relevant.

### Bitstream preservation
Preservation on the bitstream level is the basis for digital preservation. It covers e. g.
* Checking checksums of transferred files upon receiving them (or generating file checksums) and conducting regular fixity checks
* Redundant storage of data
* Generating backups (e. g. offline backups of the underlying repository database)
* Strategies for updating storage media (according to e. g. server lifetime)
  
### Preservation beyond bitstream
Preservation of file content, being able to open and render it correctly in a software is part of logical {% cite lindlar_2020_3672773 %} or technical preservation, also called digital curation. Semantic preservation is concerned with e. g. semantic drift impacting metadata. 
* Obtaining sufficient rights allowing e. g. format migrations, file repairs and re-use over the long-term like re-publication in other infrastructures
* File format identification, based format-specific bit patterns, e. g. via [DROID](https://coptr.digipres.org/index.php/DROID) during publication process
* File format validation, based on format specifications, e. g. using XML validators during publication process (for validators see also [COPTR](https://coptr.digipres.org/index.php/Validation))
* Automated extraction of technical metadata from files (see also [COPTR](https://coptr.digipres.org/index.php/Metadata_Extraction))
* Virus scans
* Replacing files with problems (e. g. invalid files) as early as possible
* Obtaining sufficient metadata
   * storing unique file identifiers, machine-readable version information and relations between files
   * indexing rights information in a machine usable way
   * indexing of identification-, validation-, metadata extraction- and virus check-output 
   * preserving and updating of descriptive metadata, according to user community needs
* Migrating at-risk files, e. g. files with obsolete formats (see also [migration tools]( https://coptr.digipres.org/index.php/File_Format_Migration))
* Providing versioning of files and publications and possibility to rollback to earlier versions
  
Many digital preservation criteria applying to repositories are also present in the certification criteria of the CoreTrustSeal and the nestor seal {% cite coretrustseal_standards_and_certificatio_2022_7051012 harmsen_henk_explanatory_2013 %}.

## Get Help
If you have any further questions about the management and analysis of your microbial research data, please contact us: [helpdesk@nfdi4microbiota.de](mailto:helpdesk@nfdi4microbiota.de) (by emailing us you agree to the privacy policy on our website: [Contact](https://nfdi4microbiota.de/contact-form/))

## References
{% bibliography --cited_in_order %}


