---
title: TRAISIM
summary: Open-source real-time training platform preparing power system operators for the grid of the future
tags:
- Current projects
- Power Systems
- Digital Twin
- Training Simulator
- Real-time Simulation
- AI/Machine Learning
date: "2024-01-01T00:00:00Z"

profile: false  # Show author profile?

# Optional external URL for project (replaces project detail page).
external_link:

# Only change the caption, not the focal_point!
image:
  caption: TRAISIM — Real-Time Operator Training Platform
  focal_point: Smart

---

## Training Simulator for Power System Operators (TRAISIM)

**Funding Agency:** [CRESYM](https://cresym.eu)  
**Start Date:** January 2025  
**Partners:** Cyprus University of Technology (CUT), Reseau de Transport d'Electricite (RTE), Collaborative Research for Energy System Modelling (CRESYM)  
**Website:** [sps-lab.org/project/traisim](https://sps-lab.org/project/traisim)  
**Code:** [github.com/SPS-L/](https://github.com/SPS-L/)

---

### Overview

TRAISIM is developing an open-source real-time training simulator that helps power system operators prepare for a grid that is becoming more dynamic, more digital, and more demanding to operate.

The project brings together high-fidelity power-system simulation, operator-focused interfaces, and modern digital-twin thinking in a single platform. Its purpose is to make advanced operator training more accessible, transparent, and adaptable for transmission system operators, researchers, and educators.

Built on top of [Dynawo](https://github.com/dynawo/dynawo), TRAISIM offers an open alternative to closed and vendor-locked training environments. This creates space for collaboration, easier experimentation, and a clearer pathway from research to real operational use.

---

### Why It Matters

Control rooms are evolving quickly. Operators must respond to renewable integration, changing network conditions, automation, and growing system complexity, all while maintaining security and reliability.

TRAISIM is designed to support that transition by offering a realistic environment where operators can train on credible scenarios, test responses to disturbances, and build confidence with tools that reflect the needs of future grids.

The project is also a strong demonstration that open-source technology can support large-scale, real-time operator training without sacrificing ambition or practical relevance.

---

### What TRAISIM Delivers

TRAISIM combines several key elements into one training environment:

- a realistic physical simulator for large transmission networks
- a control-room style human-machine interface
- orchestration tools that align simulation time and operator interaction
- trainer and scenario-management functions for guided exercises
- protection and automation behaviour for more credible event progression
- AI-enabled model adaptation to improve responsiveness where it matters most

Together, these capabilities help create a platform that is realistic enough for serious training, flexible enough for research, and open enough to grow with new operational needs.

---

### Progress So Far

In its first phase, TRAISIM has shown that open-source real-time training for large transmission systems is a realistic and promising direction. The project has already established a strong benchmarking foundation, identified the main performance bottlenecks, and defined a focused roadmap for the next stage of development.

The platform is being demonstrated on a very large transmission network model inspired by the French grid, highlighting TRAISIM's relevance for realistic TSO-scale applications.

Current work is focused on:

- improving simulation speed and robustness
- using adaptive model selection to reduce computational burden
- strengthening coordination between the simulator and the training environment
- preparing reusable methods, software improvements, and research outputs for the wider community

Early results from the adaptive model selection work are especially encouraging, showing major reductions in model size while maintaining very high predictive accuracy.

---

### Publications

TRAISIM's first public outputs are already available and showcase both the project vision and its early technical progress:

- [Towards an Open-Source Real-Time Operator-Training Platform: Analysis of Computational Efficiency](/publication/2026cpanagi/), accepted at PSCC 2026
- [TRAISIM: Training Simulator for Power System Operators](/publication/2026trpanagi/), poster presented at CRESROADS 2026

These publications present the first benchmark results, explain the platform concept, and outline the next steps in solver optimisation, AI-enabled model adaptation, and open-source dissemination.

---

### Synergy with SPS-Lab Research

TRAISIM is closely connected to other SPS-Lab research directions:

- **IBM (Interpolation-Based Method):** improved handling of controller-induced discontinuities in hybrid simulations
- **Modeling & Simulation:** scalable numerical methods for large and complex power-system models
- **TwinEU (Pilot 8, Task 5.5):** digital twin concepts and infrastructure that support the broader training-platform vision

**Contact:** [info@sps-lab.org](mailto:info@sps-lab.org)
