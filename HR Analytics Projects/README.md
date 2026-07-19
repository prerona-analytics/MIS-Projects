# HR Analytics: Workforce Management, Payroll Processing & Headcount Forecasting

## Project Overview

This project demonstrates comprehensive HR analytics capabilities for managing large-scale workforce operations. The analysis covers 5,000+ employees across 50+ facilities, 25+ departments, and 12 months of payroll and HR data. The system tracks headcount deployment, payroll processing, employee productivity, attrition analysis, and workforce forecasting with advanced dashboards and SQL queries.

## Business Context

**Challenge**: HR teams managing payroll for 5,000+ employees, struggling with headcount planning, salary variances, employee attrition, and compliance reporting across multiple facilities.

**Solution**: Integrated HR analytics platform tracking headcount allocation, payroll processing accuracy, employee performance, attrition patterns, and workforce forecasting with real-time dashboards and exception reporting.

## Datasets

### 1. Employee Master (5,000 employees)
- Employee ID, name, department, facility, designation
- Salary grade, cost centre, employment type
- Hire date, status (Active, Inactive, On Leave)
- Manager ID, reporting structure

### 2. Payroll Data (60,000 payroll records)
- Payroll ID, employee ID, month, year
- Basic salary, allowances, deductions, net pay
- Attendance, overtime hours, leave taken
- Tax calculations, compliance status

### 3. Attendance and Leave (150,000 records)
- Attendance ID, employee ID, date
- Present/absent/leave/half-day/WFH
- Leave type (sick, casual, earned, unpaid)
- Approval status

### 4. Performance and Ratings (5,000 ratings)
- Rating ID, employee ID, rating period
- Performance score (1-5), competency ratings
- Review date, reviewer ID
- Promotion eligibility, bonus percentage

### 5. Attrition and Exits (500+ exits)
- Separation ID, employee ID, last working date
- Separation reason, exit interview feedback
- Notice period, final settlement
- Rehire eligibility

### 6. Headcount Deployment (12,000 records)
- Deployment ID, facility ID, department ID
- Budgeted headcount, actual headcount
- Sanctioned positions, filled positions
- Vacancy rate, utilization percentage

## Key Responsibilities Addressed

1. Monitor headcount deployment across Pan India facilities
2. Process and reconcile monthly payroll for 5,000+ employees
3. Ensure payroll accuracy and compliance
4. Track and manage leave balances and attendance
5. Monitor salary variances and overtime costs
6. Analyse employee performance and attrition patterns
7. Forecast headcount requirements quarterly
8. Generate compliance reports for statutory requirements
9. Produce workforce analytics and HR dashboards
10. Track talent pipeline and succession planning
11. Monitor employee engagement and satisfaction scores
12. Report on HR metrics to senior management

## Advanced SQL Queries Included

### 1. Payroll Analysis
```sql
SELECT 
    e.employee_id,
    e.employee_name,
    e.department,
    p.month,
    p.basic_salary,
    p.allowances,
    p.deductions,
    p.net_pay,
    p.tax_amount,
    (p.net_pay - LAG(p.net_pay) OVER (PARTITION BY e.employee_id ORDER BY p.month)) as salary_variance,
    ROUND((p.overtime_hours * 100 / e.billable_hours), 2) as overtime_percentage
FROM employees e
JOIN payroll p ON e.employee_id = p.employee_id
WHERE p.year = 2025
ORDER BY e.department, e.employee_id, p.month;
```

### 2. Headcount vs Sanctioned Analysis
```sql
SELECT 
    f.facility_id,
    f.facility_name,
    d.department_id,
    d.department_name,
    COUNT(DISTINCT CASE WHEN e.status = 'Active' THEN e.employee_id END) as actual_headcount,
    hd.sanctioned_positions,
    (COUNT(DISTINCT CASE WHEN e.status = 'Active' THEN e.employee_id END) - hd.sanctioned_positions) as variance,
    ROUND((COUNT(DISTINCT CASE WHEN e.status = 'Active' THEN e.employee_id END) / hd.sanctioned_positions) * 100, 2) as utilization_pct,
    COUNT(DISTINCT CASE WHEN e.status = 'Active' AND e.hire_date > DATEADD(month, -3, GETDATE()) 
                        THEN e.employee_id END) as new_joiners_3m
FROM facilities f
JOIN departments d ON f.facility_id = d.facility_id
LEFT JOIN employees e ON d.department_id = e.department
LEFT JOIN headcount_deployment hd ON f.facility_id = hd.facility_id AND d.department_id = hd.department_id
GROUP BY f.facility_id, f.facility_name, d.department_id, d.department_name, hd.sanctioned_positions;
```

