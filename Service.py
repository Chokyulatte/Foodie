import data


def getRestaurants(cuisine, commune):
    keyCui = cuisine
    keyCom = commune
    #if cuisine is selected in search, fetch the corresponding list
    if keyCui != '-1':
        rListCui = data.restaurantsCuisine.get(keyCui)
    # if commune is selected in search, fetch the corresponding list
    if keyCom != '-1':
        rListCom = data.restaurantsCommune.get(keyCom)
    # if commune is not selected in search, just return the cuisine list
    if keyCom == '-1':
        return rListCui
    #if cuisine is not selected in the search, just return the commune list
    if keyCui == '-1':
        return rListCom
    #if both are selected then make a list of restaurants that are common to both commune and cuisine selected
    rList = []
    for r1 in rListCui:
        for r2 in rListCom:
            if r1.getId() == r2.getId():
                rList.append(r1)
    return rList

def getOrder(orderId):
    o1 = data.order.get(orderId)
    return o1

def saveOrder(customer, address, restaurant, totalPrice):
    o1 = data.Order(customer, address, restaurant, totalPrice)
    data.addOrder(o1)

def saveOrder(o1):
    data.order[o1.getOrderId()] = o1

def getRestaurant(restId):
    restaurant = data.restaurants_dict.get(restId)
    print(restaurant)
    return restaurant
def saveCust(cust):
    data.customer[cust.username] = cust

def getMenu(itemId):
    menu = data.restaurants_dict

def createData():
    data.createRestaurants()
    data.createOrder()
    data.createRestaurantDict()
    data.createOrder()
