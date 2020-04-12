import pymongo

Myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = Myclient["databaselaptop"]

print(Myclient.list_database_names())

#membuat tabel Laptop
Mycollaptop = mydb["Laptop"]

ListLaptop = [
    { "_id": 1, "Merk Laptop": "Asus", "Tahun Keluaran": "2019", "RAM": "8GB", "HDD": "1TB", "Harga": "8.200.000"},
    { "_id": 2, "Merk Laptop": "Acer", "Tahun Keluaran": "2018", "RAM": "8GB", "HDD": "500GB", "Harga": "7.400.000"},
    { "_id": 3, "Merk Laptop": "Lenovo", "Tahun Keluaran": "2018", "RAM": "4GB", "HDD": "500GB", "Harga": "6.200.000"},
    ]

x = Mycollaptop.insert_many(ListLaptop)
print(x.inserted_ids)

#membuat tabel Customers
Mycolcustomers = mydb["Customers"]

ListCustomers = [
    { "Username": 11111, "Password": "pass1", "Nama": "Yaqdhan", "Email": "Yaqdhan@yahoo.com", "Alamat": "Giri Kencana", "no_hp": "081908951625"},
    { "Username": 22222, "Password": "pass2", "Nama": "Farhan", "Email": "Farhan@yahoo.com", "Alamat": "Gotong Royong 2", "no_hp": "081291634282"},
    { "Username": 33333, "Password": "pass3", "Nama": "Machfut", "Email": "Machfut@yahoo.com", "Alamat": "Mabes TNI", "no_hp": "082179149191"}
    ]

y = Mycolcustomers.insert_many(ListCustomers)
print(y.inserted_ids)

#membuat tabel Admin
Mycoladmin = mydb["Admin"]

ListAdmin = [
    {"Username": 111, "Password": "admin111", "Nama": "Ridwan Syah"},
    {"Username": 222, "Password": "admin222", "Nama": "I Gusti Putu"}
    ]

z = Mycoladmin.insert_many(ListAdmin)
print(z.inserted_ids)

for x in Mycollaptop.find():
  print(x)
for y in Mycolcustomers.find():
  print(y)
for z in Mycoladmin.find():
  print(z)
