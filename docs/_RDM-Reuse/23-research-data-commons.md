---
title: Research Data Commons (RDC)
category: RDM-Reuse
layout: default
docs_css: markdown
---

# Overview
The Research Data Commons (RDC) is conceptualised as an expandable, cloud-based research infrastructure that provides scientists, data providers, and data consumers with powerful tools for creating FAIR data products and facilitates the exchange of data and services in a collaborative manner, both within the German National Research Data Infrastructure (NFDI) and beyond.
In NFDI4Microbiota, RDC development specifically serves to empower users from this domain to reuse heterogeneous data sources, correlate them and conduct complex analyses to extract new research insight. In agreement with the FAIR principles, we work to make the offered data products and services computer-actionable, i.e., services will provide a FAIR application program interface (API). Based on an initial design of an architecture, RDC is developed incrementally, with the initial architecture becoming more specific and the first services of a reference implementation available. Selected components may be developed in cooperation with other NFDI consortia, and services will be continuously growing in number as the NFDI4Microbiota project progresses.

# Architecture
A brief overview of the RDC architecture is outlined in the attached figure. In order to manage the complexity of the RDC, we decided to organize the software architecture in layers and software components that interact with each other via well-defined interfaces. There are a total of four layers entitled:

* Cloud Layer
* Mediation Layer
* Semantic Layer
* Application Layer
* Management and Governance
* External Data Interfaces

![Architecture of the Research Data Commons]({{ '/assets/img/rdc.png' | relative_url }} "Architecture of the Research Data Commons"){:width="70%"}

The lower layers contain more technical functionality whereas the upper layers are primarily designed to end-users with domain knowledge. Each of the three lower layers consists of a few different technical components.

The **Cloud Layer** is the technical backbone based on a multi-cloud infrastructure including for example the de.NBI cloud and GDWG. These clould providers offer scalable functionality for distributed computing as well as cloud storage with near infinite resources such that users are empowered to run compute-intensive jobs or analyze very large data sets in a user-friendly way. In addition, there are cloud services like the Aruna Object Storage (AOS) for managing data in a unified model.

The **Mediation Layer** provides a self-service collection of community-agnostic tools for creating FAIR data products. A community-specific community, for example, a team that works together in one of the Use Case projects of NFDI4Microbiota, is responsible for a specific data product and also responsible for its development process. A community unterstands the purpose the data product under its responsibility is generally used for, e.g. specific analyses and annotations. In particular, a data product uses common terminology of a certain discipline or subdiscipline. The mediation layer offers tools for data product developers to manage metadata, transform data from a technical data model into a semantic model, and improve data quality. Workflows serve to describe the steps of creating the data product from the source data sets, and thus, it also documents the provenance of a data product.

The **Semantic Layer** provides the community-specific data products that are created and maintained in the Mediation Layer using the technical datasets accessible from the Cloud Layer and other data from interfaces to external data providers. The data products comply with the FAIR principles and are computer-actionable, i.e. a computer system is able to find and access them and understand the corresponding schema. Data products are either physically available or built on demand when the product is accessed. In addition, self-service collection of community-agnostic tools are provided, such as Jupyter notebooks, which enable domain experts to create, deploy, and maintain community-specific applications on top of these data products.

The **Application Layer** consists of concrete applications and services developed for end users. These services can be community-agnostic, such as a search tool for datasets, or community-specific, such as a data portal for dragonflies or other species of interest. Community-specific applications are built on top of the data products in the semantic layer, while community-agnostic applications can access data from different layers. For example, the search tool requires access to data from the Cloud Layer and the Semantic Layer.

In addition to these four layers, there are two other essential elements in the architecture. The first one **Management & Governance** features tools and policies to manage rules and access rights for the resources offered in the four horizontal layers, including user management and monitoring of usage of the technical resources. The second, called **External Data Interfaces**, features a collection of interfaces for accessing external data sets. Obviously, RDC requires connectivity to established large data providers without the need to manage copies of their data in the Cloud Layer.
