---
title: TRAISIM
summary: Open-Source Real-Time Training Simulator for Power System Operators
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
**Partners:** Cyprus University of Technology (CUT), Réseau de Transport d'Électricité (RTE), Collaborative Research for Energy System Modelling (CRESYM)  
**Website:** [sps-lab.org/project/traisim](https://sps-lab.org/project/traisim)  
**Code:** [github.com/SPS-L/](https://github.com/SPS-L/)

---

### Motivation

Modern power grids are complex cyber-physical infrastructures integrating renewables, distributed resources, and advanced protection. Transmission System Operators (TSOs) must make real-time decisions amid intricate model interactions and emerging AI-support tools. Existing operator training platforms rely on static or simplified modules, reduced-order models, or pre-computed scenario databases — most closed-source and vendor-locked — limiting transparency and excluding smaller TSOs and academia.

**Core challenge:** Simulate a 6,000-bus network *faster than real-time* on commodity x86 hardware, within the 1–2 s SCADA refresh constraint, with full model-level fidelity (DAE solvers, protection logic, dynamic loads).

**TRAISIM's answer:** An open-source training platform built on [Dynawo](https://github.com/SPS-L/dynawo) — algorithmic transparency, no license costs, deployable in existing control centres.

---

### Platform Architecture

TRAISIM integrates six tightly coupled subsystems that deliver a realistic, real-time control-room experience:

| Subsystem | Role |
|---|---|
| **Game Master AI** | Injects faults & constructs training scenarios |
| **HMI** | Control-room user interface |
| **Orchestrator** | Time synchronisation & SCADA information flow |
| **Automata** | Protection finite-state machines |
| **Physical Simulator** | Dynawo / DynaWaltz DAE solver (KINSOL Newton + KLU sparse LU, adaptive timestep) |
| **Trainer** | Supervises sessions and injects disturbances |

The physical simulator targets the full **RTE French Transmission Network** (63 kV – 400 kV):

- 7,075 branches · 335 synchronous generators · 3,039 dynamic loads · 839 load tap changers
- Three model fidelity levels: **Model 1** (80 k variables, ✓ real-time), **Model 2** (210 k, △ marginal), **Model 3** (320 k, × requires optimisation)

![TRAISIM Architecture](traisim_architecture.png)

---

### Benchmarking Results — Year 1 (Phase 1, Jan–Dec 2025)

Using 14 contingency scenarios (Loss of Busbar Section, Loss of Line, Loss of Generator) on the RTE 6,000-bus grid, worst-case solving times versus the 1 s budget:

| Model | Configuration | T_sol | Status |
|---|---|---|---|
| M1 | LBS Default | 0.70 s | ✓ Real-time |
| M2 | LBS Default | 1.84 s | ✗ Exceeds budget |
| M2 | LBS **Tuned** | 0.89 s | ✓ Real-time |
| M3 | LBS Default | 2.87 s | ✗ Exceeds budget |
| M3 | LBS **Tuned** | 1.40 s | ✗ Exceeds budget |

**Key finding:** KLU Analyze (symbolic Jacobian factorization) re-analyzes the full sparsity structure on every topology change — consuming 32.5% of solver time and running 2.3× longer in Model 3 vs. Model 2. Tuning `fnormtolAlgJ` + `msbsetAlgJ` achieves a **2× speedup** for Model 2, but Model 3 (320 k variables) remains infeasible without structural algorithmic changes.

> 📄 **PSCC 2026:** *"Towards an Open-Source Real-Time Operator-Training Platform: Analysis of Computational Efficiency"* — accepted, Limassol, June 8–12, 2026.

---

### Extension 2026 — Work Packages

**WP1 · Solver Optimization**
- Profile and reduce KLU Analyze call frequency; skip re-analysis when discrete events preserve matrix sparsity
- Incremental Jacobian structure updates: warm-start BTF permutations & cache sparsity patterns for known post-event topologies
- Thread-level parallelism for Euler Evaluation-J & KLU Factor via OpenMP
- Target: ~30% overall speedup

**WP2 · Adaptive Model Selection (AMS)**
- AI-driven fidelity control using **GATv2** Graph Attention Network with multi-task prediction heads → per-component activity scores
- Dynamic fidelity assignment: full detail where needed, Ward-equivalent simplification elsewhere
- Trained on ~12,000 dynamic simulations across multiple operating points and N-1 contingencies
- Early results: **75.7% continuous variable reduction**, 99.35% power prediction accuracy, 99.71% voltage prediction accuracy

**WP3 · Orchestrator Co-Design**
- Slack-time API between orchestrator and simulator: signal available headroom δt = T_sync − T_sol
- Dead-time offloading: pre-compute & cache KLU Analyze for anticipated topological changes
- Adaptive solver aggressiveness: dynamically tighten/relax tolerances based on real-time headroom budget

**WP4 · Validation & Dissemination**
- Recommendations report with implementation roadmap for upstream Dynawo integration
- Open-source release of solver patches & AMS module on [SPS-L GitHub](https://github.com/SPS-L/)
- Three peer-reviewed papers: benchmarking (PSCC 2026), solver optimisation (POSYDYS), AMS methodology (journal)

---

### Adaptive Model Selection (AMS)

The AMS module predicts component-level dynamic activity *before* each training session, selecting only the fidelity needed for the active scenario. A **GATv2** graph neural network learns which network components participate actively in disturbance propagation, enabling hybrid models that retain full detail where needed and simplify elsewhere.

Components with activity score > ε retain full-order dynamic models; those below threshold switch to simplified equivalents. Three KPI groups are independently normalised: generator S-power, frequency, and voltage.

**Early AMS Results:**

| Metric | Reduction / Accuracy |
|---|---|
| Continuous variables | −75.7% (74.5–76.4%) |
| Discrete variables | −69.2% (67.5–69.7%) |
| Root functions | −37.4% (37.1–37.6%) |
| Power prediction accuracy | 99.35% |
| Voltage prediction accuracy | 99.71% |

---

### Project Timeline

| Phase | Period | Milestone |
|---|---|---|
| **Phase 1 – Task 1** | Jan–Apr 2025 | Benchmarking methodology; 1 s step validated; headroom metric δt established; 14 scenarios catalogued |
| **Phase 1 – Task 2** | May–Aug 2025 | Code-level profiling; KLU Analyze identified as primary hotspot (32.5%); 2× speedup via tuning |
| **Phase 1 – Task 3** | Sep–Dec 2025 | 3-model fidelity comparison; PSCC 2026 accepted; Technical Reports 1 & 2 delivered |
| **Phase 2 – WP2 Baseline** | Jan–Mar 2026 | 12 k simulations; GATv2 trained; 75% variable reduction; frequency KPI split identified |
| **Phase 2 – WP2 Refinement** | Apr–Jun 2026 | Split prediction into 3 models; retrain frequency model; add high-RES operating points |
| **Phase 2 – WP1/WP3/WP4** | Apr–Sep 2026 | Solver optimisation roadmap; PSCC 2026 presentation; POSYDYS paper; AMS journal planning |
| **AMS Consolidation** | Jul–Sep 2026 | Full AMS prototype; accuracy–performance trade-off validated; journal paper drafted |

---

### Synergy with SPS-Lab Research

TRAISIM is tightly connected to other SPS-Lab projects:

- **IBM (Interpolation-Based Method):** Efficient handling of digital controller-induced discontinuities, enabling accurate simulation of hybrid systems with frequent switching events.
- **Modeling & Simulation:** Scalable, robust simulation tools for large, complex power systems — parallelisation strategies and advanced numerical methods.
- **TwinEU (Pilot 8, Task 5.5):** The core digital twin infrastructure developed within this European project forms the foundation of TRAISIM's training platform.

**Contact:** [info@sps-lab.org](mailto:info@sps-lab.org)
