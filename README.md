# ICAsa – Air Quality Exposure Analysis Prototype

## Overview

**ICAsa** is a prototype web application designed to analyze local air quality data (ICA / AQI) and estimate long-term exposure for residential areas.
The project aggregates environmental data and computes interpretable indicators to help users understand average air quality conditions in urban environments.

The application was implemented as a local prototype consisting of a **FastAPI backend** and a **Chrome extension frontend**.
This project represents my **first end-to-end full-stack and data-driven web application**.

> ⚠️ This project is a prototype developed as a learning experience and is not intended for production use.

## Demo

▶️ **[Watch demo video – ICAsa prototype](https://youtu.be/Jz-RyCHPPMQ)**

The video demonstrates the Chrome extension interacting with the local FastAPI backend to retrieve and display aggregated air quality information.

## Project Origin and Attribution

This repository is a **reconstructed public version** of a collaborative university project originally developed in a **private repository**.

Due to repository visibility restrictions, the original project cannot be shared publicly.
This version has been created for **portfolio and documentation purposes**, based on the parts of the implementation I developed.

I was responsible for the majority of the technical work, including:
- Data ingestion and preprocessing
- ICA / AQI computation logic
- Backend API design
- Frontend–backend integration

No proprietary, confidential, or teammate-only material is included in this repository.

## Motivation

Air quality has a direct impact on long-term health, yet available information is often fragmented or difficult to interpret for non-expert users.
ICAsa was conceived as a lightweight tool to bridge this gap by:
- Aggregating air quality measurements from open data sources
- Computing long-term average exposure indicators
- Presenting results in a simple, user-oriented way

The project prioritizes **interpretability and accessibility** over predictive modeling.

## System Architecture

The application follows a simple client–server architecture:

### Backend
- Implemented using **FastAPI**
- Responsibilities:
  - Loading and cleaning air quality datasets
  - Computing ICA / AQI indicators
  - Exposing REST endpoints for querying results

### Frontend
- Implemented as a **Chrome extension** using **JavaScript**
- Responsibilities:
  - Interacting with the backend API
  - Triggering queries based on user navigation
  - Displaying aggregated air quality information

## Data

The project relies on **publicly available air quality datasets**, focusing on:
- Urban monitoring stations
- Aggregated measurements over time
- City- or district-level indicators

All data used is non-sensitive and aggregated.

## Setup and Execution

This project consists of two main components: a backend API and a browser extension frontend.
The steps below describe how to run the prototype locally.

### Requirements

- Python 3.9+
- Google Chrome
- pip

### Backend Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Navigate to the backend directory:

```bash
cd app
```

Start the FastAPI server:

```bash
uvicorn api:app --reload
```

### Frontend Setup (Chrome Extension)

1. Open the Chrome extensions page:

   ```
   chrome://extensions/
   ```
2. Enable **Developer mode** (toggle in the top-right corner).
3. Click **Load unpacked** and select the `ExtensionFrontend` directory.
4. Ensure the backend server is running.

### Usage

1. Open [idealista](https://www.idealista.com/) in Chrome.
2. Navigate to a **region or municipality-level** page (not a specific address).
3. The extension queries the local API and displays aggregated air quality information.

> ⚠️ Note: The prototype is designed to work at region or municipality level and may not function correctly for more granular locations.

## Limitations and Future Work

* This repository does not yet include the full original source code.
* The prototype is limited to specific locations and data sources.
* Future improvements could include:

  * Completing full code recovery
  * Expanding coverage to additional cities
  * Improving UI/UX and visualizations
  * Adding temporal trend analysis

## Tech Stack

* **Backend:** FastAPI (Python)
* **Frontend:** JavaScript (Chrome Extension)
* **Data processing:** Python
* **APIs:** REST

## Status

This project is presented as an **early-stage prototype and learning experience**.
It documents my first exposure to:

* Full-stack web development
* API-driven design
* Integrating data analysis into interactive applications
