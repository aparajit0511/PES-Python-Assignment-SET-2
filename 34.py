lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,12]
lst3 = [5,2,6,7,8]

lst1.sort()
lst2.sort()
lst3.sort()

max_list = []
min_list = []

max_list.append(lst1[-1])
max_list.append(lst1[-2])

max_list.append(lst2[-1])
max_list.append(lst2[-2])

max_list.append(lst2[-1])
max_list.append(lst2[-2])



min_list.append(lst1[-1])
min_list.append(lst1[-2])

min_list.append(lst2[-1])
min_list.append(lst2[-2])

min_list.append(lst2[-1])
min_list.append(lst2[-2])


average_max_list = sum(max_list) // len(max_list)
average_min_list = sum(min_list) // len(min_list)