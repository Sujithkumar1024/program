n = int (input("enter n:"))
arr = list (map(int,input().split()))
total_sum =  sum(arr)
left_sum = 0
for i in range (n):
    right_sum = total_sum-left_sum - arr[i]
    if left_sum == right_sum:
        print("YES")
        break
    left_sum += arr[i]
else:
    print("NO")