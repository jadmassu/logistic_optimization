# Logistic optimization: Delivery drivers location optimization with Causal Inference

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)

## Project Overview

The project focuses on analyzing delivery data to identify the reasons behind unfulfilled delivery requests and developing solutions to optimize the placement of motorbike drivers. By examining patterns in delivery demand and pilot availability, the aim is to recommend strategic locations for drivers that will increase the completion rate of delivery orders, enhance customer satisfaction, and drive business growth.

## Tech Stack

- **Programming Languages:** Python
- **Render large data:** Datashader

## Setup Instructions

### Prerequisites

- Python 3.x

### Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/jadmassu/logistic_optimization.git

   ```

2. **Set Up Virtual Environment**
   ```sh
   conda activate base   # replace base with your environment name
   anaconda-navigator
   ```
3. **Install Requirements**

   ```sh
   pip install -r requirements.txt

   ```

4. **Set Up Virtual Environment**
   ```sh
   Create a .env file and add the following variables
   ```

## Code Structure

    ├── data
    │   ├── raw              # Original data files
    │   ├── processed        # Cleaned and prepped data
    │   └── ...
    ├── notebook
    │   ├── exploratory      # Initial data exploration
    │   ├── analysis         # In-depth data analysis
    │   ├── modeling         # Model development
    │   └── ...
    ├── results
    │   ├── figures          # Visualizations
    │   ├── models           # Trained models
    │   └── ...
    ├── scripts
    │   ├── data_processing  # Data cleaning and transformation
    │   └── ...
    ├── service              # Services for communicating with external API
    ├── utils                # Utility scripts
    ├── requirements.txt     # Python dependencies
    ├── README.md            # Project documentation
    └── ...

### License

This project is licensed under the MIT License. See the LICENSE file for details.
