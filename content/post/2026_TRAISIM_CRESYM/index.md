---
title: "TRAISIM progress presented to CRESYM partners"
subtitle: ""
summary: "The lab presented the progress of TRAISIM — an open-source real-time training simulator for power system operators developed with CRESYM and RTE."
authors: ["s.-eleftheriadis", "m.-hashemnezhad", "s.-panagi", "p.-aristidou"]
tags: ['TRAISIM', 'CRESYM']
categories: ['blog']
date: 2026-10-27T00:00:00+02:00
lastmod: 2026-10-27T00:00:00+02:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: true

projects: ["traisim"]
---

On 27 October 2026, presented the progress of **[TRAISIM](/project/traisim/)** to **[CRESYM](https://cresym.eu)** partners. TRAISIM is our open-source real-time **Training Simulator for Power System Operators**, developed jointly with **Réseau de Transport d'Électricité (RTE)** and **CRESYM**.

The [presentation](./TRAISIM_Progress_Oct_2026.pdf) covers real-time dynamic simulation on a model of the French transmission system, with more than 6,000 buses. It sets out two routes toward a one-second solve budget. Adaptive model selection keeps full switching detail only where a planned disturbance needs it, removing about 72% of the continuous variables and 66% of the discrete variables on the French test set. The method is released as [DYNAGNN](https://github.com/SPS-L/DYNAGNN). Solver improvements reduce the work inside each step of [Dynawo](https://github.com/dynawo/dynawo) without changing the model, and a fixed Jacobian pattern has been proposed to the open-source project.

Related results were reported at [PSCC 2026](/publication/2026cpanagi/) and at [PoSyDyS 2026](/publication/2026celeftheriadis/), where the adaptive-model paper received the [Best Paper Award](/post/2026_posydys_award/).
