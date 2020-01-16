#from prettytable import PrettyTable

import prettytable

table = prettytable.PrettyTable()

table.field_names = ["first_name", "last_name", "height_cm", "weight_kg"]

table.add_row(["Lebron","James", 203, 113])
table.add_row(["Kevin","Durant", 210, 108])

print(table)