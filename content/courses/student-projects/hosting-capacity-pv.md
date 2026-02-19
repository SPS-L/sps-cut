---
title: Hosting Capacity Assessment for PV Integration in LV Feeders (Automation + Reporting)
linktitle: Hosting Capacity PV
date: '2026-02-15'
type: book
draft: false
weight: 80
---

## Background and Objectives

The rapid growth of rooftop photovoltaic (PV) installations in LV distribution networks increases the likelihood of voltage rise and thermal overloading. Hosting capacity analysis aims to determine the maximum PV penetration that a feeder can accommodate before operational limits are violated. These limits are typically defined by statutory voltage bounds and equipment thermal ratings.

Many hosting capacity studies rely on deterministic worst-case assumptions or limited manual scenario evaluation. However, realistic assessment must account for variability in load demand, PV production, and spatial placement of installations. Automated, scenario-based approaches—such as Monte Carlo simulations—offer a more comprehensive picture of network limits, but require structured workflows and consistent reporting to be useful for planning.

This project focuses on implementing an automated hosting capacity assessment framework in pandapower[^pandapower]. The goal is to evaluate voltage and thermal constraints under randomized PV placement and sizing scenarios and to produce standardized outputs suitable for planning and comparative studies.

The student will:

- Implement Monte Carlo PV placement and sizing across an LV feeder model.
- Define and enforce constraints: voltage limits and thermal loading limits.
- Compute hosting capacity distributions and risk metrics (e.g., probability of violations).
- Identify limiting factors and critical network components (buses/lines).
- Generate standardized plots and summary tables automatically.

This project requires strong *programming* and *analytical* skills.

## Deliverables

- End-to-end hosting capacity pipeline (scripts + configuration).
- A technical report with methodology, results, sensitivity analysis, and limitations.
- A presentation summarizing outcomes and planning insights.

## Student profile

- Strong Python skills (Pandas/NumPy).
- Background in electric power systems (minimum [Power Systems I]({{< ref "/courses/een320/_index.md">}})).
- Basic knowledge of statistics is a plus.

Before asking any questions, please check the [FAQ]({{< relref "faq.md" >}}).

[^pandapower]: [pandapower – An Open-Source Python Tool for Convenient Modeling, Analysis and Optimization of Electric Power Systems](https://www.pandapower.org/)
