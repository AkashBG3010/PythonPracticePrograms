class User:
    def log(self):
        print(self)

class New_User(User):
    def log(self):
        print("I'm a new user")

class Customer(User):

    def log(self):
        print("I'm a customer")

    def __init__(self, name, membership_type):  # encapsulation
        self.name = name
        self.membership_type = membership_type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    def update_membership(self, new_membership):
        print("calculating costs...")
        self.membership_type = new_membership

    def __str__(self):
        return self.name + " " + self.membership_type

    def print_all_customers(Customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True

        return False

    __hash__ = None
    __repr__ = __str__

users = [Customer("caled", "Gold"),
             Customer("John", "Silver"),
             New_User()]

# print(customers[0].name)    # normal
# customers[1].log()       # inheritance

for user in users:
    user.log()      # polymorphism

