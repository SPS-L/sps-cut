---
title: Modeling and Simulation
summary: Advanced or dedicated methods for time simulation of electric power systems
tags:
- themes
date: "2020-04-01T00:00:00Z"

profile: false  # Show author profile?

# Optional external URL for project (replaces project detail page).
external_link: 

image:
  caption: Photo from [paper](/publication/2019jmarkovic/)
  focal_point: Smart
---

## Modeling and Simulation at SPS-Lab: Extended and Enhanced Description

The **Modeling and Simulation** research theme at the Sustainable Power Systems Lab (SPS-Lab) addresses the growing complexity of modern electric power systems by developing advanced computational tools and methodologies that integrate numerical analysis, power system modeling, and state-of-the-art simulation techniques. As power grids evolve—incorporating large-scale renewable integration, distributed energy resources (DERs), and smart digital controllers—the need for accurate, scalable, and real-time simulation frameworks becomes increasingly critical.

### **Research Focus and Objectives**

- **Integrated Modeling Approaches:** SPS-Lab's work spans the development of detailed models that capture the dynamic behavior of both transmission and distribution networks. This is essential for studying scenarios with high DER penetration, where interactions between network layers and local controllers can significantly impact system stability and performance.
- **Advanced Simulation Algorithms:** The lab pioneers the use of domain decomposition and parallel processing techniques, such as Schur-complement-based algorithms, to enable the simulation of large-scale power systems on modern multi-core computing platforms. These methods allow for the independent and parallel solution of sub-systems, dramatically reducing computation times while preserving simulation accuracy.
- **Smart Digital Controller Integration:** Recognizing the proliferation of digital and data-driven controllers in smart grids, SPS-Lab develops novel methods for efficiently simulating hybrid systems characterized by both continuous and discrete dynamics. This includes fast, interpolation-based techniques that handle the frequent discrete events introduced by digital controllers without sacrificing the benefits of variable time-step integration.

### **Key Methodologies and Innovations**

- **Domain Decomposition and Parallelization:** By partitioning the power system into interconnected sub-domains (e.g., separating the transmission network from multiple distribution networks), the simulation task can be distributed across multiple processor cores. This approach not only accelerates computation but also enhances scalability, making it feasible to simulate systems with tens of thousands of buses and components.
- **Dynamic Model Reduction (Localization):** To further speed up simulations, SPS-Lab employs localization techniques that dynamically identify and simplify the modeling of sub-systems (such as distribution networks) that are not actively participating in system dynamics during a disturbance. These latent sub-systems are replaced with reduced-order models, while active areas retain full detail, ensuring both efficiency and fidelity.
- **Handling Hybrid and Discrete Events:** The lab's research addresses the challenges posed by the widespread use of digital controllers, which introduce numerous discrete events into the simulation. Their interpolation-based method allows for the accurate and efficient simulation of both equation-based and black-box controllers, maintaining accuracy without the need for excessive time-step reductions.

### **Applications and Impact**

- **Real-Time and Faster-Than-Real-Time Simulation:** The developed tools and algorithms enable real-time or faster-than-real-time analysis, which is vital for dynamic security assessment, operator training, and the integration of advanced protection and control schemes in future grids.
- **Scalability to Large-Scale Systems:** SPS-Lab's methodologies have been validated on large-scale test systems, including combined transmission and distribution networks with over 14,000 buses and thousands of dynamic components, demonstrating both high accuracy and significant computational speedup (up to 7.5 times faster than traditional methods).
- **Support for Future Grid Scenarios:** The lab's research is particularly relevant for future power systems characterized by high DER penetration, active demand response, and the deployment of smart grid technologies. The ability to model and simulate such systems in detail supports robust planning, operation, and security analysis.

### **Collaborative and Open Research**

SPS-Lab's modeling and simulation research is conducted in collaboration with leading academic and industrial partners, ensuring that developed tools address real-world challenges and are validated against practical scenarios. The lab's commitment to open, modular, and extensible simulation frameworks fosters innovation and facilitates the integration of new models, controllers, and computational techniques.

**In summary:**  
The Modeling and Simulation theme at SPS-Lab delivers cutting-edge computational methods and tools that empower researchers and operators to analyze, design, and secure the next generation of electric power systems. By combining advanced modeling, parallel simulation, and efficient handling of digital controllers, the lab enables accurate, scalable, and real-time dynamic studies essential for the reliable operation of increasingly complex and intelligent power grids.