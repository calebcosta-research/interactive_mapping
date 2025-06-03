# Avalanche Risk Monitoring System

This project provides a prototype structure for building a live avalanche risk monitoring platform. It combines satellite imagery, drone-based reconnaissance, environmental models, and computer vision analysis to predict weak points on the snowpack. The platform is designed to be deployable in the field with Starlink Roam providing WiFi connectivity.

## Project Structure

- **satellite/** – Scripts and tools for retrieving and pre-processing satellite or remote sensing imagery.
- **drone/** – Drone control utilities and computer vision pipelines for analyzing aerial footage.
- **models/** – Environmental and machine learning models used to estimate avalanche risk.
- **app/** – Code for the field application or web interface that displays risk maps and topography.
- **config/** – Configuration files such as credentials, model parameters, or API keys.
- **data/** – Organized storage for raw and processed datasets.
  - **data/raw/** – Unprocessed downloads from satellites, sensors, or drone cameras.
  - **data/processed/** – Cleaned or transformed data ready for modeling.
- **docs/** – Documentation and design notes.
- **scripts/** – Helper scripts for managing the data pipeline and deployments.

## Getting Started

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

2. Retrieve remote sensing data and store under `data/raw/`.
3. Run analysis scripts in `models/` to train or update risk predictions.
4. Launch the app from the `app/` directory to view the latest maps.

## Future Work

- Integrate weather forecast APIs for real-time snowfall and temperature gradient inputs.
- Develop a computer vision model that identifies avalanche start zones from drone imagery.
- Build a field-ready application leveraging Starlink connectivity for data uploads and map updates.

