#Exercise 1

# Create a class called cart that retains items and has methods to add, remove, and show

from IPython.display import clear_output
class shopping_cart:

    def __init__(self, add, remove, show, clear, quit, shop):
        self.add_to_cart = add
        self.remove_from_cart = remove
        self.show_cart = show
        self.clear_cart = clear
        self.quit_cart = quit
        self.shop_cart = shop
        

    def main():     
        my_cart = shopping_cart()
        correct_answer = ('Add', 'Remove', 'Show', 'Clear', 'Quit')

        while True:
            answer = input('Welcome to Braxton Shoppe What would you like to do? Add/Remove/Show/Clear/Quit ').title()
    
            while answer not in correct_answer:
                answer = 'That is not an option. What would you like to do? Add/Remove/Show/Clear/Quit '.title()
            if answer == 'quit':
                clear_output()
                break
            elif answer == 'add':
                my_cart.add_to_cart()
            elif answer == 'remove':
                my_cart.remove_from_cart()
            elif answer == 'clear':
                my_cart.clear_cart(my_cart)

    def add_to_cart(self):
        item = input('What would you like to add to your cart? ').title()
        if item in self.shop_cart:
            amount = int(input(f'How many {item} would you like to add to your cart? '))
            self.cart[item]['amount'] += amount 
        else:
            price = float(input(f'What is the price of {item}'))
            amount = int(input(f'How many {item} would you like to add to your cart? '))
            self.cart[item] = {'price': price, 'amount': amount}
        clear_output()
        print(f'{amount} {item} have been added to your cart! ')

    def remove_from_cart(self):
        item = input('What would you like to remove from your cart? ').title()
        if item in self.shop_cart:
            amount = int(input(f'How many {item} would you like to remove from your cart? '))
            self.cart[item]['amount'] -= amount 
        print(f'{amount} {item} have been removed from your cart! ')
        pass
    def show_cart():
        print(my_cart)
        pass

    def clear_cart(self):
        my_cart.clear()
        pass



    main()

# Exercise 2

class Buddy():

    def __init__(self, animal, energy_level = 100):
        self.animal = animal
        self.energy_level = energy_level
    
    def play(self, time_played):
        new_energy_level = time_played // 3
        self.energy_level -= new_energy_level 
        print(f'The {self.animal} is done playing for now. It has an energy level of {self.energy_level}')
        pass

    def sleep(self, hours_slept):
        new_energy_level = hours_slept * 20
        self.energy_level += new_energy_level 
        print(f'The {self.animal} is done sleeping now. It has an energy level of {self.energy_level}')
        pass

    def eat(self, calories):
        new_energy_level = calories * 1
        self.energy_level += new_energy_level 
        print(f'The {self.animal} is done eating now. It has an energy level of {self.energy_level}')
        pass
# instince
animal_1 = Buddy('Tiger')

animal_1.play(36) 
animal_1.sleep(3)  
animal_1.eat(500)