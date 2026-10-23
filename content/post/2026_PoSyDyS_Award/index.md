---
title: "Best Paper Award at PoSyDyS 2026 for Stefanos Eleftheriadis"
subtitle: ""
summary: "PhD candidate Stefanos Eleftheriadis received the Best Paper Award at the Power System Dynamics Summit (PoSyDyS 2026) in Graz for work on adaptive model reduction for real-time dynamic simulation, carried out within the TRAISIM project."
authors: ["s.-eleftheriadis"]
tags: ['posydys26', 'Award', 'TRAISIM', 'CRESYM']
categories: ['blog']
date: 2026-09-11T00:00:00+03:00
lastmod: 2026-10-23T00:00:00+03:00
featured: true
draft: false

image:
  caption: "Best Paper Award presentation at PoSyDyS 2026, Graz"
  focal_point: "Center"
  preview_only: false

projects: ["traisim"]
---

Our PhD candidate [Stefanos Eleftheriadis](/group/stefanos-eleftheriadis/) received the **Best Paper Award** at the [Power System Dynamics Summit (PoSyDyS 2026)](https://posydys.tugraz.at/), held on 9–11 September 2026 in Graz, Austria, and organised by Graz University of Technology. Congratulations Stefanos and co-authors!

The award-winning paper is:

> **[Adaptive Reduced System Modeling for Real-time Dynamic Simulations](/publication/2026celeftheriadis/)**
> {{% mention "s.-eleftheriadis" %}}, {{% mention "m.-hashemnezhad" %}}, {{% mention "s.-panagi" %}}, T. Vermeulen, G. Joseph, {{% mention "p.-aristidou" %}}

## About the work

The paper proposes an adaptive approach to reducing large-scale power system models while preserving the level of detail needed for accurate dynamic simulations. Given the operating state and the location of a disturbance, graph-neural-network predictors identify which substations need full detail and simplify the rest. On a realistic French transmission network model with more than 6,000 buses, the method cuts model size by about 60% and speeds up simulation by up to 2.6×, with errors below the solver tolerance.

This is an important step towards real-time dynamic simulation of large power systems, one of the key challenges addressed by the **[TRAISIM](/project/traisim/)** project, developed with [CRESYM](https://cresym.eu) and RTE. CRESYM also [shared the news](https://www.linkedin.com/feed/update/urn:li:activity:7505204760971616258/) on LinkedIn.

![Stefanos Eleftheriadis with the PoSyDyS 2026 Best Paper Award certificate](certificate.jpg)

Read more about [our participation in PoSyDyS 2026](/post/2026_posydys/).
