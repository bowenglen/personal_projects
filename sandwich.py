def print_menu(dict):
    for key in sorted(dict):
        print(key, dict[key])


def main():
    veggie = ["lettuce", "spinach", "cucumber", "tomato", "onion"]
    blt = ["butter", "bacon", "lettuce", "tomato", "mozzarella"]
    turkey = ["turkey", "swiss cheese", "avocado"]
    bowen = ["butter", "beef", "lettuce", "onion", "brie", "toasted"]

    menu = {"veggie": veggie, "blt": blt, "turkey": turkey, "bowen burger": bowen}

    getMenu = ["menu", "choice", "choices", "kind", "kinds", "items"]

    breads = ["white bread", "wheat bread", "rye bread"]
    spreads = ["butter", "mayonnaise", "ketchup", "mustard"]
    options = ["toasted", "cold", "sriracha"]
    exceptions = ["no", "hold the", "without", "not want"]
    spreads_alternates = ["butter", "mayo", "mayonnaise", "ketchup", "catsup", "mustard"]

    ordering = True
    takeOrder = True
    getBread = True
    getSpread = True
    getOption = True

    sandwich_exceptions = []
    sandwich_options = []

    # loop start
    while ordering:

        while takeOrder:
            customerRequest = input("How can we help you?\n")
            listedRequest = customerRequest.lower().split()

            for word in listedRequest:
                if word in getMenu:
                    print_menu(menu)
                elif word in menu:
                    usualSandwichIngredients = menu[word]
                    sandwichIngredients = usualSandwichIngredients
                    sandwich_name = word
                    takeOrder = False
                break
                else:
                    print("I'm sorry, we don't have that sandwich. Please check our menu.")
                    # back to loop start
                    break

        for word in listedRequest:
            if word in exceptions:
                tempException = listedRequest(listedRequest.index(word) + 1)
                if tempException in usualSandwichIngredients:
                    sandwichIngredients.remove(tempException)
                    sandwich_exceptions.append(tempException)

        while getBread:
            for bread in breads:
                if bread in listedRequest:
                    sandwich_bread = bread
                    getBread = False
                else:
                    # ask for bread
                    print("Available Breads:")
                    print(breads)
                    askBread = input("Please enter desired bread.\n")
                    askBreadLower = askBread.lower()
                    if askBreadLower in breads:
                        sandwich_bread = askBreadLower
                        getBread = False

        while getSpread:
            for spread in spreads_alternates:
                if spread in listedRequest:
                    sandwich_spread = spread
                    getSpread = False
                else:
                    # ask for spread
                    print("Available Spreads:")
                    print(spreads)
                    askSpread = input("Please enter desired spread.")
                    if askSpread in spreads:
                        sandwich_spread = spread
                        getSpread = False
                        break

        for word in sandwichIngredients:
            if word in options:
                sandwich_options.append(word)

        print("Name of Sandwich: " + sandwich_name)
        print("Usual Ingredients: ")
        print(usualSandwichIngredients)
        print("Bread-type: " + sandwich_bread)
        print("Spreads: " + sandwich_spread)
        print("Options: ")
        print(sandwich_options)
        print("Exceptions: ")
        print(sandwich_exceptions)

        confirmOrder = input("Is this correct? Press 1 for Yes, or any key for no")
        if confirmOrder == 1:
            ordering = False
        else:
            break

main()
