from datetime import datetime

INITIAL_VALUE = 0.0

def id_creator() -> str:
    return str(datetime.now().timestamp())

class Balance:

    def __init__(self, balance: float):
        self.balance = balance
        self.transactions = {
            f"{id_creator()}": {
                "description": "Initial balance",
                "date": datetime.now(),
                "amount": balance,
                "type": "credit"
            }
        }

    def add_transaction(self, description: str, date: datetime, amount: float, type_of_transaction: str) -> None:
        id_number = id_creator()
        self.transactions[id_number] = {
            "description": description,
            "date": date,
            "amount": amount,
            "type": type_of_transaction
        }

    def print_transactions(self):
        print("-" * 20)
        for id_number, transaction in self.transactions.items():
            print(f" date: {transaction['date'].strftime('%H:%M:%S')} \n description: {transaction['description']} \n amount: {transaction['amount']} \n type: {transaction['type']}")
            print("-" * 20)

def main() -> None:
    global INITIAL_VALUE

    menu = "\n1. Add transaction \n2. Print transactions \n3. Exit\n"

    try:
        INITIAL_VALUE = float(input("Enter the initial balance: "))
    except ValueError:
        raise f'{INITIAL_VALUE} is not the correct type, you must input a float'
    balance = Balance(INITIAL_VALUE)
    while True:
        print(menu)
        option = input("Choose an option: ")
        if option == "1":
            description = input("Description: ")
            date = datetime.now()
            amount = float(input("Amount: "))
            type_of_transaction = input("Type of transaction: ")
            balance.add_transaction(description, date, amount, type_of_transaction)
        elif option == "2":
            balance.print_transactions()
        elif option == "3":
            break
        else:
            print("Invalid option")

    balance.add_transaction("Initial balance", datetime.now(), INITIAL_VALUE, "credit")


if __name__ == "__main__":
    main()
