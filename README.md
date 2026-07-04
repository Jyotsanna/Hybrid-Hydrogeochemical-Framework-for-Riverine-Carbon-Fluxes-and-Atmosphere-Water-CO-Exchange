# Hybrid-Hydrogeochemical-Framework-for-Riverine-Carbon-Fluxes-and-Atmosphere-Water-CO-Exchange# 🌍 Hybrid Hydrogeochemical Framework for Riverine Carbon Fluxes and Atmosphere–Water CO₂ Exchange

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Research](https://img.shields.io/badge/Research-Hydrogeochemistry-success)]()
[![GIS](https://img.shields.io/badge/GIS-ArcGIS%20%7C%20QGIS-orange)]()

---

## Overview

This repository contains the computational framework and supporting materials developed as part of my Master's research in **Physical Geography**. The study investigates the hydrogeochemical evolution of river water and groundwater and quantifies riverine carbon dynamics using a combination of hydrochemical analysis, geochemical modelling, statistical techniques, and geospatial analysis.

The repository demonstrates how field observations, laboratory measurements, and computational methods can be integrated to understand the processes controlling water chemistry and carbon transport in a tropical river basin.

---

# Research Background

Rivers play an essential role in the global carbon cycle by transporting dissolved carbon from continents to oceans while simultaneously exchanging carbon dioxide (CO₂) with the atmosphere.

Hydrogeochemical processes such as mineral weathering, groundwater–surface water interaction, evaporation, and anthropogenic activities influence river chemistry and carbon transport. Understanding these processes is important for:

- Water resource management
- Climate change research
- Carbon cycle assessment
- River basin management
- Environmental sustainability

---

# Research Objectives

The major objectives of this research are:

- Investigate the hydrochemical characteristics of river water and groundwater.
- Assess the suitability of water for drinking and irrigation.
- Identify dominant hydrogeochemical processes.
- Evaluate the influence of natural and anthropogenic factors on water chemistry.
- Apply geochemical modelling to understand mineral-water interactions.
- Estimate carbon dynamics using carbonate chemistry.
- Demonstrate basic computational methods for hydrochemical calculations using Python.

---

# Study Area

The research focuses on the **Cauvery River Basin**, one of the major river basins in southern India.

The basin experiences tropical monsoon climatic conditions and exhibits considerable spatial variation in geology, geomorphology, land use, groundwater conditions, and hydrochemistry. These variations make it an ideal natural laboratory for investigating hydrogeochemical processes and riverine carbon transport.

---

# Methodology

The research workflow consists of the following major steps:

```
Field Sampling
      ↓
Laboratory Analysis
      ↓
Hydrochemical Analysis
      ↓
Water Quality Assessment
      ↓
Statistical Analysis
      ↓
Geochemical Modelling
      ↓
Carbonate System Analysis
      ↓
GIS Mapping
      ↓
Interpretation
```

---

# Hydrochemical Parameters

The repository includes calculations for commonly used hydrochemical parameters such as:

- Total Dissolved Solids (TDS)
- Total Hardness (TH)
- Sodium Percentage (Na%)
- Sodium Adsorption Ratio (SAR)
- Residual Sodium Carbonate (RSC)
- Magnesium Hazard (MH)
- Permeability Index (PI)

---

# Mathematical Equations

## Total Dissolved Solids

TDS = EC × 0.64

---

## Total Hardness

TH = 2.497(Ca) + 4.115(Mg)

---

## Sodium Percentage

Na% = ((Na + K)/(Ca + Mg + Na + K)) ×100

---

## Sodium Adsorption Ratio

SAR = Na / √((Ca + Mg)/2)

---

## Residual Sodium Carbonate

RSC = (HCO₃ + CO₃) − (Ca + Mg)

---

## Magnesium Hazard

MH = Mg/(Ca + Mg) ×100

---

## Permeability Index

PI = ((Na + √HCO₃)/(Ca + Mg + Na)) ×100

---

# Repository Structure

```
Hybrid-Riverine-Carbon-Fluxes/

│
├── README.md
├── LICENSE
├── requirements.txt
│
├── hydrochemical_analysis.py
│
├── data/
│
├── figures/
│
├── results/
│
└── thesis/
```

---

# Python Libraries Used

The analysis uses the following scientific Python libraries:

- pandas
- numpy
- matplotlib
- scipy
- scikit-learn

Install the required libraries using:

```bash
pip install -r requirements.txt
```

---

# Running the Code

Clone the repository:

```bash
git clone https://github.com/yourusername/Hybrid-Riverine-Carbon-Fluxes.git
```

Move into the repository:

```bash
cd Hybrid-Riverine-Carbon-Fluxes
```

Run the analysis:

```bash
python hydrochemical_analysis.py
```

---

# Results

The Python script demonstrates calculations for:

- Water quality indices
- Hydrochemical parameters
- Pearson correlation
- Principal Component Analysis (PCA)
- Hierarchical Cluster Analysis

The repository is intended as an educational and research resource illustrating the computational implementation of hydrochemical methods.

---

# Software Used

- Python
- ArcGIS
- IBM SPSS Statistics
- PHREEQC
- CO₂SYS
- Microsoft Excel

---

# Applications

The methods presented here are applicable to:

- Hydrogeochemistry
- Groundwater studies
- Surface water quality assessment
- River basin management
- Environmental monitoring
- Carbon cycle research
- Climate change studies
- Earth System Science

---

# Future Work

Future versions of this repository may include:

- Complete Jupyter notebooks
- Automated GIS workflows
- Additional geochemical models
- Interactive visualizations
- Climate scenario analysis
- Machine learning applications for water quality prediction

---

# Citation

If you use this repository in your research, please cite:

> R, J. (Year). *Hybrid Hydrogeochemical Framework for Riverine Carbon Fluxes and Atmosphere–Water CO₂ Exchange*. GitHub Repository.

---

# About the Author

**Jyotsna **

**Research Interests**

- Hydrogeochemistry
- Climate Change
- Earth System Science
- Physical Geography
- GIS and Remote Sensing
- Riverine Carbon Cycling
- Environmental Modelling
- Scientific Computing

---

# License

This project is distributed under the MIT License.

---

# Acknowledgements

I gratefully acknowledge the Department of Geography, Jamia Millia Islamia, for providing the academic environment and support that made this research possible. I also thank my research supervisor for valuable guidance throughout the study.

---

⭐ If you find this repository useful, consider giving it a star.
