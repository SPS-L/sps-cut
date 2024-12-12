---
# Leave the homepage title empty to use the site title
title:
date: 2024-11-24
type: landing

sections:
  - block: hero
    content:
      title: |
        About us
      image:
        filename: pylon2.jpg
      text: |
        <br>
        
        The [group](people/) is led by Dr. {{% mention "p.-aristidou" %}} and is part of the [Department of Electrical Engineering and Computer Engineering and Informatics](https://www.cut.ac.cy/faculties/fet/eecei/?languageId=1) at the Cyprus University of Technology.
        
        We work on making future electric power systems sustainable, secure, and resilient. Our research brings together mathematical tools from the areas of numerical analysis and optimization, with high performance computational tools and machine learning techniques, to tackle modern power system problems.
  
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '2'
  
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: coders.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

  - block: collection
    content:
      title: Latest Preprints
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: ''
    design:
      view: citation
      columns: '2'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '2'

  - block: contact
    id: contact
    content:
      title: Contact
      subtitle: ''
      text: ''
      # Contact details - edit or remove options as needed
      email: info@sps-lab.org
      phone: +357 25 002618
      address:
        street: 33 Saripoloy str
        city: Limassol
        region: 
        postcode: '3036'
        country: Cyprus
        country_code: CY
      coordinates:
        latitude: '34.6752303'
        longitude: '33.0432417'
      directions: Enter Ttofis building, head to 5th floor, office 521B
      # Automatically link email and phone or display them just as text?
      autolink: true
      # Choose an email form provider (netlify/formspree)
      form:
        provider: netlify
        formspree:
          # If using Formspree, enter your Formspree form ID
          id: ''
        netlify:
          # Enable CAPTCHA challenge to reduce spam?
          captcha: false
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '2'
---
