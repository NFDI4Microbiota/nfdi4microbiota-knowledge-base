---
title: Licenses
category: Research-Data-Management
layout: default
docs_css: markdown
---


# Introduction
In order to make data and software more accessible, licenses are an important tool to ensure what can be used for what.
By default any creator of data, software, writing or any other content involving a sufficient amount of creativity is the copyright owner of that content without having to declare the copyright explicitly.
Defining or using a suitable license for published content usually has the benefit of giving all parties legal certainty and understanding of permission to use.

In sciences, two categories of licenses can applied to either software or data and results that explicitly describe whether and how others can use it.

# Properties of recommendable licenses
* Standardized, i.e. machine-readable, text
* Available in an easy-to-read version
* No transfer of exclusive rights
* Compatible with many jurisdictions
* Common

# Licenses for data and other creative works
Also scientific data and output are subject to copyright if their generation requires a sufficient amount of creativity (this might be contested in some contexts).
However, since scientists conduct experiments mostly within their employment of their funding institution, the copyright lies with both and should ideally be discussed with the employer (the universities legal department) in high profile cases.

Similar to the publication of source code, a license communicates who can use the data or results for what and should be distributed with the publication in repositories or databases.

Publishing figures and articles in journals, usually requires accepting the license agreement of the publisher and involves either a complete transfer of rights on your own work or picking an open access journal with acceptable permissive licenses.


## Recommendations
Because publicly funded sciences should make their data and results publicly available (often required by the employer or funder), choosing a permissive license is highly encouraged.

The [same criteria as for software](#software-licenses) apply and the [Creative Commons (CC)](https://creativecommons.org) licenses are most widely used as well as easily understandable.

There are different versions of CC that consist of the core license with further extensions to [choose from](https://creativecommons.org/choose) that can be combined to achieve the desired permissions:

- **Public dedication (Zero or 0):** Allows re-users to distribute, remix, adapt, and build upon the material in any medium or format, with no conditions. Excludes the following extensions.
- **Attribution (BY):** Credit must be given to the creator.
- **Share-Alike (SA):** Adaptations must be shared under the same terms.
- **Non-commercial (NC):** Only non-commercial uses of the work are permitted.
- **Non-derivative (ND):** No derivatives or adaptations of the work are permitted (not compatible with share-alike).


![ccsprectrum]({{ '/assets/img/Creative_commons_license_spectrum.svg' | relative_url }})

([Source](https://commons.wikimedia.org/wiki/File:Creative_commons_license_spectrum.svg), CC-BY Shaddim; original CC license symbols by Creative Commons)


## Usage
Creators can declare a works license by selecting it during upload to a website/database/repository or attaching a line stating the title, author and license to the published work.

Here we look at some examples of license usage, found on [Zenodo](https://zenodo.org/).

### CC BY 4.0 example usage
We are going to be looking at two examples here: 
1. [Metagenome-assembled genomes (MAGs), colorectal cancer (CRC)](https://zenodo.org/records/7008911) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7008911.svg)](https://doi.org/10.5281/zenodo.7008911)
2. [Metagenome assemblies and metagenome-assembled genomes from the Daphnia magna microbiota](https://zenodo.org/records/4435010) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4435010.svg)](https://doi.org/10.5281/zenodo.4435010)

Both datasets have been submitted to Zenodo under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/). That means that the data that has been deposited is free to share and free to redistribute (including commercially) in any format or medium. It also enables the data user to build upon or transform it for any purpose (including commercial use). However, the license requires the data user to give appropriate credit to the submitter/data generator. In addition, the user must also provide a link to the license and disclose any changes made when licensing their work when derived from work already under license.

### CC0 example usage
We are going to be looking at two examples here:
1. [Data from: Mining for NRPS and PKS genes revealed a high diversity in the Sphagnum bog metagenome](https://zenodo.org/records/4976456) [![DOI](https://zenodo.org/badge/DOI/10.5061/dryad.hf56v.svg)](https://doi.org/10.5061/dryad.hf56v)
2. [Data from: Generational conservation of composition and diversity of field-acquired midgut microbiota in Anopheles gambiae sensu lato during colonization in the laboratory](https://zenodo.org/records/5001400) [![DOI](https://zenodo.org/badge/DOI/10.5061/dryad.98jj7gk.svg)](https://doi.org/10.5061/dryad.98jj7gk)

Both datasets have been submitted to Zenodo under the  [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/). That means that the data that has been deposited is in the public domain. That implies that the data deposited can be copied, modified, distributed, and used even for commercial purposes, and the depositor/generator of the data waives their right to the work. The user of data does not need to seek the permission of the data/material submitter or generator.

# Software licenses
When software sources are distributed, it is considered good practice to specify an already established license under which it can be used.
Software developed in the context of science and funded by public money, usually needs to be made available free of charge and in open source by requirements of the funder or the governing institution's policies.


## Recommendations
When choosing a license, multiple aspects should be regarded depending on its application and intention:

- **Standardized:** While you can formulate your own license or freely modify most available licenses to better suit your needs, keep in mind that anyone interested in using/supporting/modifying your software needs to be familiar with the terms and in doubt has to read it.
Choosing a popular license communicates the terms to third parties extremely efficiently, because the terms and consequences are widely known.
Using fringe licenses or wording your own can unintentionally put you or others in hot legal waters down the line.
- **Easy to understand:** While legal texts (including licenses) can be worded quite awkwardly in order to be legally precise, you should try to choose a license that you yourself can read and understand easily.
This also implies that short licenses are favorable, since a single paragraph can be comprehended more easily than a multi-page document of clauses and eventualities.
- **Permissive:** Unless you have a certain intention or conviction that your software should not be used in specific circumstances where you do not want somebody to modify your software or want them to use it for commercial purposes, you should choose *permissive* licenses over restrictive.
Prominent somewhat restrictive examples are GNU GPL conform licenses that employ so-called "copyleft", a restriction that requires derivative works to use the same license.
What sounds like a good, viral mechanism to enforce free and open software can result in problems down the line.
Once a work has been put under such a license, it is often considered impractical and thus untouchable by commercial or more permissively minded entities.

Going by the above criteria, the following licenses are particularly recommended:

- [MIT](https://choosealicense.com/licenses/mit/)
- [BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)

Both basically allow anyone to do whatever with the software (sell, modify) as long as the original license and copyright is redistributed along with the software/sources.
The text is also a disclaimer that states software is distributed "as is" without warranties.

An exhaustive list of generally recommended licenses for Open Source is curated by the [Open Source Initiative](https://opensource.org/licenses).


## Usage
Typically, developers or distributors add a plain-text file called `LICENSE` to the source code or binary of their software that contains the chosen license text.
Especially source repositories like github or gitlab will allow you to choose a license per project and automatically adding such a `LICENSE` file to the source code.
The benefit of selecting a license on the code hosting platform is the machine readable interpretation of your permissions which can potentially increase visibility in search results across the platform.

# Further resources

- [Creative Commons license chooser](https://creativecommons.org/choose): Explanations and guide to choosing CC licenses for your work.
- [tl;drLegal](https://tldrlegal.com/): Software licenses in plain English with a short feature list.
- [ChooseALicense](https://choosealicense.com/licenses/): Simple but incomplete recommendation for software licenses with short feature lists.
