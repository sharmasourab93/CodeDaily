def sockmerchant(n, ar):
    pair, pair_count = [], 0
    for i in range(n):
        if ar[i] not in pair:
            pair.append(ar[i])
        else:
            pair.remove(ar[i])
            pair_count += 1
    
    return pair_count
    

if __name__ == '__main__':
    num = 9
    array = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = sockmerchant(num, array) # expected result 3
    print(result)