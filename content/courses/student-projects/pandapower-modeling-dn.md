---
title: Pandapower-Based Modeling of Distribution Networks as a Preparation for Data-Driven Studies
linktitle: Pandapower DN Modeling
date: '2026-02-15'
type: book
draft: false
weight: 70
---

## Background and Objectives

Distribution network studies increasingly rely on flexible, script-based modeling environments that enable reproducible simulations and large-scale scenario analysis. While open-source tools such as pandapower[^pandapower] provide a powerful Python framework for modeling LV and MV grids, practical modeling workflows are often developed in an ad-hoc manner. Network models may be modified manually, stored in inconsistent formats, or updated without structured documentation, making them difficult to reuse across projects.

Modern research and industrial studies—such as hosting capacity assessment, voltage control, forecasting, and optimization—require traceable model versions, repeatable scenario generation, and consistent data interfaces. Without a well-defined modeling workflow, simulation results become hard to reproduce, extend, and compare, limiting the value of the model for systematic studies.

This project addresses the need for a structured and reproducible modeling workflow for LV/MV distribution networks in pandapower. The objective is not only to run power flow simulations, but to design a modeling pipeline that supports efficient updates, scenario management, and seamless integration with future data-driven studies.

The student will:

- Become familiar with pandapower data structures and grid elements (lines, transformers, loads, DER).
- Understand an existing LV/MV feeder model provided by the lab.
- Implement typical network edits (new loads, PV additions, line/transformer parameter changes, switching actions).
- Build an organized data pipeline (CSV/JSON/YAML) to modify the model programmatically.
- Validate changes via power flow and key metrics (voltages, line loading, losses).
- Document a repeatable modeling and update workflow with clear assumptions and versioning.

This project requires good *programming* skills in Python.

## Deliverables

- A pandapower project with a reproducible workflow (scripts + structured input data).
- A technical report describing the modeling pipeline, update methodology, and limitations.
- A presentation summarizing results and recommendations.

## Student profile

- Good programming skills in Python.
- Background in electric power systems (minimum [Power Systems I]({{< ref "/courses/een320/_index.md">}})).
- Familiarity with Git is a plus.

Before asking any questions, please check the [FAQ]({{< relref "faq.md" >}}).

[^pandapower]: [pandapower – An Open-Source Python Tool for Convenient Modeling, Analysis and Optimization of Electric Power Systems](https://www.pandapower.org/)
