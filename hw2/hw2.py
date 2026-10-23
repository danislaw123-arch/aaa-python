import csv

def read_to_dict(filename):
    employees = []
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter = ";")
        next(reader)
        for row in reader:
            employee = {
                "fio": row[0],
                "department": row[1],
                "team": row[2],
                "position": row[3],
                "score": row[4],
                "salary": row[5]
            }
            employees.append(employee)
    return employees

def hierarchy(employees):
    hier = {}
    for employee in employees:
        if employee["department"] not in hier:
            hier[employee["department"]] = set()
            hier[employee["department"]].add(employee["team"])
        else:
            hier[employee["department"]].add(employee["team"])
    return hier

def summary(employees):
    salaries = {}
    for employee in employees:
        if employee["department"] not in salaries:
            salaries[employee["department"]] = []
            salaries[employee["department"]].append(int(employee["salary"]))
        else:
            salaries[employee["department"]].append(int(employee["salary"]))
    summ = {}
    for department in salaries:
        summ[department] = {
        "number of people": len(salaries[department]),
        "min salary": min(salaries[department]),
        "max salary": max(salaries[department]),
        "average salary": sum(salaries[department]) / len(salaries[department])
        }
    return summ

def write_summary(summ, filename):
    with open(filename, "w") as f:
        writer = csv.writer(f, delimiter = ";")
        writer.writerow(["Департамент", "Численность", "Мин", "Макс", "Средняя"])
        for department, stats in summ.items():
            writer.writerow([department, stats["number of people"], stats["min salary"], stats["max salary"], stats["average salary"]])

def reports(a):
    employees = read_to_dict("Corp_Summary.csv")
    if a == 1:
        return hierarchy(employees)
    elif a == 2:
        return summary(employees)
    elif a == 3:
        write_summary(summary(employees), "report.csv")


print(reports(1))
print(reports(2))
reports(3)