---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

{% for post in site.publications reversed %}
### {{ post.title }}

**Authors:** {{ post.authors }}

![{{ post.title }} figure]({{ post.image | prepend: base_path }})

{% endfor %}
