---
title: Contributing to the NFDI4Microbiota Knowledge Base
category: Getting-Started
layout: default
docs_css: markdown
---



This document contains instructions on how to contribute to the Knowledge base and is intended for contributors with no prior GitHub experience. Feel free to skip to the appropriate section if you feel like you are an experienced user.

The main steps a user must follow to contribute to the Knowledge Base are:

1. Create a GitHub account
2. Make changes to files in the repository:
    - Edit existing files *or*
    - Create new files
3. Add your name to the [03-contributors.md](https://github.com/NFDI4Microbiota/nfdi4microbiota-knowledge-base/blob/main/docs/_Getting-Started/03-contributors.md) file

## Create a GitHub account

Users will need a GitHub account if they wish to contribute to the Knowledge Base. If you do not already have an account, go to the GitHub [homepage](https://github.com/) and click the `Sign Up` button to create one. Then follow the instructions. Once you have created an account, and signed in, go to the [Knowledge Base repository](https://github.com/NFDI4Microbiota/nfdi4microbiota-knowledge-base.github.io)

## Make changes to the repository

### Edit existing files

In order to make changes to the respository, users must edit Markdown files in the GitHub editor. If you have never used Markdown files before, [here](https://www.markdowntutorial.com/) is a link to a markdown tutorial. If you just need to look up syntax, follow this [link](https://www.markdownguide.org/basic-syntax/).

*Note: Markdown files are files which end with the `.md` suffix for example, this `02-Contributing.md` file. Please do not try to edit non Markdown files.*

To edit an existing file:

1. Navigate to the file on the repository and click on it
2. Click on the pen icon on the top right to begin editing
3. After editing the file, add a commit name that includes the name of the edited file and the [issue number](#github-issues) (if available) e.g. `#32 fixed typo in RDM page`
4. Select the `Create new branch` option and add a branch name which includes the name of the edited file and the [issue number](#github-issues) (if available)
5. Press the `Propose changes` button
6. Write a comment briefly describing the changes you have made
   1. If you are working on a page related to Research Data Management (RDM), assign @jvddorpe (Justine Vandendorpe) as a reviewer
   2. If you are working on a page related to Workflows, assign @KK-NFDI (Kassian Kobert) as a reviewer.
7. Assign the pull request to `Mahdi Robbani`
8. Press the `Create pull request` button

[Here](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files) is a guide to editing files on GitHub if you need futher help.

*Note: All files should be edited according to the [style guide](#markdown-style-guide).*

### Create new files

If you want to create a page on the website that doesn't already exist, create a new issue.

#### GitHub Issues

A [GitHub Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) is a way to keep track of changes we want to make to the repository. Anyone can create an issue if they think a new page should be created or if they desire any changes to a page. These can be seen in the `Issues` tab at the top of the page. All issues have an associated issue number e.g. #32 and if this number is used in commit messages, those changes then appear in the issue, making it easier to see what changes a page has undergone.

To create a new issue:

1. Go to the [issues page](https://github.com/NFDI4Microbiota/nfdi4microbiota-knowledge-base.github.io/issues)
2. Click the `New issue` button
3. Add the title (the name of the suggested page) and add a description of what you want to include in the new page
4. Assign the issue to `Mahdi Robbani`
5. Click the `Submit new issue` button

[Here](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue) is a guide on creating issues on GitHub if you need further help.

## Add your name to the CONTRIBUTORS file

We appreciate your contribution! Please add your name to the [03-contributors.md](https://github.com/NFDI4Microbiota/nfdi4microbiota-knowledge-base/blob/main/docs/_Getting-Started/03-contributors.md) file.


## Contribution Rules

When adding or editing files, please observe the following rules:

1. Use respectful and inclusive language
2. Use American English
3. Keep the content factual
4. Reference sources appropriately (see below)
5. Use a single `#` for the main file heading and use `##`, `###`, etc, for all subheadings
6. Place image files in the `assets/img/` directory

*Note: we might edit your contribution to homogenize the writing style.*

## Cite sources

1. Websites can be linked in the text (e.g. [NFDI4Microbiota](https://nfdi4microbiota.de/)).
2. Journal articles can be referenced at the bottom of the page, as in a regular scientific journal.
3. In order to reference an article:
   1. Add the reference to the `docs/_bibliography/references.bib` file in Bibtex format
   2. Cite the reference in the text using `{% raw %}{% cite <reference_name> %}{% endraw %}`
