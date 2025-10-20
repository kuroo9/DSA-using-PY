expense=[(2200,2350,2600,2130,2190)]# Calculate the total expense for the first quarter (Jan, Feb, Mar)
total=expense[0]+expense[1]+expense[2]
print(total)
#extra dollars in feb compared to jan
extra=expense[1]-expense[0]
print(extra)
#exactly 2000 expense in any month
for i in expense:
    if i==2000:
        print("found this month with 2000 expense",i)
#add june expense
expense.append(1980)
print(expense)
#increase april expense by 200


