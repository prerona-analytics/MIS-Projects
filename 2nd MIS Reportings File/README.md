# Facilities Management MIS: Invoice Processing, Budget Tracking & Vendor Management

## Project Overview

This project demonstrates comprehensive Facilities Management Information System (MIS) capabilities for managing multi-site facility operations. The analysis covers invoice processing workflows, budget monitoring, vendor management, and compliance reporting for a Pan India facilities network.

The system tracks 50,000+ vendor invoices across multiple facilities, monitors facility-wise budgets, manages headcount deployments across sub-contractors, and ensures timely SLA compliance for payment and reporting cycles.

## Business Context

**Challenge**: Facilities Management teams spending 30-40% of time on manual invoice processing, budget reconciliation, and vendor tracking across multiple facilities and cost centres.

**Solution**: Integrated MIS system automating invoice workflows, budget monitoring, vendor management, and compliance reporting with real-time dashboards and exception alerts.

## Key Responsibilities Addressed

1. Monitor and ensure all vendor invoices processed per SLA timelines
2. Track facility-wise budgets and communicate variations to facility leads
3. Ensure monthly bills submitted and reimbursed to sub-contractors within agreed timelines
4. Manage consolidated Blanket Purchase Orders quarterly with required approvals
5. Monitor purchases against BPO and ensure all purchases covered under PO
6. Track Capex requests facility-wise with detailed business cases
7. Provide timely location-wise management reports to Hub Lead
8. Deliver monthly FM meeting reports with analysis to JLLM meeting
9. Ensure legal and statutory compliance across all facilities
10. Track vendor contracts and renewals
11. Quarterly and yearly budget forecasting with client finance team
12. Monitor headcount deployment across Pan India sub-contractor facilities
13. Coordinate with Facility Managers to meet client objectives
14. Manage billing and cost centre recovery

## Dataset Overview

The analysis uses 5 interconnected datasets representing 6 months of facility operations:

### 1. Facilities Master Data (50 facilities)
- Facility ID, facility name, location, state
- Facility manager, contact details
- Monthly budget allocation
- Headcount approval limit
- Facility tier (Tier-1, Tier-2, Tier-3)

### 2. Invoice Data (50,000 records)
- Invoice ID, facility ID, vendor ID
- Invoice date, invoice amount, GST
- Invoice type (monthly bill, Capex, one-time service)
- Processing date, approval date, payment date
- SLA status (on-time, delayed)
- Cost centre

### 3. Budget and Actual Spend (500 facility-month records)
- Facility ID, month, budgeted amount
- Actual spend (facility charges, vendor bills, Capex)
- Variance amount and percentage
- Budget status (on-track, overspend, underspend)

### 4. Vendor Management (100 vendors)
- Vendor ID, vendor name, vendor category
- Contract start date, contract end date, renewal date
- Contract amount, payment terms
- Performance rating, on-time delivery percentage

### 5. Headcount and Deployments (250 records)
- Facility ID, sub-contractor ID, deployment date
- Headcount deployed, approved headcount
- Utilization rate, overdeployment flag

### 6. Purchase Orders and Contracts (75 records)
- PO ID, facility ID, vendor ID
- PO amount, PO validity period
- Coverage percentage (amount ordered vs PO)
- Outstanding PO balance

**Note:** All data is synthetically generated to reflect realistic facilities management patterns. No real facility or vendor data is included.

## Methodology

### 1. Data Integration
- Merged 5 datasets on facility ID and vendor ID
- Created fact tables for invoices, budgets, and deployments
- Aggregated data at facility, vendor, and facility-manager levels

### 2. Invoice Processing Analysis
- Tracked invoice volume and value by facility and vendor
- Calculated SLA compliance (on-time vs delayed payments)
- Identified bottlenecks in approval and payment workflows
- Measured average processing time by invoice type

### 3. Budget Monitoring
- Calculated variance between budgeted and actual spend
- Identified overspending facilities and cost centres
- Tracked budget utilization trends month-over-month
- Forecasted remaining budget for year-end

### 4. Vendor Performance
- Calculated on-time payment rate by vendor
- Tracked vendor contract renewal dates
- Measured invoice accuracy (no rework required)
- Identified high-risk vendors

### 5. Compliance and Controls
- Tracked PO coverage (% of invoices covered by existing POs)
- Monitored headcount deployment vs approved limits
- Identified statutory compliance issues
- Flagged duplicate invoices or duplicate payments

