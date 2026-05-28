---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

<ul style="list-style: none; padding: 0;">
{% assign pubs = site.publications | sort: "date" | reverse %}
{% for pub in pubs %}
  <li style="margin-bottom: 2.5em; border-bottom: 1px solid #eee; padding-bottom: 2em;">
    <p style="margin-bottom: 0.3em;"><strong>{{ pub.title }}</strong></p>
    <p style="margin-bottom: 0.3em; font-style: italic; color: #555;">{{ pub.authors | replace: "Xiangyu Yin", "<strong>Xiangyu Yin</strong>" }}</p>
    <p style="margin-bottom: 0.3em;">{{ pub.content | markdownify | strip_html | strip_newlines | replace: '  ', ' ' | strip }}</p>
    <p style="margin-bottom: 0.6em; color: #888;"><em>{{ pub.venue }}</em></p>
    {% if pub.image %}
    <img src="{{ pub.image }}" alt="{{ pub.title }}" style="width: 100%; max-height: 320px; object-fit: contain; background: #fff; border: 1px solid #eee; border-radius: 4px; display: block;">
    {% endif %}
  </li>
{% endfor %}
</ul>
