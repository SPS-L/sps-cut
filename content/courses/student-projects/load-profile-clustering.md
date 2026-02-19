---
title: Load Profile Clustering for Representative Scenario Reduction
linktitle: Load Profile Clustering
date: '2026-02-15'
type: book
draft: false
weight: 110
---

## Background and Objectives

Distribution network assessment increasingly relies on time-series simulations using high-resolution load and PV profiles over months or years. While such simulations provide detailed operational insight, they are computationally expensive and can become impractical when embedded in iterative studies such as optimization, uncertainty analysis, or control design.

Scenario reduction techniques address this challenge by selecting a limited number of representative operating conditions that preserve the statistical characteristics of the full dataset. Clustering-based approaches can identify typical daily patterns (e.g., seasonal or weekday/weekend behaviors), enabling major computational savings while maintaining acceptable accuracy for planning metrics.

This project investigates clustering-based scenario reduction for load and PV profiles in distribution networks. The aim is to identify representative scenarios (days or operating points), quantify the accuracy vs. complexity trade-off, and provide practical guidelines for reduced-scenario simulation studies.

The student will:

- Analyze annual (or multi-month) load and PV time-series datasets.
- Apply clustering techniques (e.g., k-means, hierarchical clustering) to identify typical patterns.
- Select representative scenarios and define scenario weights.
- Compare reduced-scenario simulation results with full time-series results.
- Quantify approximation error and computational savings, and provide recommendations.

This project requires good *programming* skills and basic familiarity with data analysis or machine learning methods.

## Deliverables

- A scenario reduction pipeline with documented configuration options.
- Quantitative evaluation results (error vs. number of scenarios, runtime savings).
- Technical report and presentation.

## Student profile

- Good Python skills.
- Background in electric power systems (minimum [Power Systems I]({{< ref "/courses/een320/_index.md">}})).
- Basic statistics or ML familiarity is helpful.

Before asking any questions, please check the [FAQ]({{< relref "faq.md" >}}).
