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

STEPSS is developed by [Dr. Petros Aristidou](https://sps-lab.org/author/petros-aristidou/) (Cyprus University of Technology) and [Dr. Thierry Van Cutsem](https://thierryvancutsem.github.io/home/), consultant to transmission system operators and formerly Research Director at the Fund for Scientific Research (FNRS) and Adjunct Professor at the University of Liège.

It is free of charge for teaching, academic research and personal non-profit use. The platform is not under one single licence, because each component carries its own: the two user interfaces are Apache 2.0, the RAMSES solver is the property of the University of Liège and free for non-commercial use only, and Helios and CODEGEN are under Academic Public Licences. The free version of RAMSES is limited to 1000 buses and two cores. The [licence terms](https://stepss.sps-lab.org/getting-started/license/) set out what applies to what, and how to ask about commercial use.

### Two editions

STEPSS names the platform, not any one program. It comes in two editions, which drive the same engines and read the same data files, so a case built in one runs unchanged in the other.

- **STEPSS GUI** is a desktop application. Install it from a Windows, macOS or Linux installer that needs nothing else on the machine, from the APT repository on Debian and Ubuntu, from the Scoop bucket on Windows, or run `stepss.jar` on a Java runtime you already have. Load a network, run static and dynamic simulations, plot live curves and build your own models, without touching a command line. [Install it](https://stepss.sps-lab.org/getting-started/installation/), or [open one of the bundled test systems](https://stepss.sps-lab.org/gui/first-run/) and simulate it without preparing any data of your own.
- **STEPSS in Python** is the `stepss` package: `pip install stepss`. Script simulations, sweep parameters and work directly with NumPy, SciPy and Jupyter. It bundles the RAMSES and Helios engines, so it needs no separate solver installation. [Documentation](https://stepss.sps-lab.org/python/).

STEPSS GUI additionally carries CODEGEN, so building your own device models is done there.

### Core modules

- **[HELIOS](https://stepss.sps-lab.org/user-guide/power-flow/)** performs the power flow computation that determines the initial operating point of a dynamic simulation, using the Newton-Raphson method in polar coordinates and with optional transformer ratio adjustment.
- **RAMSES** (RApid Multithreaded Simulation of Electric power Systems) simulates the dynamic evolution of the power system in response to disturbances and actions specified by the user. It offers Backward Euler, Trapezoidal and BDF2 integration, and exploits multi-core processors through OpenMP parallelism.
- **CODEGEN** (CODE GENerator) translates a model described by the user in a text file into its equivalent in Fortran 2003, ready to be compiled and linked into a user-defined version of RAMSES. Models can also be assembled graphically with [CODEGEN Studio](https://stepss.sps-lab.org/developer/cg-studio/).

### Also included

- **[URAMSES](https://stepss.sps-lab.org/developer/uramses/)** lets you compile your own Fortran device models and link them against a pre-compiled RAMSES library, as a shared library for the Python edition or a standalone executable.
- **DYNGRAPH** extracts and plots time-series curves from the binary observable files produced by RAMSES.
- **[Small-signal stability analysis](https://stepss.sps-lab.org/user-guide/eigenanalysis/)** is performed by RAMSES itself, computing the eigenvalues, eigenvectors and participation factors of the system at a chosen instant of a run. It is driven from the Analysis tab of STEPSS GUI, or from a disturbance record, and needs no other software.

### Downloads and documentation

- [Install STEPSS GUI](https://stepss.sps-lab.org/getting-started/installation/): installers for Windows, macOS and Linux, the APT repository on Debian and Ubuntu, the Scoop bucket on Windows, and `stepss.jar`
- STEPSS in Python: `pip install stepss`, and see the [Python installation guide](https://stepss.sps-lab.org/python/installation/) for the system libraries Linux and macOS need
- [Online documentation](https://stepss.sps-lab.org/) and [Quick Start](https://stepss.sps-lab.org/getting-started/quickstart/)
- [Complete User Guide (PDF)](https://stepss.sps-lab.org/stepss_docs.pdf)
- [Video guide for the use of CODEGEN in STEPSS](https://youtu.be/q5EFn2pdkCg)
- [Licence terms](https://stepss.sps-lab.org/getting-started/license/)
