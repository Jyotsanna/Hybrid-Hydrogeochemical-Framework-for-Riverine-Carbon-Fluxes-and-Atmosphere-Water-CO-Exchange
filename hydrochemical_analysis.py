"""
=============================================================
Hybrid Hydrogeochemical Analysis Toolkit
Author: Jyotsna Roy
Repository:
Hybrid-Riverine-Carbon-Fluxes

Description:
This script contains basic hydrochemical calculations used for
surface water and groundwater quality assessment.

Equations implemented include:

1. Total Dissolved Solids (TDS)
2. Total Hardness (TH)
3. Sodium Percentage (Na%)
4. Sodium Adsorption Ratio (SAR)
5. Residual Sodium Carbonate (RSC)
6. Magnesium Hazard (MH)
7. Permeability Index (PI)
8. Pearson Correlation
9. Principal Component Analysis (PCA)
10. Hierarchical Cluster Analysis

=============================================================
"""

import math
import pandas as pd
from scipy.stats import pearsonr
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import linkage


# ============================================================
# 1. Total Dissolved Solids
# Equation:
#
# TDS = EC × 0.64
#
# EC = Electrical Conductivity (µS/cm)
# ============================================================

def calculate_tds(ec):
    return ec * 0.64


# ============================================================
# 2. Total Hardness
#
# TH = 2.497(Ca) + 4.115(Mg)
#
# Result in mg/L as CaCO3
# ============================================================

def total_hardness(ca, mg):
    return 2.497 * ca + 4.115 * mg


# ============================================================
# 3. Sodium Percentage
#
# Na% = ((Na + K)/(Ca + Mg + Na + K))*100
# ============================================================

def sodium_percentage(ca, mg, na, k):
    return ((na + k) / (ca + mg + na + k)) * 100


# ============================================================
# 4. Sodium Adsorption Ratio
#
# SAR = Na / √((Ca + Mg)/2)
# ============================================================

def sar(na, ca, mg):
    return na / math.sqrt((ca + mg) / 2)


# ============================================================
# 5. Residual Sodium Carbonate
#
# RSC = (HCO3 + CO3) - (Ca + Mg)
# ============================================================

def rsc(hco3, co3, ca, mg):
    return (hco3 + co3) - (ca + mg)


# ============================================================
# 6. Magnesium Hazard
#
# MH = Mg/(Ca+Mg) ×100
# ============================================================

def magnesium_hazard(ca, mg):
    return (mg / (ca + mg)) * 100


# ============================================================
# 7. Permeability Index
#
# PI=((Na+√HCO3)/(Ca+Mg+Na))*100
# ============================================================

def permeability_index(na, hco3, ca, mg):
    return ((na + math.sqrt(hco3)) /
            (ca + mg + na)) * 100


# ============================================================
# 8. Pearson Correlation
# ============================================================

def pearson_correlation(df, variable1, variable2):

    r, p = pearsonr(df[variable1], df[variable2])

    print("===================================")
    print("Pearson Correlation")
    print("Variables :", variable1, "vs", variable2)
    print("Correlation coefficient (r):", round(r,4))
    print("P-value:", p)
    print("===================================")

    return r, p


# ============================================================
# 9. Principal Component Analysis
# ============================================================

def perform_pca(df, n_components=2):

    pca = PCA(n_components=n_components)

    components = pca.fit_transform(df)

    print("===================================")
    print("Principal Component Analysis")
    print("Explained Variance Ratio")
    print(pca.explained_variance_ratio_)
    print("===================================")

    return components


# ============================================================
# 10. Hierarchical Cluster Analysis
# ============================================================

def hierarchical_cluster(df):

    clusters = linkage(df, method='ward')

    print("===================================")
    print("Hierarchical Cluster Analysis")
    print("Ward Linkage Completed")
    print("===================================")

    return clusters


# ============================================================
# Example Hydrochemical Dataset
# ============================================================

sample = {

    "EC":250,

    "Ca":45,

    "Mg":18,

    "Na":55,

    "K":4,

    "HCO3":180,

    "CO3":0

}


print("\n")

print("===================================")
print("HYDROCHEMICAL CALCULATIONS")
print("===================================")

tds = calculate_tds(sample["EC"])
print("Total Dissolved Solids =", round(tds,2),"mg/L")

th = total_hardness(sample["Ca"],sample["Mg"])
print("Total Hardness =",round(th,2),"mg/L")

na_percent = sodium_percentage(
    sample["Ca"],
    sample["Mg"],
    sample["Na"],
    sample["K"]
)

print("Sodium Percentage =",round(na_percent,2),"%")

sar_value = sar(
    sample["Na"],
    sample["Ca"],
    sample["Mg"]
)

print("SAR =",round(sar_value,2))

rsc_value = rsc(
    sample["HCO3"],
    sample["CO3"],
    sample["Ca"],
    sample["Mg"]
)

print("Residual Sodium Carbonate =",round(rsc_value,2))

mh = magnesium_hazard(
    sample["Ca"],
    sample["Mg"]
)

print("Magnesium Hazard =",round(mh,2),"%")

pi = permeability_index(
    sample["Na"],
    sample["HCO3"],
    sample["Ca"],
    sample["Mg"]
)

print("Permeability Index =",round(pi,2),"%")

print("===================================\n")


# ============================================================
# Example Statistical Analysis
# ============================================================

df = pd.DataFrame({

    "Na":[20,30,40,50,60,70],

    "Cl":[18,29,39,49,58,69],

    "Ca":[45,40,38,36,34,30],

    "Mg":[18,17,16,15,14,13]

})

pearson_correlation(df,"Na","Cl")

perform_pca(df)

hierarchical_cluster(df)

print("\nAnalysis Completed Successfully.")