### 3. Attrition Analysis with Running Total
```sql
SELECT 
    MONTH(ex.last_working_date) as separation_month,
    COUNT(DISTINCT ex.employee_id) as separations,
    COUNT(DISTINCT CASE WHEN ex.separation_reason = 'Voluntary' THEN ex.employee_id END) as voluntary,
    COUNT(DISTINCT CASE WHEN ex.separation_reason = 'Involuntary' THEN ex.employee_id END) as involuntary,
    SUM(COUNT(DISTINCT ex.employee_id)) OVER (ORDER BY MONTH(ex.last_working_date)) as cumulative_attrition,
    ROUND((COUNT(DISTINCT ex.employee_id) / (SELECT COUNT(*) FROM employees WHERE status = 'Active')) * 100, 2) as attrition_rate
FROM exits ex
GROUP BY MONTH(ex.last_working_date)
ORDER BY separation_month;
```

### 4. Department-wise Salary Analysis
```sql
SELECT 
    e.department,
    COUNT(DISTINCT e.employee_id) as headcount,
    ROUND(AVG(p.basic_salary), 2) as avg_salary,
    MIN(p.basic_salary) as min_salary,
    MAX(p.basic_salary) as max_salary,
    ROUND(STDEV(p.basic_salary), 2) as salary_stddev,
    ROUND(SUM(p.basic_salary + p.allowances), 0) as total_payroll_cost,
    ROUND(AVG(p.overtime_hours), 2) as avg_overtime_hours,
    RANK() OVER (ORDER BY AVG(p.basic_salary) DESC) as salary_rank
FROM employees e
JOIN payroll p ON e.employee_id = p.employee_id
GROUP BY e.department
ORDER BY salary_rank;
```

### 5. Employee Productivity and Compliance
```sql
SELECT 
    e.employee_id,
    e.employee_name,
    e.department,
    ROUND((CAST(SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END) as FLOAT) / 
            COUNT(*)) * 100, 2) as attendance_percentage,
    SUM(CASE WHEN a.leave_type IN ('Sick', 'Casual') THEN 1 ELSE 0 END) as total_leave_taken,
    ROUND(AVG(pr.performance_score), 2) as avg_performance_score,
    SUM(p.overtime_hours) as total_overtime_hours,
    CASE WHEN SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END) / CAST(COUNT(*) as FLOAT) < 0.85 
         THEN 'High Absence Risk'
         WHEN ROUND(AVG(pr.performance_score), 2) < 2.5 THEN 'Performance Issue'
         ELSE 'Compliant' END as compliance_status
FROM employees e
LEFT JOIN attendance a ON e.employee_id = a.employee_id AND YEAR(a.date) = 2025
LEFT JOIN payroll p ON e.employee_id = p.employee_id AND YEAR(p.year) = 2025
LEFT JOIN performance pr ON e.employee_id = pr.employee_id AND YEAR(pr.rating_date) = 2025
GROUP BY e.employee_id, e.employee_name, e.department;
```

## Advanced Excel Features

### 1. Payroll Dashboards
- Salary structure analysis by designation
- Overtime cost tracking and trends
- Deduction and allowance breakdown
- Tax compliance reporting

### 2. Headcount Dashboards
- Headcount vs sanctioned positions (facility-wise)
- Department-wise utilization heatmap
- New joiners and exits trend
- Vacancy analysis by skill level

### 3. Compliance Dashboards
- Attendance tracking and exception reporting
- Leave balance and utilization analysis
- Statutory compliance checklist
- Payroll accuracy audit trail

### 4. Performance Dashboards
- Employee rating distribution
- Top performers and low performers
- Department performance comparison
- Promotion pipeline analysis

### 5. Attrition Dashboards
- Monthly attrition rate trend
- Attrition by department and designation
- Exit reason analysis
- Retention strategy effectiveness

## Excel Features

### Pivot Tables with Slicers
- Facility filter across all sheets
- Department and designation slicers
- Month/Year date range selector
- Employee status filter (Active/Inactive)

### Conditional Formatting
- Red/yellow/green coding for compliance status
- Heat maps for utilization rates
- Icon sets for performance ratings
- Data bars for salary comparisons

### Complex Formulas
- SUMIFS for conditional payroll aggregation
- INDEX/MATCH for employee lookups
- Array formulas for complex HR metrics
- Nested IFs for compliance status calculation

## Key Metrics Tracked

### Payroll Metrics
- Monthly payroll processing accuracy: >99%
- Salary variance analysis: month-on-month
- Overtime cost as % of payroll: <5%
- Tax compliance rate: 100%
- Days sales outstanding on employee reimbursements

### Headcount Metrics
- Headcount utilization: 90%+
- Vacancy rate by department: <5%
- New joiners per month: tracked
- Attrition rate: <12% annually
- Department utilization variance: <5%

