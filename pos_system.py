import datetime
import csv
import pandas as pd

LOG_FILE_PATH = "./log/log_{datetime}.log"
log_file_path=LOG_FILE_PATH.format(datetime=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))

def log(txt):
    now=datetime.datetime.now().strftime('%Y年%m月%d日%H時%M分%S秒')
    logStr = '[%s:%s] %s' % ('時間',now,txt)
# ログの出力   
    with open(log_file_path , 'a' ,encoding='utf-8_sig') as f:
        f.write(logStr + '\n')
    print(logStr)

### 商品クラス
# Itemクラス
# （アトリビュート）コード・名前・金額を引数とする
# （メソッド）価格を表示できる

class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
# item_order_listは配列
# 引数はitem_master
# add_item_orderでコードを追加

def item_master_register():
    df = pd.read_csv("product_list.csv",encoding="shift-jis")
    item_master=[]
    # 商品コードの0埋め
    df['商品コード'] = df['商品コード'].astype('str').str.zfill(3)
    for master_item_number,master_item_name,master_item_price in zip (df['商品コード'],df['商品名'],df['価格']):
        item_master.append(Item(master_item_number,master_item_name,master_item_price))
    return item_master,df['商品コード']

class Order:
    # 初期化
    # Orderのクラスをもったインスタンスは
    # 3種のアトリビュートを持つ
    # item_order_list　オーダーされた商品番号が入ってる
    # item_count_list　オーダーされた数が入ってる
    # item_master　　　商品のマスター　引数となっているので、はじめにリストを設定。

    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_count_list=[]
        self.item_master=item_master

    # 注文するための関数
    # シンプルな作り
    # orderインスタンスに対して、
    # 引数で注文番号と数を指定

    def add_item_order(self,item_code,item_count):
        self.item_order_list.append(item_code)
        self.item_count_list.append(item_count)
    
    # orderした番号を１つずつ吐き出す
    def view_item_list(self):
        print("注文リスト")
        for item in self.item_master:
            print(f"商品コード:{item.item_code}　商品名:{item.item_name}　価格:{item.price}円")

    def get_item_data(self,item_code):
        for i in self.item_master :
            if i.item_code == item_code:
                print(i.item_name,i.price)
    
    def get_item_price(self,item_code):
        for i in self.item_master :
            if i.item_code == item_code:
                return i.price
    
    def get_item_name(self,item_code):
        for i in self.item_master :
            if i.item_code == item_code:
                return i.item_name
    
    def do_order(self):

        self.view_item_list()
        order_number = input("注文したい商品の商品コードを入力して下さい")
        while not order_number in list(item_master_register()[1]):
            order_number = input("【エラー！！】注文リストにある商品コードから入力してください")
        
        order_count = input("注文したい個数を入力して下さい")

        while not order_count.isdecimal():
            order_count = input("【エラー！！】数値で入力してください")

        self.add_item_order(order_number,order_count)

        order_repeat_flag = input("追加で購入されますか？（y:する　n:しない）")
        if order_repeat_flag == "y":
            self.do_order()
        elif order_repeat_flag == "n":
            pass
        else :
            order_repeat_flag = input("yかnで入力して下さい（y:する　n:しない）")
    
    def accounting(self):
        all_order_sum_price = 0
        order_text = ""
        for item_order,item_count in zip(self.item_order_list,self.item_count_list): 
            order_price = int(self.get_item_price(item_order))
            order_name = self.get_item_name(item_order)
            order_count = int(item_count)
            order_sum = order_price * order_count
        # print(f"[商品名:{o_name}][価格:{o_price}円][個数:{o_count}個]　この商品の合計金額:{o_sum}円")
            order_text += f"{order_name} {order_count}個 {order_sum}円\n"

            all_order_sum_price = all_order_sum_price + int(order_sum) 

        
        return all_order_sum_price,order_text


    def payment(self):
        all_order_sum_price = self.accounting()[0]
        order_text = self.accounting()[1]
        print(f"購入した全ての商品の合計金額は{all_order_sum_price}円です") 
        payment = input("支払う金額を入力して下さい")

        while not payment.isdecimal():
            payment = input("【エラー！！】数値で入力してください")

        while int(payment) < int(all_order_sum_price):
            payment = input(f"お金が足りません。合計金額の{all_order_sum_price}円以上を入力してください")

        change = int(payment) - int(all_order_sum_price)
        print(f"おつりは{change}円です。ご利用ありがとうございました。")
    
        log("\n領収書\n\n"
            f"{order_text}"
            f"\nお会計：{all_order_sum_price}円\n\n支払金額：{payment}円\nお釣り：{change}円")

    # def order_item_list(self):

### メイン処理
def main():
    # マスタ登録
    item_master_register()

    #初期設定
    order=Order(item_master_register()[0])

    # オーダー登録
    order.do_order()

    # 支払い
    order.accounting()

    #領収書
    order.payment()

if __name__ == "__main__":
    main()