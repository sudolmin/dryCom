import razorpay

KEY='rzp_test_9YfX33jkhilVYO'
SECRET='eFUUQHk0jCoTNMvKUK7uFcrS'
client = razorpay.Client(auth=(KEY, SECRET))
client.set_app_details({"title" : "Django", "version" : "3.0.5"})

order_amount = 100
order_currency = 'INR'
order_receipt = 'order_rcptid_11'
customer_data = {"Customer Name":'Example', "Email": "example@gmail.com", 
"Contact No.":"9988776655",'Shipping address': 'Area-Bommanahalli, City-Bangalore'}   # OPTIONAL('notes')

# client.order.create({'amount':order_amount, 'currency':order_currency, 
# 	'receipt':order_receipt, 'notes':customer_data})
# for i in range(len(client.order.payments('order_FcpzJ0FakoB1JQ')['items'])):
# 	if client.order.payments('order_FcpzJ0FakoB1JQ')['items'][i]['status']=='captured':
# 		print(client.order.payments('order_FcpzJ0FakoB1JQ')['items'][i]['id'])


print(client.order.fetch('order_Fe4KBAwy3LVB95'))
# print(client.customer.fetch('cust_FcpC6WFmJDWEHM')) 
# print("fetching the customer:\n{'id': 'cust_FcpC6WFmJDWEHM', 'entity': 'customer', 'name': 'example name', 'email': 'example@email.com', 'contact': '9988776655', 'gstin': None, 'notes': [], 'created_at': 1600067912}")

# amount *100
# data-key
# cust-name
# cust-email
# cust-contact
# shipping: put in the notes dict in dict{}
# order-info:
# paid?boolean