# from loader import db
import db_api


# # print(db.select_all_users())
# print(db.select_user_info(id=380821547))

db = db_api.Database('db_api/database/shop_database.db')

db.add_item(id=1, name='Тыква', count=10, photo_path=r'db_api/database/product_photo/pumpkin.jpeg')
db.add_item(id=2, name='Помидор', count=45, photo_path=r'db_api/database/product_photo/tomat.jpg')
db.add_item(id=3, name='Огурец', count=30, photo_path=r'db_api/database/product_photo/cucumber.jpg')


print(db.select_all_items())

print(db.get_items_count())


