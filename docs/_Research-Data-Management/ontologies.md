---
title: Controlled Vocabularies - Ontologies
category: Research-Data-Management
layout: default
docs_css: markdown
redirect_from: /Research-Data-Management
empty: false
hide: false
authors:
   - mbole
---

## **Introduction**
---
Controlled vocabularies, also known as ontologies, are standardized sets of terms and definitions used to ensure clarity, consistency, and accuracy in (meta)data annotation and communication within and across research communities. In this section, the terms "controlled vocabulary" and "ontology" will be used interchangeably.

Historically, Latin served as the lingua franca of academia, providing scholars from diverse linguistic and cultural backgrounds with a consistent and universally understood means of communication. This facilitated knowledge transfer and collaboration, eliminating many of the barriers posed by translation and interpretation.

In contemporary research, ontologies fulfill a similar role by providing structured vocabularies that clearly define and standardize terminology within as well as across specific scientific domains. The use of ontologies facilitates precise communication among researchers and between researchers and computers. Moreover, ontologies promote interoperability, enable efficient data navigation through defined search patterns, reduce ambiguity, and allow data to remain relevant and adaptable to ongoing discoveries and evolving research needs.

Ontologies are continuously refined and expanded by the research community itself. Despite the extensive coverage provided by existing ontologies, there may still be edge cases or overlapping terminologies. Researchers encountering such situations are encouraged to utilize available ontology resources: 

