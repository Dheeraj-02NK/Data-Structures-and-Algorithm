Given the participants score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given n scores. 
Store them in a list and find the score of the runner-up.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CODE:
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    k = max(arr)
    l = arr.index(k)
    print(arr[l-1])
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
