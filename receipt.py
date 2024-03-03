from prettytable import PrettyTable

items = [
   {"name": "1. Clean Code, Robert C. Martin", "net": 100.00, "vat": 8},
   {"name": "2. Applying UML and Patterns, C. Larman", "net": 300.00, "vat": 8},
   {"name": "3. Shipping", "net": 50.00, "vat": 23}
]

total_net_8 = 0
total_net_23 = 0

for item in items:
    if item["vat"] == 8:
        total_net_8 += item["net"]
    elif item["vat"] == 23:
        total_net_23 += item["net"]

total_vat_8 = total_net_8 * 8 / 100
total_vat_23 = total_net_23 * 23 / 100

table = [['', 'Total net', 'Total vat'], ["VAT 8%", total_net_8, total_vat_8], ["VAT 23%", total_net_23, total_vat_23]]
tab = PrettyTable(table[0],  align='c', valign='t')
tab.add_rows(table[1:])
print(tab)