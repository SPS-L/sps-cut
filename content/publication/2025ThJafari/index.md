+++
title = "Advanced Computational Methods for Digital Controller Integration in Power System Dynamic Simulations"
date = "2025-09-01"
authors = ["M. Jafari"]
tags = ["Digital controller","discontinuity handling","interpolation methods","power system simulation","dynamic simulation"]
publication_types = ["thesis"]
publication = "_PhD thesis at Cyprus University of Technology_"
publication_short = ""
abstract = "Dynamic simulation of power systems provides the system's response to a disturbance, which is a critical tool for optimally operating it and ensuring security. However, with increasing technological advancements and interconnecting neighbor networks, today's power systems have become a complex interconnected network of heterogeneous devices. Some traditional devices, such as synchronous machines, have slower responses, and some others, such as electronic-based devices, have faster responses. This leads to a system modeled with numerically stiff differential-algebraic equations. Furthermore, the existence of different kinds of components in the system, such as breakers and digital controllers, makes the system hybrid, i.e., discontinuities arise during the simulation that must be handled carefully. Thus, dynamic power system simulation requires solving numerous sets of nonlinear, stiff, hybrid Differential-Algebraic Equations (DAEs). In the case of hybrid systems, the real challenge is the integration over discontinuities since the solver must reduce the time step and land on the discontinuity, ensuring an accurate solution. Digital controllers are a classic source of discontinuities, introducing one discontinuity per sampling action. Therefore, the simulation of power systems with multiple digital controllers causes numerous discontinuities over the simulation horizon. Stopping at each sampling action and reducing the time steps constantly is challenging, leading to a slow and computationally inefficient simulation. In this thesis, first, the modeling of digital controllers and its challenges is discussed, then, the methods capable of simulating them are reviewed. A family of methods based on interpolation is proposed to tackle the issue of the simulation of power systems with digital controllers. The proposed methods are compared to already existing methods in terms of accuracy and performance. It is shown that, for example, the interpolation-based method is more than 16 times faster than the conventional step-reduction method for a system with 9 digital controllers. This performance gap between the methods expands as the number of controllers increases, since the conventional method's time steps become more limited while the proposed method takes relatively large time steps. Furthermore, many variations of the proposed methods are also developed, suited for different situations. For example, a light version of the interpolation-based method is devised for the simulation of computationally heavy controllers, which is about 40 percent faster than the original interpolation-based approach. Also, a novel approach for simplified simulation of power systems with digital controllers is proposed, which improves the accuracy of the traditional simplified simulations. Last but not least, a variation of the proposed method is also developed, which is based on solving the controller inputs instead of its outputs. The simulations revealed that this approach improves the performance over the original method by about 18 percent. Finally, an implementation of the interpolation-based approach using the Modelica language is provided to make it accessible. It should be noted that all the proposed interpolation-based methods have the advantage of being able to solve systems with non-equation-based digital controllers, such as machine-learning-based controllers with a variable time step approach, which is not possible with any conventional methods. In other words, the conventional methods cannot simulate the non-equation-based digital controllers quickly and accurately, as either they have to reduce the time steps constantly to catch the sampling actions of the controllers, or ignore some events to speed up. Furthermore, conventional variable-step solvers that rely on modeling the controllers with continuous equations will fail to model and simulate those types of controllers, as they cannot be described with DAEs."
summary = ""
featured = false
projects = ["mod-sim"]
slides = ""
doi = ""
url_code = ""
url_dataset = ""
url_poster = ""
url_slides = ""
url_source = "https://hdl.handle.net/20.500.14279/35985"
url_video = ""
math = true
highlight = true
[image]
image = ""
caption = ""
+++