1. [Ontology Lookup Service - OLS](https://www.ebi.ac.uk/ols4/),
2. [Open Biological and Biomedical Ontology Foundry - OBO Foundry](https://obofoundry.org/),
3. [BioPortal](https://bioportal.bioontology.org/),
4. [Ontobee](https://ontobee.org/),
5. [OntoPortal](https://ontoportal.org/),
6. [Bioregistry](https://bioregistry.io/),

and engage with the ontology-development communities by submitting ontology request on:

1. [Participate in ENVO](https://sites.google.com/site/environmentontology/participate?authuser=0),
2. [How to create an OBO ontology from scratch](https://oboacademy.github.io/obook/howto/create-ontology-from-scratch/), [Contributing to OBO ontologies](https://oboacademy.github.io/obook/lesson/contributing-to-obo-ontologies/),
3. [OntoPortal Documentation](https://ontoportal.github.io/documentation/administration/ontologies/submitting_ontologies),
4. [National Cancer Institute - Term Suggestion Request](https://evsexplore.semantics.cancer.gov/evsexplore/termform),

This section will furhter instruct researchers on how to utilize existing resources to biologically annotate their data with ontologies using the [Ontology Lookup Service - OLS](https://www.ebi.ac.uk/ols4/).

### **Environmental example - Sampling site**
---
Recommended Ontologies: [The Environment Ontology - ENVO](https://sites.google.com/site/environmentontology/about-envo?authuser=0)

To illustrate the application of ontologies for a sampling site, we will consider a hypothetical scenario involving the annotation of metagenomic samples collected from a rhizosphere environment in a forest in Germany. 

In preparation for annotating these samples, the researcher may utilize the [EMBL-EBI Ontology Lookup Service - OLS](https://www.ebi.ac.uk/ols4/) to identify appropriate ontology terms:

1. Identifying a broad environmental context (env_broad_scale):
Starting with a general search term such as [biome
\[ENVO_00000428\]](http://purl.obolibrary.org/obo/ENVO_00000428), the researcher encounters several subclasses. Upon further exploration, a more precise subclass [terrestrial biome
\[ENVO:00000446\]](http://purl.obolibrary.org/obo/ENVO_00000446) is found, although it remains somewhat broad for accurate sample annotation.

2. Defining a specific environment (env_broad_scale; env_local_scale):
A more precise subclass, [woodland biome \[ENVO:01000175\]](http://purl.obolibrary.org/obo/ENVO_01000175) (env_broad_scale), and subsequently [temperate woodland biome \[ENVO:01000221\]](http://purl.obolibrary.org/obo/ENVO_01000175) (env_local_scale) are identified, providing a more accurate description of the environmental context of the sample.

3. Identify the sampled material (env_medium):
To pinpoint the material or medium that was sampled, we take a subclass of [soil \[ENVO:00001998\]](http://purl.obolibrary.org/obo/ENVO_00001998), that adequately describes our sample, in this case [rhizosphere \[ENVO:00005801\]](http://purl.obolibrary.org/obo/ENVO_00005801).

Along with the environmental context, other metadata can be captured and described with ontologies:

#### **Location**
[Gazeteer - GAZ](https://www.ebi.ac.uk/ols4/ontologies/gaz) - A gazetteer constructed on ontological principles. The countries are actively maintained.

Other resources:
[Basic Geo (WGS84 lat/long) Vocabulary](https://www.w3.org/2003/01/geo/) - This is a basic RDF vocabulary that provides the Semantic Web community with a namespace for representing lat(itude), long(itude) and other information about spatially-located things, using WGS84 as a reference datum.

### **Host-associated examples - Host Metadata**
---
#### **Human-associated - Ontology recommendations**
[Human Disease Ontology - DOID](https://www.disease-ontology.org/) - The Disease Ontology has been developed as a standardized ontology for human disease with the purpose of providing the biomedical community with consistent, reusable and sustainable descriptions of human disease terms, phenotype characteristics and related medical vocabulary disease concepts.

[Human Phenotype Ontology - HP](https://hpo.jax.org/) - The Human Phenotype Ontology provides a standardized vocabulary of phenotypic abnormalities and clinical features encountered in human disease.

[Uber-anatomy ontology - UBERON](https://obophenotype.github.io/uberon/) - Uberon is an integrated cross-species anatomy ontology representing a variety of entities classified according to traditional anatomical criteria such as structure, function and developmental lineage. The ontology includes comprehensive relationships to taxon-specific anatomical ontologies, allowing integration of functional, phenotype and expression data.

[Foundational Model of Anatomy Ontology - FMA](http://si.washington.edu/projects/fma/) - The FMA is a domain ontology that represents a coherent body of explicit declarative knowledge about human anatomy. Its ontological framework can be applied and extended to all other species. The Foundational Model of Anatomy (FMA) ontology is one of the information resources integrated in the distributed framework of the Anatomy Information System developed and maintained by the Structural Informatics Group at the University of Washington.

[SNOMED Clinical Terms (International Edition)](https://www.snomed.org/) - SNOMED CT or SNOMED Clinical Terms is a systematically organized computer processable collection of medical terms providing codes, terms, synonyms and definitions used in clinical documentation and reporting.

[Neuro Behavior Ontology - NBO](https://www.ebi.ac.uk/ols4/ontologies/nbo) - An ontology of human and animal behaviours and behavioural phenotypes.

[The BRENDA Tissue Ontology - BTO](https://www.ebi.ac.uk/ols4/ontologies/bto) - A structured controlled vocabulary for the source of an enzyme comprising tissues, cell lines, cell types and cell cultures.

[Gene Ontology - GO](http://geneontology.org/) - The Gene Ontology (GO) provides a framework and set of concepts for describing the functions of gene products from all organisms.

[Chemical Entities of Biological Interest - ChEBI](https://www.ebi.ac.uk/chebi/beta/) - An open-access database and ontology of chemical entities. The chemical entities in ChEBI are either naturally occurring molecules or synthetic compounds used to intervene in the processes of living organisms. ChEBI uses the nomenclature, symbolism and terminology endorsed by the International Union of Pure and Applied Chemistry (IUPAC) and the Nomenclature Committee of the International Union of Biochemistry and Molecular Biology (NC-IUBMB). ChEBI also incorporates an ontological classification, whereby the relationships between chemical entities or classes of entities and their parents and/or children are defined; this enables queries based for example on chemical class and role.

[National Ccancer Institute Thesaurus - NCIT](https://evsexplore.semantics.cancer.gov/evsexplore/welcome) - NCI Thesaurus (NCIt) provides reference terminology for many NCI and other systems. It covers vocabulary for clinical care, translational and basic research, and public information and administrative activities.

---
#### **Animal-associated - Ontology recommendations**
[NCBI organismal classification - NCBITAXON](https://www.ncbi.nlm.nih.gov/taxonomy) - An ontology representation of the NCBI organismal taxonomy.

[Biological Spatial Ontology - BSPO](https://obofoundry.org/ontology/bspo) - An ontology for respresenting spatial concepts, anatomical axes, gradients, regions, planes, sides and surfaces. These concepts can be used at multiple biological scales and in a diversity of taxa, including plants, animals and fungi. The BSPO is used to provide a source of anatomical location descriptors for logically defining anatomical entity classes in anatomy ontologies.

[Uber-anatomy ontology - UBERON](https://obophenotype.github.io/uberon/) - Uberon is an integrated cross-species anatomy ontology representing a variety of entities classified according to traditional anatomical criteria such as structure, function and developmental lineage. The ontology includes comprehensive relationships to taxon-specific anatomical ontologies, allowing integration of functional, phenotype and expression data.

[Cell Ontology - CL](https://obofoundry.org/ontology/cl.html) - The Cell Ontology is a structured controlled vocabulary for cell types in animals.

[Neuro Behavior Ontology - NBO](https://www.ebi.ac.uk/ols4/ontologies/nbo) - An ontology of human and animal behaviours and behavioural phenotypes.

[The BRENDA Tissue Ontology - BTO](https://www.ebi.ac.uk/ols4/ontologies/bto) - A structured controlled vocabulary for the source of an enzyme comprising tissues, cell lines, cell types and cell cultures.

[Gene Ontology - GO](http://geneontology.org/) - The Gene Ontology (GO) provides a framework and set of concepts for describing the functions of gene products from all organisms.

[Chemical Entities of Biological Interest - ChEBI](https://www.ebi.ac.uk/chebi/beta/) - An open-access database and ontology of chemical entities. The chemical entities in ChEBI are either naturally occurring molecules or synthetic compounds used to intervene in the processes of living organisms. ChEBI uses the nomenclature, symbolism and terminology endorsed by the International Union of Pure and Applied Chemistry (IUPAC) and the Nomenclature Committee of the International Union of Biochemistry and Molecular Biology (NC-IUBMB). ChEBI also incorporates an ontological classification, whereby the relationships between chemical entities or classes of entities and their parents and/or children are defined; this enables queries based for example on chemical class and role.

[The Environment Ontology - ENVO](http://environmentontology.org/) - ENVO is an ontology which represents knowledge about environments,environmental processes, ecosystems, habitats, and related entities.

[An ontology of core ecological entities - ECOCORE](https://www.ebi.ac.uk/ols4/ontologies/ecocore) - An ontology of core ecological entities.

[Foundational Model of Anatomy Ontology - FMA](http://si.washington.edu/projects/fma/) - The FMA is a domain ontology that represents a coherent body of explicit declarative knowledge about human anatomy. Its ontological framework can be applied and extended to all other species. The Foundational Model of Anatomy (FMA) ontology is one of the information resources integrated in the distributed framework of the Anatomy Information System developed and maintained by the Structural Informatics Group at the University of Washington.

---
#### **Plant-associated - Ontology recommendations**
[NCBI organismal classification - NCBITAXON](https://www.ncbi.nlm.nih.gov/taxonomy) - An ontology representation of the NCBI organismal taxonomy.

[Agronomy Ontology - AGRO](https://www.ebi.ac.uk/ols4/ontologies/agro) - AgrO is an ontlogy for representing agronomic practices, techniques, variables and related entities.

[Flora Phenotype Ontology - FLOPO](https://www.ebi.ac.uk/ols4/ontologies/flopo) - Traits and phenotypes of flowering plants occurring in digitized Floras.

[Plant Experimental Conditions Ontology - PECO](http://planteome.org/) - A structured, controlled vocabulary which describes the treatments, growing conditions, and/or study types used in plant biology experiments.

[Plant Ontology - PO](http://browser.planteome.org/amigo) - An ontology that describes plant anatomy, morphology, and growth and development in plants.

[Plant Phenology Ontology - PPO](https://www.ebi.ac.uk/ols4/ontologies/ppo) - An ontology that defines plant phenological classes and is used to run the plantphenology.org data portal. Reuses terms from PO and PATO where possible.

[Plant Trait Ontology - TO](https://www.ebi.ac.uk/ols4/ontologies/to) - An ontology that describes phenotypic traits in plants. Each trait is a distinguishable feature, characteristic, quality or phenotypic feature of a developing or mature plant.

[Plant Stress Ontology - PSO](https://www.ebi.ac.uk/ols4/ontologies/pso) - An ontology containing biotic and abiotic plant stresses.

[The BRENDA Tissue Ontology - BTO](https://www.ebi.ac.uk/ols4/ontologies/bto) - A structured controlled vocabulary for the source of an enzyme comprising tissues, cell lines, cell types and cell cultures.

[Gene Ontology - GO](http://geneontology.org/) - The Gene Ontology (GO) provides a framework and set of concepts for describing the functions of gene products from all organisms.

[Chemical Entities of Biological Interest - ChEBI](https://www.ebi.ac.uk/chebi/beta/) - An open-access database and ontology of chemical entities. The chemical entities in ChEBI are either naturally occurring molecules or synthetic compounds used to intervene in the processes of living organisms. ChEBI uses the nomenclature, symbolism and terminology endorsed by the International Union of Pure and Applied Chemistry (IUPAC) and the Nomenclature Committee of the International Union of Biochemistry and Molecular Biology (NC-IUBMB). ChEBI also incorporates an ontological classification, whereby the relationships between chemical entities or classes of entities and their parents and/or children are defined; this enables queries based for example on chemical class and role.

[The Environment Ontology - ENVO](http://environmentontology.org/) - ENVO is an ontology which represents knowledge about environments,environmental processes, ecosystems, habitats, and related entities.

[An ontology of core ecological entities - ECOCORE](https://www.ebi.ac.uk/ols4/ontologies/ecocore) - An ontology of core ecological entities.

---
#### **Marine - Ontology recommendations**
[NCBI organismal classification - NCBITAXON](https://www.ncbi.nlm.nih.gov/taxonomy) - An ontology representation of the NCBI organismal taxonomy.

[The Environment Ontology - ENVO](http://environmentontology.org/) - ENVO is an ontology which represents knowledge about environments,environmental processes, ecosystems, habitats, and related entities.

[Gene Ontology - GO](http://geneontology.org/) - The Gene Ontology (GO) provides a framework and set of concepts for describing the functions of gene products from all organisms.

[Chemical Entities of Biological Interest - ChEBI](https://www.ebi.ac.uk/chebi/beta/) - An open-access database and ontology of chemical entities. The chemical entities in ChEBI are either naturally occurring molecules or synthetic compounds used to intervene in the processes of living organisms. ChEBI uses the nomenclature, symbolism and terminology endorsed by the International Union of Pure and Applied Chemistry (IUPAC) and the Nomenclature Committee of the International Union of Biochemistry and Molecular Biology (NC-IUBMB). ChEBI also incorporates an ontological classification, whereby the relationships between chemical entities or classes of entities and their parents and/or children are defined; this enables queries based for example on chemical class and role.

[Biological Spatial Ontology - BSPO](https://obofoundry.org/ontology/bspo) - An ontology for respresenting spatial concepts, anatomical axes, gradients, regions, planes, sides and surfaces. These concepts can be used at multiple biological scales and in a diversity of taxa, including plants, animals and fungi. The BSPO is used to provide a source of anatomical location descriptors for logically defining anatomical entity classes in anatomy ontologies.

[Uber-anatomy ontology - UBERON](https://obophenotype.github.io/uberon/) - Uberon is an integrated cross-species anatomy ontology representing a variety of entities classified according to traditional anatomical criteria such as structure, function and developmental lineage. The ontology includes comprehensive relationships to taxon-specific anatomical ontologies, allowing integration of functional, phenotype and expression data.

[Cell Ontology - CL](https://obofoundry.org/ontology/cl.html) - The Cell Ontology is a structured controlled vocabulary for cell types in animals.

[Neuro Behavior Ontology - NBO](https://www.ebi.ac.uk/ols4/ontologies/nbo) - An ontology of human and animal behaviours and behavioural phenotypes.

[The BRENDA Tissue Ontology - BTO](https://www.ebi.ac.uk/ols4/ontologies/bto) - A structured controlled vocabulary for the source of an enzyme comprising tissues, cell lines, cell types and cell cultures.

[An ontology of core ecological entities - ECOCORE](https://www.ebi.ac.uk/ols4/ontologies/ecocore) - An ontology of core ecological entities.

[Foundational Model of Anatomy Ontology - FMA](http://si.washington.edu/projects/fma/) - The FMA is a domain ontology that represents a coherent body of explicit declarative knowledge about human anatomy. Its ontological framework can be applied and extended to all other species. The Foundational Model of Anatomy (FMA) ontology is one of the information resources integrated in the distributed framework of the Anatomy Information System developed and maintained by the Structural Informatics Group at the University of Washington.

---
#### **Terrestrial and Terrestrial-Constructed - Ontology recommendations**
[NCBI organismal classification - NCBITAXON](https://www.ncbi.nlm.nih.gov/taxonomy) - An ontology representation of the NCBI organismal taxonomy.

[The Environment Ontology - ENVO](http://environmentontology.org/) - ENVO is an ontology which represents knowledge about environments,environmental processes, ecosystems, habitats, and related entities.

[An ontology of core ecological entities - ECOCORE](https://www.ebi.ac.uk/ols4/ontologies/ecocore) - An ontology of core ecological entities.

[Chemical Entities of Biological Interest - ChEBI](https://www.ebi.ac.uk/chebi/beta/) - An open-access database and ontology of chemical entities. The chemical entities in ChEBI are either naturally occurring molecules or synthetic compounds used to intervene in the processes of living organisms. ChEBI uses the nomenclature, symbolism and terminology endorsed by the International Union of Pure and Applied Chemistry (IUPAC) and the Nomenclature Committee of the International Union of Biochemistry and Molecular Biology (NC-IUBMB). ChEBI also incorporates an ontological classification, whereby the relationships between chemical entities or classes of entities and their parents and/or children are defined; this enables queries based for example on chemical class and role.

---
### **Cultured sample - Sample metadata**
---

[NCBI organismal classification - NCBITAXON](https://www.ncbi.nlm.nih.gov/taxonomy) - An ontology representation of the NCBI organismal taxonomy.

[Microbial Conditions Ontology - MCO](https://www.ebi.ac.uk/ols4/ontologies/mco) - A domain ontology that provides a controlled vocabulary for the unambiguous description of microbial growth conditions. The purpose of this ontology is to set an standard for the structured annotation of the experimental conditions in public repositories.

[Ontology for Biomedical Investigations - OBI](https://obi-ontology.org/) - The Ontology for Biomedical Investigations (OBI) helps you communicate clearly about scientific investigations by defining more than 2500 terms, including study designs, the collection and preparation of the targets of investigation, assays, instrumentation and reagents used, as well as the data generated and the types of analysis performed on the data to reach conclusions, and their documentation.

[Chemical Entities of Biological Interest - ChEBI](https://www.ebi.ac.uk/chebi/beta/) - An open-access database and ontology of chemical entities. The chemical entities in ChEBI are either naturally occurring molecules or synthetic compounds used to intervene in the processes of living organisms. ChEBI uses the nomenclature, symbolism and terminology endorsed by the International Union of Pure and Applied Chemistry (IUPAC) and the Nomenclature Committee of the International Union of Biochemistry and Molecular Biology (NC-IUBMB). ChEBI also incorporates an ontological classification, whereby the relationships between chemical entities or classes of entities and their parents and/or children are defined; this enables queries based for example on chemical class and role.

---
### **Data type - Techical ontologies recommendations**
---
#### **Nucleotide sequecing ((Meta)Genomic, (Meta)Transcriptomics, Amplicon, Viral) - Ontology recommendations**
[NCBI organismal classification - NCBITAXON](https://www.ncbi.nlm.nih.gov/taxonomy) - An ontology representation of the NCBI organismal taxonomy.

[Ontology for Biomedical Investigations - OBI](https://obi-ontology.org/) - The Ontology for Biomedical Investigations (OBI) helps you communicate clearly about scientific investigations by defining more than 2500 terms, including study designs, the collection and preparation of the targets of investigation, assays, instrumentation and reagents used, as well as the data generated and the types of analysis performed on the data to reach conclusions, and their documentation.

[Genomic Epidemiology Onotology - GENEPIO](https://genepio.org/) - The Genomic Epidemiology Ontology aims to provide a comprehensive controlled vocabulary for infectious disease surveillance and outbreak investigations. It is an application ontology that draws on many other ontologies including anatomy, taxonomy, disease, symptoms, environment and food types for foodborn pathogen metadata.

[BioAssay Ontology - BAO](http://bioassayontology.org/) - The BioAssay Ontology (BAO) describes chemical biology screening assays and their results including high-throughput screening (HTS) data for the purpose of categorizing assays and data analysis.

[The Ontology of Data Analysis and Management - EDAM](http://edamontology.org/) - EDAM is a comprehensive ontology of well-established, familiar concepts that are prevalent within scientific data analysis and data management (both within and beyond life sciences and imaging). EDAM includes topics, operations, types of data and data identifiers, and data formats. EDAM provides a set of concepts with preferred terms and synonyms, related terms, definitions, and other information - organised into a simple and intuitive hierarchy for convenient use (see figures below). EDAM is particularly suitable for semantic annotations and categorisation of diverse scientific resources: e.g. tools, workflows, learning materials, or standards. EDAM is also useful in data management itself, for recording provenance metadata of processed scientific data.

---
#### **(Meta)Proteomics - Ontology recommendations**
[Proteomics Identification Database Ontology - PRIDE](https://www.ebi.ac.uk/ols4/ontologies/pride) - Proteomics Identification Database Ontology, terms describing proteomics data and experimental metadata.

[Mass Spectroscopy - MS](https://www.ebi.ac.uk/ols4/ontologies/ms) - The Controlled Vocabularies (CV’s) of the Proteomic Standard Initiative (PSI) provide a consensus annotation system to standardize the meaning, syntax and formalism of terms used across proteomics, as required by the PSI Working Groups. Each PSI working group develops the CV’s required by the technology or data type it aims to standardize, following common recommendations for devoplement and maintenance.

[BioAssay Ontology - BAO](http://bioassayontology.org/) - The BioAssay Ontology (BAO) describes chemical biology screening assays and their results including high-throughput screening (HTS) data for the purpose of categorizing assays and data analysis.

[The BRENDA Tissue Ontology - BTO](https://www.ebi.ac.uk/ols4/ontologies/bto) - A structured controlled vocabulary for the source of an enzyme comprising tissues, cell lines, cell types and cell cultures.

[Protein Modifaction - MOD](https://www.ebi.ac.uk/ols4/ontologies/mod) - Protein chemical modifications, classified by molecular structure or amino acid.

[The Ontology of Data Analysis and Management - EDAM](http://edamontology.org/) - EDAM is a comprehensive ontology of well-established, familiar concepts that are prevalent within scientific data analysis and data management (both within and beyond life sciences and imaging). EDAM includes topics, operations, types of data and data identifiers, and data formats. EDAM provides a set of concepts with preferred terms and synonyms, related terms, definitions, and other information - organised into a simple and intuitive hierarchy for convenient use (see figures below). EDAM is particularly suitable for semantic annotations and categorisation of diverse scientific resources: e.g. tools, workflows, learning materials, or standards. EDAM is also useful in data management itself, for recording provenance metadata of processed scientific data.

[Chemical Methods Ontology - CHMO](https://www.ebi.ac.uk/ols4/ontologies/chmo) - CHMO, the chemical methods ontology, describes methods used to collect data in chemical experiments, such as mass spectrometry and electron microscopy prepare and separate material for further analysis, such as sample ionisation, chromatography, and electrophoresis synthesise materials, such as epitaxy and continuous vapour deposition It also describes the instruments used in these experiments, such as mass spectrometers and chromatography columns. It is intended to be complementary to the Ontology for Biomedical Investigations (OBI).

[Reaction Ontologies - RXNO](https://www.ebi.ac.uk/ols4/ontologies/rxno) - RXNO is the name reaction ontology. It contains more than 500 classes representing organic reactions such as the Diels–Alder cyclization.

[Molecular Process Ontology - MOP](https://www.ebi.ac.uk/ols4/ontologies/mop) -  It contains the molecular processes that underlie the name reaction ontology RXNO, for example cyclization, methylation and demethylation.

---
#### **Metabolomics - Ontology recommendations**
[Metabolomics Standards Initiative Ontology - MSIO](https://www.ebi.ac.uk/ols4/ontologies/msio) - MSIO aims to provide a single point of entry to support semantic markup of experiments making use of NMR and MS techniques to identify, measure and quantify small molecules known as metabolites. MSIO covers metabolite profiling, targeted or undertargeted, tracer based applications. MSIO reuses a number of resources such as [CHEBI](https://www.ebi.ac.uk/ols/ontologies/chebi), [DUO](https://www.ebi.ac.uk/ols/ontologies/duo), [NMRCV](https://www.ebi.ac.uk/ols/ontologies/nmrcv), [OBI](https://www.ebi.ac.uk/ols/ontologies/obi), and [STATO](https://www.ebi.ac.uk/ols/ontologies/stato).

[Nuclear Magnetic Resonance Controlled Vocabulary - NMRCV](http://nmrml.org/cv/) - This simple taxonomy of terms (no DL semantics used) serves the nuclear magnetic resonance markup language (nmrML) with meaningful descriptors to amend the nmrML xml file with CV terms. Metabolomics scientists are encouraged to use this CV to annotrate their raw and experimental context data, i.e. within nmrML.

[BioAssay Ontology - BAO](http://bioassayontology.org/) - The BioAssay Ontology (BAO) describes chemical biology screening assays and their results including high-throughput screening (HTS) data for the purpose of categorizing assays and data analysis.

[The BRENDA Tissue Ontology - BTO](https://www.ebi.ac.uk/ols4/ontologies/bto) - A structured controlled vocabulary for the source of an enzyme comprising tissues, cell lines, cell types and cell cultures.

[Protein Modifaction - MOD](https://www.ebi.ac.uk/ols4/ontologies/mod) - Protein chemical modifications, classified by molecular structure or amino acid.

[The Ontology of Data Analysis and Management - EDAM](http://edamontology.org/) - EDAM is a comprehensive ontology of well-established, familiar concepts that are prevalent within scientific data analysis and data management (both within and beyond life sciences and imaging). EDAM includes topics, operations, types of data and data identifiers, and data formats. EDAM provides a set of concepts with preferred terms and synonyms, related terms, definitions, and other information - organised into a simple and intuitive hierarchy for convenient use (see figures below). EDAM is particularly suitable for semantic annotations and categorisation of diverse scientific resources: e.g. tools, workflows, learning materials, or standards. EDAM is also useful in data management itself, for recording provenance metadata of processed scientific data.

[Chemical Methods Ontology - CHMO](https://www.ebi.ac.uk/ols4/ontologies/chmo) - CHMO, the chemical methods ontology, describes methods used to collect data in chemical experiments, such as mass spectrometry and electron microscopy prepare and separate material for further analysis, such as sample ionisation, chromatography, and electrophoresis synthesise materials, such as epitaxy and continuous vapour deposition It also describes the instruments used in these experiments, such as mass spectrometers and chromatography columns. It is intended to be complementary to the Ontology for Biomedical Investigations (OBI).

[Reaction Ontologies - RXNO](https://www.ebi.ac.uk/ols4/ontologies/rxno) - RXNO is the name reaction ontology. It contains more than 500 classes representing organic reactions such as the Diels–Alder cyclization.

---
#### **Synthetic and Systems Biology - Ontology Recommendations**
[Synthetic Biology Open Language Ontology - SBOL Ontology](https://sbolstandard.org/ontology/) - The SBOL-OWL ontology provides a set of controlled terms that are used to describe genetic circuit designs using [SBOL](https://sbolstandard.org/datamodel-about/).

[Systems Biology Ontology - SBO](https://www.ebi.ac.uk/ols4/ontologies/sbo) - The Systems Biology Ontology is a set of controlled, relational vocabularies of terms commonly used in Systems Biology, and in particular in computational modeling. The ontology consists of six orthogonal vocabularies defining: the roles of reaction participants (eg. “substrate”), quantitative parameters (eg. “Michaelis constant”), a precise classification of mathematical expressions that describe the system (eg. “mass action rate law”), the modeling framework used (eg. “logical framework”), and a branch each to describe entity (eg. “macromolecule”) and interaction (eg. “process”) types. SBO terms can be used to introduce a layer of semantic information into the standard description of a model, or to annotate the results of biochemical experiments in order to facilitate their efficient reuse.

[Sequence Types and Features Ontology - SO](http://www.sequenceontology.org/) - The Sequence Ontology is a set of terms and relationships used to describe the features and attributes of biological sequence. SO includes different kinds of features which can be located on the sequence. Biological features are those which are defined by their disposition to be involved in a biological process. Examples are binding_site and exon. Biomaterial features are those which are intended for use in an experiment such as aptamer and PCR_product. There are also experimental features which are the result of an experiment. SO also provides a rich set of attributes to describe these features such as “polycistronic” and “maternally imprinted”.

[TErminology for the Description of DYnamics - TEDDY](https://www.ebi.ac.uk/ols4/ontologies/teddy) - The TErminology for the Description of DYnamics (TEDDY) project aims to provide an ontology for dynamical behaviours, observable dynamical phenomena, and control elements of bio-models and biological systems in Systems Biology and Synthetic Biology.

[Molecular Process Ontology - MOP](https://www.ebi.ac.uk/ols4/ontologies/mop) -  It contains the molecular processes that underlie the name reaction ontology RXNO, for example cyclization, methylation and demethylation.

[Reaction Ontologies - RXNO](https://www.ebi.ac.uk/ols4/ontologies/rxno) - RXNO is the name reaction ontology. It contains more than 500 classes representing organic reactions such as the Diels–Alder cyclization.
