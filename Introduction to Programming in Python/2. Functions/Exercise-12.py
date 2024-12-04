#12. The following checksum formula is widely used by banks and credit card companies to validate legal account numbers:
#d0 + f(d1) + d2 + f(d3) + d4 + f(d5) + d6 + ... = 0 (mod 10)
# For example, 17327 is valid because 1 + 5 + 3 + 4 + 7 = 20, which is a multiple of 10.
def f(n):
    n = n * 2
    return sum(int(digit) for digit in str(n))

def check_sum(account_number):
    list_of_accnum = [int(digit) for digit in str(account_number)]
    total = 0
    for i in range(len(list_of_accnum)):
        if i % 2 == 0:
            total += f(list_of_accnum[i])
        else:
            total += list_of_accnum[i]
    
    c = (10 - (total % 10)) % 10
    return c
    
def full_account(account_number):
    if len(str(account_number))!= 10:
        raise ValueError("Please fill in the valid account number")
    
    last_digit = check_sum(account_number)
    return int(f"{account_number}{last_digit}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <10-digit-number>")
        sys.exit(1)
    
    try:
        ten_digit_number = int(sys.argv[1])
        if len(str(ten_digit_number)) != 10:
            raise ValueError
    except ValueError:
        print("Please fill in the valid account number")
        sys.exit(1)
    
    valid_number = full_account(ten_digit_number)
    print(f"Valid 11-digit-number account is: {valid_number}")