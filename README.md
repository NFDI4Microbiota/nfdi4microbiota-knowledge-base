# NFDI4Microbiota Knowledge Base

[![CC BY 4.0][cc-by-shield]][cc-by]
[![Deployment to production](https://github.com/NFDI4Microbiota/nfdi4microbiota-knowledge-base/actions/workflows/deploy_to_denbi_server.yml/badge.svg)](https://github.com/NFDI4Microbiota/nfdi4microbiota-knowledge-base/actions/workflows/deploy_to_denbi_server.yml)
## What is the NFDI4Microbiota Knowledge Base

This knowledge base is a collection of documents and references important to the [NFDI4Microbiota](https://nfdi4microbiota.de/) consortium. It is also a collection of internal and external knowledge we wish to share with the Microbiota research community, and we welcome any contributions by them.

## Contributing to the Knowledge Base

If you want to contribute to the Knowledge Base, please see the [contributing.md](https://github.com/NFDI4Microbiota/nfdi4microbiota-knowledge-base/blob/main/docs/_Getting-Started/contributing.md) file, and be sure to add yourself to the [contributors.md](https://github.com/NFDI4Microbiota/nfdi4microbiota-knowledge-base/blob/main/docs/_Getting-Started/contributors.md) file.

## Workflow

You should create branches from the dev branch, and create pull requests for the dev branch when you're done. Changes on the dev branches can be seen here: https://dev.knowledgebase.nfdi4microbiota.de/

## Running the Knowledge Base locally

### Ubuntu/Debian (Linux) and Mac

1. Install [Ruby](https://www.ruby-lang.org/en/downloads/) (2.7.0 or higher): `sudo apt install ruby-full`
2. Install [GCC](https://gcc.gnu.org/install/) and [Make](https://www.gnu.org/software/make/): `sudo apt install build-essential`
3. Install required gems: `make build`
4. Create the knowledge base: `make serve`
5. Go to `localhost:4000` on your web browser

### Windows
1. Install RubyInstaller and with it Jekyll as shown [here](https://jekyllrb.com/docs/installation/windows/)
2. Clone the KB git repository into your chosen folder and open that folder with your favorite IDE.
3. Run `bundle install` to install missing gems.
4. Start a local server by running: `bundle exec jekyll serve`
5. Open your browser and go to: `http://127.0.0.1:4000/`

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
