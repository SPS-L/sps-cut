---
title: TRAISIM
summary: Power System Training Digital Twin for Complex and Critical Scenarios
tags:
- Current projects
- Power Systems
- Digital Twin
- Training Simulator
- Real-time Simulation
date: "2024-01-01T00:00:00Z"

profile: false  # Show author profile?

# Optional external URL for project (replaces project detail page).
external_link:

# Only change the caption, not the focal_point!
image:
  caption: Training simulator
  focal_point: Smart

---

## Power System Training Digital Twin for Complex and Critical Scenarios (TRAISIM)

**Funding Agency:** CRESYM  
**Start Date:** 2024  
**Partners:** Cyprus University of Technology (CUT), RTE  
**Website:** cresym.eu/traisim/

### Project Overview

TRAISIM is an innovative research initiative that advances the frontier of real-time power system simulation and operator training. Building on the core digital twin infrastructure developed within the European project TWINEU (Pilot 8, Task 5.5), TRAISIM targets the most demanding aspects of power system operation: complex, critical, and high-impact scenarios where reliability and speed are paramount. The project is a collaboration between the Sustainable Power Systems Lab (SPS-Lab) at CUT, RTE, and the CRESYM consortium, and is strategically positioned to address the evolving challenges of modern power grids.

### Context and Motivation

The energy landscape is undergoing a profound transformation. The rapid integration of renewable energy sources, proliferation of power electronic interfaces, and the increasing complexity of grid topologies are fundamentally altering how power systems are operated and controlled. These trends introduce new forms of uncertainty and dynamic behavior, making traditional simulation and training tools insufficient for today's—and tomorrow's—needs.

Operators must now manage systems that are not only larger and more interconnected, but also characterized by a mix of slow- and fast-acting devices, frequent switching events, and hybrid dynamics. This environment demands advanced digital twins capable of simulating real-world scenarios in real time, supporting both automated and human-in-the-loop decision-making. TRAISIM directly addresses these needs by delivering a training simulator that is both computationally efficient and numerically robust, even under the most challenging conditions.

### Research Objectives

TRAISIM's core mission is to deliver a high-fidelity, real-time digital twin environment for power system operator training. Its objectives include:

- **Developing a virtual environment** that can accurately simulate complex and critical grid scenarios, including rare but high-impact events.
- **Implementing advanced computational tools and methods** to support proactive, informed operator decisions—integrating lessons learned from the SPS-Lab's broader research in modeling, simulation, and control.
- **Ensuring real-time performance** by systematically benchmarking and optimizing solver configurations, numerical stability, and computational efficiency, leveraging the Dynawo simulation platform.
- **Evaluating and tuning simulation performance** through structured procedures, including sensitivity analyses, event-based benchmarking, and code-level profiling to identify and address bottlenecks.
- **Integrating renewable energy and power electronics** into realistic training scenarios, reflecting the latest grid developments.
- **Enhancing decision-support tools** by building on the lab's expertise in hybrid system modeling, digital controller integration (as in the IBM project), and scalable simulation frameworks (as in the Modeling and Simulation research line).
- **Systematic assessment of simulator behavior** across a broad range of modeling conditions, guiding its adoption in real-time operational environments.

### Technical Innovation

TRAISIM stands out for its rigorous approach to simulation benchmarking and optimization:

- **Reproducible, high-performance simulation environment:** The project establishes a controlled computational setup, including CPU frequency locking and process prioritization, to ensure consistent, reliable performance metrics.
- **Real-time constraint validation:** TRAISIM introduces new methodologies for validating that simulations run at least as fast as physical processes, a critical requirement for operator training and real-time applications.
- **Advanced solver tuning:** Through detailed sensitivity analyses and parameter optimization, the project identifies and implements solver configurations that minimize computational delays during disturbances, topology changes, and large-scale events.
- **Profiling and code optimization:** TRAISIM leverages advanced profiling tools (e.g., Intel VTune) to pinpoint and address memory, parallelism, and algorithmic bottlenecks, ensuring scalability and responsiveness even as system complexity grows.
- **Integration with digital controller modeling:** The project builds on SPS-Lab's work in the IBM project, applying interpolation-based methods to handle the challenges of digital controller events without excessive computational overhead.

### Synergy with SPS-Lab Research

TRAISIM is deeply connected to other SPS-Lab projects:

- **IBM (Interpolation-Based Method):** TRAISIM leverages IBM's efficient treatment of digital controller-induced discontinuities, enabling accurate and fast simulation of hybrid systems with frequent events.
- **Modeling and Simulation:** TRAISIM benefits from the lab's broader expertise in scalable, robust simulation tools for large, complex power systems, including parallelization strategies and advanced numerical methods.
- **Collaborative Ecosystem:** By working closely with RTE and CRESYM, TRAISIM ensures that its developments are aligned with real-world operational needs and can be transferred to industry practice.

### Impact and Future Directions

TRAISIM's outcomes will directly enhance the preparedness of system operators, equipping them with state-of-the-art digital twins for training in the most demanding scenarios. The project's systematic approach to benchmarking, solver optimization, and integration of advanced modeling techniques will set new standards for real-time power system simulation. Its methodologies and results will inform future research across the SPS-Lab and its partners, supporting the ongoing transition to smarter, more resilient energy systems.

**In summary:**  
TRAISIM is a flagship project at the intersection of simulation science, power system engineering, and operator training. By building on and contributing to the SPS-Lab's research ecosystem, it delivers a next-generation digital twin platform that meets the real-time, high-fidelity demands of modern power grids and their operators.
