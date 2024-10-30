---
title: FAIR Data Principles
category: Research-Data-Management
layout: default
docs_css: markdown
---

## Why FAIR Principles Matter in Microbiology

Microbes exhibit remarkable versatility, thriving in environments as varied as the human body and extreme habitats like deep-sea vents. Their interactions within these diverse environments have significant implications for medicine, biotechnology, and agriculture. As microbiology research becomes increasingly data-driven, leveraging advanced multi-omics technologies, it holds great promise but also presents certain challenges.
To fully leverage extensive (microbiological) data, it must be well-organized and carefully annotated. This involves adhering to best practices for data analysis, documenting data with comprehensive metadata, and ensuring it is shared in a way that ensures reusability and reproducibility. The FAIR principles—Findable, Accessible, Interoperable, and Reusable—offer a clear framework for effective data management, making data easier to use and share within the scientific community.

## What are FAIR Principles?

The FAIR data principles are a concise and measurable set of principles that may act as a guideline for those wishing to enhance the reusability of their data holdings. FAIR stands for Findable, Accessible, Interoperable and Reusable {% cite wilkinson_2016  %}. The FAIR data principles aims at {% cite wilkinson_2016 lowenberg_2021 %}:

* Improving the infrastructure supporting the reuse of scholarly data.
* Enhancing the ability of machines to automatically find and use data.
* Supporting the reuse of data by individuals, which “is essential to the advancement of research and clinical practice”.

![FAIR Data Principles]({{ '/assets/img/fair_principles_cropped.png' | relative_url }})

The principles {% cite wilkinson_2016 go_fair_2022 %} are reproduced below:

## To be Findable

* (Meta)data are assigned a globally unique and persistent identifier.
* Data are described with rich metadata.
* Metadata clearly and explicitly include the identifier of the data it describes.
* (Meta)data are registered or indexed in a searchable resource (e.g. data repository).

## To be Accessible

* (Meta)data are retrievable by their identifier using a standardized communications protocol (e.g. http(s)).
* The protocol is open, free, and universally implementable.
* The protocol allows for an authentication and authorization procedure, where necessary.
* Metadata are accessible, even when the data are no longer available.

## To be Interoperable 

Data interoperability is the ability of a dataset to work with other datasets or systems without special effort on the part of the user {% cite godan_action_2019_3588148 %}.

* (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation (e.g. controlled vocabularies/ontologies/thesauri, a good data model).
* (Meta)data use vocabularies that follow the FAIR principles (e.g. using FAIR Data Point).
* (Meta)data include qualified references to other (meta)data (e.g. specifying if one dataset builds on another one, properly citing all datasets).

## To be Reusable

* Meta(data) are richly described with a plurality of accurate and relevant attributes (i.e. metadata that richly describes the context under which the data was generated such as the experimental protocols, the species used).
* (Meta)data are released with a clear and accessible data usage license.
* (Meta)data are associated with detailed provenance.


## Challenges in Adopting FAIR Principles in Microbiology Research

Despite the advantages, some challenges exist in adopting FAIR principles in the field of microbiology. Researchers may encounter difficulties due to varying levels of awareness about data standards and where to deposit complex microbial data. Inconsistent reporting practices across the field can also pose challenges. Data sharing requirements (e.g. for journals, funding agencies) are not always comprehensive, sometimes focusing only on certain types of data, which can lead to variability in what is shared. The diversity of metadata, such as experimental and environmental conditions, can further complicate standardization efforts. Additionally, technical issues such as data quality and version management, combined with limited incentives for adherence to FAIR principles, may affect adoption {% cite huttenhower_2023 %}.

## Further resources
* Introducing the FAIR Principles for research software: [Barker *et al.* 2022](https://doi.org/10.1038/s41597-022-01710-x)

### Learning resources
* Course on FAIR in (biological) practice: [The Carpentries Incubator](https://carpentries-incubator.github.io/fair-bio-practice/)
* How to be FAIR with your data. A teaching and training handbook for higher education institutions: [Engelhardt *et al.* 2022](https://doi.org/10.5281/zenodo.6674301)
* Unit on the benefits and challenges associated with sharing research data openly: [The University of Edinburgh](https://mantra.ed.ac.uk/fairsharingandaccess/)

### How to make data FAIR?
* Guidelines to FAIRify data management and make data reusable: [PARTHENOS](https://doi.org/10.5281/zenodo.2668479)
* Preparing data for sharing: [Knight 2015](https://www.slideshare.net/lshtm/preparing-data-for-sharing-the-fair-principles)
* Recipes that help you to make and keep data FAIR: [FAIR Cookbook](https://faircookbook.elixir-europe.org/content/home.html)
* Top 10 FAIR Data & Software Things: [Martinez *et al.* 2019](https://doi.org/10.5281/zenodo.3409968)

### How to assess the FAIRness of your datasets?
* FAIR data maturity model indicators: [Bahim *et al.* 2020](https://doi.org/10.5334/dsj-2020-041), Table 1
* FAIR evaluator service: [Fraunhofer FIT](https://gitlab.fit.fraunhofer.de/abu.ibne.bayazid/fairevaluator)
* How FAIR are your data? [Jones and Grootveld 2017](https://doi.org/10.5281/zenodo.5111307)
* Self-Assessment Tool to Improve the FAIRness of Your Dataset ([SATIFYD](https://satifyd.dans.knaw.nl/)) 

## Get Help
If you have any further questions about the management and analysis of your microbial research data, please contact us: [helpdesk@nfdi4microbiota.de](mailto:helpdesk@nfdi4microbiota.de) (by emailing us you agree to the [privacy policy - in German](https://nfdi4microbiota.de/legals/privacy-policy.html) on our website: [Contact](https://nfdi4microbiota.de/contact-form/).)

## References
{% bibliography --cited_in_order %}
