---
title: STEPSS
summary: STATIC AND TRANSIENT ELECTRIC POWER SYSTEMS SIMULATION
tags:
- Software tools
- Dynamics
date: "2025-05-01T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: 

image:
  caption: Photo by Thierry Van Cutsem
  focal_point: Smart
---

**Project website**: https://stepss.sps-lab.org/

STEPSS (Static and Transient Electric Power Systems Simulation) is a power system simulation platform for static and dynamic studies of electrical grids. It computes the power flow of a network and simulates its dynamic response to disturbances under the phasor (RMS) approximation.

STEPSS is developed by [Dr. Petros Aristidou](https://sps-lab.org) (Cyprus University of Technology) and Dr. Thierry Van Cutsem (University of Liège), and is distributed under the STEPSS Academic Public License: free of charge for teaching, academic research and personal non-profit use.

### Core modules

- **[HELIOS](https://stepss.sps-lab.org/user-guide/pfc/)** performs the power flow computation that determines the initial operating point of a dynamic simulation, using the Newton-Raphson method in polar coordinates and with optional transformer ratio adjustment.
- **RAMSES** (RApid Multithreaded Simulation of Electric power Systems) simulates the dynamic evolution of the power system in response to disturbances and actions specified by the user. It offers Backward Euler, Trapezoidal and BDF2 integration, and exploits multi-core processors through OpenMP parallelism.
- **CODEGEN** (CODE GENerator) translates a model described by the user in a text file into its equivalent in Fortran 2003, ready to be compiled and linked into a user-defined version of RAMSES. Models can also be assembled graphically with [CODEGEN Studio](https://stepss.sps-lab.org/developer/cg-studio/).

### Also included

- **[PyRAMSES](https://stepss.sps-lab.org/pyramses/installation/)** is the Python interface to the simulation engine, for scripting simulations, extracting results and working with the scientific Python ecosystem. Install it with `pip install pyramses`.
- **[URAMSES](https://stepss.sps-lab.org/developer/uramses/)** lets you compile your own Fortran device models and link them against a pre-compiled RAMSES library, as a shared library for PyRAMSES or a standalone executable.
- **DYNGRAPH** extracts and plots time-series curves from the binary observable files produced by RAMSES.
- **[Eigenanalysis](https://stepss.sps-lab.org/user-guide/eigenanalysis/)** is a MATLAB-based tool for small-signal stability studies, computing eigenvalues and eigenvectors of power system models extracted from RAMSES.

### Downloads and documentation

- [Download STEPSS](https://github.com/SPS-L/stepss-java-ui/releases/latest/download/stepss.jar) — always the latest release; see the [installation guide](https://stepss.sps-lab.org/getting-started/installation/) for the Java prerequisites
- [Online documentation](https://stepss.sps-lab.org/) and [Quick Start](https://stepss.sps-lab.org/getting-started/quickstart/)
- [Complete User Guide (PDF)](https://stepss.sps-lab.org/stepss_docs.pdf)
- [Video guide for the use of CODEGEN in STEPSS](https://youtu.be/q5EFn2pdkCg)
- [Licence terms](https://stepss.sps-lab.org/getting-started/license/)
