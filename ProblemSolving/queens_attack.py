

def remove_entries(coed, result, bit=False):
    for iter in result:
        m, n = iter
        if n < coed and not bit:
            result.remove(iter)
        elif m < coed:
            result.remove(iter)
    return result
     

def queen_attack(n, k, r_q, c_q, obstacles):
    i, j = 1, c_q
    result = []
    while 1 <= i <= n:
        if (i, j) == (r_q, c_q):
            pass
        elif [i, j] in obstacles:
            if i > r_q:
                break
            elif i < r_q:
                result = remove_entries(r_q, result)
        else:
            result.append((i, j))
            
        i += 1
    
    print("Debug 1", result)
    i, j = r_q, 1
    while 1 <= j <= n:
        if (i, j) == (r_q, c_q):
            pass
        elif [i, j] in obstacles:
            if j > c_q:
                break
            elif j < c_q:
                result = remove_entries(c_q, result)
        else:
            result.append((i, j))
            
        j += 1

    i, j = r_q, c_q
    print("Debug 2", result)
    while i <= n and j <= n:
        if (i, j) == (r_q, c_q):
            pass
        
        elif [i, j] in obstacles:
            break
        
        else:
            result.append((i, j))
        i += 1
        j += 1
    
    i, j = r_q, c_q
    print("Debug 3", result)
    while i > 0 and j > 0:
        if (i, j) == (r_q, c_q):
            pass
        elif [i, j] in obstacles:
            break
            
        else:
            result.append((i, j))
            
        i -= 1
        j -= 1
        
    
    print("Debug 4", result)
    i, j = r_q, c_q
    while i > 0 and j <= n:
        if (i, j) == (r_q, c_q):
            pass
        elif [i, j] in obstacles:
            break
        else:
            result.append((i, j))
        
        i -= 1
        j += 1
        
    print("Debug 5", result)
    i, j = r_q, c_q
    while i <= n and j > 0:
        if (i, j) == (r_q, c_q):
            pass
        elif [i, j] in obstacles:
            break
        else:
            result.append((i, j))
            
        i += 1
        j -= 1
        
    
    return len(result)


if __name__ == '__main__':
    n, k = input().split()
    n, k = int(n), int(k)
    r_q, c_q = input().split()
    r_q, c_q = int(r_q), int(c_q)
    obstacles = []
    if k == 0:
        pass
    else:
        for i in range(k):
            kitem = input().split()
            kitem = [int(i) for i in kitem]
            obstacles.append(kitem)
    
    result = queen_attack(n, k, r_q, c_q, obstacles)
    print(result)
