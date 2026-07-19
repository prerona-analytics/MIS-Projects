"""
Generate synthetic HR Analytics data
"""
import pandas as pd
import numpy as np

np.random.seed(42)

# Employees
employees = pd.DataFrame({
    'employee_id': range(1, 5001),
    'employee_name': [f'Employee-{i}' for i in range(1, 5001)],
    'department': np.random.choice(['IT', 'HR', 'Finance', 'Operations', 'Sales', 'Support'], 5000),
    'facility_id': np.random.choice(range(1, 51), 5000),
    'designation': np.random.choice(['L1', 'L2', 'L3', 'L4', 'Manager', 'Senior Manager'], 5000),
    'status': np.random.choice(['Active', 'Inactive'], 5000, p=[0.95, 0.05])
})
employees.to_csv('employees.csv', index=False)

# Payroll
payroll = pd.DataFrame({
    'payroll_id': range(1, 60001),
    'employee_id': np.random.choice(employees['employee_id'], 60000),
    'month': np.random.randint(1, 13, 60000),
    'basic_salary': np.random.uniform(50000, 200000, 60000),
    'allowances': np.random.uniform(10000, 50000, 60000),
    'deductions': np.random.uniform(5000, 25000, 60000),
    'overtime_hours': np.random.randint(0, 50, 60000)
})
payroll['net_pay'] = payroll['basic_salary'] + payroll['allowances'] - payroll['deductions']
payroll.to_csv('payroll.csv', index=False)

# Attendance
attendance = pd.DataFrame({
    'attendance_id': range(1, 150001),
    'employee_id': np.random.choice(employees['employee_id'], 150000),
    'status': np.random.choice(['Present', 'Absent', 'Leave', 'WFH'], 150000, p=[0.75, 0.05, 0.15, 0.05]),
    'leave_type': np.random.choice(['Sick', 'Casual', 'Earned', 'Unpaid', 'None'], 150000)
})
attendance.to_csv('attendance.csv', index=False)

# Performance
performance = pd.DataFrame({
    'rating_id': range(1, 5001),
    'employee_id': employees['employee_id'],
    'performance_score': np.random.uniform(1, 5, 5000),
    'promotion_eligible': np.random.choice([True, False], 5000, p=[0.25, 0.75])
})
performance.to_csv('performance.csv', index=False)

# Exits
exits = pd.DataFrame({
    'separation_id': range(1, 501),
    'employee_id': np.random.choice(employees['employee_id'], 500, replace=False),
    'separation_reason': np.random.choice(['Voluntary', 'Involuntary', 'Retirement'], 500),
    'notice_period_days': np.random.randint(15, 90, 500)
})
exits.to_csv('exits.csv', index=False)

# Headcount Deployment
headcount = pd.DataFrame({
    'deployment_id': range(1, 12001),
    'facility_id': np.random.choice(range(1, 51), 12000),
    'department': np.random.choice(['IT', 'HR', 'Finance', 'Operations', 'Sales', 'Support'], 12000),
    'sanctioned_positions': np.random.randint(10, 150, 12000),
    'actual_headcount': np.random.randint(8, 150, 12000)
})
headcount.to_csv('headcount_deployment.csv', index=False)

print("✓ Generated 5,000 employees, 60K payroll, 150K attendance records")
