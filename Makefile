# Search index is built once up front; rerun `make serve` to reindex after content changes
serve:
	bundle exec jekyll build
	npx -y pagefind@1.5.2 --site _site
	bundle exec jekyll serve --trace

build:
	bundle install

check_links:
	python utils/check_links.py