### Compliance Metrics
- Attendance percentage: >85%
- Leave taken vs balance: tracked
- Payroll accuracy: >99%
- Compliance issues flagged: zero tolerance
- Statutory deadline compliance: 100%

### Performance Metrics
- Average performance score: tracked
- High performers: top 20%
- Performance outliers: flagged
- Promotion eligibility: tracked
- Succession pipeline: maintained

## Project Structure

```
hr_analytics_project/
|-- README.md (this file)
|-- GITHUB_UPLOAD_GUIDE.md
|-- LICENSE
|-- requirements.txt
|-- .gitignore
|
|-- Data/
|   |-- employees.csv (5,000 records)
|   |-- payroll.csv (60,000 payroll entries)
|   |-- attendance.csv (150,000 records)
|   |-- performance.csv (5,000 ratings)
|   |-- exits.csv (500+ exit records)
|   |-- headcount_deployment.csv (12,000 records)
|
|-- SQL/
|   |-- hr_analytics_queries.sql (10+ complex queries)
|
|-- Excel/
|   |-- hr_analytics_dashboard.xlsx
|   |-- payroll_dashboard.xlsx
|   |-- headcount_dashboard.xlsx
|   |-- compliance_dashboard.xlsx
|
|-- Python/
|   |-- generate_hr_data.py
|   |-- hr_analytics.py
|   |-- dashboard_generator.py
|
|-- Dashboards/
|   |-- payroll_analytics.html
|   |-- headcount_analytics.html
|   |-- attrition_analytics.html
|   |-- compliance_report.html
|   |-- executive_summary.html
```

## Installation and Setup

### Requirements

```bash
pip install pandas numpy scipy matplotlib seaborn openpyxl xlsxwriter
```

### How to Run

#### Step 1: Generate HR Data
```bash
python generate_hr_data.py
```

#### Step 2: Load to SQL
```bash
# Import CSVs to your SQL database
# Run hr_analytics_queries.sql
```

#### Step 3: Open Excel Dashboards
```bash
# Open hr_analytics_dashboard.xlsx
# Refresh data and interact with slicers
```

#### Step 4: View HTML Dashboards
```bash
# Open dashboards in browser for interactive visualizations
```

## Key Findings (Example Output)

### Payroll Insights
- Total annual payroll cost: INR 5+ crores
- Average salary: INR 8-12 lakhs per annum
- Overtime cost trend: Increasing 2% month-on-month
- Tax compliance: 100% adherence to regulations

### Headcount Insights
- Current headcount: 4,950 active employees
- Facility utilization: 92-95% across all sites
- Vacancy rate: 3.5% (mostly entry-level positions)
- New joiners: 150-200 per month
- Attrition rate: 10.2% annualized

### Compliance Insights
- Attendance percentage: 87.3%
- Leave balance utilization: 78% of annual entitlement
- Payroll accuracy: 99.8% (2 errors out of 1,000 entries)
- Compliance issues: 0 critical, 3 minor (addressed)

### Performance Insights
- Average performance rating: 3.2/5
- High performers (4-5 rating): 25%
- Performance outliers: 12 employees below 2.0
- Promotion pipeline: 150 eligible for next level

## Recommendations

1. **Optimize Payroll Processing**: Implement batch processing for salary calculations; reduce manual intervention
2. **Headcount Planning**: Use forecasting model to predict quarterly requirements; maintain 95% utilization
3. **Reduce Attrition**: Focus on entry-level retention; implement mentorship program
4. **Improve Attendance**: Set facility-wise targets; zero tolerance for compliance violations
5. **Performance Management**: Quarterly reviews instead of annual; continuous feedback loop
6. **Succession Planning**: Identify high performers for senior roles; build bench strength

## Skills Demonstrated

✓ **5,000+ employee records** managed across Pan India network
✓ **60,000+ payroll entries** processed and reconciled
✓ **150,000+ attendance records** tracked and analyzed
✓ **Complex SQL queries** with window functions, CTEs, joins
✓ **Advanced Excel models** with pivot tables, slicers, formulas
✓ **Interactive dashboards** with HTML/Plotly
✓ **Payroll accuracy** and compliance tracking
✓ **Headcount forecasting** and resource planning
✓ **Attrition analysis** and workforce retention
✓ **End-to-end HR analytics** from data to insights

## Contact

For questions about this HR analytics portfolio project, please reach out.

## License

MIT License - Portfolio demonstration project.

---

**Portfolio Note:** This analysis demonstrates comprehensive HR operations and analytics capabilities matching MIS Executive responsibilities for workforce management, payroll processing, headcount deployment, and compliance reporting across large-scale organizations. All data is synthetically generated for portfolio purposes.
