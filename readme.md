# ✈️ Airline Revenue Data Pipeline & Analytics Dashboard

## Executive Summary

This project delivers an **end-to-end, production-style data pipeline and analytics dashboard** designed to support **revenue optimisation, capacity planning, and cancellation risk management** for an airline business.

The solution ingests transactional booking data from a PostgreSQL database, processes it through a scalable AWS-based data pipeline, and surfaces **executive-ready insights** via a Tableau dashboard. It demonstrates strong capability across **data engineering, analytics, and business storytelling**.

<img width="1600" height="1000" alt="Dashboard" src="https://github.com/user-attachments/assets/400bc16f-7da0-44f9-9372-b8e8b8790945" />

Key outcomes include:

* **£8.2K confirmed revenue identified** with clear optimisation opportunities
* **26.3% cancellation risk surfaced**, with actionable route-level alerts
* Clear recommendations for **marketing spend reallocation**, **UX optimisation**, and **seasonal capacity planning**
---
## Business Problem

Airline commercial teams need timely, reliable insights to:

* Maximise confirmed revenue
* Reduce cancellations and booking leakage
* Allocate marketing budget effectively across channels
* Anticipate seasonal demand and capacity constraints

Raw booking data alone is insufficient. This project transforms raw operational data into **decision-ready intelligence**.

---

## Solution Overview

The solution consists of two core components:

1. **Cloud Data Pipeline** – Automated ingestion, transformation, and storage of clean analytical data
2. **Tableau Executive Dashboard** – High-impact visual analytics focused on revenue, risk, and growth opportunities

---

## Data Pipeline Architecture


<img width="3825" height="600" alt="Blank diagram" src="https://github.com/user-attachments/assets/f4a8c33f-5c52-4f72-86dc-001822000871" />

* PostgreSQL Database – Source of airline booking transactions

* S3 Raw Bucket – Stores extracted Parquet files for auditability and reprocessing

* Dockerised Transformation Layer – Python pipeline reads raw data with boto3 and cleans it using Pandas

* S3 Processed Bucket – Stores analytics-ready Parquet datasets, optimised for query performance

* AWS Athena – Serverless SQL querying over processed datasets

* Tableau Public – Interactive dashboards for executives

**Why this architecture matters:**

* Scalable and cloud-native
* Clear separation of raw vs processed data
* Reproducible and production-aligned design

---

## Analytics & Dashboard Overview

The Tableau dashboard is designed for **commercial leaders and revenue managers**, not just analysts.

### Headline KPIs

* **Confirmed Revenue:** £8.2K
* **Pending Bookings:** 8
* **Cancellation Rate:** 26.3%
* **VIP Customers Identified:** 3

---

## Key Insights & Recommendations

### 1️⃣ Booking Channel Performance

* **Website generates the highest revenue (£5.8K)** but has the **lowest conversion rate (43.8%)**
* **Mobile and Agency channels convert at ~69%**

📌 *Recommendation:*

* Prioritise **website UX optimisation** to unlock immediate revenue gains
* Shift marketing spend toward higher-converting channels while UX improvements are implemented

---

### 2️⃣ Geographic Revenue Distribution

* **Netherlands (£2.3K)** identified as the top international market

📌 *Recommendation:*

* Expand targeted marketing and route promotions for high-performing international regions

---

### 3️⃣ Cancellation Risk Analysis

* Certain routes show **100% cancellation rates** (e.g. IPA → LON, CDG → AMS)

📌 *Recommendation:*

* Immediate review of pricing, scheduling, or customer experience issues on high-risk routes
* Introduce stricter confirmation or deposit policies where appropriate

---

### 4️⃣ Seasonal Demand & Capacity Planning

* Revenue builds steadily to a **£5.2K peak in July**

📌 *Recommendation:*

* Increase summer seat capacity and staffing ahead of peak demand
* Lock in pricing strategies earlier in the booking curve

---

### 5️⃣ High-Value Customers (VIPs)

* Top 3 VIP customers identified based on total spend

📌 *Recommendation:*

* Introduce loyalty incentives and personalised offers to retain high-value customers

---

### 6️⃣ Top Revenue Routes

* Top-performing routes contribute disproportionately to revenue

📌 *Recommendation:*

* Double down on marketing and route optimisation for these high-return segments

---

## Tools & Technologies

**Data Engineering**

* Python (Pandas)
* Docker
* AWS S3
* AWS Athena
* boto3

**Analytics & Visualisation**

* Tableau Public
* SQL

**Data Formats**

* Parquet (columnar, analytics-optimised)

---

## Why This Project Matters

This project demonstrates:

* **End-to-end ownership** from raw data to executive insight
* Strong **data engineering fundamentals** aligned with real-world architectures
* Ability to translate data into **commercially relevant decisions**
* Executive-level storytelling, not just dashboards

It is intentionally designed to reflect how modern analytics teams operate in production environments.
---
## Future Enhancements

* Automated orchestration (Airflow / AWS Step Functions)
* Incremental loads and CDC
* Predictive cancellation modelling
* Cost and profitability analysis per route
---
