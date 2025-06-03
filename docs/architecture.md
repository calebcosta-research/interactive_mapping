# System Architecture

This document outlines the high-level architecture of the avalanche risk monitoring system.

1. **Data Acquisition**
   - Satellite and remote sensing data is periodically retrieved using APIs.
   - A drone captures high-resolution imagery or video of target slopes.

2. **Processing Pipeline**
   - Raw imagery is stored under `data/raw/`.
   - Pre-processing and feature extraction produce cleaned datasets in `data/processed/`.
   - Machine learning models in `models/` use environmental metrics and computer vision outputs to calculate risk scores.

3. **Visualization**
   - The application in `app/` visualizes risk maps, optionally overlaying topographical data.
   - Starlink Roam provides connectivity for remote updates.
