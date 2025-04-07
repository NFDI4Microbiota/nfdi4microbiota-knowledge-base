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
To pinpoint the material or medium that was sampled, we take a subclass of [soil /[ENVO:00001998/]](http://purl.obolibrary.org/obo/ENVO_00001998), that adequately describes our sample, in this case [rhizosphere /[ENVO:00005801/]](http://purl.obolibrary.org/obo/ENVO_00005801).

### Host-associated examples - Host Metadata

#### Human-associated

#### Animal-associated

#### Plant-associated

#### Marine

#### Terrestrial and Terrestrial- Constructed
