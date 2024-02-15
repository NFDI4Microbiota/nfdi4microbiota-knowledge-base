---
title: Research Data Commons (RDC)
category: Standard-Operating-Procedures
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

![Architecture of the Research Data Commons](/nfdi4microbiota-knowledge-base/assets/img/rdc.png "Architecture of the Research Data Commons").
