def closest_min_max(arr):
    mini=float('inf')
    maxi=-float('inf')
    n=len(arr)

    for i in range(n):
        if arr[i]<mini:
            mini=arr[i]
        elif arr[i]>maxi:
            maxi=arr[i]

    r_min=-1
    r_max=-1
    res=n

    for i in range(n):
        if arr[i]==maxi:
            r_max=i
            if r_min>=0:
                res=min(res,i-r_min+1)
        elif arr[i]==mini:
            r_min=i
            if r_max>=0:
                res=min(res,i-r_max+1)
    return res

arr = list(map(int, input().split()))
print(closest_min_max(arr))