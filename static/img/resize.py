from PIL import Image

# Đường dẫn đến bức ảnh gốc
original_image_path = "javascript-racer.jpg"

# Đường dẫn đến nơi lưu bức ảnh sau khi resize
resized_image_path = "1.jpg"

# Kích thước mới của bức ảnh (ở đây là 300x300)
new_size = (250, 180)

# Mở bức ảnh gốc
original_image = Image.open(original_image_path)

# Resize bức ảnh gốc
resized_image = original_image.resize(new_size)

# Lưu bức ảnh đã resize
resized_image.save(resized_image_path)
# import os
# from PIL import Image

# # Đường dẫn đến thư mục chứa các bức ảnh
# folder_path = "img/"

# # Kích thước mới của bức ảnh (ở đây là 300x300)
# new_size = (250, 180)

# # Lặp qua từng tệp tin trong thư mục
# for filename in os.listdir(folder_path):
#     # Kiểm tra nếu đường dẫn là tệp tin hợp lệ (không phải thư mục)
#     if os.path.isfile(os.path.join(folder_path, filename)):
#         # Đường dẫn đến tệp tin gốc
#         original_image_path = os.path.join(folder_path, filename)
        
#         # Tạo đường dẫn đến tệp tin sau khi resize
#         resized_image_path = os.path.join(folder_path, "resized", filename)
        
#         # Tạo thư mục resized nếu chưa tồn tại
#         os.makedirs(os.path.join(folder_path, "resized"), exist_ok=True)
        
#         # Mở bức ảnh gốc
#         original_image = Image.open(original_image_path)
        
#         # Resize bức ảnh gốc
#         resized_image = original_image.resize(new_size)
        
#         # Lưu bức ảnh đã resize
#         resized_image.save(resized_image_path)
