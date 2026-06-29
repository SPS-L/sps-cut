+++
title = "Adaptive Reduced System Modeling for Real-time Dynamic Simulations"
date = "2026-06-29"
authors = ["S. Eleftheriadis","M. Hashemnezhad","S. Panagi","T. Vermeulen","G. Joseph","P. Aristidou"]
tags = ["Adaptive model reduction", "Critical area identification", "Large-scale power systems", "Machine learning", "posydys26"]
publication_types = ["paper-conference"]
publication = "Power System Dynamic Summit (PoSyDyS 2026)"
publication_short = ""
abstract = "Real-time dynamic simulation requires that each simulated time interval complete within the equivalent wall-clock CPU time, a strict budget that large power system models, with hundreds of thousands of state variables, cannot meet. Existing model reduction methods either sacrifice internal network detail, are valid only near a fixed operating point, or cannot adapt to changing contingencies online. This paper proposes an Adaptive Model Selection (AMS) framework that automatically reduces a full-detail dynamic model to a smaller, contingency-specific model by identifying which substations require full fidelity and simplifying the rest. Given the pre-disturbance operating state and event location, a pair of Graph Attention Network (GAT)-based ordinal predictors classify each component’s expected dynamic activity level; substations predicted to be inactive are simplified from node-breaker to bus-breaker representation. Applied to a realistic French transmission network model (over 6,000 buses), AMS reduces continuous and discrete model variables by approximately 60%, achieves up to 2.6x simulation speedup, and maintains trajectory errors below the numerical solver tolerance, demonstrating a practical route toward real-time operation of large-scale dynamic simulation."
summary = ""
featured = false
projects = ['traisim']
slides = ""
doi = ""
url_code = ""
url_dataset = ""
url_poster = ""
url_slides = ""
url_source = ""
url_video = ""
math = true
highlight = true
[image]
image = ""
caption = ""
+++
