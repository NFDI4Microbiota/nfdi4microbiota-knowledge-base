---
title: Data Organization
category: RDM-Process
layout: default
docs_css: markdown
---

## Motivation

### 5S Methodology
“5S” {% cite Wikipedia:5S %} is a workplace organisation method that uses a list of five Japanese words translated into English as: sort, set in order, shine, standardise and sustain. In the context of organising research data, 'sort' would refer to deleting unnecessary files. 'Set in order' would refer to developing and documenting naming conventions and folder structures. 'Shine' would refer to following conventions and developing routines. 'Standardise' would refer to documenting rules and responsibilities and developing best practices and standard operating procedures (SOPs). And 'sustain' would refer to regularly checking that rules are being followed and making improvements where necessary {% cite assmann_2022 %}.

### Further Resources on the 5S Methodology
* [The 5S Methodology in Research Data Management](https://doi.org/10.5281/zenodo.4494258)
* [5S Data: Setz dich auf deine 5 Buchstaben und organisiere deine Daten! (Coffee Lecture)](https://youtu.be/73XzLsLrwMk)

## File Naming
---

### File Naming Convention

In order to maximise access to your data, to stay organised and to identify your files quickly, files and folders should be named in a meaningful and systematic way {% cite LMA_RDMWG:2024a rehwald_2022 %}. A file naming convention provides a framework for naming your files and/or folders in a way that describes what they contain and how they relate to other files. This framework will help you, your future self, and others in a shared or collaborative group file-sharing environment to navigate your work more easily {% cite LMA_RDMWG:2024a %}. 

Thus, within your research group, we recommend {% cite biernacka:2020 bobrov_2021 bobrov_2021 bres_2022 %} that you:
1. Adopt a naming convention for files and folders.
2. Document your file and folder naming convention.
3. Stay consistent: the naming convention should be chosen in advance to ensure that it can be systematically followed and contains the same information (such as date and time) in the same order (e.g. yyyy-mm-dd) {% cite biernacka:2020 %}.

### Criteria for a Good Naming Convention
Avoid automatically generated names (e.g. from digital cameras) as they can lead to conflicting names due to repetition {% cite biernacka:2020 %}. A good naming convention produces file names that are human-readable, machine-readable, and play well with your system's default ordering {% cite Goldman:2020a %}.
 
### Human-Readability
File names should be descriptive and provide just enough contextual information to establish a link to a particular experiment or data collection {% cite bobrov_2021 LMA_RDMWG:2024a %}. To achieve this, you should choose names that reflect the content and are unique {% cite lindstädt_2019%}.

### Machine-Readability
In some operating systems, long file paths can cause technical problems. Therefore, file names should be as long as necessary and as short as possible to keep them concise and readable on any operating system. It is recommended to limit file names to ≤ 32 characters (32CharactersLooksExactlyLikeThis.txt). Avoid using special characters (e.g. {}[]<>()* % # ' ; " , : ? ! & @ $ ~), umlauts (ä, ö, ü, ß,...) or spaces {% cite biernacka:2020 %}. Periods should only be used before version numbers and file extensions, which should be preserved from the system (e.g. .ERL, .CSV, .TIF) {% cite lindstädt_2019 %}. You can use underscores (_), hyphens (-), or CamelCase instead to make file names both human- and machine-readable {% cite LMA_RDMWG:2024a %}.

### Play Well With Default Ordering
The computer organises files by name, character by character. To browse your files easily, you should choose names that can be sorted alphabetically, numerically or chronologically to ensure that the files appear in a logical order. If you want chronological order, start with a date in ISO 8601 format (YYYY-MM-DD or YYYYMMDD) {% cite Briney:2020 lindstädt_2019 %}. When using sequential numbering, make sure to use leading zeros. For a sequence of 1-10: 01-10 and for a sequence of 1-100: 001-010-100. Scalability should be taken into account (e.g. if a two-digit file number is chosen, the number of files is limited to 99) {% cite biernacka:2020 %}.

Name components that are already part of the folder name do not have to be repeated in the file names {% cite biernacka:2020 %}. Also consider the system under which the file is stored for later access and retrieval of the data.

### Examples of File Names
Below are some examples of file names that are human-readable (if you know the code/abbreviations), machine-readable, and properly sortable {% cite bres_2022 %}:
* 2016-01-04_ProjectA_Ex1Test1_SmithE_v1.0.xlsx
* 2000_USNM_379221_01.tiff
* USNM_379221_01.tiff

Here are some examples of file names that need improvement {% cite bres_2022 %}:
* Test data 2016.xlsx 
* Meeting notes Jan 17.doc
* Notes Eric.txt

### Tools for Simultaneous Renaming of Files

#### Multiple OS
* [Adobe Bridge](https://www.adobe.com/products/bridge.html)
* [jExifToolGUI](https://github.com/hvdwolf/jExifToolGUI/blob/master/README.md)

#### Linux
* [Gnome Commander](https://gcmd.github.io/)
* [GPRename](https://gprename.sourceforge.net/)

#### Mac
* [ExifRenamer](https://www.qdev.de/?location=mac/exifrenamer)
* [NameChanger](https://mrrsoftware.com/namechanger/)
* [Renamer 6](https://renamer.com/)

#### Unix
* mv command

#### Windows
* [Advanced Renamer](https://www.advancedrenamer.com/)
* [Altap Salamander](https://www.altap.cz/)
* [Ant Renamer](http://www.antp.be/software/renamer)
* [Bulk Rename Utility](https://www.bulkrenameutility.co.uk/)
* [ExifToolGUI](https://exiftoolgui.informer.com/)
* [Rename-It!](https://sourceforge.net/projects/renameit/)
* [Total Commander](https://www.ghisler.com/deutsch.htm)
* [WildRename](https://www.cylog.org/utilities/wildrename.jsp)

### Further Resources on File Naming
* [File naming examples](https://doi.org/10.3897/rio.6.e56508) (Table 1)
* Information and steps for creating [naming conventions](https://datamanagement.hms.harvard.edu/plan-design/file-naming-conventions)
* Information about [file naming](https://rdm.elixir-belgium.org/file_naming)
* Information on [File Naming and Folder Hierarchy](https://libraries.mit.edu/data-management/store/organize/)
* Information and examples for [microscopy data](https://www.adelaide.edu.au/microscopy/facilities-services/data-access#how-do-i-organise-my-microscopy-files)
* [File Naming Convention Worksheet](https://doi.org/10.7907/894Q-ZR22)
* [Worksheet for Naming and Organizing Files](https://www.dropbox.com/scl/fi/1zd63iszw33rh4hjcu1dl/Worksheet_fileOrg.docx?rlkey=q0t25t1wttp4qx2p1ne39qfhd&e=1&dl=0)
* [Checklist for FIle Naming Conventions](https://osf.io/dpu45)
* A detailed [documentation of a File Naming Convention](https://www.data.cam.ac.uk/files/gdl_tilsdocnaming_v1_20090612.pdf)

## File Versioning
---
Versioning or version control is the practice of tracking and managing changes to a file or set of files over time so that you can later retrieve specific versions.

We recommend that you meet with project partners to decide how versioning will be carried out, how version changes will be documented, and how a version change will be defined {% cite bres_2022 %}.

### Purpose and Use of Versioning
Versioning helps you to keep a complete long-term change history of each file by tracking, tracing and annotating your steps (i.e. changes made to the file(s)) and also allows you to go back one step. Versioning also allows you to keep multiple versions of each file, and to create new versions of the same file - or even new results - by incorporating new data and/or changes to a file’s structure; this is particularly important in the case of software. Versioning also supports debugging in software. Overall, versioning makes your research easier to understand  {% cite biernacka:2020 bres_2022 Di_Russo:2020 %}. 

### Version Control Methods and Tools
Versioning can be done in the file name (see semantic versioning below), in the data (e.g. in the header or a column for comments), in a text file (e.g. in a README file), or using a version control system (VCS). A VCS is a software tool that helps to manage changes to one or more files over time. Examples of VCSs include Git (e.g. Bitbucket, GitHub, GitLab) and Apache Subversion {% cite Git:n.d. %}. For collaborative document and storage locations (e.g. wiki, Google Docs, cloud), versioning is available in situ {% cite biernacka:2020 %} (i.e. within the document/storage location and in real-time). 

### Apply Versioning Methods
Manual file versioning can be done using [semantic versioning](https://semver.org/). You can do this by adding a "v" to the end of each file name, followed by a maximum of three numbers separated by a period (note that these are the only periods allowed in a file name other than the one before the extension). The first number is called MAJOR and indicates important changes. The second number is called MINOR and indicates less drastic changes. The third number is called PATCH, and is mainly used by software developers to indicate bug fixes, but could also be used when fixing typos. Examples of semantic versioning would look like this {% cite bobrov_2021 bres_2022 %}: Filename_vMAJOR.MINOR.PATCH.FileExtension
* `Ex1Test1_SmithE_v1.0.0.xlsx`
* `Ex1Test1_SmithE_v1.2.5.xlsx`
* `Ex1Test1_SmithE_v2.1.1.xlsx`

If you decide to use manual file versioning, it is recommended that you use a version control table (a version control table template from the University of Sydney Library can be downloaded [here](https://www.library.sydney.edu.au/content/dam/library/documents/support/doc_versioncontrol.docx)). It is also recommended that you assign responsibilities for completing files, store milestone versions, and store obsolete versions separately after backup. How many versions of a file will be kept, which versions (e.g. major versions instead of minor versions (version 2.0 but not 2.1)), for how long, and how the versions will be organised need to be decided in advance {% cite biernacka:2020 %}, ideally with project partners.

## Folder Structure
---
To make it easier to find files, especially if you have a lot of data, you should avoid a chaotic or alphabetical approach to storing data. Instead, a proper folder structure is a hierarchical arrangement in which folders are created to make it easier to find data {% cite biernacka:2020 %}. A typical hierarchical folder structure has a root folder and several levels of subfolders. A carefully planned folder structure, with understandable folder names and an intuitive design, is the foundation of good data organisation. The folder structure provides an overview of what information can be found where, enabling both current and future contributors to understand what files have been produced in the project {% cite Mičetić:n.d. %}.

### General Characteristics of an Efficient Folder Structure

An efficient folder structure allows "someone", perhaps your future self, to look at your files and immediately understand in detail what you have done and why {% cite Goldman:2020b %}. Therefore you should choose a folder structure that is hierarchical, clear, comprehensive, efficient and conclusive {% cite bres_2022 bres_2023 %}. To make it clear and comprehensive for other team members, make sure the structure is self-explanatory and has intuitive navigation {% cite biernacka:2020 bobrov_2021 bres_2022 %}.
Short, meaningful folder names that follow a comprehensive naming convention make browsing a folder structure more efficient {% cite assmann_2022 RDM_Guide:n.d. %}. Sometimes it is a good idea to number the folders to ensure that they work well with the system's default order {% cite assmann_2022 %}. For clarity, the folder structure should be identical on servers and local devices {% cite biernacka:2020 %}.

There is no one-size-fits-all solution: the optimal folder structure depends on the specific project requirements {% cite bres_2023 %}. To make the structure easy to browse, do not make it too deep: use a maximum of 3 to 4 levels {% cite bres_2022 voigt_2022 %}. In addition, if the folders are too large, it is difficult to find the right file in the folder: so limit your folders to a maximum of 10 items per folder {% cite 
bres_2022 %}. 

There are several approaches to building your hierarchy. For some projects, it may be helpful to use a folder structure that follows the different parts or workflow of the project. This can support the step-by-step creation, analysis and publication of data {% cite biernacka:2020 bres_2022 %}. You can also consider basing your hierarchy on functionalities, people involved, date or time period, data types, creation methods or processing steps {% cite bres_2023 %}. Be careful to distinguish between {% cite Schmid:2021 Von_der_Dunk:2021 %}:
* Work _vs._ private material
* Own work _vs._ work of others (papers _vs._ literature)
* Research _vs._ administrative content
* Raw data _vs._ processed data _vs._ final data
* Experiment _vs._ analysis
* Experimental runs/replicates (where appropriate) 

You should avoid using generic "current stuff" folders. Also, be careful about creating researcher-specific folders within a project: folders are about the content, not the authors {% cite Pasquier:2024 %}. If you use researcher-specific folders, external contributors will not be able to understand what data is stored in these folders. Use one folder per dataset, containing data and its description. If you have multiple datasets, the project information can be described in the parent folder {% cite rehwald_2022 %}. 

Make sure you don't have overlapping categories, as you shouldn't have copies of files in different folders, since this can lead to confusion and make it difficult to keep track of different versions of the file {% cite Goldman:2020b %}. If you need to see a file in more than one folder, you can use shortcuts to the file instead. This allows you to keep a single reference file {% cite RDM_Guide:n.d. %}. In particular, make sure you have a 'raw data' folder for each type of data or experiment {% cite RDM_Guide:n.d. %}. It is important to store your raw data separately so that the original versions of the files or their documentation are preserved and the original files can be reconstructed {% cite biernacka:2020 %}.

### Example of Folder Structure
* Project
    * Data
        * Raw_data
        * Processed_data
        * Documentation
    * Code
        * Src
        * Output
            * Plots
        * Documentation
    * Protocols
* Manuscripts
* Conference_reports
* Administrative_information

### Further Resources on Folder Structure
* [Checklist Directory Form](https://osf.io/fp9j5)
* [Worksheet for Naming and Organizing Files and Folders](https://www.dropbox.com/scl/fi/1zd63iszw33rh4hjcu1dl/Worksheet_fileOrg.docx?rlkey=q0t25t1wttp4qx2p1ne39qfhd&e=1&dl=0)
* [Information on File Naming and Folder Hierarchy](https://libraries.mit.edu/data-management/store/organize/)

**Reusable folder structures**
* [GIN-Tonic](https://gin-tonic.netlify.app/standard/)
* [Basic Folder Structure](http://nikola.me/folder_structure.html)
* [Folder Structure generator](https://www.tiesdekok.com/folder-structure-generator/)
* [Template for research repositories](https://doi.org/10.5281/zenodo.4410128)
* [Simple Open Data template](https://doi.org/10.5281/zenodo.4899847)

## Tools
---
* [Data Curation Tool](https://github.com/fair4health/data-curation-tool) (FAIR4Health)
* [FAIRDOM](https://fair-dom.org/news/2021-11-30-covid-community-conference-fairdomhub.html): “Project space [...] used by the community to organize, share and publish data, documents, literature and computational models, as well as to list contributors”
* G-Node Infrastructure ([GIN](https://gin.g-node.org/)) = Modern Research Data Management for Neuroscience (see Notes for more details)

