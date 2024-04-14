# Set of available coffee types
coffee_available = {'espresso', 'latte', 'cappuccino'}

# Requirements for each type of coffee in terms of resources and cost
requirements = {
    'espresso': {'Water': 50, 'Milk': 0, 'Coffee': 18, 'Money': 1.5},
    'latte': {'Water': 200, 'Milk': 150, 'Coffee': 24, 'Money': 2.5},
    'cappuccino': {'Water': 250, 'Milk': 100, 'Coffee': 24, 'Money': 3}
}

# Dictionary containing current resource levels and accumulated money
resources = {
    'Water': 300,   # amount of water in ml
    'Milk': 200,     # amount of milk in ml
    'Coffee': 100,   # amount of coffee in grams
    'Money': 0      # money collected in dollars
}

def get_report():
    """Prints a report of the current resource levels and money collected."""
    print(f'Water: {resources['Water']}ml \nMilk: {resources['Milk']}ml \nCoffee: {resources['Coffee']}g \nMoney: ${resources['Money']}')


def make_coffee(order):
    """Deducts the required resources for a coffee order and returns a message."""
    resources['Water'] -= requirements[order]['Water']
    resources['Milk'] -= requirements[order]['Milk']
    resources['Coffee'] -= requirements[order]['Coffee']
    return 'Here is your {}. Enjoy!'.format(order)

def process_coins(order):
    """Processes the coin input by the user, checks if enough money was inserted, and provides change."""
    print('Insert coins')
    quarter = float(input('How many quarters?: ')) * 0.25
    dimes = float(input('How many dimes?: ')) * 0.10
    nickles = float(input('How many nickles?: ')) * 0.05
    pennies = float(input('How many pennies?: ')) * 0.01

    amt_inserted = round(quarter + dimes + nickles + pennies, 2)

    if requirements[order]['Money'] > amt_inserted:
        print('Sorry that\'s not enough money. Money refunded.')
    else:
        change = amt_inserted - requirements[order]['Money']
        resources['Money'] += requirements[order]['Money']
        print(f'Here is ${change} in change.')

# Main loop handling user interaction
status = True
while status:
    order = input('What would you like? (espresso/latte/cappuccino):')

    if order in coffee_available:
        # Check if there are enough resources to make the selected coffee
        if resources['Water'] < requirements[order]['Water']:
            print(f'Sorry there is not enough water for {order}.')
        elif resources['Milk'] < requirements[order]['Milk']:
            print(f'Sorry there is not enough milk for {order}.')
        elif resources['Coffee'] < requirements[order]['Coffee']:
            print(f'Sorry there is not enough coffee for {order}.')
        else:
            process_coins(order)
            print(make_coffee(order))
    elif order == 'off':
        status = False  # Turn off the machine
    elif order == 'report':
        get_report()  # Generate a report of the current resources
    else:
        print('That\'s not part of our menu, please order again')
        