from collections import Counter
def checkmag(magzine,note):
    flag = True
    c1 = Counter(magzine)
    c2 = Counter(note)
    for k ,v in c2.items():
        if k in c1 and c1[k]>=v:
            continue
        else:
            flag=False
            break
    if flag == True:
        return 'Yes'
    else:
        return 'No'
        
    
    



if __name__ == '__main__':
    nt=input().rstrip().split()
    A = int(nt[0])
    b = int(nt[1])
    magzine = input().split()
    note = input().split()
    res = checkmag(magzine,note)
    print(res)
    