### 6. Reporting and Dashboards
- Built facility-wise dashboard with budget and actual
- Created vendor performance scorecard
- Developed invoice processing funnel
- Built headcount and deployment tracker

## Key Performance Measures

- **Invoice Processing**: 100% SLA compliance, zero payment delays
- **Budget Compliance**: Monthly variance tracking, quarterly forecasting
- **Vendor Performance**: On-time payment rate, invoice accuracy
- **Compliance**: Zero duplicate invoices, 100% PO coverage
- **Accruals**: Monthly accrual compilation on Pan India basis
- **Reporting**: Timely delivery of all monthly and quarterly reports

## Tools and Technologies

- **Data Processing**: Python (Pandas, NumPy)
- **Analytics**: SQL, Excel (Pivot Tables, VLOOKUP)
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Dashboard Tools**: Power BI, Excel, Google Sheets (export-ready data)
- **Reporting**: Automated Excel reports, HTML dashboards

## Key Files

### Data and Code
- `generate_mis_data.py`: Generates all 5 datasets (50K+ records)
- `data_preparation.py`: ETL, feature engineering, data cleaning
- `mis_analysis.py`: Invoice, budget, vendor, and compliance analysis
- `reporting_dashboard.py`: Dashboard and report generation

### Data Files (Generated)
- `facilities.csv`: 50 facility records
- `invoices.csv`: 50,000 invoice records
- `budget_actual.csv`: 500 facility-month budget records
- `vendors.csv`: 100 vendor records
- `headcount_deployments.csv`: 250 deployment records
- `purchase_orders.csv`: 75 PO records
- `processed_mis_data.csv`: Aggregated facility-wise MIS data

### Outputs
- `invoice_processing_dashboard.html`: Invoice workflow analysis
- `budget_monitoring_dashboard.html`: Facility-wise budget tracking
- `vendor_performance_dashboard.html`: Vendor scorecard
- `compliance_report.html`: Compliance and control monitoring
- `monthly_mis_report.xlsx`: Automated monthly report
- `mis_summary_report.txt`: Executive summary

### Documentation
- `README.md`: This file
- `MIS_DATA_DICTIONARY.md`: Complete data schema
- `GITHUB_UPLOAD_GUIDE.md`: How to upload to GitHub

## Installation and Setup

### Requirements

```bash
pip install pandas numpy scipy matplotlib seaborn openpyxl xlsxwriter
pip install jupyter notebook
```

### Python Version

Python 3.8 or higher

## How to Run (End to End)

### Step 1: Generate MIS Data

```bash
python generate_mis_data.py
```

Outputs all 6 CSV files with realistic FM data.
**Time:** 2-3 minutes

### Step 2: Data Preparation and ETL

```bash
python data_preparation.py
```

Cleans data, creates derived metrics, flags issues.
**Time:** 2-3 minutes

### Step 3: MIS Analysis

```bash
python mis_analysis.py
```

Runs all analyses: invoice processing, budget variance, vendor performance, compliance.
**Time:** 3-5 minutes

### Step 4: Generate Dashboards and Reports

```bash
python reporting_dashboard.py
```

Creates interactive dashboards and automated monthly report.
**Time:** 2-3 minutes

**Total execution time:** 10-15 minutes for complete analysis

## Advanced Visualizations Included

### 1. Invoice Processing Dashboard
- Invoice volume trend by facility (line chart)
- SLA compliance rate by facility (bar chart with pass/fail color coding)
- Average processing time by invoice type (column chart)
- Invoice approval funnel (waterfall chart)
- Delayed invoices by facility and reason (heatmap)

### 2. Budget Monitoring Dashboard
- Facility-wise budget vs actual comparison (grouped bar chart)
- Budget variance trend over time (area chart)
- Facilities with variance alerts (highlighted table)
- Budget utilization by cost centre (pie chart)
- Year-to-date budget forecast (line chart with confidence interval)

### 3. Vendor Performance Dashboard
- Vendor on-time payment rate (horizontal bar chart)
- Invoice volume by vendor (bubble chart sized by value)
- Contract renewal timeline (Gantt chart)
- Vendor performance scorecard (table with colour coding)
- High-risk vendor alerts (exception report)

