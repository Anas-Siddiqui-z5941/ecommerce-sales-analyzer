# 🛍️ E-Commerce Sales Analyzer

A Python data analysis tool that processes e-commerce sales data to extract key business insights — top products, revenue metrics, category performance, and more. Results are exported to a structured text report.

---

## ✨ Features

- **Revenue metrics** — calculates total revenue and average order value
- **Top selling product** — identifies the product with highest quantity sold
- **Highest revenue category** — finds the category generating the most revenue
- **Most sold category** — finds the category with the highest units sold
- **Auto-generated report** — exports all insights to `report.txt`
- **Modular design** — analysis logic, utilities, and entry point are cleanly separated

---

## 📊 Sample Insights Generated

```
========================================
       E-COMMERCE SALES REPORT
========================================
Total Revenue        : ₹125,430.00
Average Order Value  : ₹2,508.60
Top Selling Product  : Wireless Headphones
Highest Revenue Category : Electronics
Most Sold Category   : Clothing
========================================
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pandas library

```bash
pip install pandas
```

### Run the analyzer

```bash
git clone https://github.com/Anas-Siddiqui-z5941/ecommerce-sales-analyzer.git
cd ecommerce-sales-analyzer
python main.py
```

The report will be saved to `report.txt` in the project folder.

---

## 📁 Project Structure

```
ecommerce-sales-analyzer/
│
├── main.py          # Entry point — loads data, runs analysis, saves report
├── analysis.py      # Core analysis functions — revenue, top products, categories
├── utils.py         # Utility functions — data loading and report generation
├── report.txt       # Auto-generated output report
├── data/            # Contains the sales dataset (CSV)
└── README.md
```

---

## ⚙️ Analysis Functions

| Function | Description |
|---|---|
| `calculate_metrics()` | Computes total revenue and average order value |
| `top_selling_product()` | Returns product with highest quantity sold |
| `highest_revenue_category()` | Returns category with highest total revenue |
| `most_sold_category()` | Returns category with highest units sold |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)

---

## 👤 Author

**Anas Mohiuddin Siddiqui**  
B.Tech CSE @ Integral University | Aspiring ML Engineer  
[LinkedIn](https://www.linkedin.com/in/anas-siddiqui-z5941) • [GitHub](https://github.com/Anas-Siddiqui-z5941)
