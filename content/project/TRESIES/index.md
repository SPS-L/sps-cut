---
title: TRESIES
summary: Towards resilience and sustainability in islanded energy systems
tags:
- Past projects
- Microgrids
- Renewable Energy
- Energy Storage
- Stochastic Optimization
- PyEPLAN
date: "2019-09-27T00:00:00Z"

profile: false  # Show author profile?

# Optional external URL for project (replaces project detail page).
external_link: 

image:
  caption: Alderney island. Photo by [Neil Howard](https://www.flickr.com/photos/neilsingapore/)
  focal_point: Smart
---

## Summary

Remote rural and islanded communities face many difficulties in adequate and secure energy supply. In many cases, connecting these communities to the bulk electricity grid is economically challenging or impossible due to geographical constraints. Climate change and reliance on fossil fuels make the electrification of these communities more complicated. 

The TRESIES (Towards Resilience and Sustainability in Islanded Energy Systems) project focused on developing sustainable microgrid solutions for remote island communities. We collaborated with Alderney Electricity Ltd (AEL) on the existing microgrid in Alderney, the 3rd largest of the Channel Islands, to investigate reinforcement and investment solutions that increase resilience and sustainability through employing and extending the microgrid planning tools developed by our group.

## Project Background

Alderney Island, with an area of 3 square miles and a population of about 2000 people, runs a closed complex energy system that entirely relies on imported fuel oils for electricity, heating, and transportation. The island's major economic activities include e-trade, ecotourism, small businesses, and healthcare services. AEL is the sole energy supplier, responsible for importing and distributing different fuels (kerosene and transport fuels) as well as generating and distributing electricity.

The AEL network consists of:
- **Primary Distribution**: 11kV network with 21 substations
- **Secondary Distribution**: 415V network
- **Generation**: 8×450kVA diesel generators at the power station
- **Transformers**: Two 2.5MVA transformers connecting power station to 11kV network
- **Distribution**: 500kVA transformers at various substations
- **Cabling**: Mainly underground copper core cables (16mm² PILC, 25mm² PILC, and 70mm² XLPE)

## Methodology

The project employed a comprehensive two-stage stochastic optimization approach using the Python-based Energy Planning (PyEPLAN) tool. The methodology included:

### 1. Stochastic Microgrid Investment Planning (SMIP) Model
- **Objective**: Minimize total investment and operational costs
- **Planning Horizon**: Single-year with representative days
- **Uncertainty Modeling**: Load demands and renewable energy source (RES) power generation
- **Mathematical Formulation**: Mixed-Integer Linear Programming (MILP) problem

### 2. Scenario Generation Using K-means Clustering
- **Data Source**: Yearly historical patterns from 2013
- **Scenarios**: Best (risk-seeker), nominal (risk-neutral), and worst (risk-averse) representative days
- **Technique**: K-means clustering to capture uncertainty spectrum

### 3. Technology Assessment
The study evaluated three main renewable technologies:
- **Solar Power**: 1.8MW capacity with 16.27% capacity factor
- **Wind Power**: 1.8MW capacity with 54.39% capacity factor  
- **Battery Storage**: Various capacities for energy arbitrage

### 4. Network Modeling
- **Power Flow**: Linearized DistFlow model for AC power flow equations
- **Constraints**: Active/reactive power balance, voltage limits, thermal limits
- **Investment Variables**: Here-and-now decisions (not function of uncertain parameters)
- **Operation Variables**: Wait-and-see decisions (function of uncertain parameters)

## Key Findings

### Optimal Technology Mix
The analysis revealed that the best low-carbon investment plan for Alderney involves a hybrid microgrid including:
- **1.8MW Wind Farm**: Primary renewable generation source
- **1.8MW Solar Farm**: Complementary renewable generation
- **Battery Storage**: Energy arbitrage and system stability
- **Existing Diesel Units**: Backup generation for reliability

### Cost Analysis
- **Investment Costs**: £96,040/MW for batteries, £56,280/MW for solar, £81,070/MW for wind
- **Operational Costs**: £196.2/MWh for diesel generation
- **Penalty Costs**: £1,962/MWh for load curtailment

### Scenario Sensitivity
- **Best Case**: 1.8MW wind unit sufficient (total cost: £0.15M)
- **Nominal Case**: Hybrid solution with solar and wind (total cost: £0.25M)
- **Worst Case**: Conservative approach using existing infrastructure (total cost: £1.66M)

### Representative Days Analysis
The study found that 5 nominal representative days can appropriately characterize the uncertain profiles of load demand and RES generation on Alderney Island with reasonable computational complexity.

## Technical Implementation

### PyEPLAN Tool Features
- **Data Processing Module**: Historical data collection and scenario generation
- **Investment Planning Module**: Long-term planning with MILP optimization
- **Operation Planning Module**: Real-time operation optimization
- **Open Source**: Built with Pyomo optimization modeling framework

### Network Constraints
- Active and reactive power balance at each node
- Voltage magnitude limits (0.95-1.05 pu)
- Thermal limits on distribution lines
- Battery energy storage constraints
- Generator operational limits

## Project Impact

The TRESIES project demonstrated that:
1. **Sustainable microgrids are feasible** for remote island communities
2. **Hybrid renewable systems** provide optimal cost-benefit ratios
3. **Stochastic optimization** is essential for reliable planning under uncertainty
4. **Open-source tools** like PyEPLAN enable practical implementation

The project was funded through a UKRI EPSRC Impact Accelerator Award and co-funded by Alderney Electricity Ltd, providing a practical roadmap for transitioning remote island communities from fossil fuel dependence to sustainable energy systems.
