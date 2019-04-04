from model.Menu import Menu
from model.Order import Order
from model.Customers import Customers
from model.Address import Address
from model.Restaurant import Restaurant

restaurantsCuisine = dict()
restaurantsCommune = dict()
customers = dict()
order = dict()
restaurants_dict = dict()

def createRestaurants():
    #separate keys, one for cuisine and one for commune
    rList = []
    m1 = Menu(1, "Pizza - Margareta", " Yummy for students", "5")
    m2 = Menu(2, "Pizza - Chicken Twist", "With paprika", "6")
    m3 = Menu(3, "Pizza - Mexican Delight", "With cheese", "7")
    #added an id for restaurants for easy fetch of restaurants- fetch by id rather than name
    r1 = Restaurant(1, "Pizza Hut", "Italian", "Evere")
    r1.addMenuItem(m1)
    r1.addMenuItem(m2)
    r1.addMenuItem(m3)
    rList.append(r1)

    r3 = Restaurant(2, "Domino's Pizza", "Italian", "Evere")
    r3.addMenuItem(Menu(1, "Pizza - Margareta", " Yummy for students", "5"))
    r3.addMenuItem(Menu(2, "Pizza - Veggie Farm", " Yummy for students", "6"))
    r3.addMenuItem(Menu(3, "Pizza - Mexican Delight", "Big size", "7"))
    rList.append(r3)

    keyCui = r1.getCuisine()
    keyCom = r1.getCommune()
    restaurantsCuisine[keyCui] = rList
    restaurantsCommune[keyCom] = rList

    r2List = []
    r2 = Restaurant(3, "Ashoka", "Indian", "Evere")
    r2.addMenuItem(Menu(1, "Chicken Tikka Masala", "Taj-mahal taste", "5"))
    r2.addMenuItem(Menu(2, "Biryani", "Summer taste", "5"))
    r2.addMenuItem(Menu(3, "Gulab Jamun", "unforgetable taste", "2"))
    r2List.append(r2)

    key2Cui = r2.getCuisine()
    key2Com = r2.getCommune()
    restaurantsCuisine[key2Cui] = r2List
    restaurantsCuisine[key2Com] = r2List

def createRestaurantDict():
    r1 = Restaurant("001", "Pizza Hut", "Italian", "Evere")
    r2 = Restaurant("003", "Ashoka", "Indian", "Evere")
    r3 = Restaurant("002","Domino's Pizza", "Italian", "Evere")

    r1.addMenuItem(Menu(1, "Pizza - Margareta", " Yummy for students", "5"))
    r1.addMenuItem(Menu(2, "Pizza - Chicken Twist", "With paprika", "6"))
    r1.addMenuItem(Menu(3, "Pizza - Mexican Delight", "With cheese", "7"))

    r2.addMenuItem(Menu(1, "Chicken Tikka Masala", "Taj-mahal taste", "5"))
    r2.addMenuItem(Menu(2, "Biryani", "Summer taste", "5"))
    r2.addMenuItem(Menu(3, "Gulab Jamun", "unforgetable taste", "2"))

    r3.addMenuItem(Menu(1, "Pizza - Margareta", " Yummy for students", "5"))
    r3.addMenuItem(Menu(2, "Pizza - Veggie Farm", " Yummy for students", "6"))
    r3.addMenuItem(Menu(3, "Pizza - Mexican Delight", "Big size", "7"))

    restaurants_dict[1] = r1
    restaurants_dict[2] = r2
    restaurants_dict[3] = r3

def createCustomers():
    add1 = Address("2", "Pleinlaan", "etterbeek", "1050")
    cust1 = Customers("Nabila", "123456", "nabila@vub.be", "09876543", add1)
    add2 = Address("9", "Kroonlan", "Ixelles", "1000")
    cust2 = Customers("Aparna", "12321", "aparna.khire@vub.be", "0213749", add2)
    add3 = Address("9", "Louiza", "Ixelles", "1020")
    cust3 = Customers("Shofia", "98789", "shofiana.fitri@vub.be", "0937284", add3)
    add4 = Address("4", "Kroonlan", "Ixelles", "1000")
    cust4 = Customers("Siyu", "09876", "siyu@vub.be", "02786494", add4)
    customers["Nabila"] = cust1
    customers["Aparna"] = cust2
    customers["Shofia"] = cust3
    customers["Siyu"] = cust4

def createOrder():
    o1 = Order("Shofia", "etterbeek", "Ashoka", "30")
    o1.addOrderItem(Menu(2, "Biryani", "unforgetable taste", "5"))
    key9 = o1.getOrderId()
    order[key9] = o1


users = dict()
users['Nabila'] = '123456'
users['Aparna'] = '12321'
users['Shofia'] = '98789'
users['Siyu'] = '09876'