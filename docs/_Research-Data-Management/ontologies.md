---
title: Controlled Vocabularies - Ontologies
category: Research-Data-Management
layout: default
docs_css: markdown
redirect_from: /Research-Data-Management
empty: false
hide: false
---

## Introduction
---
Controlled vocabularies, also known as ontologies, are standardized sets of terms and definitions used to ensure clarity, consistency, and accuracy in (meta)data annotation and communication within and across research communities. In this section, the terms "controlled vocabulary" and "ontology" will be used interchangeably.

Historically, Latin served as the lingua franca of academia, providing scholars from diverse linguistic and cultural backgrounds with a consistent and universally understood means of communication. This facilitated knowledge transfer and collaboration, eliminating many of the barriers posed by translation and interpretation.

In contemporary research, ontologies fulfill a similar role by providing structured vocabularies that clearly define and standardize terminology within as well as across specific scientific domains. The use of ontologies facilitates precise communication among researchers and between researchers and computers. Moreover, ontologies promote interoperability, enable efficient data navigation through defined search patterns, reduce ambiguity, and allow data to remain relevant and adaptable to ongoing discoveries and evolving research needs.

Ontologies are continuously refined and expanded by the research community itself. Despite the extensive coverage provided by existing ontologies, there may still be edge cases or overlapping terminologies. Researchers encountering such situations are encouraged to utilize available ontology resources (e.g., [Ontology Lookup Service - OLS](https://www.ebi.ac.uk/ols4/), [Open Biological and Biomedical Ontology Foundry - OBO Foundry](https://obofoundry.org/)) and engage with ontology-development communities:

1. [Participate in ENVO](https://sites.google.com/site/environmentontology/participate?authuser=0).
2. [How to create an OBO ontology from scratch](https://oboacademy.github.io/obook/howto/create-ontology-from-scratch/)

This section will furhter instruct researchers on how to utilize existing resources to biologically annotate their data with ontologies using the [Ontology Lookup Service - OLS](https://www.ebi.ac.uk/ols4/).

### Environmental example - Sampling site
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

### Host-associated examples - Host Metadata
---
#### Human-associated - Ontology recommendations
[Human Disease Ontology - DOID](https://www.disease-ontology.org/) - The Disease Ontology has been developed as a standardized ontology for human disease with the purpose of providing the biomedical community with consistent, reusable and sustainable descriptions of human disease terms, phenotype characteristics and related medical vocabulary disease concepts.

[Human Phenotype Ontology - HP](https://hpo.jax.org/) - The Human Phenotype Ontology provides a standardized vocabulary of phenotypic abnormalities and clinical features encountered in human disease.

[Uber-anatomy ontology - UBERON](https://obophenotype.github.io/uberon/) - Uberon is an integrated cross-species anatomy ontology representing a variety of entities classified according to traditional anatomical criteria such as structure, function and developmental lineage. The ontology includes comprehensive relationships to taxon-specific anatomical ontologies, allowing integration of functional, phenotype and expression data.

[SNOMED Clinical Terms (International Edition)](https://www.snomed.org/) - SNOMED CT or SNOMED Clinical Terms is a systematically organized computer processable collection of medical terms providing codes, terms, synonyms and definitions used in clinical documentation and reporting.

[Neuro Behavior Ontology - NBO](https://www.ebi.ac.uk/ols4/ontologies/nbo) - An ontology of human and animal behaviours and behavioural phenotypes.

[The BRENDA Tissue Ontology - BTO](https://www.ebi.ac.uk/ols4/ontologies/bto) - A structured controlled vocabulary for the source of an enzyme comprising tissues, cell lines, cell types and cell cultures.

[Gene Ontology - GO](http://geneontology.org/) - The Gene Ontology (GO) provides a framework and set of concepts for describing the functions of gene products from all organisms.

[Chemical Entities of Biological Interest - ChEBI](https://www.ebi.ac.uk/chebi/beta/) - An open-access database and ontology of chemical entities. The chemical entities in ChEBI are either naturally occurring molecules or synthetic compounds used to intervene in the processes of living organisms. ChEBI uses the nomenclature, symbolism and terminology endorsed by the International Union of Pure and Applied Chemistry (IUPAC) and the Nomenclature Committee of the International Union of Biochemistry and Molecular Biology (NC-IUBMB). ChEBI also incorporates an ontological classification, whereby the relationships between chemical entities or classes of entities and their parents and/or children are defined; this enables queries based for example on chemical class and role.

#### Animal-associated
[NCBI organismal classification - NCBITAXON](https://www.ncbi.nlm.nih.gov/taxonomy) - An ontology representation of the NCBI organismal taxonomy.

[Biological Spatial Ontology - BSPO](https://obofoundry.org/ontology/bspo) - An ontology for respresenting spatial concepts, anatomical axes, gradients, regions, planes, sides and surfaces. These concepts can be used at multiple biological scales and in a diversity of taxa, including plants, animals and fungi. The BSPO is used to provide a source of anatomical location descriptors for logically defining anatomical entity classes in anatomy ontologies.

[Uber-anatomy ontology - UBERON](https://obophenotype.github.io/uberon/) - Uberon is an integrated cross-species anatomy ontology representing a variety of entities classified according to traditional anatomical criteria such as structure, function and developmental lineage. The ontology includes comprehensive relationships to taxon-specific anatomical ontologies, allowing integration of functional, phenotype and expression data.

[Cell Ontology - CL](https://obofoundry.org/ontology/cl.html) - The Cell Ontology is a structured controlled vocabulary for cell types in animals.

[Neuro Behavior Ontology - NBO](https://www.ebi.ac.uk/ols4/ontologies/nbo) - An ontology of human and animal behaviours and behavioural phenotypes.

[The BRENDA Tissue Ontology - BTO](https://www.ebi.ac.uk/ols4/ontologies/bto) - A structured controlled vocabulary for the source of an enzyme comprising tissues, cell lines, cell types and cell cultures.

[Gene Ontology - GO](http://geneontology.org/) - The Gene Ontology (GO) provides a framework and set of concepts for describing the functions of gene products from all organisms.

[Chemical Entities of Biological Interest - ChEBI](https://www.ebi.ac.uk/chebi/beta/) - An open-access database and ontology of chemical entities. The chemical entities in ChEBI are either naturally occurring molecules or synthetic compounds used to intervene in the processes of living organisms. ChEBI uses the nomenclature, symbolism and terminology endorsed by the International Union of Pure and Applied Chemistry (IUPAC) and the Nomenclature Committee of the International Union of Biochemistry and Molecular Biology (NC-IUBMB). ChEBI also incorporates an ontological classification, whereby the relationships between chemical entities or classes of entities and their parents and/or children are defined; this enables queries based for example on chemical class and role.

#### Plant-associated
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

#### Marine
[NCBI organismal classification - NCBITAXON](https://www.ncbi.nlm.nih.gov/taxonomy) - An ontology representation of the NCBI organismal taxonomy.


#### Terrestrial and Terrestrial- Constructed
