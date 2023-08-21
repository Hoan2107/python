# Tạo danh sách sản phẩm
products = [
    {"id": 1, "name": "Sản phẩm 1", "price": 10},
    {"id": 2, "name": "Sản phẩm 2", "price": 20},
    {"id": 3, "name": "Sản phẩm 3", "price": 30},
]

# Tạo danh sách giỏ hàng
cart = []

# Hiển thị danh sách sản phẩm
print("Danh sách sản phẩm:")
for product in products:
    print(f"{product['id']}. {product['name']} - {product['price']} đ")

# Nhập lựa chọn từ người dùng
choice = input("Nhập số tương ứng với sản phẩm bạn muốn thêm vào giỏ hàng (0 để kết thúc): ")

# Xử lý lựa chọn
while choice != "0":
    product_id = int(choice)
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        cart.append(product)
        print(f"Sản phẩm '{product['name']}' đã được thêm vào giỏ hàng.")
    else:
        print("Không tìm thấy sản phẩm.")
    
    choice = input("Nhập số tương ứng với sản phẩm bạn muốn thêm vào giỏ hàng (0 để kết thúc): ")

# Hiển thị giỏ hàng
print("Giỏ hàng:")
for product in cart:
    print(f"{product['name']} - {product['price']} đ")
