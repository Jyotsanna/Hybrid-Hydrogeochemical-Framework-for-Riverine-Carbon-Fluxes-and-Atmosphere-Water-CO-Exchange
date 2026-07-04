# Dataset Documentation

## Overview

This repository contains the hydrochemical dataset used to investigate water quality, hydrogeochemical processes, and riverine carbon dynamics within the Cauvery River Basin. The dataset comprises field observations, laboratory measurements, and derived hydrochemical indices that form the basis of the statistical and geochemical analyses presented in this repository.

The data were collected from surface water and groundwater sampling locations distributed across the river basin. Each sample was analysed for major physicochemical parameters, major ions, and water quality indices following standard analytical procedures.

---

# Study Area

**River Basin:** Cauvery River Basin, India

The Cauvery River Basin extends across southern India and includes diverse geological formations, climatic conditions, and land-use patterns. These variations influence hydrochemical evolution and make the basin suitable for studying weathering processes and riverine carbon transport.

---

# Dataset Organization

```
data/

├── raw/
│     ├── surface_water.csv
│     ├── groundwater.csv
│     └── station_metadata.csv
│
├── processed/
│     ├── hydrochemistry_processed.csv
│     └── hydrochemical_indices.csv
│
└── metadata/
      ├── parameter_description.csv
      └── units.csv
```

---

# Variables Included

## Sampling Information

| Variable  | Description                          | Unit            |
| --------- | ------------------------------------ | --------------- |
| Sample_ID | Unique sample identifier             | -               |
| Station   | Sampling location                    | -               |
| Latitude  | Geographic latitude                  | Decimal Degrees |
| Longitude | Geographic longitude                 | Decimal Degrees |
| Elevation | Elevation above mean sea level       | m               |
| Date      | Sampling date                        | YYYY-MM-DD      |
| Season    | Pre-monsoon / Monsoon / Post-monsoon | -               |

---

## Field Measurements

| Variable    | Description             | Unit  |
| ----------- | ----------------------- | ----- |
| Temperature | Water temperature       | °C    |
| pH          | Acidity/alkalinity      | -     |
| EC          | Electrical conductivity | µS/cm |
| TDS         | Total dissolved solids  | mg/L  |

---

## Major Cations

| Variable         | Unit |
| ---------------- | ---- |
| Calcium (Ca²⁺)   | mg/L |
| Magnesium (Mg²⁺) | mg/L |
| Sodium (Na⁺)     | mg/L |
| Potassium (K⁺)   | mg/L |

---

## Major Anions

| Variable            | Unit |
| ------------------- | ---- |
| Bicarbonate (HCO₃⁻) | mg/L |
| Carbonate (CO₃²⁻)   | mg/L |
| Chloride (Cl⁻)      | mg/L |
| Sulphate (SO₄²⁻)    | mg/L |
| Nitrate (NO₃⁻)      | mg/L |

---

# Derived Hydrochemical Indices

The following indices are calculated from the measured parameters:

| Index                           | Purpose                          |
| ------------------------------- | -------------------------------- |
| Total Hardness (TH)             | Drinking water quality           |
| Sodium Percentage (Na%)         | Irrigation suitability           |
| Sodium Adsorption Ratio (SAR)   | Soil sodicity assessment         |
| Residual Sodium Carbonate (RSC) | Irrigation hazard                |
| Magnesium Hazard (MH)           | Soil quality evaluation          |
| Permeability Index (PI)         | Long-term irrigation suitability |

---

# Example Dataset

| Sample_ID | Station    |  pH |  EC | TDS | Ca | Mg | Na |   K | HCO₃ | Cl |
| --------- | ---------- | --: | --: | --: | -: | -: | -: | --: | ---: | -: |
| SW01      | Upstream   | 7.3 | 280 | 179 | 42 | 16 | 18 | 2.3 |  156 | 21 |
| SW02      | Midstream  | 7.6 | 365 | 234 | 48 | 19 | 24 | 3.1 |  182 | 29 |
| SW03      | Downstream | 7.8 | 420 | 269 | 51 | 22 | 31 | 3.5 |  201 | 37 |

> **Note:** The values shown above are illustrative examples demonstrating the dataset structure. They are not intended to replace the original research measurements.

---

# Data Processing Workflow

```
Field Sampling
        ↓
Laboratory Analysis
        ↓
Data Validation
        ↓
Data Cleaning
        ↓
Hydrochemical Calculations
        ↓
Statistical Analysis
        ↓
Interpretation
```

---

# Quality Assurance

To ensure data reliability, the following quality-control procedures were applied:

* Instrument calibration before field measurements.
* Standard laboratory analytical methods.
* Duplicate sample analysis where applicable.
* Consistency checks for hydrochemical parameters.
* Verification of data entry and unit conversions.

---

# Applications

The dataset supports a range of environmental and hydrogeochemical investigations, including:

* Water quality assessment.
* Hydrochemical facies analysis.
* Irrigation suitability evaluation.
* Drinking water quality assessment.
* Weathering process identification.
* Statistical analysis of water chemistry.
* River basin management.
* Riverine carbon cycle research.
* Environmental monitoring.

---

# Data Availability

The complete research dataset forms part of the author's Master's dissertation. To protect research integrity and institutional ownership, only representative data structures and computational examples are included in this repository.

Researchers interested in collaboration or academic use of the full dataset are welcome to contact the author.

---

# Citation

If you use this repository or its analytical workflow, please cite the associated thesis and this GitHub repository in any resulting publications.
