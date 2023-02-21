
# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    i = 0
    while i< len(arr):
        index = arr[i]-1
        if arr[i]!=arr[index]:
            arr[i],arr[index]=arr[index],arr[i]
            count+=1
        else:
            i+=1
    return count            
            
        
                

if __name__ == '__main__':
    
    

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)

    