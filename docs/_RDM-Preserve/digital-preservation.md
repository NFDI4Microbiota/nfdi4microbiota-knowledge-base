---
title: Digital Preservation
category: RDM-Preserve
layout: default
docs_css: markdown
---

## Definition of Digital Preservation

Digital preservation (DP) means taking certain measures to ensure that digital material can be found and accessed in the long term (“long-term accessibility of data”). It aims to preserve information in a way that is understandable and reusable for a specific community and to prove its authenticity. {% cite CCSDS_OAIS:2012 noauthor_iso_OAIS_2012 dpc_glossary_2015 %}. 

The long-term timeframe starts now and lasts long as necessary. It may extend into an indefinite future, where there are usually concerns about changing technologies, storage media, obsolete data formats or standards (Definition "Long Term" {% cite CCSDS_OAIS:2012 %}).

## Digital Preservation During Research

Sustainable handling of data naturally facilitates the long-term accessibility of the data. 
Best practice methods are:
* Naming, versioning and data structures, etc. - see also: [Data Organisation](https://knowledgebase.nfdi4microbiota.de/RDM-Process/14-data-organization.html)
* Documenting data with metadata and context information to ensure reusability: commenting, adding descriptive, administrative and technical metadata, assigning user license. – see also: [Metadata and Metadata standards](https://knowledgebase.nfdi4microbiota.de/Research-Data-Management/03-md.html)
* Using well-known open file formats during the project phase - see below - or converting data into reusable file formats (needs documenting: original file or converted file)
* Storing data in compliance with the 3-2-1 rule: 
   * Keep 3 copies of any important file
   * Store files on 2 different types of data carriers 
   * Keep at least 1 copy off-site.

### Data Selection

To make well-founded decisions regarding data selection the suggested steps are:

* **Step 1:** Identify data that **must** and **can** be kept: consider legal or policy compliance risks, as well as funder requirements.
* **Step 2:** Identify data that **should** be kept: data which was expensive to generate, which is impossible to reproduce, particularly curated data and/or data which supports research findings in papers.
* **Step 3:** Weigh up the **costs** and identify any need for external advice in case of shortfall in the budget.
* **Step 4:** Identify **purposes** that the data could fulfill: consider the purpose or ‘reuse case’ of your data, including reuse outside your research group.
* **Step 5:** Complete the data **appraisal**, i.e. list what data must, should or could be kept to fulfill which potential reuse purposes. Summarize any actions needed to prepare the data for deposit - or justification for not keeping it. - see also: Digital preservation in [Data Management Plans (DMPs)](https://knowledgebase.nfdi4microbiota.de/RDM-Plan/dmp.html#digital-preservation-in-dmps) 


See also: How-to guide of the Edinburgh Digital Curation Centre {% cite dcc_five_2014 %}.

### File Format Recommendation
Saving and publishing your research in recommended file formats in addition to the original format supports the reusability and long-term accessibility of your data. 


Attributes of those file formats are: 
* Open rather than proprietary (examples for [open files formats](https://en.wikipedia.org/wiki/List_of_open_file_formats))
* Well-documented (e. g. the format specifications have been published as ISO-standard)
* In widespread use
* Simple (e.g. csv rather than xlsx)
* Text-based (i.e. any file you can open with a text editor and read) rather than binary (e.g. txt files rather than doc files)
* Can be exported into an open format (e.g. xlsx, docx, etc. can be unpacked into folders of xml files)
* Machine-readable
  
For biomaterial data, recommended formats are CSV, TXT and XML.

## Digital Preservation in Labs

Depending on the project, institution and funding guidelines, the time at which the data of a research project is transferred to a local data centre for final documentation or to a repository, e.g. for publication, varies. Until then, preparing and setting up long-term archiving in your lab or on-site facility is an effort that will undoubtedly contribute to the sustainability of your research.
The following section is intended to provide a basic understanding of the possible measures:
* Determine responsibilities
   * Define who will be responsible for the data of your organization/research project in the long-term. Determine handover scenarios in the event that the person leaves.
   * Define possible risks of data loss and which follow-up measures should be taken - even after the project has been completed. 
   * Decide on a technical support, which hardware and software is required and who will provide the resources. - see also: [Data Management Plans (DMP)](https://nfdi4microbiota.github.io/nfdi4microbiota-knowledge-base/RDM-Plan/dmp.html#content-of-dmps)
* Determine who should be able to find and access the data.
   * How will these persons be made aware of the existence of relevant data in this location? How can they can search for specific projects or files?
   * Set up a website, an index or a database with required metadata and ensure that necessary metadata is entered.
* Formulate your own criteria for selecting the data that you want to and can preserve. 
   * The criteria should be available to all researchers involved. - see above: “Data Selection”
* Determine how long data should be kept. 
   * Set up a system that informs the person(s) responsible that the data can be deleted - unless this has not been specified for an indefinite period.
* Define the necessary rights for data storage, active data preservation and, if applicable, deletion.
   * In the event that the rights need to be transferred to another person at some point, the necessary procedures and documentation must be set up.
   * If the rights for folders, files, database entries or similar differ among your preserved data, document these with the data and make this documentation machine-readable.
* Determine the level of digital preservation 
   * **DP at Bitstream level:** This is the basis for being able to preserve digital objects and control changes at all.
      * Check that files must not be encrypted, password-protected or protected against printing or copying of content. 
      * Check that files are virus-free
      * Generate and check the checksums of files if transferred or on receipt, document them and conduct regular fixity checks so it is noticeable if files are no longer intact
      * Store data redundantly - see above: [3-2-1 rule](https://knowledgebase.nfdi4microbiota.de/RDM-Preserve/25-digital-preservation.html#digital-preservation-for-researchers) 
      * Develop strategies for monitoring and updating storage media (e.g. according to the technical lifespan)
      * Perform control, logging and versioning of any changes
   * **DP at Content preservation level:** This is generally understood to cover the combination of technical-logical and semantic preservation in order to understand for what the data is intended and how it is organized technically. {% cite markus_long-term_2024 lindlar_2020_3672773 %}. 
      * Check whether manuals (readme, codebook, data dictionary..) are available, e.g. to describe the software used or the structure of the data 
      * Describe your data with sufficient metadata (incl. information about versions, other publications, relationships between files) that support the FAIR principles and store it with your data, e.g. in a database
      * Check whether codes and scripts are prepared according to coding best practices.
      * Decide in favour of granting sufficient rights to enable technical maintenance measures (file repairs, file format migrations, ...)
      * Check whether availble software can open the file and render the file contents correctly 
      * Make sure the file format matches the file extension – even if software can render the file with the mismatch. Try tools - see also: [COPTR file format identification tools](https://coptr.digipres.org/index.php/File_Format_Identification), specifically [DROID](https://coptr.digipres.org/index.php/DROID)
      * Check if the files conform to their format specifications (e. g. well-formed and valid XML-file). Try tools - see also: [COPTR validators](https://coptr.digipres.org/index.php/Validation)
      * Replace files with problems and document all changes made to the digital object as part of the curative process.
      * Document all versions of files with the option to revert to previous versions if required
  
## Digital Preservation for Repository Operators

Repositories usually contain publications in the form of files and are dependent on the quality of submission. Similar to digital preservation in laboratories, digital preservation in repositories depends on sustainable organisational and technical capabilities to prevent technical and semantic obsolescence. In addition, repositories have a particular responsibility to provide published research data and their metadata in a machine readable and usable way that meet the needs of their user community. - see also: [FAIR-principles](https://nfdi4microbiota.github.io/nfdi4microbiota-knowledge-base/Research-Data-Management/04-fair.html).  However, the deliberate design of the metadata schema and the repository's publication policy may impose specific requirements for the acceptance of the digital object. Digital Preservation may add additional data quality processes.


Most measures mentioned in the section “DP for labs” are just as essential for repositories (see above). 
Additionally, some workflows and tools beneficial for repository operators are listed below: 

* Check all mandatory metadata and encourage further comprehensive description - also for files
* Extract technical metadata from files automatically (see also: [COPTR metadata extraction tools](https://coptr.digipres.org/index.php/Metadata_Extraction)
* Specify who is responsible if files or file content are at risk, including responsibility for follow-up measures if problems occur at a later date. It can be very helpful not to lose contact with the depositor, e. g. researcher. 
* Encourage your users to inform you about publications in your repository that cannot be used
* Replace files with problems (e.g. invalid files) as early as possible, e.g. migrate obsolete file formats to sustainable formats. - see also: [COPTR migration tools](https://coptr.digipres.org/index.php/File_Format_Migration).  
* Document all technical changes made to the digital object and ensure that versioning is activated so that you can revert to previous versions if necessary.

  
Many of the criteria for digital preservation that apply to repositories can also be found in certification such as CoreTrustSeal and the nestor seal {% cite coretrustseal_standards_and_certificatio_2022_7051012 harmsen_henk_explanatory_2013 %}. Taking certification material into account is a good idea in any case, even if certification is not or not yet an issue. Research funders increasingly recommend publication of research data in certified repositories.



