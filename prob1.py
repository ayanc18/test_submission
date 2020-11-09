def count_max_seat(m,n,k):
    if m == 0 or n == 0 or k==0:
        return 0
    else:
        if m % 2 == 0:
            row_box_count = m/2
        else:
            row_box_count = int(m/2) + 1
        if n % 2 == 0:
            col_box_count = n/2
        else:
            col_box_count = int(n/2) + 1
        count = int(row_box_count * col_box_count)
        print("max seat: "+str(count))
        if k <= count:
            return True
        else:
            return False

def main():
    m = input("Please Provide value for M (rows): ")
    while m.isdigit() != True:
        m = input("Please Provide value for M (rows): ")
    n = input("Provide value for N (columns): ")
    while n.isdigit() != True:
        n = input("Provide value for N (columns): ")
    k = input("Provide value for K (number of persons): ")
    while k.isdigit() != True:
        k = input("Provide value for K (number of persons): ")
    output = count_max_seat(int(m),int(n),int(k))
    print(output)
    pass

if __name__ == '__main__':
    main()