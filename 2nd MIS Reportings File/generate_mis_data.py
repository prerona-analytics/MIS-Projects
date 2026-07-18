"""
Generate synthetic Facilities Management MIS data
"""
import pandas as pd
import numpy as np

np.random.seed(42)

facilities = pd.DataFrame({'facility_id': range(1, 51), 'facility_name': [f'Facility-{i}' for i in range(1, 51)], 'monthly_budget': np.random.uniform(100000, 500000, 50)})
facilities.to_csv('facilities.csv', index=False)

invoices = pd.DataFrame({'invoice_id': [f'INV-{i:06d}' for i in range(1, 50001)], 'facility_id': np.random.choice(range(1, 51), 50000), 'invoice_amount': np.random.lognormal(10, 1, 50000), 'sla_status': np.random.choice(['On-Time', 'Delayed'], 50000, p=[0.94, 0.06])})
invoices.to_csv('invoices.csv', index=False)

vendors = pd.DataFrame({'vendor_id': range(1, 101), 'vendor_name': [f'Vendor-{i}' for i in range(1, 101)], 'on_time_rate': np.random.uniform(0.75, 0.99, 100)})
vendors.to_csv('vendors.csv', index=False)

print("✓ Generated 50K invoices, 50 facilities, 100 vendors")
