import shop as sh
import status as st
import opening as op
import member_edit as me


def next_operation():
    input("▼")




mode = "main_menu"
name = op.main()


"""
yes_no = ""
while yes_no != "y":
    name = str(input("主人公の名前を入力してください。>>>"))
    print("主人公の名前は「"+ name + "」でよろしいですか？")
    yes_no = str(input("ゲームをはじめる場合は「y」を入力してください。>>>"))
    if yes_no == "y":
        print("ゲームをはじめます。")
        sh.next_operation()
    else:
        print("再度、名前を入力してください。")
"""

money = 1000
dungeon_list = ["山の遺跡", "塔の遺跡", "森の遺跡", "戻る"]
On = True

inventory = [
             {"name":"燃料", "type":0, "sort":0, "price":100, "sell_price":20, "possession_num":0, "fight_on_tank":False, "fight_on_land":False, "use_in_status":True, "use_only_dungeon":False}, 
             {"name":"弾薬", "type":0, "sort":1, "price":100, "sell_price":20, "possession_num":0, "fight_on_tank":False, "fight_on_land":False, "use_in_status":True, "use_only_dungeon":False},
             {"name":"リペア", "type":0, "sort":2, "price":20, "sell_price":10, "possession_num":0, "fight_on_tank":True, "fight_on_land":False, "use_in_status":True, "use_only_dungeon":False},
             {"name":"回復薬", "type":0, "sort":3, "price":30, "sell_price":20, "possession_num":0, "fight_on_tank":False, "fight_on_land":True, "use_in_status":True, "use_only_dungeon":False},
             {"name":"高級回復薬", "type":0, "sort":4, "price":100, "sell_price":20, "possession_num":0, "fight_on_tank":False, "fight_on_land":True, "use_in_status":True, "use_only_dungeon":False},
             {"name":"回復スプレー", "type":0, "sort":5, "price":100, "sell_price":20, "possession_num":0, "fight_on_tank":False, "fight_on_land":True, "use_in_status":True, "use_only_dungeon":False},
             {"name":"ロケット弾", "type":0, "sort":6, "price":300, "sell_price":100, "possession_num":0, "fight_on_tank":True, "fight_on_land":True, "use_in_status":False, "use_only_dungeon":False},
             {"name":"手りゅう弾", "type":0, "sort":7, "price":350, "sell_price":100, "possession_num":0, "fight_on_tank":True, "fight_on_land":True, "use_in_status":False, "use_only_dungeon":False},
             {"name":"煙幕", "type":0, "sort":8, "price":100, "sell_price":20, "possession_num":0, "fight_on_tank":True, "fight_on_land":True, "use_in_status":False, "use_only_dungeon":False},
             {"name":"とぶやつ", "type":0, "sort":9, "price":1000, "sell_price":200, "possession_num":0, "fight_on_tank":False, "fight_on_land":False, "use_in_status":False, "use_only_dungeon":True},
             {"name":"金のかけら", "type":0, "sort":10, "price":-1, "sell_price":500, "possession_num":0, "fight_on_tank":False, "fight_on_land":False, "use_in_status":False, "use_only_dungeon":False},
             {"name":"銀の板", "type":0, "sort":11, "price":-1, "sell_price":250, "possession_num":0, "fight_on_tank":False, "fight_on_land":False, "use_in_status":False, "use_only_dungeon":False},
             {"name":"パール", "type":0, "sort":12, "price":-1, "sell_price":100, "possession_num":0, "fight_on_tank":False, "fight_on_land":False, "use_in_status":False, "use_only_dungeon":False},
             {"name":"赤の珠", "type":0, "sort":13, "price":-1, "sell_price":-1, "possession_num":0, "fight_on_tank":False, "fight_on_land":False, "use_in_status":False, "use_only_dungeon":False},
             {"name":"黒の珠", "type":0, "sort":14, "price":-1, "sell_price":-1, "possession_num":0, "fight_on_tank":False, "fight_on_land":False, "use_in_status":False, "use_only_dungeon":False},
             {"name":"青の珠", "type":0, "sort":15, "price":-1, "sell_price":-1, "possession_num":0, "fight_on_tank":False, "fight_on_land":False, "use_in_status":False, "use_only_dungeon":False},
            ]

digger = {"now_HP":500, "max_HP":500, "now_gas":800, "max_gas":800}
       
equip = []         

member = [
          {"name":name, "now_HP":120, "max_HP":120, "skill":[], "ATK1":{"name":"拳銃","ATK":[12, 30], "HIT":100, "SPD":12}}
         ]

