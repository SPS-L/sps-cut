---
title: PyEPLAN
summary: A Python-based Energy Planning tool
tags:
- Software tools
- Open-source
- Energy planning
- Microgrid optimization
- MILP optimization
- Python
- Renewable energy
date: "2025-01-27T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: 

image:
  caption: 
  focal_point: Smart
---

**Project external link**: https://pyeplan.sps-lab.org/

PyEPlan stands for "Python-based Energy Planning tool". It is a free software toolbox for Planning and Operation of Sustainable Micro-grids.

PyEPlan provides a comprehensive framework for microgrid planning and operation optimization, featuring:

* **Data Processing (datsys)**: Historical weather data extraction and representative day clustering using PVGIS API
* **Network Routing (rousys)**: Optimal feeder routing using minimum spanning tree algorithms  
* **Investment & Operation (inosys)**: Long-term capacity expansion and short-term dispatch optimization using MILP

The tool supports both on-grid and off-grid microgrid configurations, handles uncertainty through scenario-based optimization, and integrates renewable energy sources with conventional generation and energy storage systems.

## Installation

PyEPlan is available on PyPI and can be installed using pip:

```bash
pip install pyeplan
```

For development installation from source:

```bash
git clone https://github.com/sps-lab/pyeplan.git
cd pyeplan
pip install -e .
```

## System Requirements

- Python 3.7 or higher
- MILP solver (e.g., Gurobi, CPLEX, or CBC)
- Internet connection for PVGIS API access
- Sufficient RAM for large-scale optimization problems

## Applications

PyEPlan is designed for various energy planning and microgrid applications:

- **Rural Electrification**: Planning off-grid microgrids for remote communities
- **Campus/Industrial Microgrids**: Optimization of on-grid microgrid systems
- **Renewable Energy Integration**: Planning and operation with solar, wind, and storage
- **Grid Expansion Studies**: Optimal feeder routing and capacity planning
- **Energy Storage Optimization**: Battery sizing and operation strategies
- **Scenario Analysis**: Uncertainty handling through multiple weather and load scenarios

## Key Features

- **Multi-objective Optimization**: Cost minimization, reliability maximization, and environmental impact reduction
- **Weather Data Integration**: Automatic historical data extraction from PVGIS
- **Representative Day Clustering**: Efficient handling of seasonal variations
- **Network Topology Optimization**: Optimal feeder routing using graph algorithms
- **Mixed-Integer Linear Programming**: Robust mathematical optimization framework
- **Open Source**: Apache License 2.0 for academic and commercial use

## Documentation

Comprehensive documentation is available at [https://pyeplan.sps-lab.org/](https://pyeplan.sps-lab.org/) including:

- Getting Started guide with examples
- User guide for input data, planning, and output
- API reference for developers
- Release notes and updates

## Citing PyEPlan

If you use PyEPlan in your research, please cite it using the DOI: [10.5281/zenodo.3894705](https://zenodo.org/badge/DOI/10.5281/zenodo.3894705.svg)

PyEPlan is available on [PyPI](https://pypi.org/project/pyeplan/) and the source code is hosted on [GitHub](https://github.com/sps-lab/pyeplan).

