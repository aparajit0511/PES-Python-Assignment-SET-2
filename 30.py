our_list = []

for i in range(int(input())):
    our_list.append(int(input()))

for i in range(len(our_list)):
    for j in range(len(our_list) - 1):
        if our_list[j] > our_list[j+1]:
            our_list[j], our_list[j+1] = our_list[j+1], our_list[j]


print(our_list)