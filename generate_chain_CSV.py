#!/usr/bin/env python3
"""
chain_lookup.py

Generates a CSV lookup table of chain link counts for combinations of:
  - sprocket teeth T1 and T2 (11 to 65 teeth)
  - center-to-center distances (200mm to 500mm in 5mm steps)

Usage:
    python chain_lookup.py
"""

import numpy as np
import pandas as pd
from math import ceil, pi

def generate_chain_lookup(
    teeth_min=11,
    teeth_max=65,
    dist_min_mm=200,
    dist_max_mm=500,
    dist_step_mm=5,
    pitch_in=0.5,
    output_csv="chain_sprocket_links_lookup.csv"
):
    """
    Generates a CSV lookup table of chain link counts for all combinations of:
      - sprocket teeth T1 and T2 from teeth_min to teeth_max (inclusive)
      - center-to-center distances from dist_min_mm to dist_max_mm (step dist_step_mm)
    The link count is computed via the approximate formula and rounded up.
    """
    records = []
    for T1 in range(teeth_min, teeth_max + 1):
        for T2 in range(teeth_min, teeth_max + 1):
            for C_mm in range(dist_min_mm, dist_max_mm + 1, dist_step_mm):
                # Convert mm to inches
                C_in = C_mm / 25.4
                # Continuous link count formula
                N_cont = (
                    (T1 + T2) / 2
                    + 2 * C_in / pitch_in
                    + (T1 - T2)**2 / (4 * pi**2 * C_in)
                )
                # Round up to the next whole link
                N_links = int(ceil(N_cont))
                records.append((T1, T2, C_mm, N_links))

    # Create DataFrame and save to CSV
    df = pd.DataFrame(records, columns=['T1', 'T2', 'C_mm', 'links'])
    df.to_csv(output_csv, index=False)
    print(f"Lookup table saved to {output_csv} with {len(df)} rows.")

if __name__ == "__main__":
    generate_chain_lookup()
