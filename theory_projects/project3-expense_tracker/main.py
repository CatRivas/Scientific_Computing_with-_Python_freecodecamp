import os

def screen_cleaner():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def add_expense(expenses, amount, category):
    expenses.append(
                    {'category': category,
                    'amount': amount,
                    }
    )

    # print(expenses)


def print_expenses(expenses):
    for expense in expenses:
        print(f'Category: {expense["category"]}, Amount: {expense["amount"]}')


def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))


def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)


def main():
    expenses = []

    while True:

        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            category = input('Enter category: ')
            amount = float(input('Enter amount: '))
            add_expense(expenses, amount, category)
            input("\nPress Enter to continue...") #pause before cleaning
            
        elif choice == '2':
            if expenses: #checks if there is items in the list
                print('\nAll Expenses:')
                print_expenses(expenses)
            else:
                print('\nNo expenses found')
            input("\nPress Enter to continue...")  #pause before cleaning

        elif choice == '3':
            print(f'\nTotal Expenses: {total_expenses(expenses)}')
            input("\nPress Enter to continue...")  

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(
                expenses, category)
            print_expenses(expenses_from_category)
            input("\nPress Enter to continue...")  

        elif choice == '5':
            print('Exiting the program.')
            break

        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")  

        screen_cleaner()


if __name__ == '__main__':
    main()
