# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 12:14:09 2025
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Material and Specimen Parameters
original_length = 50.0  # mm
cross_sectional_area = 100.0  # mm^2

# Load data
data = pd.read_csv('tensile_test.csv')

# Calculate Stress and Strain
data['Stress_MPa'] = data['Load_N'] / cross_sectional_area
data['Strain'] = data['Extension_mm'] / original_length

# Plot Stress-Strain Curve
plt.figure(figsize=(10,6))
plt.plot(data['Strain'], data['Stress_MPa'], marker='o', linestyle='-', color='blue')
plt.title('Stress-Strain Curve of Steel Specimen', fontsize=16)
plt.xlabel('Strain (mm/mm)', fontsize=14)
plt.ylabel('Stress (MPa)', fontsize=14)
plt.grid(True)
plt.show()

# Determine Young's Modulus (Elastic Modulus)
linear_region = data.iloc[:10]
coefficients = np.polyfit(linear_region['Strain'], linear_region['Stress_MPa'], 1)
youngs_modulus = coefficients[0]
print(f"Young's Modulus: {youngs_modulus:.2f} MPa")

# Determine Ultimate Tensile Strength (UTS)
uts = data['Stress_MPa'].max()
print(f"Ultimate Tensile Strength (UTS): {uts:.2f} MPa")

# Determine Yield Strength (0.2% Offset Method)
offset = 0.002
offset_line = youngs_modulus * (data['Strain'] - offset)
difference = data['Stress_MPa'] - offset_line
yield_index = difference.abs().idxmin()
yield_strength = data['Stress_MPa'][yield_index]
print(f"Yield Strength (Approximate): {yield_strength:.2f} MPa")