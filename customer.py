class Customer:
    def __init__(self, customer_id, customer_name):

        if not isinstance(customer_id, int) or isinstance(customer_id, bool):
            raise TypeError("The customer ID must be an integer")

        if customer_id <= 0:
            raise ValueError("The customer ID must be greater than 0")

        if not isinstance(customer_name, str):
            raise TypeError("The customer name must be a string")

        if not customer_name.strip():
             raise ValueError("The customer name must not be empty")

        self._customer_id = customer_id
        self._customer_name = customer_name


    @property
    def customer_id(self):
        return self._customer_id

    @property
    def customer_name(self):
            return self._customer_name


def main():


    # ID is a text
    try:
        customer = Customer("123", "safaa")
        print("Fail: Text ID was accepted")

    except TypeError as te:
        print(f"Pass: Text ID correctly rejected --> {te}")

    # ID is a bool
    try:
        customer = Customer(True, "safaa")
        print("Fail: Boolean ID was accepted")

    except TypeError as te:
        print(f"Pass: Boolean ID correctly rejected --> {te}")

    # ID is a zero
    try:
        customer = Customer(0, "safaa")
        print("Fail: Zero ID was accepted")

    except ValueError as ve:
        print(f"Pass: Zero ID correctly rejected --> {ve}")

    # ID is a negative
    try:
        customer = Customer(-1, "safaa")
        print("Fail: Negative ID was accepted")

    except ValueError as ve:
        print(f"Pass: Negative ID correctly rejected --> {ve}")

    # valid customer name
    try:
        customer = Customer(1, "atia")
        print(customer.customer_name)
        print("Pass: Valid customer name")
    except ValueError as ve:
        print(f"Fail: Unexpected ValueError: {ve}")
    except TypeError as te:
        print(f"Fail: Unexpected ValueError: {te}")


    # empty customer name
    try:
        customer = Customer(123, "")

        print("Fail: Empty name was accepted")

    except ValueError as ve:
        print(f"Pass: Empty name correctly rejected --> {ve}")

    except TypeError as te:
        print(f"Fail: Expected ValueError but got TypeError --> {te}")


    # name contains only spaces
    try:
        customer = Customer(123, "   ")

        print("Fail: Spaces-only name was accepted")

    except ValueError as ve:
        print(f"Pass: Spaces-only name correctly rejected --> {ve}")

    except TypeError as te:
        print(f"Fail: Expected ValueError but got TypeError --> {te}")

    # name is not string
    try:
        customer = Customer(123, 12345)

        print("Fail: Non-string name was accepted")

    except TypeError as te:
        print(f"Pass: Non-string name correctly rejected --> {te}")

    except ValueError as ve:
        print(f"Fail: Expected TypeError but got ValueError --> {ve}")

    # can not change the name
    try:
        customer = Customer(123, "atia")
        customer.customer_name = "Ahmed"
        print("Fail: Customer name was changed")

    except AttributeError as ae:
        print(f"Pass: Customer name cannot be changed directly --> {ae}")

    # ID cannot be changed
    try:
        customer = Customer(123, "safaa")
        customer.customer_id = 156
        print("Fail: Customer ID was changed")

    except AttributeError as ae:
        print(f"Pass: Customer ID cannot be changed directly --> {ae}")


    # check the customer data

    customer = Customer(123, "safaa")

    if customer.customer_id == 123:
        print("Pass: Customer ID is correct")
    else:
        print("Fail: Customer ID is incorrect")

    if customer.customer_name == "safaa":
        print("Pass: Customer name is correct")
    else:
        print("Fail: Customer name is incorrect")

if __name__ == "__main__":
    main()