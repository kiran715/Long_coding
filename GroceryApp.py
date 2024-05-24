class User:
    users = []
    def __init__(self, userId, name, email, password, role):
        self.userId = userId
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        User.users.append(self)
    
class Product:
    products = []
    def __init__(self, productId, productName, quantity, price):
        self.productId = productId
        self.productName = productName
        self.quantity = quantity
        self.price = price
        Product.products.append(self)


class Cart:
    cartItems = []
    def __init__(self, cartId, userId, productId, quantity, total_price):
        self.cartId = cartId
        self.userId = userId
        self.productId = productId
        self.quantity = quantity
        self.total_price = total_price
        Cart.cartItems.append(self)


class Payment:
    payments = []
    def __init__(self, paymentId, paymentMehthod, cardNum, month, year, cvv, amount, status):
        self.paymentId = paymentId
        self.paymentMethod = paymentMehthod
        self.cardNum = cardNum
        self.month = month
        self.year = year
        self.cvv = cvv
        self.amount = amount
        self.status = status
        Payment.payments.append(self)


class GroceryApp:
    # def __init__(self):
    #     self.users = []
    #     self.products = []
    #     self.cartItems = []
    #     self.payments = []

    def validateLogin(self, email, password, users):
        for user in users:
            if user.email == email and user.password == password:
                return user
        return None
    
    # def addUser(self, user):
    #     self.users.append(user)

    # def addProdcut(self, product):
    #     self.products.append(product)
    
    # def addCart(self, cart):
    #     self.cartItems.append(cart)

    # def addPayment(self, payment):
    #     self.payments.append(payment)
    def show_items(self, groceryList):
        print("Grocery Items List : ")
        for details in groceryList:
            print("product id : ", details.productId)
            print("Product Name : ", details.productName)
            print("Quantity : ", details.quantity)
            print("Price : ", details.price)
            print("-------------------------------------")
            


    def asCustomer(self, currentUser, groceryList, cartItemList, paymentList):
        stayIn = True
        print("Entered as customer")
        while stayIn:
            print("1. View Grocery Items \n 2. Add to Cart \n 3. View Cart \n 4. Make payment \n 5. Exit")
            ch = int(input("Enter your choice : "))
            if ch == 1:
                self.show_items(groceryList)
            
            elif ch == 2:
                productId = int(input("Enter product id : "))
                quantity = int(input("Enter quantity : "))
                productPrice = [item.price for item in Product.products if productId == item.productId]
                total_price = quantity * productPrice[0]
                cartItem = Cart(len(Cart.cartItems) + 1, currentUser.userId, productId, quantity, total_price)
            elif ch == 3:
                print("Cart Items : ")
                for cart in cartItemList:
                    if cart.userId == currentUser.userId:
                        print("Cart ID : ", cart.cartId)
                        print("Product ID : ", cart.productId)
                        print("Quantity : " , cart.quantity)
                        print("Price : ", cart.total_price)
                        print("-------------------------------------")
            elif ch == 4:
                method = input("Enter payment Method : ")
                cardNum = int(input("Enter card Number : "))
                month = input("Enter month : ")
                year = int(input(" Enter year : "))
                amount = int(input("Enter amount : " ))
                status = input("Enter payment status : ")
                payment = Payment(len(paymentList) + 1, method, cardNum, month, year, amount, status)
                print("Payment made successfully")

            elif ch == 5:
                stayIn = False
    def asAdmin(self, currentUser, productList):
        stayIn = True
        while stayIn:
            print("1. View Product details \n 2. Add products \n 3. Exit")

            ch = int(input("Enter your choice : "))
            if ch == 1:
                self.show_items(productList)
            
            elif ch == 2:
                productName = input("Enter product Name : ")
                quantity = int(input("Enter quantity : "))
                price = int(input("Enter Price : "))
                newProduct = Product(len(productList) + 1, productName, quantity, price)
                print("Item added to Product list succesfully")
            elif ch == 3:
                stayIn = False


App = GroceryApp()

user1  = User(1, "Kiran", "kiran@gmail.com", "kiran", "customer")
user2 = User(2, "Admin", "admin@gmail.com", "admin123", "admin")

product1 = Product(1, "Apple", 5, 10)
product2 = Product(2, "Orange", 6, 20)


loggedUser = App.validateLogin("kiran@gmail.com", "kiran", User.users)
if loggedUser != None and loggedUser.role == "customer":
    App.asCustomer(loggedUser, Product.products, Cart.cartItems, Payment.payments)


            


            
    