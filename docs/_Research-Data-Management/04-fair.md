---
title: FAIR Data Principles
category: Research-Data-Management
layout: default
docs_css: markdown
---
# Introduction

The FAIR data principles are a concise and measurable set of principles that may act as a guideline for those wishing to enhance the reusability of their data holdings. FAIR stands for Findable, Accessible, Interoperable and Reusable {% cite wilkinson_2016  %}. The FAIR data principles aims at {% cite wilkinson_2016 lowenberg_2021 %}:

* Improving the infrastructure supporting the reuse of scholarly data.
* Enhancing the ability of machines to automatically find and use data.
* Supporting the reuse of data by individuals, which “is essential to the advancement of research and clinical practice”.

![FAIR Data Principles](/assets/img/fair_principles_cropped.png)

The principles {% cite wilkinson_2016 go_fair_2022 %} are reproduced below:

# To be Findable

* (Meta)data are assigned a globally unique and persistent identifier.
* Data are described with rich metadata.
* Metadata clearly and explicitly include the identifier of the data it describes.
* (Meta)data are registered or indexed in a searchable resource (e.g. data repository).

# To be Accessible

* (Meta)data are retrievable by their identifier using a standardized communications protocol (e.g. http(s)).
* The protocol is open, free, and universally implementable.
* The protocol allows for an authentication and authorization procedure, where necessary.
* Metadata are accessible, even when the data are no longer available.

# To be Interoperable 

Data interoperability is the ability of a dataset to work with other datasets or systems without special effort on the part of the user {% cite godan_action_2019_3588148 %}.

* (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation (e.g. controlled vocabularies/ontologies/thesauri, a good data model).
* (Meta)data use vocabularies that follow the FAIR principles (e.g. using FAIR Data Point).
* (Meta)data include qualified references to other (meta)data (e.g. specifying if one dataset builds on another one, properly citing all datasets).

# To be Reusable

* Meta(data) are richly described with a plurality of accurate and relevant attributes (i.e. metadata that richly describes the context under which the data was generated such as the experimental protocols, the species used).
* (Meta)data are released with a clear and accessible data usage license.
* (Meta)data are associated with detailed provenance.

# Further resources
* Introducing the FAIR Principles for research software: [Barker *et al.* 2022](https://doi.org/10.1038/s41597-022-01710-x)

## Learning resources
* Course on FAIR in (biological) practice: [The Carpentries Incubator](https://carpentries-incubator.github.io/fair-bio-practice/)
* How to be FAIR with your data. A teaching and training handbook for higher education institutions: [Engelhardt *et al.* 2022](https://doi.org/10.5281/zenodo.6674301)
* Unit on the benefits and challenges associated with sharing research data openly: [The University of Edinburgh](https://mantra.ed.ac.uk/fairsharingandaccess/)

## How to make data FAIR?
* Guidelines to FAIRify data management and make data reusable: [PARTHENOS](https://doi.org/10.5281/zenodo.2668479)
* Preparing data for sharing: [Knight 2015](https://www.slideshare.net/lshtm/preparing-data-for-sharing-the-fair-principles)
* Recipes that help you to make and keep data FAIR: [FAIR Cookbook](https://faircookbook.elixir-europe.org/content/home.html)
* Top 10 FAIR Data & Software Things: [Martinez *et al.* 2019](https://doi.org/10.5281/zenodo.3409968)

## How to assess the FAIRness of your datasets?
* FAIR data maturity model indicators: [Bahim *et al.* 2020](https://doi.org/10.5334/dsj-2020-041), Table 1
* FAIR evaluator service: [Fraunhofer FIT](https://gitlab.fit.fraunhofer.de/abu.ibne.bayazid/fairevaluator)
* How FAIR are your data? [Jones and Grootveld 2017](https://doi.org/10.5281/zenodo.5111307)
* Self-Assessment Tool to Improve the FAIRness of Your Dataset ([SATIFYD](https://satifyd.dans.knaw.nl/)) 

# References

{% bibliography --cited_in_order %}
