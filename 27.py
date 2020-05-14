string = list(input())

start = 0
end = len(string)-1

flag = 0

while start < end:
    if string[start] != string[end]:
        print("String Not Palindrome")
        flag = 1
        break

    start +=1
    end-=1


if flag == 0:
    print("String is Palindrome")
