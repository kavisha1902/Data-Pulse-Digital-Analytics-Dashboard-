# 📊 Digital Analytics Dashboard

A full end-to-end analytics pipeline built on real-world eCommerce clickstream data — from raw CSV ingestion to a Power BI dashboard with automated email reporting via n8n.

---

## 🗂️ Project Structure

```
digital-analytics-dashboard/
├── data/
│   ├── funnel.csv
│   ├── brand_performance.csv
│   ├── hourly_traffic.csv
│   └── category_performance.csv
├── notebooks/
│   └── eda.ipynb
├── scripts/
│   ├── clean_data.py
│   └── auto_report.py
├── screenshots/
│   ├── powerBI dashboard.png
│   ├── gmail received.png
│   ├── n8n workflow.png
│   └── eda output.png
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Data Analysis | Python, pandas, numpy |
| Database | SQLite, SQLAlchemy |
| Visualization | Power BI Desktop |
| Automation | n8n (self-hosted) |
| Email Delivery | SMTP (Gmail) |
| Notebook | Jupyter Lab |

---

## 📁 Dataset

**eCommerce Behavior Data from Multi-Category Store — November 2019**  
Source: [Kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)

| Detail | Info |
|---|---|
| Rows loaded | 500,000 |
| Columns | 9 |
| Time Period | November 2019 |
| Key columns | event_type, brand, category_code, price, user_id, user_session |

> Note: Raw CSV not included in repo due to file size (~1.1GB). Download from Kaggle link above.

---

## 🔍 Key Insights

| Metric | Value |
|---|---|
| Total Views | 482,642 |
| Total Cart Additions | 7,763 |
| Total Purchases | 9,595 |
| Conversion Rate | 1.99% |
| Top Brand (by views) | Samsung (57,015 views) |
| Top Category | Electronics (175,560 views) |

---

## 📊 Dashboard

Built in Power BI with 4 visuals and 3 KPI cards:

- **Conversion Funnel** — View → Cart → Purchase drop-off
- **Top Brands Performance** — Bar chart by brand and event type
- **Hourly Traffic Trend** — Line chart showing peak traffic hours
- **Category Breakdown** — Stacked bar across product categories

![Power BI Dashboard](screenshots/powerBI%20dashboard.png)

---

## ⚙️ Pipeline Overview

```
Raw CSV (Nov 2019)
      ↓
Python Cleaning (pandas)
      ↓
SQLite Database (SQLAlchemy)
      ↓
SQL Aggregation Queries
      ↓
Power BI Dashboard
      ↓
Automated Email Report (n8n + SMTP)
```

---

## 🤖 n8n Automation Workflow

Self-hosted n8n workflow with 3 nodes:

1. **Manual Trigger** — initiates the workflow on demand
2. **Code Node** — generates the analytics summary
3. **Send Email (SMTP)** — delivers the report to inbox via Gmail SMTP

![n8n Workflow](screenshots/n8n%20workflow.png)

### Email Report Received

![Gmail Report](screenshots/gmail%20received.png)

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install pandas numpy sqlalchemy matplotlib seaborn jupyter
```

### 2. Run EDA notebook
```bash
jupyter notebook notebooks/eda.ipynb
```

### 3. Generate and send summary report
```bash
python scripts/auto_report.py
```

### 4. Start n8n
```bash
n8n start
# Open http://localhost:5678
```

---

## 📌 Notes

- In production, this pipeline would be triggered on arrival of new monthly data files
- n8n workflow is designed to be extended with a Schedule Trigger for fully automated periodic reporting
- Power BI dashboard connects directly to the exported CSV files from the SQL query layer

---

## 👩‍💻 Author

**Kavisha Sharma**  
B.E. Computer Science (AI/ML) — Chandigarh University  
UID: 23BAI70487
