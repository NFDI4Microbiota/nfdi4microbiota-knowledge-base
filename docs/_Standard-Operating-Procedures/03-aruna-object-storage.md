---
title: Aruna Object Storage (AOS)
category: Standard-Operating-Procedures
layout: default
docs_css: markdown
---

# Abstract
Aruna Object Storage (AOS) is a modern distributed storage platform designed to meet the increasing demand for effective data management and storage of scientific data. It is the central storage of the [Research Data Commons (RDC)](02-research-data-commons) cloud layer and the data foundation for the upper layers. It is a cloud-native, scalable system with an API and a S3-compatible interface. It allows resource organization into Objects, Datasets, Collections and Projects. Additionally, it provides an event-driven architecture which enables automation, data validation and improves accessibility and reproducibility of scientific results. AOS is open-source and available at [https://aruna-storage.org](https://aruna-storage.org).

# Factsheet
* ![Aruna Object Storage Logo](/nfdi4microbiota-knowledge-base/assets/img/aruna_dark_font.png "Aruna Object Storage Logo").
* Status: V2.x BETA, V1.x deprecated
* Current Version: V2.0.x beta
* Weblink: [https://aruna-storage.org](https://aruna-storage.org)
* Keywords:  data management, storage, FAIR, multi-cloud, cloud-native, data mesh
* RDC Integration: integrated or connected

# Overview
AOS is a fast, secure and geo-redundant data storage. It offers a sophisticated metadata management according to the FAIR principles. It builds the foundation for RDCs mediation and semantic layer and and handles all stored data objects secure, and data-agnostically.

AOS key features are:
* Data storage - Easily store large volumes of arbitrary data.
* Metadata enrichment - Enrich and group a user's data and metadata together for easier access and better organization.
* Secure Storage - Secure data storage from the moment of upload.
* FAIR - All data is managed according to the FAIR principles.
* Easy Sharing - Flexible data sharing made easy with flexible presigned URLs.
* Effortless Migration - Effortless migration from other cloud storage providers such as AWS (Amazon Web Services) thanks to the S3 compatible interface.

Storing data in localized, domain-specific data silos has limited use for collaboration, reuse and data analysis. AOS offers significant benefits for research data in NFDI4Biodiversity. These benefits include improved collaboration, compliance with FAIR principles, scalability, robust data security and seamless integration with existing systems and workflow tools. Ultimately, this facilitates scientific progress and enhances the quality of our research.

![Aruna Object Storage Concept](/nfdi4microbiota-knowledge-base/assets/img/concept_aruna.png "Aruna Object Storage Concept")
