# Ecommerce Customer Analytics

## Overview
Analyzed 793K+ e-commerce transactions from a UK-based wholesale gift retailer 
to segment customers by behavior, measure retention across cohorts, and uncover 
high-lift product associations driving bundling opportunities.

## Dataset
- Source: UCI Online Retail II
- Size: 793,309 rows × 8 columns (after cleaning)
- Period: Dec 2009 – Dec 2011
- Scope: 5,860 unique customers · 43 countries · £17.3M total revenue

## Key questions answered
1. Which customer segments drive the most revenue?
2. Where does retention break down in the customer lifecycle?
3. Which products are most frequently bought together?

## Methods & tools
| Step | Tool/Method |
|------|-------------|
| Data cleaning | Pandas |
| SQL queries | DuckDB |
| RFM Segmentation | Pandas, custom scoring |
| Cohort retention | Pandas pivot tables |
| Market basket analysis | mlxtend (association rules) |
| Visualization | Seaborn, Matplotlib, Power BI |

## Key findings
- Champions are 25% of customers but generate 70% of revenue 
  (avg CLV £8,262 vs £430 for Lost customers — a 19x gap)
- 79% of customers never return after their first order; 
  Month-1 retention averages just 20.8% across all cohorts
- Three product pairs show lift scores above 9.0 — top pair 
  (SWEETHEART + STRAWBERRY CERAMIC TRINKET BOX) has 69% confidence

## How to run
git clone https://github.com/rudraparmar442/Ecommerce-Customer-Analytics
pip install pandas matplotlib seaborn mlxtend duckdb
jupyter notebook
