---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

<ul>
{% assign pubs = site.publications | sort: "date" | reverse %}
{% for pub in pubs %}
  <li>
    <p><strong>Title:</strong> {{ pub.title }}</p>
    <p><strong>Authors:</strong> {{ pub.authors }}</p>
    <p><strong>Abstract:</strong> {{ pub.content | markdownify | strip_html | strip_newlines | replace: '  ', ' ' | strip }}</p>
    <p><strong>Venue:</strong> {{ pub.venue }}</p>
  </li>
{% endfor %}
</ul>
