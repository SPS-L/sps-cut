---
title: Sensitivity Analysis of Voltage to Load and PV Variations
linktitle: Voltage Sensitivity Analysis
date: '2026-02-15'
type: book
draft: false
weight: 90
---

## Background and Objectives

Distribution networks are increasingly exposed to operational variability due to higher penetration of distributed PV generation and electrification-driven load growth. In LV and MV feeders, voltage levels can change significantly even under modest variations of load or local generation due to radial topologies, higher R/X ratios, and limited voltage regulation equipment.

Understanding how voltages respond to incremental changes in load or PV generation is important for identifying weak buses, anticipating constraint violations, and supporting the design of voltage control strategies. Although time-series power flow simulations provide detailed system trajectories, they often do not offer systematic insight into where the network is most sensitive and which changes drive the largest voltage impacts.

This project performs a structured voltage sensitivity analysis under varying load and PV scenarios using pandapower[^pandapower]. The aim is to quantify sensitivity patterns across the feeder, identify critical nodes, and provide clear visual and numerical indicators that can support planning or control studies.

The student will:

- Develop a parametric simulation framework in pandapower.
- Perform systematic load and PV scaling studies across multiple scenarios.
- Define and compute voltage sensitivity indices per bus (and optionally per time segment).
- Identify critical buses and feeder areas most prone to voltage issues.
- Visualize sensitivity patterns and interpret operational implications.

This project requires good *programming* and *analytical* skills.

## Deliverables

- Automated sensitivity analysis scripts and scenario configurations.
- Sensitivity metrics, plots, and summary tables.
- Technical report and presentation.

## Student profile

- Good Python skills.
- Background in electric power systems (minimum [Power Systems I]({{< ref "/courses/een320/_index.md">}})).
- Familiarity with basic data analysis is a plus.

Before asking any questions, please check the [FAQ]({{< relref "faq.md" >}}).

[^pandapower]: [pandapower – An Open-Source Python Tool for Convenient Modeling, Analysis and Optimization of Electric Power Systems](https://www.pandapower.org/)
