
# E-commerce customer behaviour analysis
## Executive summary

**Business context:** A UK-based wholesale gift retailer seeks to understand
which customer segments drive revenue, where retention breaks down, and which
products are most frequently bought together.

**Dataset:** UCI Online Retail II — 793,309 transactions after cleaning,
5,860 unique customers, 43 countries, Dec 2009 – Dec 2011.
Total revenue: £17,324,932.

---
## Key findings

### Finding 1 — Champions generate disproportionate revenue
Champions represent 25% of customers
but generate 70% of total revenue (£8,262
average CLV vs £430 for Lost customers — a 19x gap).

→ **Action:** Prioritise loyalty programme investment on Champions.
A 5% improvement in Champion retention recovers ~£606,428
in annual revenue.

### Finding 2 — Retention collapses after first purchase
Average Month-1 retention across all cohorts is 20.8% —
meaning 79% of customers never return after their
first order. The strongest cohort was 2009-12 at 35%,
suggesting seasonal or campaign effects worth investigating.

→ **Action:** Implement a first-30-days email sequence targeting
new customers. Moving Month-1 retention from 21% to 30%
would add ~£22,250 in recovered revenue
from the New Customers segment alone.

### Finding 3 — High-lift product pairs signal bundling opportunities
Three product pairs show lift scores above 9.0, meaning customers buy
them together far more than chance predicts:
- SWEETHEART + STRAWBERRY CERAMIC TRINKET BOX (lift: 13.82, confidence: 69%)
- WOODEN FRAME ANTIQUE WHITE + WHITE FINISH (lift: 11.70, confidence: 60%)
- LOVE + HOME BUILDING BLOCK WORD (lift: 9.97, confidence: 53%)

→ **Action:** Bundle these pairs as gift sets for Q4. Test a
'frequently bought together' placement on the top 2 pairs.

---
## Recommended next steps
1. Launch a Champion loyalty tier with early access and volume discounts
2. Design a 3-email onboarding sequence at Day 3, Day 14, and Day 30
3. Create 3 bundled gift SKUs from the top association rule pairs before Q4

---
## Caveats
- December 2011 data is truncated (ends Dec 4) — Month-1 retention for
  the 2011-11 cohort (6.3%) reflects this, not real churn
- CLV is historical and descriptive, not predictive
- Guest transactions (22.6% of raw rows) excluded — behaviour may differ
