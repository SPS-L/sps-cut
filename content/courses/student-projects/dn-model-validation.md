---
title: Automated Validation of Distribution Network Models
linktitle: DN Model Validation
date: '2026-02-15'
type: book
draft: false
weight: 100
---

## Background and Objectives

Reliable simulation studies depend on accurate and consistent distribution network models. In practice, LV/MV grid models are often assembled from heterogeneous sources and manually updated over time. This process can introduce structural and parametric inconsistencies, such as disconnected buses, incorrect switch states, unrealistic line/transformer parameters, or equipment ratings that do not match operating conditions.

Even minor modeling errors can significantly distort power flow results and lead to misleading conclusions in hosting capacity studies, voltage control analysis, and network planning. Despite this risk, systematic validation routines are often missing in academic and prototype modeling environments, where model correctness is commonly assessed through manual checks.

This project addresses the need for a structured, automated validation framework for distribution network models in pandapower[^pandapower]. The objective is to develop reusable validation routines that check connectivity and plausibility, and to generate diagnostic reports that help ensure models are simulation-ready before downstream studies are performed.

The student will:

- Identify typical modeling errors and inconsistencies in LV/MV networks.
- Develop automated validation checks for:
  - network connectivity and radiality (where applicable)
  - parameter plausibility (line impedances, transformer ratings, load values)
  - operational feasibility after power flow (voltage and thermal plausibility)
- Generate structured validation reports with flagged issues and recommendations.
- Test the validation tool on one or more benchmark feeders.

This project requires strong *programming* skills and attention to software quality.

## Deliverables

- A Python-based validation tool (library or scripts) with clear documentation.
- A set of validation rules and example outputs.
- Technical report and presentation summarizing findings and limitations.

## Student profile

- Strong Python skills.
- Background in electric power systems (minimum [Power Systems I]({{< ref "/courses/een320/_index.md">}})).
- Interest in software quality and reproducibility is a plus.

Before asking any questions, please check the [FAQ]({{< relref "faq.md" >}}).

[^pandapower]: [pandapower – An Open-Source Python Tool for Convenient Modeling, Analysis and Optimization of Electric Power Systems](https://www.pandapower.org/)
