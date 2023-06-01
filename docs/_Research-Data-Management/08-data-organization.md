---
title: Data Organization
category: Research-Data-Management
layout: default
docs_css: markdown
---
## Introduction
For data organization, we suggest to use the 5S methodology that uses a list of five words {% cite assmann_2022 %}:
1. **Sort**: delete unnecessary files.
2. **Set in order**: develop and document naming conventions and folder structures.
3. **Shine**:
    * Comply with conventions.
    * Develop routines.
4. **Standardize**:
    * Document rules and responsibilities.
    * Develop best practices and Standard Operating Procedures (SOPs).
5. **Sustain**:
    * Regularly check whether rules are followed.
    * Implement improvements if necessary.

## File naming
File names should ideally allow to establish a connection to a certain experiment or data collection {% cite bobrov_2021 %}. Within your research group, it is recommended {% cite bobrov_2021 bres_2022 %} to:
1. **Choose** a file and folder naming convention.
2. **Document** your convention, for instance in Standard Operating Procedures (SOPs).
3. Make the documentation **available** to all research group members.
4. Stay **consistent**.

### Recommendations for naming conventions
If you need to choose a file and folder naming convention, it is recommended {% cite assmann_2022 bobrov_2021 bres_2022 %} to include the following:
* Favor **alphabetically sortable** names (e.g. starting with the date: YYYY-MM-DD).
* Limit file names to **maximum 32 characters** (32CharactersLooksExactlyLikeThis.txt). Short names are easier to find and they need a shorter path, whereas long names can cause technical problems. Thus, select a name that is as short as possible and as long as necessary.
* Favor names that **reflect** and are **unique** to the **content** (i.e. person, project ID/part, sample ID, experiment ID, status, data, version number and/or software name).
* Use **periods** only before file extensions.
* Do not use **special characters** or **whitespaces** which can be confusing to both machines and humans.
* Use **leading zeros** when using sequential numbering:
    * For a sequence of 1-10: 01-10
    * For a sequence of 1-100: 001-010-100

### Examples of file names
* **Good structure**: YYYY-MM-DD_JV_ProjectID_ExperimentID with IDs being linked to a table with data documentation such as metadata {% cite bobrov_2021 %}.
* **Good names** {% cite bres_2022 %}:
    * 2016-01-04_ProjectA_Ex1Test1_SmithE_v1.0.xlsx
    * 2000_USNM_379221_01_tiff
    * USNM_379221_01.tiff
* **Bad names** {% cite bres_2022 %}:
    * Test data 2016.xlsx
    * Meeting notes Jan 17
    * Notes Eric.txt
    * Final FINAL last version.docx

### Tools for simultaneous renaming of files

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

## File versioning

## Folder structure

## Further resources

### 5S methodology
* Lang, K., Roman, G., Jessica, R., Annett, S., Nadine, N., & Lehmann, A. (2021). The 5S Methodology in Research Data Management. Zenodo. [https://doi.org/10.5281/ZENODO.4494258](https://doi.org/10.5281/ZENODO.4494258)
* ["*5S Data: Setz dich auf deine 5 Buchstaben und organisiere deine Daten! (Coffee Lecture)*"](https://youtu.be/73XzLsLrwMk) (in German only)

### Organizing data in spreadsheets
* Broman, K. W., & Woo, K. H. (2018). Data Organization in Spreadsheets. In The American Statistician (Vol. 72, Issue 1, pp. 2–10). Informa UK Limited. [https://doi.org/10.1080/00031305.2017.1375989](https://doi.org/10.1080/00031305.2017.1375989)
* Perkel, J. M. (2022). Six tips for better spreadsheets. In Nature (Vol. 608, Issue 7921, pp. 229–230). Springer Science and Business Media LLC. [https://doi.org/10.1038/d41586-022-02076-1](https://doi.org/10.1038/d41586-022-02076-1)
* [Tidy data for librarians](https://librarycarpentry.org/lc-spreadsheets/)

### Tools
* [FAIR4Health Data Curation Tool](https://github.com/fair4health/data-curation-tool)
* G-Node Infrastructure ([GIN](https://gin.g-node.org/)) = Modern Research Data Management for Neuroscience

## References
{% bibliography --cited_in_order %}
