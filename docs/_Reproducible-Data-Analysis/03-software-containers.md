---
title: Software containers
category: Reproducible-Data-Analysis
layout: default
docs_css: markdown
empty: true
---

# Software Containers

## Introduction to Software Containers
Software containers, such as [Apptainer](https://apptainer.org/) (formerly known as Singularity) and [Docker](https://www.docker.com/) provide a way to encapsulate an application and its environment for consistent, portable, and reproducible execution across various computing environments.
This is crucial for scientific research, ensuring that analyses remain consistent regardless of the underlying infrastructure.

## Why Use Software Containers?
- **Consistency and Reproducibility**: Containers ensure your analysis runs the same way, everywhere.
- **Isolation**: Package your application with its dependencies to avoid conflicts.
- **Portability**: Easily share your computational environment with others.

## Getting Started with Containers
Apptainer is a popular choice in scientific and high-performance computing (HPC) environments due to its ability to handle container privileges.
It offers secure, user-friendly containerization, making it ideal for computational biology and bioinformatics.
Based on the same technology, Docker images are compatible with Apptainer and most commands function similarly.

NFDI4Microbiota recommends that researchers start out with Apptainer if you are not bound to a docker environment, because it is usually much easier and nudges you to follow the [best practices] by default.

For installation and quick start, always refer to the main documenation page from the containirazation software of choice.

[Apptainer Quick Start](https://apptainer.org/docs/user/latest/quick_start.html)
[Docker Quick Start](https://docs.docker.com/guides/get-started/)


## Example of Working with Containers

### Apptainer
To start getting an idea what a container actually is, it is relevant to get some examples.
A good example of a software available as a apptainer container is [Virsorter2](https://github.com/jiarong/VirSorter2), a multi-classifier with an expert-guided approach to detect diverse DNA and RNA virus genomes.

Running VirSorter2 using Apptainer looks like:
```sh
$ apptainer build virsorter2.sif docker://jiarong/virsorter:latest
```
You will get a file `virsorter2.sif`, which is a apptainer image that can be run like a binary executable file.
You can use the absolute path of this file to replace Virsorter2 in commands.
Also this image has the database and dependencies included, so you can skip the download of databases and dependencies.

### Docker
Similarly with Docker, the user can find an example of running BLAST [here](https://biocontainers-edu.readthedocs.io/en/latest/running_example.html)


## Best Practices for Container Creation {best-practices}
When creating containers, incorporating best practices ensures efficiency, security, and reproducibility. Here's a concise guide, drawing from broader container best practices, including insights from [Google Cloud's recommendations](https://cloud.google.com/architecture/best-practices-for-building-containers):

- **Use Specific Versions**: Specify exact versions of base images, software, and libraries, in order to avoid breaking changes occuring when updating with the `latest` tag and ensures consistency across environments.

- **Minimize Layer Size**: Structure your definition file to combine related commands into single layers to reduce the container size which speeds up download and deployment.

- **Clean Up**: Remove unnecessary packages and clear cache in the same layer where installations occur to minimize the container's footprint.

- **Non-root User**: Run the container as a non-root user whenever possible, which enhances the security of the container, reducing the risk of privilege escalation attacks.

- **Base Image Selection**: Choose a minimal base image that includes only the necessary packages and libraries for your application, to minimizes the attack surface and the container size.

- **Immutable Containers**: Treat containers as immutable.
For updates or changes, build a new container image.
This facilitates modularity and version control while ensuring reproducibility.

- **Security Scanning**: Regularly scan your containers for vulnerabilities and apply patches as needed.
Keeping your containers updated is crucial for security.

- **Efficient Data Management**: Store data and logs outside of containers to ensure persistence and scalability.
Use volumes or bind mounts for data that needs to persist beyond the life of the container.

- **Documentation**: Include a `%help` section in your definition file, providing users with information on how to use the container, including running the software and accessing data.


## Advanced Usage
#### [Integration with Nextflow](https://www.nextflow.io/docs/latest/container.html)
- **Nextflow and Containers**: Simplifies complex workflows by executing each step in a container for consistency across environments.
- **Configurations**: Supports managing containers through `nextflow.config`, streamlining execution.

#### [Kubernetes and Containers](https://kubernetes.io/docs/home/)
- **Container Orchestration**: Automates deployment, scaling, and management of containerized applications, essential for microservices architecture.
- **Scalability and Management**: Provides tools for load balancing, auto-scaling, and efficient resource allocation across diverse infrastructures.

# Get Help
If you have any further questions about the management and analysis of your microbial research data, please contact us: [helpdesk@nfdi4microbiota.de](mailto:helpdesk@nfdi4microbiota.de) (by emailing us you agree to the privacy policy on our website: [Contact](https://nfdi4microbiota.de/contact-form/))

## Resources and Further Reading
- [Apptainer User Guide](https://apptainer.org/docs/user/latest/introduction.html): Comprehensive documentation for getting started with Apptainer.
- [BioContainers Community](https://biocontainers.pro/): A resource for finding and sharing containerized bioinformatics tools.
- [Docker Introduction Lesson (Beta version)](https://carpentries-incubator.github.io/docker-introduction/)
- [Singularity Introduction (Alpha version)](https://carpentries-incubator.github.io/singularity-introduction/)
