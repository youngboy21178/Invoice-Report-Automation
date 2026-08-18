import pandas as pd 

file = "D:/Python/invoice-report-automation/sample-data/01_top_categories_by_revenue.csv"
data = pd.read_csv(file)
data_count = len(data["revenue"])
data["revenue_first_num"] = data["revenue"].astype(str)
numbers = {str(a+1):0 for a in range(9)}
print(numbers)
for e in data["revenue_first_num"] : 
    numbers[e[0]] += 1
for e in numbers : 
    print(f"key: {e} value: {(numbers[e]/data_count)*100}%")
