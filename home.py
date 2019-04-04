from flask import Flask,render_template, redirect, url_for, request,flash
from model.Address import Address
from model.Customers import Customers
from model.Order import Order
from model.Menu import Menu
import Service
import data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretKey';
listCustomers = []

@app.route('/')
def index():
    Service.createData()
    return render_template('home.html')

@app.route('/register', methods=['GET','POST'])
def process_registration():
    error = None
    if request.method == 'GET/POST' :
        username = request.form("username"),
        email = request.form("email"),
        password = request.form("password"),
        phone = request.form("phone"),
        bn = request.form("bn"),
        street = request.form("street"),
        area = request.form("area"),
        pin = request.form("pin"),
        #addObj = Address(bn,street,area,pin)
        #custObj = Customers(username, email, password, phone, addObj)
        #data.customers[custObj.getUsername()] = custObj
        user = data.customers(username = username, email = email, password = password, phone = phone, bn = bn, street = street, area = area, pin = pin )
        listCustomers.append(user)
        custDB = Service.saveCust()
        if user == custDB:
            flash('You are successfully registered')
        else :
            flash('Error occured')
        return redirect(url_for('/home'))
    return render_template('registration.html', error = error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        data.users.items()
        user_key_list = data.users.keys()  # create list of usernames from dictionary
        for username in user_key_list:  # check if username is in list of keys from users dict.
            if request.form['username'].lower() != username.lower() or request.form['password'] != data.users.get(username):
                error = 'Invalid Credentials. Please try again.'
            else:
                return redirect('/home')
    return render_template('login.html', error=error)


@app.route("/address", methods=['GET', 'POST'])
def selAddress():
    val2=request.form.get('hname')
    print(val2)
    orderId = request.args['orderId']
    o1 = Service.getOrder(orderId)

    if request.method == 'POST':
        if request.form.get('addresses') == '1': #default address
            print('default address selected')
            cust = o1.getCustomer();
            o1.setAddress(cust.getAddress())
        if request.form.get('addresses') == '2': #new address
            bn = request.form.get('bn')
            street = request.form.get('street')
            area = request.form.get('area')
            pin = request.form.get('pin')
            address = Address(bn, street, area, pin)
            o1.setAddress(address)
            # add this address to the session object having the order object
        redirect(url_for('orderReceipt', orderId=orderId))

    # if request.form["addresses"] == '1': to get the address obj from the customer obj from the session
    if request.method == 'GET':
        return render_template('addressPreference.html')

@app.route("/receipt", methods=['GET'])
def orderReceipt():
    if request.method == 'GET':
        orderId = request.args['orderId'] #gets the id from the url passed in the home page
        o1 = Service.getOrder(orderId)
        return render_template('receipt.html', order=o1)


#dummy method created by Appy, use the below line to get the restaurant id for order page, from the previous page
@app.route("/orderold", methods=['GET', 'POST'])
def placeOrder():
    if request.method == 'GET':
        selRest = request.args['selRest'] #gets the id from the url passed in the home page
        #find the menu based on restaurant number= selRest
        return render_template('order.html')
    if request.method == 'POST':
        return redirect('/address')


@app.route('/order', methods=['GET', 'POST'])
def selectOrder():
    Service.createData()
    if request.method == 'GET':
        selRest = request.args['selRest']
        restaurant = Service.getRestaurant(int(selRest))
        resultMenus=restaurant.getMenu()
        if request.method == 'POST' :
            if request.form['action'] == 'Total':
                cost_item = 0
                qwtList = ['1','2','3','4','5']
                qwt = int(request.form.get('quantity'))
                for qwt in qwtList:
                    price_item = Menu.getPrice(qwt)
                    cost_item = qwt * price_item
                return  cost_item
            checkedOrder = request.form.getlist('order')  # use getlist just in case multichecked
            orders = Service.getOrder(checkedOrder)
            total = Menu.getPrice(orders)
        return render_template('order.html',result=resultMenus)
    if request.method == 'POST':
        o1 = Order(Customers('username', 'email', 'password', 1234, None),None,None,100)
        Service.saveOrder(o1)
        return redirect(url_for('selAddress', orderId=o1.getOrderId()))


@app.route('/home', methods=['GET', 'POST'])
def selectRestaurant():
    Service.createData() # to remove this
    communeList = ['Evere','Etterbeek', 'Elsene', 'Auderghem', 'Watermael']
    cuisineList = ['Indian', 'Italian', 'Chinese']

    if request.method == 'POST':
        if request.form['action'] == 'Submit': #if we are only searching
            selcuisine = request.form['cuisine']
            selcommune = request.form['commune']
            result = Service.getRestaurants(selcuisine, selcommune)
            return render_template("selectRestaurant.html", result=result, commune=communeList, cuisine=cuisineList, selcom=selcommune, selcui=selcuisine)
        elif request.form['action'] == 'Next': #if we have selected a restaurant from the list
            selRest = request.form['restaurant'] #take the id of the retaurant selected
            return redirect(url_for('selectOrder',selRest=selRest)) #send this id to the next page ie order page

    return render_template("selectRestaurant.html", commune=communeList, cuisine=cuisineList)


if __name__ == '__main__':
    app.run(debug=True)
