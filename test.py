def ask_hsdp():
    choices = ['h', 's', 'd', 'p']
    while True:
        choice = input("What would you like to do? h(hit), s(stand), d(double), p(split)")
        if choice in choices:
            return choice
        else:
            print("Please pick a valid choice")
        

ask_hsdp()