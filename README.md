# 🎮 Game Economy & Logistics Operations - Data Pipeline

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![DuckDB](https://img.shields.io/badge/DuckDB-Latest-yellow.svg)
![dbt](https://img.shields.io/badge/dbt-Data_Build_Tool-FF694B.svg)
![Looker Studio](https://img.shields.io/badge/BI-Looker_Studio-4285F4.svg)

## 📌 Project Overview
This project is an end-to-end **Modern Data Stack (MDS)** implementation designed to simulate, process, and analyze the virtual economy and logistics operations of a mobile simulation game. 

It demonstrates the complete lifecycle of a data engineering project: from generating raw telemetry data to building a dimensional data warehouse, and finally delivering actionable business intelligence (BI) to stakeholders.

## 🏗️ Architecture & Tech Stack
The pipeline follows a robust **ELT (Extract, Load, Transform)** architecture:

1. **Data Generation (Python):** Simulates 5,000+ daily transaction logs, including character dispatches, route selections, and probabilistic success rates.
2. **Data Warehouse (DuckDB):** Serves as the lightweight, high-performance analytical database engine.
3. **Data Transformation (dbt):** - Implements a Star Schema architecture.
   - Cleanses raw CSVs in the **Staging Layer**.
   - Joins dimensions and calculates complex business logic (e.g., Net Profit, Hourly Wage, ROI) in the **Marts Layer**.
4. **Business Intelligence (Looker Studio):** An interactive, dark-themed executive dashboard visualizing core KPIs.

## 📊 Key Business Metrics Analyzed
- **Top-Tier Rarity ROI:** Analyzing the overwhelming revenue generation of "Red Card" characters (e.g., Aria) compared to standard units.
- **Logistics Efficiency (Profit/Hour):** Calculating the true time-value of different trade routes (e.g., Capital -> Black Market).
- **Macro Economy Health:** Monitoring daily server-wide net profit trends and VIP player contribution ratios.

## 📂 Repository Structure
```text
looker_game_project/
│
├── data/                           # Raw and processed CSV data files
├── game_economy_dbt/               # dbt project directory
│   ├── models/
│   │   ├── staging/                # Staging models (stg_users, stg_routes, etc.)
│   │   └── marts/                  # Core business models (fct_logistics_performance)
│   ├── dbt_project.yml             # dbt configuration
│   └── profiles.yml                # DuckDB connection profile
│
├── generate_mock_data.py           # Python script to simulate game logs
├── export_for_looker.py            # Python script to extract final wide-table for BI
├── dashboard_preview.png           # Screenshot of the Looker Studio Dashboard
└── README.md
