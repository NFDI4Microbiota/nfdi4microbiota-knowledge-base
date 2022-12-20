serve:
	bundle exec jekyll serve --trace

build:
	bundle install

check_links:
	python utils/check_links.py
