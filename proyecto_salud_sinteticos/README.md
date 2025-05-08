# Synthetic Health Data Generation Project

A project focused on developing a pipeline for generating synthetic health data, aiming to support research, development, and testing while preserving patient privacy.

## Overview

This project explores various techniques for synthetic data generation within the healthcare domain. The primary goal is to produce datasets that are statistically similar to real-world patient data but do not contain any real patient information. This allows for wider data sharing and use in scenarios where access to sensitive data is restricted.

## Table of Contents 

## 🎯 Project Goals

* To implement and evaluate different synthetic data generation models (e.g., GANs, VAEs, statistical methods).
* To establish a robust pipeline for data ingestion from various sources, preprocessing, synthetic data generation, and rigorous evaluation.
* To ensure the generated synthetic data maintains high utility (e.g., for machine learning tasks) and fidelity (statistical similarity) compared to original data.
* To develop and manage data loading processes to a PostgreSQL database and a designated cloud storage bucket.


## 🛠️ Technology Stack

* **Programming Language:** Python 3.x
* **Core Libraries:**

    * Pandas & NumPy (Data manipulation and numerical operations)
    * Scikit-learn (Preprocessing, machine learning models, and evaluation metrics)
    * JupyterLab (Interactive development environment)
    * Psycopg2-binary (PostgreSQL database adapter)
    * SQLAlchemy (SQL toolkit and Object Relational Mapper - useful with Pandas and databases)
    * SDV (Synthetic Data Vault) (Framework for synthetic data generation)
    * CTGAN (GAN-based model for tabular synthetic data generation)
    * Matplotlib & Seaborn (Data visualization)
   
    
* **Database:** PostgreSQL

* **Storage:** (Specify bucket type/??, e.g., AWS S3, Google Cloud Storage, when known)

* **Version Control:** Git & GitHub

## 📂 Project Structure

Here's an overview of how the project is organized:


proyecto_salud_sinteticos/ 

├── config/                     # Configuration files (e.g., database.ini, api_keys_example.json)

│   └── db_config_example.json  # Example, actual config should be gitignored

├── data/                       # All project data
│   ├── 01_raw/                 # Immutable original datasets
│   ├── 02_processed/           # Cleaned, transformed, intermediate data
│   ├── 03_validation/          # Datasets for validation purposes (e.g., hold-out sets)
│   ├── 04_synthetic/           # Generated synthetic datasets
│   └── caches/                 # Temporary cached data (gitignored)

├── docs/                       # Project documentation (reports, environment.yml, diagrams)
│   └── environment.yml         # Example: Conda environment definition

├── models/                     # Saved/trained machine learning models (e.g., .pkl, .h5)

├── notebooks/                  # Jupyter notebooks for exploration, analysis, and experimentation
│   ├── 01_setup_and_config/
│   ├── 02_data_ingestion/
│   ├── 03_data_quality_assessment/
│   ├── 04_exploratory_data_analysis_eda/
│   ├── 05_data_preprocessing/
│   ├── 06_modeling/
│   ├── 07_evaluation/
│   └── archive/                # Older or less relevant notebooks

├── reports/                    # Generated reports, figures, and final outputs/visualizations
│   └── figures/                # For plots and images saved from notebooks/scripts

├── src/                        # Source code (Python modules and scripts)
│   ├── init.py                 # Makes src a Python package
│   ├── data_processing/        # Modules for data loading, cleaning, transformation
│   │   ├── init.py
│   │   └── cleaners.py         # Example cleaner module
│   ├── database_utils.py       # Utility functions for database interactions
│   ├── modeling/               # Modules related to model definitions, training, evaluation
│   │   ├── init.py
│   │   └── sdv_models.py       # Example modeling module
│   └── utils.py                # General helper functions (e.g., config loading)

├── .gitignore                  # Specifies intentionally untracked files
├── LICENSE                     # Project's software license (e.g., MIT)
├── README.md                   # This file: main project documentation
└── requirements.txt            # Python dependencies for pip