---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Setting a JupyterHub for the lab"
subtitle: ""
summary: "Just a record of how we set up the JupyterHub for teaching/research in the lab."
authors: ["P. Aristidou"]
tags: []
categories: ['blog']
date: 2020-06-29T00:00:48+03:00
lastmod: 2024-09-29T00:00:48+03:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
# 
projects: []
---


JupyterHub is a fantastic platform for getting students up and running with Jupyter notebooks without the hassle of installations and maintenance on individual machines. In our lab, we use [The Littlest JupyterHub (TLJH)](https://tljh.jupyter.org/) since we have only a few users. It can be set up on cloud instances or servers you own. Check out [the installation guide](https://tljh.jupyter.org/en/latest/install/index.html) for more details. We use [our own server](https://sps.cut.ac.cy/jhub), so I'll walk you through the process assuming you have an Ubuntu-based server with remote SSH access and admin rights.

## Installation Process

First, let's upgrade the server and install some essential packages:

```bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install python3 python3-dev git curl xorg
```

If Apache is enabled, it needs to be disabled since it conflicts with the built-in Traefik reverse proxy used by JupyterHub:

```bash
sudo systemctl status apache2
sudo systemctl disable apache2
sudo apt remove apache2
```

Next, we'll install Anaconda. Head over to [Anaconda's archive](https://repo.anaconda.com/archive/) to get the latest version and update the link accordingly:

```bash
cd /tmp
curl -O https://repo.anaconda.com/archive/Anaconda3-2023.07-Linux-x86_64.sh
bash Anaconda3-2023.07-Linux-x86_64.sh
cd ~
source ~/.bashrc
conda info
```

If needed, create a sudo account for JupyterHub admin access:

```bash
adduser apetros
usermod -aG sudo apetros
```

Now, let's install JupyterHub using TLJH:

```bash
curl -L https://tljh.jupyter.org/bootstrap.py | sudo -E python3 - --admin apetros_new
```

We can fine-tune server parameters to manage resources for students effectively. For example:

```bash
sudo tljh-config set limits.memory 6G
sudo tljh-config set limits.cpu 1
sudo tljh-config set user_environment.default_app jupyterlab
sudo tljh-config set services.cull.every 600
sudo tljh-config set services.cull.timeout 1800
sudo tljh-config reload
```

To set up HTTPS, replace `_your-email_` and `_your-domain_` with your own details:

```bash
sudo tljh-config set https.enabled true
sudo tljh-config set https.letsencrypt.email your_email
sudo tljh-config add-item https.letsencrypt.domains your_domain
sudo tljh-config reload proxy
```

## Post-Installation Setup

Once JupyterHub is up and running, install the necessary packages for your courses. In my courses, I use:

- **Pandas**: For energy analytics.
- **Pyomo, IPOPT, CoinCBC**: For optimization problems.
- **Pandapower**: For power-flow and short-circuit analysis.
- **PyPSA, STEPSS**: For power system dynamics.

Install these packages as follows:

```bash
sudo -E conda install -c conda-forge scipy numpy pandas numba matplotlib pyomo ipopt glpk coincbc pypsa networkx cartopy
sudo -E pip install pandapower
sudo -E pip install stepss
```

### Setting Up STEPSS

[STEPSS in Python](https://stepss.sps-lab.org/python/) bundles the RAMSES and Helios
engines, so there is no separate solver to install. On Linux it links against three
system runtime libraries, which are not always present on a server image:

```bash
sudo apt-get update
sudo apt-get install libopenblas0 libgfortran5 libgomp1
```

These provide the BLAS/LAPACK routines the solver uses, the GNU Fortran runtime, and
the OpenMP runtime for multi-core execution. Nothing needs adding to
`LD_LIBRARY_PATH`: they install into the standard system paths, so JupyterHub picks
them up with no spawner configuration. If `import stepss` fails with a
shared-library error, these are what is missing. See the
[Python installation guide](https://stepss.sps-lab.org/python/installation/) for the
macOS equivalents and for pinning a particular engine version.

To get started, click [here](https://sps-lab.org/jhub-nordic) to clone the [repository with the Nordic system](https://github.com/SPS-L/stepss-IEEE-Nordic-Test-system).
