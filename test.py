import pos_system as PS
import csv
import pandas as pd

df = pd.read_csv("product_list.csv",encoding="shift-jis")

df['商品コード'] = df['商品コード'].astype('str').str.zfill(3)

print(df)

for i ,m in zip(PS.item_master_register()[1],df['商品コード']):
     if i==m:
          print(1)
     else :
          print(2)

# for num in df['']:
#      print(f'{num:03}')

# item_master=[]

# for master_item_number,master_item_name,master_item_price in zip (df['商品コード'],df['商品名'],df['価格']):
#     item_master.append(PS.Item(master_item_number,master_item_name,master_item_price))

# order=PS.Order(item_master)
# order.view_item_list()

# print(list(PS.item_master_register()[1]))

# test_price = int(input("入力"))

# if test_price in PS.item_master_register()[1]:
#      print("happy")
# else:
#      print("error")