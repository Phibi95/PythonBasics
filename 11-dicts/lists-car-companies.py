companies = ["VW","Audi","Tesla"]

while True:
    companies.sort()
    print(companies)

    new_company = input("Gib eine Automarke ein:")
    companies.append(new_company)