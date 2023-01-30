---
title: Workflow Guidelines
category: Reproducible-Data-Analysis
layout: default
docs_css: markdown
redirect_from: /Reproducible-Data-Analysis
---

## Introduction

This page should give an overview of suggested standards for workflows. Not all points are applicable to, or reasonable for, all situations. Thus, the following suggestions should be taken as guidelines for good workflow practices, not strict requirements. In this context, we consider a workflow to be a pipeline of programs for data processing.

## FAIR Principles for Data management

In NFDI4Microbiota, we aim to follow the FAIR principles for data management (see [here](https://nfdi4microbiota.github.io/nfdi4microbiota-knowledge-base/RDM/03-fair) for more details).
In essence, data should be Findable, Accessible, Interoperable, and Reusable.
For workflows this means, data and/or results in the form of processed data should (if possible):

- Should easily be deposited to public data repositories
- Follow commonly accepted data formats
- Contain all relevant (meta-)data for reuse

E.g. See [here](https://ena-docs.readthedocs.io/en/latest/submit/assembly/metagenome/mag.html) for submitting a metagenome-assembled genome to the “European Nucleotide Archive” ([ENA](https://www.ebi.ac.uk/ena/browser/home) )
Also consider uploading/providing intermediate results, if the pre-processing done by the workflow is time-consuming and the data is of broad interest.

## Accessibility of the Workflow
Similar to data, the workflow itself should be accessible and (re-)usable by a broad user-base.
In particular, this means the workflow should:  

- Make use of an established, well documented, workflow-engine such as [nextflow](https://www.nextflow.io/) or snakemake.
- Be licensed under a permissive license.
- Not make use of proprietary software in the pipeline (or work without it).
- Be made available for download (e.g. on [GitHub](https://github.com/) ) and/or execution.
- If you are maintaining the workflow and offering support to users, supply a way to contact help/support.

## Documentation

Any workflow should be well documented. (e.g. via a README.md or wiki etc.). This includes documentation on different levels. In particular, a workflow should:

- Have a concise high level documentation describing the overall goal of the workflow and the type of addressed problem.
- Contain a detailed description of input parameters and generated output.
- Describe each workflow step and its resource requirements (c.f. Technical requirements).
- Have sufficient/extensive source code documentation.
- Ideally contain some kind of stripped down demo input-data that allows a user to test the workflow with minimal effort and required resources. This is meant in a similar sense as  the demo datasets of R/Bioconductor packages.
- As a recommendation: Have a graphical representation of the workflow as part of the user documentation.

## Reproducibility

Ideally, results obtained with the workflow should be reproducible. That is, given the same input data and same parameters, the same version of a workflow should always produce the same result. This requirement is non-trivial. Using different versions of the underlying tools, (unseeded) random results, different operating systems, or even different resolutions for race conditions can all result in different output for a given workflow. Containerization is a good way to address some of these concerns.
Thus, a good workflow should:

- Be implemented/supplied by making use of containerization (e.g. using [Docker](https://www.docker.com/resources/what-container/)) or similar
- Be versioned according to [semantic versioning](https://semver.org/)
- Note the used parameters and tool versions as part of the output
- Use and note seeds used for randomized steps in the pipeline (if possible)

## Quality Control

A good workflow should consistently produce good results. For this reason, we propose the following quality control measures. Workflows should:

- Set reasonable default parameters, such that standard use-cases require minimal adjustment
- Allow for (optional) preprocessing for quality control
- Note the quality as part of the results, such that one can estimate how reliable the results are
- Be supplied alongside a simple test case and matching expected result, such that the continued validity of the workflow can be verified (e.g. as part of a CI/CD process)

## Technical requirements

Execution of workflows on Slurm based clusters is directly supported in the nextflow as well as snakemake workflow engines. However, for running smoothly, in particular on a larger scale, well designed workflow should follow the subsequent recommendations:

- Specify the required resources in each workflow step's executor as accurately as possible. E.g. A memory demanding assembly step should also request an appropriate amount of memory to guarantee that the workflow engine schedules the job to a cluster node fulfilling the memory demands.
- Minimize the dependencies of your workflow on the execution environment and make your workflow as self-contained as possible by using containerization.
- Make sure that in case of an error, correct return/error codes are set and meaningful error messages are written to STDERR.
- Make sure that your workflow is as robust as possible. This also addresses (input-)parameter checking and appropriate error handling.
- If your workflow reads large input data it should be possible to read such data directly from an S3 bucket by providing bucket URI and credentials.
- It should also be possible to directly write all outputs to an S3 bucket.