member_all = [
              {"name":name, "sort":0, "now_HP":120, "max_HP":120, "skill":[], "ATK":{"name":"拳銃","ATK":[12, 30], "HIT":100, "SPD":12}, "unlock":True}, 
              {"name":"ラセツ", "sort":1 ,"now_HP":152, "max_HP":152, "skill":[], "ATK":{"name":"カナタ", "ATK":[18, 25], "HIT":100, "SPD":12}, "unlock":False},
              {"name":"ヤシャ", "sort":2 ,"now_HP":108, "max_HP":108, "skill":[], "ATK":{"name":"槍", "ATK":[20, 25], "HIT":90, "SPD":12}, "unlock":False},
              {"name":"ゴンダ", "sort":5 ,"now_HP":100, "max_HP":100, "skill":[], "ATK":{"name":"ロケット砲", "ATK":[40, 55], "HIT":70, "SPD":4}, "unlock":False}, 
              {"name":"タケミ", "sort":12 ,"now_HP":98, "max_HP":98, "skill":[], "ATK":{"name":"スパナ", "ATK":[8, 10], "HIT":100, "SPD":2}, "unlock":False},
              {"name":"ウタノ", "sort":15 ,"now_HP":110, "max_HP":110, "skill":[], "ATK":{"name":"機関銃", "ATK":[10, 15], "HIT":100, "SPD":12}, "unlock":False},
              {"name":"シロタ", "sort":16 ,"now_HP":150, "max_HP":150, "skill":[], "ATK":{"name":"ハンマー", "ATK":[18, 30], "HIT":100, "SPD":12}, "unlock":False},
              {"name":"トウコ", "sort":17 ,"now_HP":130, "max_HP":130, "skill":[], "ATK":{"name":"ハンマー", "ATK":[20, 30], "HIT":100, "SPD":12}, "unlock":False},
             ]


menu = [
        {"title":"遺跡", "mode":"dungeon"},
        {"title":"ショップ", "mode":"shop"},
        {"title":"ステータス", "mode":"status"},
        {"title":"チームメンバー変更", "mode":"member_edit"},
        {"title":"終わる", "mode":"main_menu"},
        ]

group_list = ["レッドドラゴン", "ブラックタイガー", "ホワイトベア"]


joined_group = op.choose_group(group_list)

while On == True:
    for i in range(len(menu)):
        print(str(i+1), menu[i]["title"])

    jump = int(input("何をする？>>>"))
    print()
    if jump == 1:
        mode = menu[jump-1]["mode"]
    elif jump == 2:
        mode = "shop"
    elif jump == 3:
        mode = "status"
    elif jump == 4:
        mode = "member_edit"
    elif jump == 5:
        mode = "main_menu"
        sh.next_operation()
        print()
        On = False
    else:
        print("入力した値に対応する行動はありません。")

    if mode == "dungeon":
        for i in range(len(dungeon_list)):
            print(str(i+1), str(dungeon_list[i]))
        select = int(input("どのダンジョンを探索しますか？>>>"))
        print()
        
        if select == 4:
            print("メインメニューに戻ります。")
            sh.next_operation()
            mode = "main_menu"
        elif select == 1 or 2 or 3:
            print(str(dungeon_list[select-1]) + "に侵入します。")
            sh.next_operation()
            print("ダンジョンに行く処理と帰ってきた想定")
            print("500ペラを獲得、燃料が320、HPが200減った。")
            money += 500
            if digger["now_HP"] < 200:
                digger["now_HP"] = 1
            else:
                digger["now_HP"] -= 200
            if digger["now_GAS"] < 320:
                digger["now_GAS"] = 1
            else:
                digger["now_GAS"] -= 320

            sh.next_operation()
            print("やれやれ、なんとか帰還できたな。")
            print("今回の探索も成功でやんす！")
            sh.next_operation()
            print()
            mode = "main_menu"

    if mode == "shop":
        print("ショップへ移動します。")
        sh.next_operation()
        mode, money, inventory = sh.shop_main(mode, money, inventory)
    
    if mode == "status":
        print("ステータス画面に移動します。")
        sh.next_operation()
        inventory, member, equip, mode, digger = st.status_main(inventory, member, equip, name, mode, digger)

    if mode == "member_edit":
        print("仲間の変更画面に移動します。")
        sh.next_operation()
        member = me.member_edit_main(member, member_all)
         
