---
title: Metadata & Metadata Standards
category: Research-Data-Management
layout: default
docs_css: markdown
redirect_from: /Research-Data-Management
empty: false
hide: false
---


<img src="https://upload.wikimedia.org/wikipedia/commons/e/ee/Metadata_is_a_love_note_to_the_future_%288071729256%29.jpg" alt="Metadata Is a Love Note to the Future - Jason Scott" width="200"/>

(CC-BY - [cea +](https://www.flickr.com/people/33255628@N00), [Source](https://en.wikipedia.org/wiki/File:Metadata_is_a_love_note_to_the_future_(8071729256).jpg))

## Metadata is data about data
---

Before we delve into specifications on what metadata standards for the microbiology community are, let us explain what metadata is. 

In general, metadata provides us with information about other data but does not tell us anything about the content of the data itself. Instead, it describes other types of information to help you understand or use the data you are working with. In the simplest terms, metadata is **data** about data. 

In microbiology, metadata provides crucial contextual information about biological samples, aiding in the interpretation and reuse of experimental data. For instance, consider metadata associated with an RNA-Seq sample from a bacterial strain isolated from soil. The metadata could include details such as:

1. **Strain Information:**
   - **Strain Identifier:** JCM 14847
   - **Species:** *Pseudomonas aeruginosa*
   - **Source:** Soil sample collected from [Location], [Date]
   - **Isolation Method:** Nutrient Agar plate streaking

2. **Sample Collection Information:**
   - **Sample Identifier:** RNA-Seq_Sample_001
   - **Collection Date:** [Date]
   - **Sample Type:** Bacterial culture
   - **Growth Medium:** LB broth
   - **Growth Conditions:** Temperature, pH, and duration of incubation
   - **Subculture History:** Number of passages, growth conditions

3. **Experimental Conditions:**
   - **Treatment Conditions:** Control or experimental treatment
   - **Treatment Duration:** Time exposed to treatment
   - **Concentration:** Concentration of treatment agent

4. **RNA-Seq Experimental Details:**
   - **Library Preparation Method:** TruSeq Stranded mRNA Library Prep Kit
   - **Sequencing Platform:** Illumina NovaSeq
   - **Sequencing Depth:** Number of reads obtained
   - **Quality Control Metrics:** RNA integrity number (RIN), sequencing quality scores

5. **Bioinformatics Analysis Details:**
   - **Read Alignment Algorithm:** HISAT2
   - **Genome Reference:** *Pseudomonas aeruginosa* PAO1
   - **Differential Expression Analysis:** Software used, statistical thresholds
   - **Gene Annotation:** Functional databases used for annotation

6. **Ethical and Legal Considerations:**
   - **Ethical Approval:** Institutional review board (IRB) approval number
   - **Data Sharing Policy:** Conditions for data sharing, data access restrictions

For more details on the distinction between different types of metadata,  we refer you to the FAIR Cookbook recipe [FAIR and the notion of metadata](https://w3id.org/faircookbook/FCB068) section.

## When should you collect your metadata
---
As is usually the case in sciences, your research (and the wider microbiological community) can benefit highly from the rigorous and timely planning of your experiments, including metadata collection. In this case, we refer you to other subsections of this Knowledge Base: [**Data Management Plans (DMPs)**](./08-dmp.md) that could help you plan your experiments.

Metadata collection should be planned, but at the same time, it can be overwhelming. What amount of metadata is enough to describe your data? Was it crucial to note down the pipette I was using, or should I have noted down the location of the sampling site? Will I still understand in a year what I wrote down in my notebook/ELN? Will other researchers make sense of the (meta)data I collected? Will other researchers be able to replicate my research if I did not note down my in-house DNA extraction protocol? 

These and other considerations should be thoroughly thought out before the start of your experimental procedures. Some of the metadata can even be collected and documented before starting the experiments if you already know how to collect your samples, process, sequence them (if sequencing is a part of the analysis), and analyze them. 

## Metadata collection example
---
We will look into an example of microbiological environmental metadata, where we gather samples from a forest environment, specifically plant rhizosphere, and we will be doing amplicon and metagenomic sequencing. We will not dive specifically into all omics types and biological/environmental on this page. Instead, we encourage readers to read our [MetadataStandards](https://github.com/NFDI4Microbiota/MetadataStandards) resource repository. 

Our proposal for a sampling campaign to analyze plant-rhizosphere microbiomes was accepted. In the proposal, we outlined the purpose and goal of our campaign. Since our funding is public, our funding agency requires us to submit our generated and gathered data to a public repository (e.g., ENA, NCBI, DDBJ). To find where you can deposit your data, we refer our readers to the [Data Repositories](./data-repositories.md) section of this KnowledgeBase. There we see that our Nucleic acid sequences can be deposited in ENA.

We immediately jump to [**ENA's Sample Checklist browser**](https://www.ebi.ac.uk/ena/browser/checklists) and find a checklist that best corresponds to our sampling campaign. After some scrolling, we discover the [GSC MIxS plant associated; Checklist: ERC000020](https://www.ebi.ac.uk/ena/browser/view/ERC000020), that list some of the **Mandatory** metadata fields that need to be filled out for data submission, along with their **Field Format** and **Field restriction** and **Optional** fields. The metadata fields correspond to technical metadata (e.g., sequencing method, sample volume or weight for DNA extraction, nucleic acid extraction, library size, etc.) along with some metadata fields corresponding to the biological and environmental metadata (e.g., broad-scale environmental context, local environmental context, environmental medium, geographic location (latitude) and geographic location (longitude), host metadata, sample collection metadata, etc.)

Alternatively, we can hop over to the [MetadataStandards/Plant-associated microbiome biological-environmental metadata](https://github.com/NFDI4Microbiota/MetadataStandards/blob/main/Biological_Environmental/PlantAssoc_BioEnv_Metadata.md) where we can find a similar (but stripped down) checklist with some filed out examples for biological and environmental metadata. For the technical metadata corresponding to this example sampling campaign we would refer the reader to the [Amplicon sequencing](https://github.com/NFDI4Microbiota/MetadataStandards/blob/main/Technical/Amplicon_Technical_Metadata.md) and [Metagenome sequencing](https://github.com/NFDI4Microbiota/MetadataStandards/blob/main/Technical/Metagenome_Technical_Metadata.md) section of our [Technical MetadataStandards](https://github.com/NFDI4Microbiota/MetadataStandards/tree/main/Technical) part of repository.

By now, we should have a rough estimation of what kind of biological/environmental metadata we can collect before sampling, during sampling, and what could be collected during the processing of samples. 


# Metadata standards
---
Once a community agrees to a set of relevant metadata for their field, they can devise metadata standards.
A metadata standard is usually defined for a given type of data and by different stakeholders (e.g., users communities, data repositories).
For every metadata field part of a metadata standard, one could expect a human-readable description of the metadata field paired with a machine-readable persistent identifier of the field, then an indication of the level of requirements of this field in the standard and how many values of this field are expected (that is the cardinality).

[More than a thousand standards are listed by the organization `FAIRsharing.org`](https://fairsharing.org/search?fairsharingRegistry=Standard) which can be overwhelming.
At NFDI4Microbiota, we compiled a [list of widely used metadata standards in the field of microbiome research](https://github.com/NFDI4Microbiota/MetadataStandards) that you can browse and use for the different types of data collected during your investigations.


## Metadata management
---
## Metadata quality control
---
 Metadata quality control involves thorough validation and standardization of metadata attributes to minimize errors and inconsistencies. For instance, in studies involving microbial sequencing data, rigorous checks are needed to verify the accuracy of sample identifiers, ensuring that each sample is uniquely identified and correctly linked to corresponding experimental conditions. Moreover, metadata completeness is essential to provide sufficient context for data interpretation and reuse. Researchers should meticulously document sample collection details, including the source organism, sampling location, and environmental conditions, to facilitate cross-study comparisons and meta-analyses. For example, in a microbiome study investigating the gut microbial composition in patients with inflammatory bowel disease, comprehensive metadata would encompass clinical metadata such as patient demographics, disease severity scores, and medication history, alongside microbial metadata like taxonomic profiles and sequencing protocols.

Furthermore, metadata quality control in microbiology extends to the curation of controlled vocabularies and ontologies to harmonize terminology and promote semantic interoperability across data sets. Standardized metadata terms ensure consistency in data annotation and facilitate data integration from diverse sources. For instance, ontologies such as the Environment Ontology (ENVO) provide a structured vocabulary for describing environmental parameters, enabling researchers to annotate microbial samples with terms like "soil pH," "temperature," and "moisture content" uniformly. Additionally, validation rules and automated workflows are employed to enforce data integrity and conformity to predefined metadata standards. For example, data submission portals for public repositories often incorporate validation checks to verify compliance with metadata schema requirements before data deposition, minimizing errors and enhancing data usability. By implementing robust metadata quality control measures, microbiology researchers can uphold data integrity, foster data harmonization and interoperability, and facilitate meaningful insights into microbial ecosystems and host-microbe 

