# Sustainable Power Systems Laboratory (SPS Lab)

[![Website](https://img.shields.io/badge/Website-sps--lab.org-blue)](https://sps-lab.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.md)
[![Hugo](https://img.shields.io/badge/Hugo-0.135.0-orange)](https://gohugo.io/)
[![Netlify](https://img.shields.io/badge/Deployed%20on-Netlify-00AD9F)](https://netlify.com/)

## About

The **Sustainable Power Systems Laboratory (SPS Lab)** is a research group led by Dr. Petros Aristidou at the [Department of Electrical Engineering and Computer Engineering and Informatics](https://www.cut.ac.cy/faculties/fet/eecei/?languageId=1) at the Cyprus University of Technology.

Our mission is to make future electric power systems sustainable, secure, and resilient. We combine mathematical tools from numerical analysis and optimization with high-performance computational tools and machine learning techniques to tackle modern power system challenges.

## Research Focus

Our research spans several key areas in power systems:

- **Low-inertia Grids**: Developing control algorithms for future power systems with reduced inertia
- **Cyber-Physical Systems**: Modeling and simulation of smart grid technologies
- **Machine Learning**: Data-driven approaches for power system applications
- **Numerical Methods**: Advanced simulation techniques for electric power systems
- **Optimization**: Planning and operation optimization for active distribution networks

## Website

This repository contains the source code for the SPS Lab website, built using [Hugo](https://gohugo.io/) with the [Hugo Blox Builder](https://github.com/HugoBlox/hugo-blox-builder) framework.

### Features

- **Responsive Design**: Mobile-friendly interface
- **Academic Publications**: Integrated publication management system
- **Research Projects**: Showcase of ongoing and completed research
- **Team Profiles**: Detailed information about lab members
- **News & Blog**: Latest updates and research highlights
- **Contact Information**: Easy access to lab contact details

## Getting Started

### Prerequisites

- [Hugo](https://gohugo.io/installation/) (version 0.135.0 or later)
- [Git](https://git-scm.com/)
- [Go](https://golang.org/) (version 1.15 or later)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/sps-cut.git
   cd sps-cut
   ```

2. **Install Hugo modules**
   ```bash
   hugo mod get
   ```

3. **Start the development server**
   ```bash
   hugo server -D
   ```

4. **View the website**
   Open your browser and navigate to `http://localhost:1313`

### Building for Production

```bash
hugo --gc --minify
```

The built site will be in the `public/` directory.

## Content Management

### Adding New Content

- **Publications**: Add to `content/publication/` directory
- **Research Projects**: Add to `content/project/` directory
- **Blog Posts**: Add to `content/post/` directory
- **Team Members**: Add to `content/authors/` directory
- **Courses**: Add to `content/courses/` directory

### Content Structure

Each content type follows Hugo's standard front matter format:

```yaml
---
title: "Your Title"
date: 2024-01-01
draft: false
tags: ["tag1", "tag2"]
summary: "Brief description"
---
```

## Deployment

The website is automatically deployed on [Netlify](https://netlify.com/) with the following configuration:

- **Build Command**: `hugo --gc --minify -b $URL`
- **Publish Directory**: `public`
- **Hugo Version**: 0.135.0

### Custom Redirects

The website includes several custom redirects for:
- JupyterHub access (`/jhub`)
- Microsoft Teams meetings (`/meet`)
- Open positions (`/open-positions`)

## Contact Information

### For Research Collaboration

- **Email**: [info@sps-lab.org](mailto:info@sps-lab.org)
- **Phone**: +357 25 002618
- **Address**: 33 Saripoloy str, Limassol, 3036, Cyprus
- **Office**: Ttofis building, 5th floor, office 521B

### For Website Issues

If you encounter any issues with the website or have suggestions for improvements:

1. **Check existing issues**: Look through the [GitHub Issues](https://github.com/your-username/sps-cut/issues)
2. **Create a new issue**: Use the issue template to report bugs or request features
3. **Contact the web team**: Email [info@sps-lab.org](mailto:info@sps-lab.org) with "Website Issue" in the subject line

## Licensing

### Website Code

This website's source code is licensed under the **MIT License** - see the [LICENSE.md](LICENSE.md) file for details.

### Research Content

**Important**: The research work, publications, and academic content featured on this website are **NOT** covered by the MIT license. Each research project, publication, or software tool may have its own specific licensing terms:

- **Academic Publications**: Subject to the respective journal/publisher licensing terms
- **Research Software**: Each tool may have its own open-source or proprietary license
- **Research Data**: May be subject to data sharing agreements or institutional policies

Please contact the respective authors or the lab directly for information about licensing specific research materials.

## Acknowledgments

- **Theme**: Built with [Hugo Blox Builder](https://github.com/HugoBlox/hugo-blox-builder)
- **Hosting**: Deployed on [Netlify](https://netlify.com/)
- **Institution**: [Cyprus University of Technology](https://cut.ac.cy)

## Support

For technical support or questions about the website, please contact [info@sps-lab.org](mailto:info@sps-lab.org).

---

**Sustainable Power Systems Laboratory**  
*Making future electric power systems sustainable, secure, and resilient*

[Website](https://sps-lab.org/) | [Contact](mailto:info@sps-lab.org) | [GitHub](https://github.com/SPS-L/)
