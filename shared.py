def calculate_summer_avg(row):
    count=0
    total=0
    for month in ["Jun","Jul","Aug"]:
        if row[month]>-9.99:
            count+=1
            total+=row[month]
    return total/count