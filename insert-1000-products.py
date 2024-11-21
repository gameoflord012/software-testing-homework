import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="toolshop"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

import random

tool_info_file = "tool-list.txt"

with open(tool_info_file, "r", encoding = "utf-8") as file:
    lines = file.readlines()
    
sql_product_images = []
sql_products = []
    
line_index = 30
for line in lines:
    tool_info  = line.strip().split(";")
    tool_name = tool_info[0]
    tool_image_url = tool_info[1]
    
    product_stock = random.randint(0, 999)
    product_price = round(random.uniform(0, 999), 2)
    
    sql_product_images.append((line_index, "Amazon", tool_image_url, f"testing_{line_index}.jpg"))
    sql_products.append((tool_name, tool_name, product_stock, product_price, random.randint(0, 1), random.randint(0, 1), random.randint(1, 2), random.randint(1, 50), line_index))
    
    line_index += 1

cur.executemany("INSERT INTO product_images (id, source_name, source_url, file_name) VALUES (%s, %s, %s, %s)", sql_product_images)
cur.executemany("INSERT INTO products (name, description, stock, price, is_location_offer, is_rental, brand_id, category_id, product_image_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", sql_products)


conn.commit()
    