---
# Leave the homepage title empty to use the site title
title:
date: 2024-11-24
type: landing

sections:

  - block: hero
    content:
      title: Sustainable Power Systems Laboratory
      image:
        # Reference an image in your `assets/media/` folder
        filename: 
      # Add your Call-To-Action (CTA) button and optional icon
      cta:
        label: 
        url: 
        #icon_pack: fas
        #icon: download
      # Optionally, add an alternative CTA link
      cta_alt:
        label: 
        url: 
      # Optionally, add a note under the Call-To-Action button
      cta_note:
        label:       
      # Add your Hero text here
      text: |-
        <br>      
        <br>
        <br>
    design:
      css_class: dark
      # Choose an optional background color, gradient, image, or video
      background:
        image:
          # Add your image background to `assets/media/`.
          filename: img/pylons.jpg
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: true

  - block: markdown
    id: about
    content:
      title: About us
      subtitle: … and what we do
      text: The [group](people/) is led by Dr. {{% mention "p.-aristidou" %}} and is part of the [Department of Electrical Engineering and Computer Engineering and Informatics](https://www.cut.ac.cy/faculties/fet/eecei/?languageId=1) at the Cyprus University of Technology. <br> We work on making future electric power systems sustainable, secure, and resilient. Our research brings together mathematical tools from the areas of numerical analysis and optimization, with high performance computational tools and machine learning techniques, to tackle modern power system problems.
    design:
      # See Page Builder docs for all section customization options.
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '2'

  - block: markdown
    id: news
    content:
      title: Recent News
      subtitle: "[All news>>](./news)"
      text: |-
        {{< readfromfile "/content/newslist.dat" 5 >}} 
    design:
      # See Page Builder docs for all section customization options.
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '2'
 
  - block: collection
    id: posts
    content:
      title: Recent Posts
      text: ""
      count: 3
      filters:
        folders:
          - post
        publication_type: ''
    design:
      view: compact
      columns: '2'

  - block: portfolio
    id: projects
    content:
      title: Research
      subtitle: Some of our ongoing and past research projects and tools
      text: 
      filters:
        # Folders to display content from
        folders:
          - project
        # Only show content with these tags
        tags: []
        # Exclude content with these tags
        exclude_tags: []
        # Which Hugo page kinds to show (https://gohugo.io/templates/section-templates/#page-kinds)
        kinds:
          - page
      # Field to sort by, such as Date or Title
      sort_by: 'Date'
      sort_ascending: false
      # Default portfolio filter button
      # 0 corresponds to the first button below and so on
      # For example, 0 will default to showing all content as the first button below shows content with *any* tag
      default_button_index: 0
      # Filter button toolbar (optional).
      # Add or remove as many buttons as you like.
      # To show all content, set `tag` to "*".
      # To filter by a specific tag, set `tag` to an existing tag name.
      # To remove the button toolbar, delete the entire `buttons` block.
      buttons:
        - name: Themes
          tag: 'themes'
        - name: Current projects
          tag: Current projects
        - name: Software tools
          tag: Software tools
        - name: Past projects
          tag: Past projects
    design:
      # See Page Builder docs for all section customization options.
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '2'
      # Choose a listing view
      view: Showcase
      # For Showcase view, flip alternate rows?
      flip_alt_rows: false
  
  - block: collection
    id: publications
    content:
      title: Latest Publications
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: ''
    design:
      view: citation
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
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '2'
---
