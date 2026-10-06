class Account:
    def __init__(self, owner_name, account_number):

        self._owner_name = owner_name
        self._account_number = account_number
        self._balance = 0

    @property
    def owner_name(self):
        return self._owner_name

    @property
    def account_number(self):
        return self._account_number


    @property
    def balance(self):
       return self._balance

    @owner_name.setter
    def owner_name(self, owner_name):
        self._owner_name = owner_name


    def deposit(self, amount):

        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("The amount must be a number")

        if amount <= 0:
            raise ValueError(f"Add amount must be greater than 0, got {amount}")

        self._balance += amount

    def withdraw(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("The amount must be a number")

        if amount <= 0:
            raise ValueError("The amount must be greater than 0")

        if amount > self._balance:
            raise ValueError("The amount cannot be more than balance")

        self._balance -= amount



def main():
    account = Account("atia", 1)


    # 1. Valid deposit

    try:
        account.deposit(4000)

        if account.balance == 4000:
            print("PASS: deposit(4000) accepted, balance = 4000")
        else:
            print(
                f"FAIL: deposit(4000) accepted, "
                f"but balance = {account.balance}"
            )

    except Exception as e:
        print(f"FAIL: deposit(4000) should work, got {type(e).__name__}: {e}")


    # 2. Negative deposit
    old_balance = account.balance

    try:
        account.deposit(-50)
        print("FAIL: deposit(-50) should have raised ValueError")

    except ValueError as e:
        if account.balance == old_balance:
            print(f"PASS: deposit(-50) rejected -> {e}")
        else:
            print("FAIL: balance changed after rejected deposit")

    except TypeError as e:
        print(
            f"FAIL: deposit(-50) should raise ValueError, "
            f"but raised TypeError -> {e}"
        )


    # 3. String deposit
    old_balance = account.balance

    try:
        account.deposit("ads")
        print("FAIL: deposit('ads') should have raised TypeError")

    except TypeError as e:
        if account.balance == old_balance:
            print(f"PASS: deposit('ads') rejected -> {e}")
        else:
            print("FAIL: balance changed after rejected deposit")

    except ValueError as e:
        print(
            f"FAIL: deposit('ads') should raise TypeError, "
            f"but raised ValueError -> {e}"
        )


    # 4. Zero deposit
    old_balance = account.balance

    try:
        account.deposit(0)
        print("FAIL: deposit(0) should have raised ValueError")

    except ValueError as e:
        if account.balance == old_balance:
            print(f"PASS: deposit(0) rejected -> {e}")
        else:
            print("FAIL: balance changed after rejected deposit")

    except TypeError as e:
        print(
            f"FAIL: deposit(0) should raise ValueError, "
            f"but raised TypeError -> {e}"
        )


    # 5. Boolean deposit
    old_balance = account.balance

    try:
        account.deposit(True)
        print("FAIL: deposit(True) should have raised TypeError")

    except TypeError as e:
        if account.balance == old_balance:
            print(f"PASS: deposit(True) rejected -> {e}")
        else:
            print("FAIL: balance changed after rejected deposit")

    except ValueError as e:
        print(
            f"FAIL: deposit(True) should raise TypeError, "
            f"but raised ValueError -> {e}"
        )



    # 6. Valid withdrawal
    try:
        account.withdraw(2000)

        if account.balance == 2000:
            print("PASS: withdraw(2000) accepted, balance = 2000")
        else:
            print(
                f"FAIL: withdraw(2000) accepted, "
                f"but balance = {account.balance}"
            )

    except Exception as e:
        print(
            f"FAIL: withdraw(2000) should work, "
            f"got {type(e).__name__}: {e}"
        )


    # 7. Negative withdrawal
    old_balance = account.balance

    try:
        account.withdraw(-50)
        print("FAIL: withdraw(-50) should have raised ValueError")

    except ValueError as e:
        if account.balance == old_balance:
            print(f"PASS: withdraw(-50) rejected -> {e}")
        else:
            print("FAIL: balance changed after rejected withdrawal")

    except TypeError as e:
        print(
            f"FAIL: withdraw(-50) should raise ValueError, "
            f"but raised TypeError -> {e}"
        )


    # 8. String withdrawal
    old_balance = account.balance

    try:
        account.withdraw("ads")
        print("FAIL: withdraw('ads') should have raised TypeError")

    except TypeError as e:
        if account.balance == old_balance:
            print(f"PASS: withdraw('ads') rejected -> {e}")
        else:
            print("FAIL: balance changed after rejected withdrawal")

    except ValueError as e:
        print(
            f"FAIL: withdraw('ads') should raise TypeError, "
            f"but raised ValueError -> {e}"
        )


    # 9. Zero withdrawal
    old_balance = account.balance

    try:
        account.withdraw(0)
        print("FAIL: withdraw(0) should have raised ValueError")

    except ValueError as e:
        if account.balance == old_balance:
            print(f"PASS: withdraw(0) rejected -> {e}")
        else:
            print("FAIL: balance changed after rejected withdrawal")

    except TypeError as e:
        print(
            f"FAIL: withdraw(0) should raise ValueError, "
            f"but raised TypeError -> {e}"
        )


    # 10. Boolean withdrawal
    old_balance = account.balance

    try:
        account.withdraw(True)
        print("FAIL: withdraw(True) should have raised TypeError")

    except TypeError as e:
        if account.balance == old_balance:
            print(f"PASS: withdraw(True) rejected -> {e}")
        else:
            print("FAIL: balance changed after rejected withdrawal")

    except ValueError as e:
        print(
            f"FAIL: withdraw(True) should raise TypeError, "
            f"but raised ValueError -> {e}"
        )


    # 11. Withdraw more than balance
    old_balance = account.balance

    try:
        account.withdraw(5000)
        print("FAIL: withdraw(5000) should have raised ValueError")

    except ValueError as e:
        if account.balance == old_balance:
            print(f"PASS: withdraw(5000) rejected -> {e}")
        else:
            print("FAIL: balance changed after rejected withdrawal")

    except TypeError as e:
        print(
            f"FAIL: withdraw(5000) should raise ValueError, "
            f"but raised TypeError -> {e}"
        )


    # 12. Withdraw exactly the balance
    try:
        account.withdraw(2000)

        if account.balance == 0:
            print("PASS: withdraw(2000) accepted, balance = 0")
        else:
            print(
                f"FAIL: withdraw(2000) accepted, "
                f"but balance = {account.balance}"
            )

    except Exception as e:
        print(
            f"FAIL: withdraw(balance) should work, "
            f"got {type(e).__name__}: {e}"
        )


if __name__ == "__main__":
    main()