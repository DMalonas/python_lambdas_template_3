
def is_num_decimal(x):
    return x.isdecimal()

def dec_to_bin(a, l=[]):
    binary = 0
    ctr = 0
    temp = a  # copy input decimal

    # find binary value using while loop
    while (temp > 0):
        binary = ((temp % 2) * (10 ** ctr)) + binary
        temp = int(temp / 2)
        ctr += 1
    return binary


def is_num_binary(x):
    return  all(c in '01' for c in x)


def bin_to_dec(number):
    print(len(number))
    return int(number, 2)


def twos_comp(str):
    n = len(str)
    i = n - 1
    while (i >= 0):
        if (str[i] == '1'):
            break
        i -= 1
    if (i == -1):
        return '1' + str
    k = i - 1
    while (k >= 0):
        if (str[k] == '1'):
            str = list(str)
            str[k] = '0'
            str = ''.join(str)
        else:
            str = list(str)
            str[k] = '1'
            str = ''.join(str)
        k -= 1
    return str


# ΜΕΝΟΥ
if __name__ == "__main__":
    while True:
        print("Επιλογές")
        print("========")
        print(
            "1. Μετατροπή δεκαδικού αριθμού στο δυαδικό σύστημα, 2. Μετατροπή δυαδικού αριθμού στο δεκαδικό σύστημα, 3. Εύρεση συμπληρώματος δυαδικού αριθμού"
        )
        choice = int(input("Δώστε την επιλογή σας (οτιδήποτε άλλο για έξοδο): "))
        if choice == 1:
            try:
                integer = input("\nEnter decimal: ")
                is_num_decimal(integer)
                print(dec_to_bin(int(integer), []))
            except:
                print("\nnot integer\n")
                continue
        elif choice == 2:
            try:
                binary = input("\nEnter binary: ")
                is_num_binary(binary)
                print(bin_to_dec(binary))
            except:
                print("\nnot binary\n")
        elif choice == 3:
            try:
                binary = input("\nEnter binary")
                is_num_binary(binary)
                print("two's complement: " + str(twos_comp(binary)))
            except:
                print("\nnot binary\n")
        else:
            exit(1)
