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
        for item in self.item_order_list:
            print(f"商品コード:{item}")
    
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

    # def order_item_list(self):

### メイン処理
def main():
    # マスタ登録
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))
    item_master.append(Item("004","ぶどう",300))
    
    # オーダー登録
    order=Order(item_master)
    order.add_item_order("001",1)
    order.add_item_order("002",5)
    order.add_item_order("003",7)
    
    オーダー表示
    print(order.item_count_list)
    
    sum_sum = 0 
    for item_order,item_count in zip(order.item_order_list,order.item_count_list): 
        o_price = order.get_item_price(item_order)
        o_name = order.get_item_name(item_order)
        o_count = item_count
        o_sum = o_price * o_count
        print(f"[商品名:{o_name}][価格:{o_price}円][個数:{o_count}個]　この商品の合計金額:{o_sum}円")
        sum_sum = sum_sum + o_sum 
    print(f"購入した全ての商品の合計金額は{sum_sum}円です")    

    payment = input("支払う金額を入力して下さい")

    while int(payment) < int(sum_sum):
        payment = input(f"お金が足りません。合計金額の{sum_sum}円以上を入力してください")

    change = int(payment) - int(sum_sum)
    print(f"おつりは{change}円です。ご利用ありがとうございました。")
    

 
    