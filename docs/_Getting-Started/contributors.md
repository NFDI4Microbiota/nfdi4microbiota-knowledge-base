---
title: List of contributors
category: Getting-Started
layout: default
docs_css: markdown
---

The following list contains the names of the contributors in alphabetical order. If a new name is to be added, please simply add it in the correct place.

{% assign contributors_list = "" | split: "" %}
{% for pair in site.data.contributors %}{% assign contributors_list = contributors_list | push: pair[1] %}{% endfor %}
{% assign sorted_contributors = contributors_list | sort: "name" %}
<ul>
{% for c in sorted_contributors %}<li>{{ c.name }}{% if c.orcid %} (ORCID ID: <a href="https://orcid.org/{{ c.orcid }}">{{ c.orcid }}</a>){% endif %}</li>
{% endfor %}</ul>
