---
title: PowerFactory-Based Modeling of Distribution Networks (LV/MV) as a Preparation for Future Studies
linktitle: PowerFactory Distribution Networks
toc: true
type: docs
date: "2026-02-10T00:00:00Z"
draft: true
menu:
  student-projects:
    parent: Overview
    weight: 13

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 13
---

## Background

The development and maintenance of Medium Voltage (MV) distribution network models is a particularly challenging task, mainly due to the continuous evolution of real networks. Topology changes, load growth, new connections, and equipment replacements occur frequently, making MV network models quickly outdated. As a result, MV studies are often difficult to maintain, time-consuming to update, and in many cases cannot be reused without significant manual effort.

This creates a gap between real network changes and simulation-ready models, limiting the ability to perform up-to-date MV analyses in tools such as DIgSILENT PowerFactory. To address this issue, there is a strong need for more automated and systematic modeling workflows, which can directly reflect network changes within simulation environments and reduce manual intervention.

This project proposes an initial investigation towards automated MV/LV network modeling in PowerFactory. The main objective is to explore how network data and modifications can be more efficiently transferred and updated within simulation tools, enabling faster and more reliable MV studies. The student will focus on understanding the modeling workflow and identifying ways to streamline the update process.

## Objectives

In this project, you will investigate and prototype a repeatable workflow for maintaining and updating LV/MV distribution network models in DIgSILENT PowerFactory, with emphasis on automation and structured data handling.

The student will:

- Become familiar with DIgSILENT PowerFactory and its data structure.
- Understand an already developed distribution network model (LV or MV).
- Study how typical network changes (e.g., line additions, load updates, topology changes) are implemented in PowerFactory.
- Investigate available options for:
  - data import/export
  - scripting or automation features
  - structured model updating
- Apply simple modifications to the network and observe their impact on simulations.
- Document a repeatable workflow for updating network models with minimal manual effort.

This project requires excellent *programming* skills, especially in *Python*. It is in collaboration with [EAC](http:/www.eac.com.cy).

## Deliverables

- A PowerFactory project (LV or MV) with documented update procedures.
- A technical report describing:
  - modeling workflow
  - update methodology
  - challenges and limitations
- A presentation summarizing findings and recommendations.

## Student profile

- Very good programming skills in Python.
- Prior experience in DIgSILENT PowerFactory is mandatory (otherwise a small training period is expected).
- Background in electric power systems (minimum [Power Systems I]({{< ref "/courses/een320/_index.md">}})).

Before asking any questions, please check the [FAQ]({{< relref "faq.md" >}}).


