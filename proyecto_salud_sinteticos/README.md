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

.
├── 📁 config/             # Configuration files (e.g., 🔑 database credentials )

│   └── 📄 db_config_example.json

├── 📁 data/               # All data files for the project

│   ├── 📁 raw/            # Original, immutable input datasets (e.g., CSVs, JSONs)

│   ├── 📁 processed/      # Cleaned, transformed, and preprocessed data

│   └── 📁 synthetic/      # Generated synthetic datasets

├── 📁 notebooks/          # 📓 Jupyter notebooks for experimentation and analysis

│   ├── 📄 01_data_ingestion_and_preparation.ipynb

│   └── ...                # (Other notebooks for EDA, modeling, evaluation)

├── 📁 src/                # 🐍 Source code for utility functions and reusable scripts

│   ├── 📄 data_loader.py  # Scripts for data ingestion/loading tasks

│   └── 📄 utils.py        # Helper functions used across the project

├── 📄 .gitignore          # Specifies intentionally untracked files for Git to ignore

├── 📄 LICENSE             # 📜 Project's software license (e.g., MIT) - (I need one!)

├── 📄 README.md           # ℹ️ This file: project overview, setup, and usage instructions

└── 📄 requirements.txt    # 📋 List of Python dependencies for the project


