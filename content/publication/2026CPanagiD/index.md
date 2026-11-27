+++
title = "Enhanced Optimal Power Flow Using a Trained Neural Network Surrogate for Distribution Grid Constraints"
date = "2026-11-03"

authors = ["S. Panagi", "C. Spanias", "P. Aristidou"]
tags = ["Neural Networks", "Distribution Networks", "Optimal Power Flow", "Big-M Method", "Surrogate Modeling"]
publication_types = ["paper-conference"]
publication = "_MEDPOWER 2026_"
publication_short = ""
abstract = "The growing penetration of distributed energy resources (DERs), electric vehicles (EVs), and heat pumps (HPs) in distribution networks underscores the need for secure, computationally efficient optimal power flow (OPF) solutions. Traditional OPF formulations often suffer from scalability limitations and may rely on relaxations/approximations whose exactness is not guaranteed. This paper proposes a framework in which a trained neural network (NN) surrogate is embedded directly within the OPF as a constraint replacement. Specifically, the nonlinear power-flow-to-voltage mapping is replaced by an exact mixedinteger linear encoding of the NN (i.e., the NN input–output map is represented without approximation), while all remaining OPF constraints are preserved. Using a realistic low-voltage network with integrated PV, EVs, and HPs, the proposed method achieves high voltage accuracy during post-solution AC power flow validation, with maximum deviations of less than 1.0 V in the examined test cases. The resulting NN-OPF problems are solved to global optimality within the MILP solver tolerance, and numerical results demonstrate substantially reduced computation time compared to nonlinear OPF models, with performance competitive with SOCP-based DistFlow formulations."
summary = ""
featured = false
projects = ['dense']
slides = ""
doi = ""
url_code = ""
url_dataset = ""
url_poster = ""
url_slides = ""
url_source = ""
url_video = ""
math = true
highlight = true
[image]
image = ""
caption = ""
+++
