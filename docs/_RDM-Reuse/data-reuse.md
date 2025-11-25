---
title: Data Reuse
category: Research-Data-Management
layout: default
docs_css: markdown
redirect_from: /Research-Data-Management
authors:
   - jvandendorpe
   - nacnoriko
---

## Data Discovery

### Strategies to Search for Data

The Consortium of European Social Science Data Archives (CESSDA) {% cite cessda_2017 %} has produced a list of steps in data discovery. The main ones are outlined below, and you can look at their [website](https://dmeg.cessda.eu/) for the sub-steps.
1. Develop a clear picture of the research data you need
2. Locate appropriate data resources
3. Set up a search query and search the data resource
4. Select data candidates
5. Evaluate data quality

CESSDA also suggests three steps to adjust your search strategy {% cite cessda_2017 %}:
1. Use appropriate words in appropriate fields
2. Broaden your scope
3. Narrow your scope

Other tips and tricks from the [Center for Open Science 2023](https://mailchi.mp/osf/osf-tips-mar-1386252?e=38c1d6ec62) include citation chaining (i.e. the process of mining citations in relevant literature to find more sources), looking at previous reuse, and documenting your search strategy to avoid repetition in one repository while helping you to replicate the same strategies in other data. To properly document your search strategy, keep a record of the terms used, filters, other refinements, dates and repositories searched.

### Services to Search for Data

#### Resources to Facilitate Data Reuse in Microbiology
Below are listed widely used resources in microbiology that facilitate the reuse of raw data found in the [data repositories section above]({% link _RDM-Share/data-repositories.md %}#well-established-repositories-for-data-deposition-in-microbiology). These so-called "secondary databases" provided added value through additional data types for example as reference databases or from data integration. For each resource and when available, the FAIRsharing and re3data pages are linked. On the FAIRsharing page, you will find information such as which journals endorse the resource (under "Collections & Recommendations" and then "In Policies"). On the re3data page, you will find information such as the above-mentioned criteria to select a trusted resource. DB = database.

| Domain, Data Type| Resource | FAIRsharing | re3data | 
|---|---|---|---|
| **Viruses, Knowledge resources** | [ViralZone](https://viralzone.expasy.org/) | [FAIRsharing](https://fairsharing.org/FAIRsharing.tppk10) | [re3data](https://www.re3data.org/repository/r3d100013314) |
|     | International Committee for the Taxonomy of Viruses [ICTV](https://ictv.global/) | - | - |
| **Viruses, Virus-host databases** | [Virus-HostDB](https://www.genome.jp/virushostdb) | - | - |
|     | Viral Host-Range DB [VHRDB](https://viralhostrangedb.pasteur.cloud/) | [FAIRsharing](https://fairsharing.org/FAIRsharing.7a4bbd) | - |
| **Viruses, Sequence analysis platforms** | [NCBI Virus](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/) | [FAIRsharing](https://fairsharing.org/FAIRsharing.d38075) | - |
|     | [BV-BRC](https://www.bv-brc.org/) | [FAIRsharing](https://fairsharing.org/FAIRsharing.2ea3ef) | [re3data](https://www.re3data.org/repository/r3d100014100) |
| **Viruses, Nucleic acid sequence downloads** | [RVDB](https://rvdb.dbi.udel.edu/) | - | - |
|     | ([inphared](https://github.com/RyanCook94/inphared)) | -| - |
| **Viruses, macromolecular structures** | [VIPERdb](https://viperdb.org/) | [FAIRsharing](https://fairsharing.org/FAIRsharing.45e0f5) | [re3data](https://www.re3data.org/repository/r3d100012362) |
| **Viruses, Protein sequences** | Virus Orthologous Groups ([VOGdb](https://vogdb.org/)) | - | - |
|    | Phage Orthologous Groups ([PHROGs](https://phrogs.lmge.uca.fr/index.php)) | - | - |
| **Viruses, -omics data sets** | [IMG/VR](https://img.jgi.doe.gov/cgi-bin/vr/main.cgi) | [FAIRsharing](https://fairsharing.org/FAIRsharing.2KIa7T) | - |
|  | Multi-Omics Portal of Virus Infection ([MVIP](https://mvip.whu.edu.cn/)) | - | - |
| **All, Protein sequences and families** | [InterPro](https://www.ebi.ac.uk/interpro/) | [FAIRsharing](https://fairsharing.org/FAIRsharing.pda11d) | [re3data](https://www.re3data.org/repository/r3d100010798) |
|  | [UniProt](https://www.ebi.ac.uk/uniprot/) | [FAIRsharing](https://fairsharing.org/FAIRsharing.fd6003) | [re3data](https://www.re3data.org/repository/r3d100010357) |
{: .table .table-hover}


#### Service and Resource Catalogs
ELIXIR service catalogue: [https://elixir-europe.org/services](https://elixir-europe.org/services) 
EMBL services: [https://www.ebi.ac.uk/services](https://www.ebi.ac.uk/services) (NFDI4Microbiota member)
deNBI services: [https://www.denbi.de/categories](https://www.denbi.de/categories) (NFDI4Microbiota member)
Digital Diversity DSMZ catalogue: [https://hub.dsmz.de](https://hub.dsmz.de) (NFDI4Microbiota member)


#### Services Where Data Can Be Published

* **Interdisciplinary and [discipline-specific]({% link _RDM-Share/data-repositories.md %}#well-established-repositories-for-data-deposition-in-microbiology) repositories**
* **Data reports**
* **Data journals** (see e.g. [here](https://www.forschungsdaten.org/index.php/Data_Journals))

#### Registries of Data Repositories

* Registry of Research Data Repositories ([re3data.org](https://www.re3data.org/))
* [OpenAIRE Explore](https://explore.openaire.eu/)
* [OpenDOAR](https://v2.sherpa.ac.uk/opendoar/)
* [FAIRsharing.org](https://fairsharing.org/)
* [Master Data Repository List](https://clarivate.com/webofsciencegroup/master-data-repository-list/)

#### Search Engines

* [NCBI Data sets](https://www.ncbi.nlm.nih.gov/datasets/)
* **Google**
    * [Data set Search](https://datasetsearch.research.google.com/)
    * Keyword + "data set"
* **Library search engines**
    * Bielefeld Academic Search Engine ([BASE](https://www.base-search.net/))
    * [LIVIVO – The Search Portal for Life Sciences](https://www.livivo.de/app)
* **Discipline-specific search engines**
    * Bacterial and Viral Bioinformatics Resource Center ([BV-BRC](https://www.bv-brc.org/))
    * [NFDI4Chem Search](https://search.nfdi4chem.de/)
    * [Study Hub NFDI4Health COVID-19](https://csh.nfdi4health.de/)
    * [TerrestrialMetagenomeDB](https://webapp.ufz.de/tmdb/)
* [Mendeley Data](https://data.mendeley.com/)

#### (Meta)Data Aggregators

* [B2FIND](https://b2find.eudat.eu/)
* [data.europa.eu](https://data.europa.eu/en)
* [DataCite Commons](https://commons.datacite.org/)
* [gesisDataSearch](https://datasearch.gesis.org/start)

## Data Selection
---

Below is a list of criteria for selecting trustworthy data sets {% cite bres_2022 sielemann_2020 %}. As in Sielemann *et al.* 2020 {% cite sielemann_2020 %}, for each possible criterion, several questions to consider are listed.

* **Integrity of the source**
    * Is the source/submitter associated with data fabrication/plagiarism?
    * Is the way missing values are handled documented?
 
* **Biases**
    * How was the data generated?
    * Is the data generation clearly and precisely documented?
  
* **Missing meta information (sparsity)**
    * Do you have all the relevant information?
    * Is the information understandable and consistent?
    
* **Integration of data sets from different sources**
    * Is the data comparable?
    * Are the methods used for data generation and analysis well-documented and comparable?
    
* **Quality issues**
    * Is the quality high enough to reach your goals?
    * Are there any scores/hints available to check the quality of the data set?
    
* **Copyright/Legal issues**
    * Are there any restrictions for the reuse and publication of the data, especially due to the [Nagoya protocol](https://www.cbd.int/abs/)?
   
* **Further documentation**
    * Is the research purpose/(hypo-)thesis well documented?
    * Is it documented whether the data are raw or processed? 

## Data Provenance
---
The provenance of research data can be defined as “a documented trail that accounts for the origin of a piece of data and where it has moved from to where it is presently” {% cite National_Library_of_Medicine:2022 %}. As suggested by Schröder et al. 2022, it can be accounted for by answering questions based on the W7 provenance model {% cite Schroder:2022 %}:
* W1: Who participated in the study? [List of all researchers involved in an experiment and their affiliations]
* W2: Which biological and chemical resources and which equipment was used in the study? [Resources and the equipment used in an experiment including all details such as the lot number and the passage information]
* W3: How was a particular file created? [Sequence of activities that led to the creation of a particular file]
* W4: When was an activity conducted? [Date and time point of a particular activity, its duration]
* W5: Why was the experiment done? [Objective]
* W6: Where was the experiment conducted? [Institution where the experiments was conducted]
* W7: What was the order of the stimulation parameters in a particular experiment?

## Data Reuse
---

### Benefits and Drawbacks

Making data reusable benefits researchers who publish their data, researchers who reuse data, and society. 

Researchers who publish their data see an increase in their scientific reputation, citations, and collaborations {% cite rehwald_2022 pauls_2023 %}. In addition, researchers who publish their data not only comply with the [FAIR Data Principles]({% link _Research-Data-Management/fair.md %}), but also avoid bias in the body of evidence {% cite IOM_2015 %}, increase transparency and thus trust in research {% cite engelhardt_2022 rehwald_2022 pauls_2023 %}. Finally, by sharing their resources and perspectives, researchers who publish their data enable other researchers to build on their work, accelerating scientific discovery {% cite engelhardt_2022 IOM_2015 rehwald_2022 %}.

Researchers can recycle unique data by performing secondary analyses to answer new research questions and/or with new methods {% cite rehwald_2022 pauls_2023 %}. Reusing data in this way saves resources such as time, energy, and money {% cite engelhardt_2022 FSD rehwald_2022 pauls_2023 %}. Data reuse also increases collaboration and, over time, enables the comparison of different samples {% cite rehwald_2022 pauls_2023 %}. Indeed, data reuse is essential for interdisciplinary experiments and cross-cutting research approaches {% cite pavone_2020 %}.

Making data reusable can also benefit society. It reduces unnecessary experimentation {% cite rehwald_2022 %}, avoids duplication of data collection, and minimizes collection from hard-to-reach, vulnerable or over-researched populations {% cite FSD rehwald_2022 %}. It also enables replication and thus promotes reproducibility. Finally, it benefits teaching and improves the link between academia and industry {% cite rehwald_2022 %}.

As suggested by Sielemann *et al.* 2020 {% cite sielemann_2020 %}, there are also challenges, limitations, and risks associated with data reuse.

For researchers who publish their data, preparing data sets for reuse is time-consuming. 

For researchers reusing data, there are risks such as unknown quality and normalization (i.e. "the same data is stored multiple times in the same database under different names/identifiers"). There is also the challenge of comparing and integrating data sets from different sources {% cite sielemann_2020 %}.


### Successful Cases of Data Reuse

#### Case 1: FishBase {% cite pavone_2020 %}
Various [data sources](https://web.archive.org/web/20111008223552/http://ichthyology.bio.auth.gr/files/tsikliras/d/d3.pdf) have been combined into a digital catalog of fish, known as [FishBase](https://www.fishbase.us/). The data in FishBase were processed using a new algorithm to create a [new dataset](https://thredds.d4science.org/thredds/catalog/public/netcdf/AquaMaps_08_2016/catalog.html). This new dataset was combined with other data to create [AquaMaps](https://www.aquamaps.org/), a tool for predicting the natural occurrence of marine species based on environmental parameters. This led to an increase in citations of FishBase (e.g. [Coro _et al._ 2018](https://doi.org/10.1016/j.ecolmodel.2018.01.007)) and a [report](https://europe.oceana.org/en/our-work/froese-report/overview) on EU fish stocks,the evidence for which was debated in the European Parliament in 2017. In addition, climate change predictions from AquaMaps and NASA were merged to create a [climate change timeline](https://dlnarratives.eu/timeline/climate.html). 

#### Case 2: TerrestrialMetagenomeDB
[TerrestrialMetagenomeDB](https://web.app.ufz.de/tmdb/) is a public repository of curated and standardized metadata for terrestrial metagenomes. 

#### Further Cases in Microbiology
See [Sielemann *et al.* 2020](https://doi.org/10.7717/peerj.9954).

### Relevant Licenses and Terms of Use
See [Licenses]({% link _RDM-Share/licenses.md %}).

## Data citation
---

### Common Standards for Data Citation

#### Interdisciplinary
* **DataCite 2019**: Creator (PublicationYear): Title. Version. Publisher. (resourceTypeGeneral). Identifier
* **FORCE 11**: Author(s), Year, Data set title, Data repository or archive, Version, Global persistent identifier (preferably as a link)
* [BibGuru](https://app.bibguru.com/p/3420f069-22ea-42f6-ba23-4bc6b8ae37e4)
* [DOI Citation Formatter](https://citation.crosscite.org/)
* [How to Cite Data sets and Link to Publications](https://www.dcc.ac.uk/guidance/how-guides/cite-datasets)

#### For Nucleic Acid Sequences and Functional Genomics
* [How do I cite my ArrayExpress data sets in my publication?](https://www.ebi.ac.uk/biostudies/arrayexpress/help#cite)
* [How to Cite Data in ENA](https://www.ebi.ac.uk/ena/browser/about/citing-ena)
* [Citing and linking to the GEO database](https://www.ncbi.nlm.nih.gov/geo/info/linking.html)
* [How do I cite NCBI services and databases?](https://support.nlm.nih.gov/knowledgebase/article/KA-03391/en-us)


### Code Citation

Code citation allows for greater recognition of research software. Some major platforms and tools offer code citation: GitHub, GitLab, JabRef, Zenodo, and Zotero {% cite escience_center_2021 %}.

## How-Tos
---

### How to Make Your Data Reusable?
* Properly document your data with metadata {% cite pavone_2020 %}.
* Use common metadata standards and terminologies {% cite pavone_2020 %}.
* Standardise your data.
* Share your raw data with an open license.

### How to Maximize Already Existing Data?
See Wood-Charlson *et al.* 2022 {% cite wood-charlson_2022 %}.
