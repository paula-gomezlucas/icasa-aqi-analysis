# ICAsa – Air Quality Exposure Analysis Prototype

## Overview

**ICAsa** is a prototype web application designed to analyze local air quality data (ICA / AQI) and estimate long-term exposure for residential areas.
The project aggregates environmental data and computes interpretable indicators to help users better understand average air quality conditions in urban environments.

This was my **first end-to-end web and data project**, combining backend APIs, data processing, and frontend interaction.

## Project Origin and Attribution

This repository is a **reconstructed public version** of a collaborative university project that was originally developed in a **private repository**.

Due to repository visibility restrictions, the original project cannot be shared publicly.
This version has been created for **portfolio and documentation purposes**, based on the parts of the implementation I developed.

I was responsible for the majority of the technical work, including:
- Data ingestion and preprocessing
- ICA / AQI computation logic
- Backend API design
- Frontend–backend integration

No proprietary, confidential, or teammate-only material is included in this repository.

## Motivation

Air quality has a direct impact on long-term health, yet available data is often fragmented or difficult to interpret for non-expert users.
ICAsa was conceived as a lightweight tool to bridge this gap by:
- Aggregating air quality measurements from open data sources
- Computing long-term average exposure indicators
- Presenting results in a simple, user-oriented way

The project prioritizes **interpretability and accessibility** over predictive modeling.

## System Architecture

The application followed a simple client–server architecture:

### Backend
- Implemented using **FastAPI**
- Responsibilities:
  - Loading and cleaning air quality datasets
  - Computing ICA / AQI indicators
  - Exposing REST endpoints for querying results

### Frontend
- Implemented using **JavaScript**
- Responsibilities:
  - Interacting with the backend API
  - Triggering queries based on user input
  - Displaying aggregated air quality information

The system was designed as a **prototype**, not a production-ready service.

## Data

The project relied on **publicly available air quality datasets**, focusing on:
- Urban monitoring stations
- Aggregated measurements over time
- City- or district-level indicators

All data used was non-sensitive and aggregated.

## Methodology

1. **Data ingestion**
   - Load air quality measurements from open datasets
   - Clean and standardize records

2. **Indicator computation**
   - Compute average ICA / AQI values over extended time periods
   - Aggregate results by geographic area

3. **API exposure**
   - Serve computed indicators through REST endpoints

4. **Frontend interaction**
   - Query backend endpoints
   - Present results in a user-facing interface

## Limitations and Future Work

- This repository does not yet include the full original source code.
- Some frontend and backend components are in the process of being recovered.
- Future improvements could include:
  - Completing the reconstruction of the full application
  - Expanding coverage to additional cities
  - Improving UI/UX and visualizations
  - Adding temporal trend analysis

## Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** JavaScript
- **Data processing:** Python
- **APIs:** REST

## Status

This project is presented as an **early-stage prototype and learning experience**.
It documents my first exposure to:
- Full-stack web development
- API-driven design
- Integrating data analysis into interactive applications
