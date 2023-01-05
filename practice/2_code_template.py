basket = {"MILK 1LT": 0, 'YOGURT 2%': 0, 'ICE CREAM': 0, 'NESCAFFE': 0, 'BISCUITS': 0, "CHEF'S SALAD": 0,
          'TOAST CHEESE': 0, 'EXTRA VIRGIN OLIVE OIL': 0, 'FILTERED COFFEE': 0, 'TOAST BREAD': 0}
products = [('MILK 1LT', 1.5), ('YOGURT 2%', 2.0), ('ICE CREAM', 2.5),
            ('NESCAFFE', 7.5), ('BISCUITS', 1.0), ("CHEF'S SALAD", 1.0),
            ('TOAST CHEESE', 6.0), ('EXTRA VIRGIN OLIVE OIL', 8.0),
            ('FILTERED COFFEE', 7.0), ('TOAST BREAD', 1.5)]


def product_exists(name, products):
    for entry in products:
        if entry[0] == name:
            return True
    return False


def add_products(basket, products):
    name = input('\n1 Enter name\n2 Exit product-enter mode\n ')
    if name == "2":
        return
    else:
        if product_exists(name, products):
            quant = int(input("\nEnter quantity: "))
            try:
                basket[name] += quant
            except:
                print("\nWrong key\n")
            add_products(basket, products)

def display_basket(basket, products):
    sum = 0.0
    print('AA\tPRODUCT\tQUANTITY\tPRICE\tTOTAL VALUE\n')
    display_tuple = tuple({'AA': 0, 'PRODUCT': '', 'QUANTITY': 0, 'PRICE': '', 'TOTAL VALUE': ''} for _ in range(len(products)))

    for idx in range(len(products)):
        display_tuple[idx][0] = idx + 1
        display_tuple[idx][1] = products[idx][0]
        display_tuple[idx][2] = list(basket.items())[idx][1]
        display_tuple[idx][3] = str(products[idx][1]) + "E"
        display_tuple[idx][4] = str(int(display_tuple[idx][2]) * products[idx][1])
        sum += int(display_tuple[idx][2]) * products[idx][1]
        print(str(display_tuple[idx].values())[30: -2].split(","))
    # for idx in range(len( ))
    print("\nTotal: " + str(sum) + "E")

def remove_product(basket, products):
    display_basket(basket, products)
    choice = int(input("\nChoose line to remove from basket"))
    cnt = 0
    if choice >= 0 and choice < len(basket):
        for entry in basket:
            if cnt == choice - 1:
                basket[entry] = 0
                break
            cnt += 1

def buy_products(basket, products):
    display_basket(basket, products)
    cnt = 0
    for entry in basket:
        if basket[entry] != 0:
            cnt = 1
    if cnt == 0:
        print('\nThe basket is empty\n')
        exit(1)
    choice = int(input('Do you have a member\'s card? (1 for yes | 2 for no'))
    if choice == 1:
        display_basket_with_discount(basket, products)
        print("\nThe program will now exit\n")
        exit(1)

def display_basket_with_discount(basket, products):
    sum = 0.0
    print('AA\tPRODUCT\tQUANTITY\tPRICE\tTOTAL VALUE\n')
    display_tuple = tuple(
        {'AA': 0, 'PRODUCT': '', 'QUANTITY': 0, 'PRICE': '', 'TOTAL VALUE': ''} for _ in range(len(products)))
    for idx in range(len(products)):
        display_tuple[idx][0] = idx + 1
        display_tuple[idx][1] = products[idx][0]
        display_tuple[idx][2] = list(basket.items())[idx][1]
        display_tuple[idx][3] = str(products[idx][1]) + "E"
        display_tuple[idx][4] = str(int(display_tuple[idx][2]) * products[idx][1])
        sum += int(display_tuple[idx][2]) * products[idx][1]
        print(str(display_tuple[idx].values())[30: -2].split(","))
    print("\nTotal: " + str(sum * 0.93) + "E")

if __name__ == "__main__":
    while True:
        choice = int(input("\n1. Add items to basket\n2. Show basket\n3. Remove from basket\n4. Buy products\n"))
        if choice == 1:
            add_products(basket, products)
        elif choice == 2:
            display_basket(basket, products)
        elif choice == 3:
            remove_product(basket, products)
        elif choice == 4:
            buy_products(basket, products)
        else:
            print('\nInvalid input\n')