### 4. Compliance and Controls
- PO coverage percentage by facility (gauge chart)
- Headcount deployment vs approved limit (bar chart)
- Invoice exception report (duplicate, unmatched, unapproved)
- Statutory compliance checklist (status matrix)
- Outstanding PO and Capex tracking (aging analysis)

## Key Findings (Example Output)

### Invoice Processing
- Average processing time: 4.2 days (target: 5 days)
- SLA compliance rate: 94% (target: 100%)
- Top 3 delayed facilities: Facility-10, Facility-25, Facility-35
- Most common delay reason: Missing approvals (35%)

### Budget Management
- Total monthly budget: INR 2.5 crore
- Actual spend: INR 2.3 crore (92% utilization)
- Overspending facilities: 5 (need attention)
- YTD variance: +2% (within tolerance)

### Vendor Management
- Total vendors: 100
- Active vendors (processed >5 invoices): 75
- Average on-time payment rate: 89%
- Contracts up for renewal in Q1: 12

### Compliance
- PO coverage: 96% (4% invoices without PO)
- Duplicate invoice flags: 3 (0.01% of total)
- Headcount overdeployment: 2 facilities
- Compliance issues: 0 critical, 2 minor

## Recommendations

1. **Improve Invoice Processing**: Implement pre-approval workflow for common invoice types to reduce processing time
2. **Monitor Overspending**: Weekly alerts for facilities trending toward overspend
3. **Vendor Consolidation**: Reduce vendor count from 100 to 70 to simplify management
4. **Contract Management**: Automate renewal reminders 60 days before expiry
5. **Headcount Controls**: Implement automated approval gates for headcount changes
6. **PO Coverage**: Ensure 100% of invoices matched to POs before payment
7. **Accrual Process**: Automate monthly accrual compilation to reduce manual effort

## Data Quality and Validation

- Data completeness: 99.8% (minimal missing values)
- Invoice-to-PO matching: 96%
- Budget reconciliation: 100%
- Duplicate detection: 0 duplicate invoices
- Outlier handling: Flagged 15 invoices >INR 25 lakh for review

## Reproducibility

To regenerate with new synthetic data:

```bash
python generate_mis_data.py
python data_preparation.py
python mis_analysis.py
python reporting_dashboard.py
```

All results are fully reproducible; random seeds can be changed for different data distributions.

## Project Structure

```
mis_executive_analytics_project/
|
|-- README.md (this file)
|-- MIS_DATA_DICTIONARY.md (data schema)
|-- GITHUB_UPLOAD_GUIDE.md (upload instructions)
|
|-- Code/
|   |-- generate_mis_data.py
|   |-- data_preparation.py
|   |-- mis_analysis.py
|   |-- reporting_dashboard.py
|
|-- Data/
|   |-- facilities.csv
|   |-- invoices.csv
|   |-- budget_actual.csv
|   |-- vendors.csv
|   |-- headcount_deployments.csv
|   |-- purchase_orders.csv
|   |-- processed_mis_data.csv
|
|-- Outputs/
|   |-- invoice_processing_dashboard.html
|   |-- budget_monitoring_dashboard.html
|   |-- vendor_performance_dashboard.html
|   |-- compliance_report.html
|   |-- monthly_mis_report.xlsx
|
|-- requirements.txt
|-- .gitignore
|-- LICENSE
```

## Skills and Competencies Demonstrated

✓ **End-to-End MIS Design**: Data generation → ETL → Analysis → Reporting
✓ **Invoice Processing**: Workflow automation, SLA tracking, payment cycle management
✓ **Budget Management**: Variance analysis, forecasting, budget allocation
✓ **Vendor Management**: Performance tracking, contract management, risk assessment
✓ **Compliance**: Control mechanisms, statutory requirements, audit trails
✓ **Reporting**: Automated reports, interactive dashboards, executive summaries
✓ **Data Governance**: Data quality, reconciliation, audit controls
✓ **Production Code**: 800+ lines of clean, documented Python
✓ **Professional Documentation**: Comprehensive methodology and findings

## Contact and Support

For questions about this MIS portfolio project, please reach out.

## License

MIT License - This project is provided as a portfolio demonstration.

---

**Portfolio Note:** This analysis demonstrates end-to-end MIS and facilities management capabilities including system design, data management, process automation, and reporting. All data is synthetically generated for portfolio purposes. This project aligns with MIS Executive responsibilities in facilities management, invoice processing, budget control, and vendor management.
