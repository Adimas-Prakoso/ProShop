import json
import re
from datetime import datetime
import pytz
import random
import string
from rich.logging import RichHandler
import logging
from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import requests
import smtplib
import platform
import shutil
gmail_app_pass = "oztkzjrsjmwmvmgc"

# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()]
)

def register_user(email, password, username):
    try:
        # Memeriksa apakah email kosong
        if not email:
            return {'status': False, 'message': "Email tidak boleh kosong"}

        # Memeriksa apakah password kosong
        if not password:
            return {'status': False, 'message': "Password tidak boleh kosong"}

        # Memeriksa apakah username kosong
        if not username:
            return {'status': False, 'message': "Username tidak boleh kosong"}
        
        # Memeriksa apakah username mengandung karakter khusus
        # Bagian ini memeriksa apakah username yang dimasukkan mengandung karakter khusus. Jika mengandung karakter khusus, fungsi akan mengembalikan pesan kesalahan.
        if any(char in string.punctuation for char in username):
            return {'status': False, 'message': "Username tidak boleh mengandung karakter khusus"}
        
        # Memeriksa panjang username
        # Bagian ini memeriksa panjang username yang dimasukkan. Jika panjangnya kurang dari 6 karakter, fungsi akan mengembalikan pesan kesalahan.
        if len(username) < 6:
            return {'status': False, 'message': "Username harus memiliki minimal 6 karakter"}
        
        # Memeriksa apakah email yang dimasukkan adalah alamat email yang valid
        # Bagian ini menggunakan regular expression untuk memeriksa apakah email yang dimasukkan adalah alamat email yang valid. Jika email tidak valid, fungsi akan mengembalikan pesan kesalahan.
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return {'status': False, 'message': "Alamat email yang dimasukkan bukan alamat email!"}

        # Memeriksa apakah username mengandung spasi
        # Bagian ini memeriksa apakah username yang dimasukkan mengandung spasi. Jika username mengandung spasi, fungsi akan mengembalikan pesan kesalahan.
        if ' ' in username:
            return {'status': False, 'message': "Username tidak boleh mengandung spasi"}
        
        # Memeriksa panjang kata sandi
        # Bagian ini memeriksa panjang kata sandi yang dimasukkan. Jika panjangnya kurang dari atau sama dengan 6 karakter, fungsi akan mengembalikan pesan kesalahan.
        if len(password) <= 6:
            return {'status': False, 'message': "Password harus lebih dari 6 karakter"}

        # Memeriksa kekuatan kata sandi
        # Bagian ini memeriksa kekuatan kata sandi yang dimasukkan. Kata sandi harus mengandung minimal 1 huruf besar, 1 angka, dan 1 simbol. Jika tidak memenuhi syarat, fungsi akan mengembalikan pesan kesalahan.
        if not any(char.isupper() for char in password) or not any(char.isdigit() for char in password) or not any(char.isalnum() for char in password):
            return {'status': False, 'message': "Password harus mengandung minimal 1 huruf besar, 1 angka, dan 1 simbol"}

        # Membaca data pengguna yang ada dari file
        # Bagian ini membaca data pengguna yang ada dari file JSON. Jika file tidak ada, maka akan dibuat file baru.
        with open('./database/user/users.json', 'r') as file:
            users = json.load(file)

        def generate_hash(length):
            characters = string.ascii_letters + string.digits
            while True:
                hash_id = ''.join(random.choice(characters) for _ in range(length))
                # Memeriksa apakah hash_id sudah ada di database
                # Bagian ini memeriksa apakah hash_id yang dihasilkan sudah ada di database pengguna.
                hash_exists = any(user['hash_id'] == hash_id for user in users)
                if not hash_exists:
                    break
            return hash_id

        # Memeriksa apakah email atau username sudah terdaftar
        # Bagian ini memeriksa apakah email atau username yang dimasukkan sudah terdaftar dalam sistem. Jika sudah terdaftar, fungsi akan mengembalikan pesan kesalahan.
        if any(user['email'] == email for user in users):
            return {'status': False, 'message': "Email sudah digunakan"}
        if any(user['username'] == username for user in users):
            return {'status': False, 'message': "Username sudah digunakan"}
                
        # Membuat nama pengguna random
        # Bagian ini membuat nama pengguna dari username yang dimasukkan.
        def generate_name():
            response = requests.get("https://api.namefake.com")
            data = response.json()
            name = data["name"]
            return name

        # Menggunakan fungsi generate_name untuk membuat nama pengguna
        names = generate_name()

        # Membuat objek pengguna dengan informasi yang diberikan
        # Bagian ini membuat objek pengguna baru dengan informasi yang diberikan oleh pengguna.
        user_id = len(users) + 1
        hash_id = generate_hash(64)
        user = {
            'user_id': user_id,
            'hash_id': hash_id,
            'email': email,
            'password': password,
            'username': username,
            'created_at': datetime.now(pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
            'money': 0,
            'profile': {
                'name': names,
                'profile_picture': "./views/res/images/user.jpg",
                'bio': "Hello there 👋",
                'address': "",
                'phone': "",
                'gender': "",
                'birthdate': ""
            },
            'settings': {
                'theme': "light",
                'language': "id",
                'notifications': True,
                'currency': "IDR"
            },
            'history': [],
            'charts': [],
            'order': []
        }

        # Menambahkan pengguna baru ke dalam database
        # Bagian ini menambahkan pengguna baru ke dalam database pengguna.
        users.append(user)

        # Menyimpan data pengguna yang diperbarui ke dalam file
        # Bagian ini menyimpan data pengguna yang diperbarui ke dalam file JSON.
        with open('./database/user/users.json', 'w') as file:
            json.dump(users, file, indent=4)

        # Menampilkan pesan sukses
        # Bagian ini menampilkan pesan sukses jika pengguna berhasil terdaftar.
        message = f"Pengguna berhasil terdaftar dengan username {username} dan email {email}"
        return {'status': True, 'message': message}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def generate_verification_code():
    # Menghasilkan kode verifikasi acak
    # Bagian ini menghasilkan kode verifikasi acak dengan panjang 6 karakter.
    verification_code = ''.join(random.choices(string.digits, k=6))
    return verification_code

def login_user(email, password):
    try:
        # Memeriksa apakah email kosong
        if not email:
            return {'status': False, 'message': "Email tidak boleh kosong"}

        # Memeriksa apakah password kosong
        if not password:
            return {'status': False, 'message': "Password tidak boleh kosong"}
        
        # Membaca data pengguna yang ada dari file
        # Bagian ini membaca data pengguna yang ada dari file JSON. Jika file tidak ada, maka akan dibuat file baru.
        with open('./database/user/users.json', 'r') as file:
            users = json.load(file)

        # Memeriksa apakah email terdaftar
        # Bagian ini memeriksa apakah email yang dimasukkan terdaftar dalam sistem. Jika tidak terdaftar, fungsi akan mengembalikan pesan kesalahan.
        email_registered = any(user['email'] == email for user in users)
        if not email_registered:
            return {'status': False, 'message': "Email tidak terdaftar"}

        # Memeriksa apakah email dan password sesuai
        # Bagian ini memeriksa apakah email dan password yang dimasukkan sesuai dengan data pengguna yang ada. Jika sesuai, pengguna akan berhasil masuk ke dalam sistem.
        for user in users:
            if user['email'] == email and user['password'] == password:
                # Menyimpan data login ke dalam file
                # Bagian ini menyimpan data login ke dalam file JSON.
                login_data = {'email': email, 'password': password}
                with open('./.logger', 'w') as file:
                    json.dump(login_data, file, indent=4)
                return {'status': True, 'message': f"Login berhasil dengan username {user['username']}", 'email': email, 'password': password}

        # Menampilkan pesan kesalahan jika email terdaftar tetapi password tidak sesuai
        # Bagian ini menampilkan pesan kesalahan jika password yang dimasukkan tidak sesuai dengan data pengguna yang ada.
        return {'status': False, 'message': "Email terdaftar tetapi password salah"}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def send_verification_code(email, verification_code, pesan):
    try:
        # Mendapatkan alamat IP pengguna
        # Bagian ini mendapatkan alamat IP pengguna menggunakan layanan dari ipinfo.io.
        ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
        cek_ip = requests.get(f'http://ip-api.com/json/{ip}').json()
        loc_ip = f"{cek_ip['city']}, {cek_ip['regionName']}, {cek_ip['country']}"
        # Configure SMTP server
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('adimas.my.id@gmail.com', gmail_app_pass)

        # Compose email message
        subject = 'ProShop Verification Code'
        body = f'''
        <!DOCTYPE html>
        <html lang="id">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Proshop Verification Email</title>
            <style>
              /* Global Styles */
              * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
              }}

              body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
              }}

              /* Container Styles */
              .container {{
            max-width: 600px;
            margin: 40px auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
              }}

              /* Header Styles */
              h1 {{
            color: #4285f4;
            text-align: center;
            margin-bottom: 30px;
            margin-top: 30px;
            font-size: 40px;
              }}

              h2 {{
            margin-top: 0;
              }}

              /* Content Styles */
              .content {{
            margin-bottom: 20px;
              }}

              .device-info {{
            margin-bottom: 20px;
              }}

              .device-info p {{
            margin-bottom: 10px;
              }}

              .code {{
            text-align: center;
            font-size: 60px;
            font-weight: bold;
            margin-bottom: 20px;
            margin-top: 20px;
            color: black; /* Added color property */
              }}

              .info {{
            text-align: center;
            margin-bottom: 20px;
            font-size: 14px;
            color: #666;
              }}

              /* Footer Styles */
              .footer {{
            text-align: center;
            font-size: 12px;
            color: #777;
            margin-top: 40px;
              }}
            </style>
          </head>
          <body>
            <div class="container">
            <h1>Pro Shop</h1>
            <h2>Verifikasi email Anda</h2>
            <div class="content">
            <br />
            <p>{pesan}</p>
            <br />
            <p>Informasi Perangkat:</p>
            <br />
            <br />
            <div class="device-info">
              <p>Nama Perangkat: <span style="color: red;">{platform.node()}</span></p>
              <p>Sistem: <span style="color: red;">{platform.platform()}</span></p>
              <p>IP: <span style="color: red;">{ip}</span></p>
              <p>Lokasi: <span style="color: red;">{loc_ip}</span></p>
            </div>
            <br />
            <br />
            <p>Gunakan kode ini untuk verifikasi email Anda:</p>
            <br />
            <div class="code">{verification_code}</div>
            <p class="info">Masa berlaku kode ini akan berakhir dalam 1 jam.</p>
            <p class="info">
              Jika Anda tidak mengenali {email}, Anda dapat mengabaikan email ini
              dengan aman.
            </p>
              </div>
              <p class="footer">Copyright 2023 Pro Shop. All rights reserved.</p>
            </div>
          </body>
        </html>
        '''
        message = f'Subject: {subject}\nMIME-Version: 1.0\nContent-type: text/html\n\n{body}'

        # Send email
        server.sendmail('adimas.my.id@gmail.com', email, message)
        server.quit()

        return {'status': True, 'message': 'Kode verifikasi telah dikirim ke email Anda. Silakan cek email Anda untuk melanjutkan proses verifikasi.'}
    except Exception as e:
        logging.error(f"Error occurred while sending verification code: {str(e)}")
        return {'status': False, 'message': 'Failed to send verification code'}

def login_admin(username, password):
    try:
        # Memeriksa apakah username kosong
        if not username:
            return {'status': False, 'message': "Username tidak boleh kosong"}

        # Memeriksa apakah password kosong
        if not password:
            return {'status': False, 'message': "Password tidak boleh kosong"}
        
        # Membaca data admin yang ada dari file
        # Bagian ini membaca data admin yang ada dari file JSON. Jika file tidak ada, maka akan dibuat file baru.
        with open('./database/admin/admins.json', 'r') as file:
            admins = json.load(file)

        # Memeriksa apakah username terdaftar
        # Bagian ini memeriksa apakah username yang dimasukkan terdaftar dalam sistem. Jika tidak terdaftar, fungsi akan mengembalikan pesan kesalahan.
        username_registered = False
        for admin in admins:
            if admin['username'] == username:
                username_registered = True
                break
        if not username_registered:
            return {'status': False, 'message': "Username tidak terdaftar"}

        # Memeriksa apakah username dan password sesuai
        # Bagian ini memeriksa apakah username dan password yang dimasukkan sesuai dengan data admin yang ada. Jika sesuai, admin akan berhasil masuk ke dalam sistem.
        for admin in admins:
            if admin['username'] == username and admin['password'] == password:
                return {'status': True, 'message': "Login berhasil", 'username': username, 'password': password}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def get_user_data(email, password):
    try:
        # Membaca data pengguna yang ada dari file
        # Bagian ini membaca data pengguna yang ada dari file JSON. Jika file tidak ada, maka akan dibuat file baru.
        with open('./database/user/users.json', 'r') as file:
            users = json.load(file)

        # Memeriksa apakah email dan password sesuai
        # Bagian ini memeriksa apakah email dan password yang dimasukkan sesuai dengan data pengguna yang ada. Jika sesuai, pengguna akan berhasil masuk ke dalam sistem.
        for user in users:
            if user['email'] == email and user['password'] == password:
                return user
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def change_profile(email, password, name, bio, address, phone, gender, birthdate):
    try:
        # Membaca data pengguna yang ada dari file
        # Bagian ini membaca data pengguna yang ada dari file JSON. Jika file tidak ada, maka akan dibuat file baru.
        with open('./database/user/users.json', 'r') as file:
            users = json.load(file)

        # Memeriksa apakah email dan password sesuai
        # Bagian ini memeriksa apakah email dan password yang dimasukkan sesuai dengan data pengguna yang ada. Jika sesuai, pengguna akan berhasil masuk ke dalam sistem.
        for user in users:
            if user['email'] == email and user['password'] == password:
                # Mengubah data profil pengguna
                # Bagian ini mengubah data profil pengguna sesuai dengan data yang diberikan oleh pengguna.
                user['profile']['name'] = name
                user['profile']['bio'] = bio
                user['profile']['address'] = address
                user['profile']['phone'] = phone
                user['profile']['gender'] = gender
                user['profile']['birthdate'] = birthdate

        # Menyimpan perubahan ke file
        # Bagian ini menyimpan perubahan data pengguna ke file JSON.
        with open('./database/user/users.json', 'w') as file:
            json.dump(users, file, indent=4)

        return {'status': True, 'message': 'Data profil berhasil diubah'}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {'status': False, 'message': 'Gagal mengubah data profil'}

def change_email(email, password, new_email):
    try:
        # Read existing user data from file
        with open('./database/user/users.json', 'r') as file:
            users = json.load(file)

        # Check if email and password match
        for user in users:
            if user['email'] == email and user['password'] == password:
                # Update user's email
                user['email'] = new_email

        # Save changes to file
        with open('./database/user/users.json', 'w') as file:
            json.dump(users, file, indent=4)

        return {'status': True, 'message': 'Email successfully changed'}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {'status': False, 'message': 'Failed to change email'}

def change_password(email, password, new_password):
    try:
        # Read existing user data from file
        with open('./database/user/users.json', 'r') as file:
            users = json.load(file)

        # Check if email and password match
        for user in users:
            if user['email'] == email and user['password'] == password:
                # Update user's password
                user['password'] = new_password

        # Save changes to file
        with open('./database/user/users.json', 'w') as file:
            json.dump(users, file, indent=4)

        return {'status': True, 'message': 'Password successfully changed'}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {'status': False, 'message': 'Failed to change password'}
    
def change_settings(email, password, theme, notifications, currency):
    try:
        # Read existing user data from file
        with open('./database/user/users.json', 'r') as file:
            users = json.load(file)

        # Check if email and password match
        for user in users:
            if user['email'] == email and user['password'] == password:
                # Update user's settings
                user['settings']['theme'] = theme
                user['settings']['notifications'] = notifications
                user['settings']['currency'] = currency

        # Save changes to file
        with open('./database/user/users.json', 'w') as file:
            json.dump(users, file, indent=4)

        return {'status': True, 'message': 'Settings successfully changed'}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {'status': False, 'message': 'Failed to change settings'}
    
def get_produc_by_id(product_id):
    try:
        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Mengambil informasi produk berdasarkan id
        for product in products:
            if product['product_id'] == product_id:
                return product
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

# Generate random ID based on the number of data in "./database/admin/item/items.json"
def generate_random_id():
    try:
        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Get the number of existing products
        num_products = len(products) + 1

        # Generate random ID
        random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + str(num_products)

        return random_id
    except Exception as e:
        logging.error(f"Error occurred while generating random ID: {str(e)}")

def discount_price(price, discount):
    try:
        # Calculate discounted price
        discounted_price = price - (price * discount / 100)
        return int(discounted_price) if discounted_price.is_integer() else discounted_price
    except Exception as e:
        logging.error(f"Error occurred while calculating discounted price: {str(e)}")

def get_item_by_category(produc_list, category):
    try:
        # Filter products by category
        filtered_products = [product for product in produc_list if product['category'] == category]

        return filtered_products
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def get_item_by_name(produc_list, name):
    try:
        # Search for the item by name (contains, not exact match)
        found_items = []
        for product in produc_list:
            if name.lower() in product['name'].lower():
                found_items.append(product)

        return found_items

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def list_item_by_higer_discount():
    try:
        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Filter products by discount
        discounted_products = [product for product in products if product['discount'] > 0]

        # Sort products by discount in descending order
        sorted_products = sorted(discounted_products, key=lambda x: x['discount'], reverse=True)

        return sorted_products
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def list_item_by_lower_stock():
    try:
        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Sort products by stock in ascending order
        sorted_products = sorted(products, key=lambda x: x['stock'])

        return sorted_products
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def list_item_by_higher_price(produc_list):
    try:
        # Sort products by price in descending order
        sorted_products = sorted(produc_list, key=lambda x: x['price'], reverse=True)

        return sorted_products
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def list_item_by_lower_price(produc_list):
    try:
        # Sort products by price in ascending order
        sorted_products = sorted(produc_list, key=lambda x: x['price'])

        return sorted_products
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def get_last_10_items():
    try:
        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Sort products by ID (assuming ID is unique and represents order)
        sorted_products = sorted(products, key=lambda product: product['id'], reverse=True)

        # Get the last 10 items
        last_10_items = sorted_products[:10]

        return last_10_items

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def add_item(image, name, stock, description, price, discount, category, variant):
    try:
        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Amount of products +1
        product_id = len(products) + 1

        # Create new product object
        new_product = {
            "id": product_id,
            "image_path": image,
            "name": name,
            "stock": stock,
            "description": description,
            "price": price,
            "discount": discount,
            "category": category,
            "variation": variant,
            "comments": []
        }

        # Add new product to the list
        products.append(new_product)

        # Save changes to file
        with open('./database/admin/item/items.json', 'w') as file:
            json.dump(products, file, indent=4)

        return {'status': True, 'message': 'Item added successfully'}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {'status': False, 'message': 'Failed to add item'}
    
def delete_item(product_id):
    try:
        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Find the product by ID
        for product in products:
            if product['id'] == product_id:
                # Remove the product from the list
                products.remove(product)

        # Save changes to file
        with open('./database/admin/item/items.json', 'w') as file:
            json.dump(products, file, indent=4)

        return {'status': True, 'message': 'Item deleted successfully'}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {'status': False, 'message': 'Failed to delete item'}
    
def add_comment(product_id, user_id, ratings, comment):
    try:
        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Find the product by ID
        for product in products:
            if product['id'] == product_id:
                # Create new comment object
                new_comment = {
                    "user_id": user_id,
                    "ratings": ratings,
                    "comment": comment,
                    "created_at": datetime.now(pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S')
                }

                # Add new comment to the list
                product['comments'].append(new_comment)

        # Save changes to file
        with open('./database/admin/item/items.json', 'w') as file:
            json.dump(products, file, indent=4)

        return {'status': True, 'message': 'Comment added successfully'}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {'status': False, 'message': 'Failed to add comment'}
    
def edit_item(product_id, image="", name="", stock=None, description="", price=None, discount=None, category="", variant=[]):
    try:
        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Find the product by ID
        for product in products:
            if product['id'] == product_id:
                # Update product information
                product['image_path'] = image or product['image_path']
                product['name'] = name or product['name']
                product['stock'] = stock or product['stock']
                product['description'] = description or product['description']
                product['price'] = price or product['price']
                product['discount'] = discount or product['discount']
                product['category'] = category or product['category']
                product['variation'] = variant or product['variation']

        # Save changes to file
        with open('./database/admin/item/items.json', 'w') as file:
            json.dump(products, file, indent=4)

        return {'status': True, 'message': 'Item edited successfully'}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {'status': False, 'message': 'Failed to edit item'}
    
def get_item_from_price_range(product_list, min_price, max_price):
    try:
        # Filter products by price range
        filtered_products = [product for product in product_list if min_price <= product['price'] <= max_price]

        return filtered_products
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def get_20_random_items():
    try:
        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Get 20 random items
        random_items = random.sample(products, 20)

        return random_items
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def get_8_raandom_discount_items():
    try:
        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Filter products by discount
        discounted_products = [product for product in products if product['discount'] > 0]

        # Get 8 random items with discount
        random_discount_items = random.sample(discounted_products, 8)

        return random_discount_items
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def get_all_item_in_random_order():
    try:
        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Shuffle products
        random.shuffle(products)

        return products
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def add_to_cart(product_id):
    try:
        # Read existing user data from file
        with open('./database/user/users.json', 'r') as file:
            users = json.load(file)

        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Get the current user's email and password
        with open('./.logger', 'r') as file:
            login_data = json.load(file)
            email = login_data['email']
            password = login_data['password']

        # Get the current user's data
        for user in users:
            if user['email'] == email and user['password'] == password:
                # Check if the product is already in the user's cart
                for product in user['charts']:
                    if product['id'] == product_id:
                        return {'status': False, 'message': 'Item already in cart'}

                # Find the product by ID
                for product in products:
                    if product['id'] == product_id:
                        # Add the product to the user's cart
                        user['charts'].append(product)

        # Save changes to file
        with open('./database/user/users.json', 'w') as file:
            json.dump(users, file, indent=4)

        return {'status': True, 'message': 'Item added to cart successfully'}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {'status': False, 'message': 'Failed to add item to cart'}
    
def add_to_order(product_id, image, product_name, produc_desc, price, quantity):
    try:
        # Read existing user data from file
        with open('./database/user/users.json', 'r') as file:
            users = json.load(file)

        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Get the current user's email and password
        with open('./.logger', 'r') as file:
            login_data = json.load(file)
            email = login_data['email']
            password = login_data['password']

        # Get the current user's data
        for user in users:
            if user['email'] == email and user['password'] == password:
                # Find the product by ID
                for product in products:
                    if product['id'] == product_id:
                        # Add the product to the user's order
                        add_order = {
                            'product_id': product_id,
                            'image_path': image,
                            'name': product_name,
                            'description': produc_desc,
                            'price': price,
                            'quantity': quantity,
                        }
                        user['order'].append(add_order)

        # Save changes to file
        with open('./database/user/users.json', 'w') as file:
            json.dump(users, file, indent=4)

        return {'status': True, 'message': 'Item added to order successfully'}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {'status': False, 'message': 'Failed to add item to order'}

def show_order_item(user_id):
    try:
        # Read existing user data from file
        with open('./database/user/users.json', 'r') as file:
            users = json.load(file)

        # Get the user's order
        for user in users:
            if user['user_id'] == user_id:
                if 'order' in user and user['order']:
                    return user['order']
                else:
                    return []
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
    
def deduct_money(user_id, amount):
    try:
        # Read existing user data from file
        with open('./database/user/users.json', 'r') as file:
            users = json.load(file)

        # Deduct money from the user's account
        for user in users:
            if user['user_id'] == user_id:
                user['money'] -= amount

        # Save changes to file
        with open('./database/user/users.json', 'w') as file:
            json.dump(users, file, indent=4)

        return {'status': True, 'message': 'Money deducted successfully'}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {'status': False, 'message': 'Failed to deduct money'}
    
def change_user_image(user_id, image_path):
    try:
        # Read existing user data from file
        with open('./database/user/users.json', 'r') as file:
            users = json.load(file)

        # Change user's profile picture
        for user in users:
            if user['user_id'] == user_id:
                user['profile']['profile_picture'] = image_path

        # Save changes to file
        with open('./database/user/users.json', 'w') as file:
            json.dump(users, file, indent=4)

        return {'status': True, 'message': 'Profile picture changed successfully'}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {'status': False, 'message': 'Failed to change profile picture'}
    
def copy_and_rename_image(file_path, user_id):
    # Copy and rename image file
    file_extension = file_path.split('.')[-1]
    new_file_path = f"./database/user/img/{user_id}.{file_extension}"
    shutil.copy(file_path, new_file_path)

    return new_file_path

def get_user_chart(user_id):
    try:
        # Read existing user data from file
        with open('./database/user/users.json', 'r') as file:
            users = json.load(file)

        # Get the user's cart
        for user in users:
            if user['user_id'] == user_id:
                if 'charts' in user and user['charts']:
                    return user['charts']
                else:
                    return []
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

def remove_from_cart(user_id, product_id):
    try:
        # Read existing user data from file
        with open('./database/user/users.json', 'r') as file:
            users = json.load(file)

        # Remove the product from the user's cart
        for user in users:
            if user['user_id'] == user_id:
                for product in user['charts']:
                    if product['id'] == product_id:
                        user['charts'].remove(product)

        # Save changes to file
        with open('./database/user/users.json', 'w') as file:
            json.dump(users, file, indent=4)

        return {'status': True, 'message': 'Item removed from cart successfully'}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {'status': False, 'message': 'Failed to remove item from cart'}
    
