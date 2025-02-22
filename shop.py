import math
#import random
#import numpy as np
#import sys
#import pygame
#import datetime



# 消耗品 = (o:アイテム名 , 1:種類(0:消耗品 , 1:武器 , 2:補助装備) , 2:順番(アイテムソート時に使用) , 3:購入額, 4:売却額,
# 　　　　　5:所持数 , 6:乗車戦闘中の使用 , 7:降車戦闘中の使用, 8:ステータスでのアイテム使用, 9:遺跡内限定のアイテム使用)
print()

shop_goods = [
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


# 武器　= (0:アイテム名, 1:種類, 2:順番, 3:購入額, 4:売却額,
#    　　　5:攻撃 , 6:命中 , 7:速さ, 8:現弾数, 9:最大弾数, 10:属性(0/1 /3/4/5/6(属性:無/貫通/火/電/酸/氷)), 
# 　　　   11:攻撃対象, 12:最低攻撃回数, 13:最高攻撃回数, 14:重量)
# サポート = (0:アイテム名, 1:種類, 2:順番, 3:購入額, 4:売却額,
#    　　　   5:説明 , 6:重量))

shop_weapon = [{"name":"３７ミリ砲", "type":1, "sort":0, "price":300, "sell_price":50, "ATK":45, "HIT":95, "SPD":15, "AMM":25, "CAP":25, "element":"", "Target":"", "ATK_time":[], "heavy":[" ★ ★ 　 　 　 　 ", 2]},
               {"name":"５０ミリ砲", "type":1, "sort":1, "price":500, "sell_price":100, "ATK":50, "HIT":95, "SPD":12, "AMM":20, "CAP":20, "element":"", "Target":"", "ATK_time":[], "heavy":[" ★ ★ 　 　 　 　 ", 2]},
               {"name":"７５ミリ砲", "type":1, "sort":2, "price":1500, "sell_price":300, "ATK":60, "HIT":90, "SPD":10, "AMM":15, "CAP":15, "element":"", "Target":"", "ATK_time":[], "heavy":[" ★ ★ ★ 　 　 　 ", 3]},
               {"name":"７７ミリ砲", "type":1, "sort":3, "price":2500, "sell_price":500, "ATK":65, "HIT":85, "SPD":8, "AMM":15, "CAP":15, "element":"貫通", "Target":"", "ATK_time":[], "heavy":[" ★ ★ ★ 　 　 　 ", 3]},
               {"name":"８５ミリ砲", "type":1, "sort":4, "price":2000, "sell_price":400, "ATK":75, "HIT":90, "SPD":8, "AMM":15, "CAP":15, "element":"", "Target":"", "ATK_time":[], "heavy":[" ★ ★ ★ 　 　 　 ", 3]},
"""               
               {"name":"８８ミリ砲", "type":1, "sort":5, "price":-1, "sell_price":400, "ATK":80, "HIT":85, "SPD":6, "AMM":12, "CAP":12, "element":"貫通", "Target":"", "ATK_time":[], "heavy":[" ★ ★ ★ ★ 　 　 ", 4]},
               {"name":"１０５ミリ砲", "type":1, "sort":6, "price":-1, "sell_price":600, "ATK":80, "HIT":85, "SPD":4, "AMM":8, "CAP":8, "element":"", "Target":"全体", "ATK_time":[], "heavy":[" ★ ★ ★ ★ 　 　 ", 4]},
               {"name":"１２２ミリ砲", "type":1, "sort":7, "price":-1, "sell_price":600, "ATK":90, "HIT":90, "SPD":12, "AMM":12, "CAP":12, "element":"", "Target":"", "ATK_time":[], "heavy":[" ★ ★ ★ ★ ★ 　 ", 5]},
               {"name":"１２８ミリ砲", "type":1, "sort":8, "price":-1, "sell_price":800, "ATK":100, "HIT":90, "SPD":4, "AMM":12, "CAP":12, "element":"", "Target":"", "ATK_time":[], "heavy":[" ★ ★ ★ ★ ★ 　 ", 5]},
               {"name":"１５０ミリ砲", "type":1, "sort":9, "price":-1, "sell_price":1000, "ATK":100, "HIT":85, "SPD":2, "AMM":8, "CAP":8, "element":"", "Target":"", "ATK_time":[], "heavy":[" ★ ★ ★ ★ ★ ★ ", 6]},           
"""            ,   
               {"name":"マシンガン", "type":1, "sort":10, "price":400, "sell_price":80, "ATK":20, "HIT":95, "SPD":16, "AMM":10, "CAP":10, "element":"", "Target":"", "ATK_time":[2,4], "heavy":[" ★ ★ 　 　 　 　 ", 6]},
               {"name":"ガトリング", "type":1, "sort":11, "price":600, "sell_price":120, "ATK":25, "HIT":90, "SPD":12, "AMM":10, "CAP":10, "element":"", "Target":"", "ATK_time":[2,4], "heavy":[" ★ ★ 　 　 　 　 ", 6]},
               {"name":"チェーンガン", "type":1, "sort":12, "price":800, "sell_price":150, "ATK":30, "HIT":85, "SPD":8, "AMM":10, "CAP":10, "element":"", "Target":"", "ATK_time":[2,4], "heavy":[" ★ ★ 　 　 　 　 ", 6]},
               {"name":"グレネード", "type":1, "sort":13, "price":700, "sell_price":150, "ATK":90, "HIT":70, "SPD":2, "AMM":5, "CAP":5, "element":"", "Target":"全体", "ATK_time":[], "heavy":[" ★ ★ 　 　 　 　 ",2]},
               {"name":"火グレネード", "type":1, "sort":14, "price":1000, "sell_price":200, "ATK":65, "HIT":70, "SPD":2, "AMM":5, "CAP":5, "element":"火", "Target":"全体", "ATK_time":[], "heavy":[" ★ ★ 　 　 　 　 ", 2]},
               {"name":"ウォーターガン", "type":1, "sort":26, "price":200, "sell_price":50, "ATK":15, "HIT":100, "SPD":20, "AMM":8, "CAP":8, "element":"氷", "Target":"", "ATK_time":[2,4], "heavy":[" ★ ★ 　 　 　 　 ", 2]},
              ]

money = 1000
"""
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
"""


def item_buy(show, money, inventory):
    i = str(input("購入するアイテムを選択してください。>>>"))
    while i == "":
        i = str(input("購入するアイテムを選択してください。>>>"))
    i = int(i)
    if 0 < i <= 10:
        if money < show[i-1]["price"]:
            print("所持金が足りません！")
        else:
            print(show[i-1]["name"], "を購入しますか?")
            yes_no = str(input("購入する場合は「y」を入力してください。>>>"))
            if yes_no == "y":
                print(show[i-1]["name"], "を購入しました。")
                money -= show[i-1]["price"]
                for j in range(10):
                    if inventory[j]["name"] == show[i-1]["name"]:
                        inventory[j]["possession_num"] += 1
                        break
            else:
                print("購入をキャンセルしました。")
    else:
        print("選択したアイテムが存在しません。")
    return money, inventory

def item_sell(money, inventory):
    print("売る時の処理")
    return money, inventory




#shop = shop_goods

def next_operation():
    input("▼")

def end_shop():
    print("ショップを終わります。")
    next_operation()
    return "main_menu"


def shop_main(mode, money, inventory):
    show = shop_goods
    mode = "shop"
    page = "item"
    #page_list = ["item", "weapon", "sell", "main_menu"]
    while mode == "shop":
        if page == "item":    #消耗品画面の時の処理
            for i in range(len(show)):
                if show[i]["price"] > 0:
                    print(str(i+1).rjust(2)+". "+str(show[i]["name"]).ljust(7, "　"), str(show[i]["price"]).rjust(4) + "ペラ")
            
            print()
            print("所持金："+str(money).rjust(6)+"ペラ")
            act = int(input('1. 購入, 2. 武器などを見る, 3. 所持品の売却, 4. 終わる。>>>'))
            if act == 4:
                mode = end_shop()
                return mode, money, inventory
            elif act == 3:
                print("売却画面に遷移します。")
                next_operation()
                page = "sell"
                show = inventory
            elif act == 2:
                print("車載品を表示します。")
                next_operation()
                page = "weapon"
                show = shop_weapon
            elif act != 1:
                print("error message!")
                next_operation()
            else:
                print("買うときの処理")
                money, inventory = item_buy(show, money, inventory)
                next_operation()
                
        elif page == "weapon":#車載品画面の時の処理
            for i in range(len(show)):
                if show[i]["price"] > 0:
                    print(str(i+1).rjust(2)+".", str(show[i]["name"]).ljust(8, "　"), str(show[i]["heavy"][0]), str(show[i]["price"]).rjust(4)+"ペラ")
                    print("    攻撃力："+str(show[i]["ATK"]), "命中率："+str(show[i]["HIT"]), "速さ："+str(show[i]["SPD"]), "弾数："+str(show[i]["AMM"]).rjust(2)+"/"+str(show[i]["CAP"]).rjust(2))
                    if show[i]["element"] == "貫通":
                        print("    属性：      / 貫 通 ")
                    elif show[i]["element"] != "":
                        if show[i]["Target"] == "全体":
                            print("    属性："+str(show[i]["element"]).rjust(3,"　")+"/ 全体攻撃 ")
                        if show[i]["ATK_time"] != []:
                            print("    属性："+str(show[i]["element"]).rjust(3,"　")+"/ "+str(show[i]["ATK_time"][0])+"-"+str(show[i]["ATK_time"][1])+"回攻撃")
            print()
            print("所持金："+str(money).rjust(6)+"ペラ")

            act = int(input('1. 購入, 2. 消耗品を見る, 3. 所持品の売却, 4. 終わる。>>>'))
            if act == 4:
                mode = end_shop()
                return mode, money, inventory
            elif act == 3:
                print("売却画面に遷移します。")
                next_operation()
                page = "sell"
                show = inventory
            elif act == 2:
                print("消耗品を表示します。")
                next_operation()
                page = "item"
                show = shop_goods
            elif act != 1:
                print("error message!")
                next_operation()
            else:
                print("買うときの処理")
                next_operation()
            

        
        else:                 #売却画面の時の処理
            j = 0
            for i in range(len(inventory)):
                if inventory[i]["possession_num"] > 0 and inventory[i]["sell_price"] > 0:
                    print(str(inventory[i]["name"]).ljust(7, "　") + str(inventory[i]["possession_num"]) + "個", str(inventory[i]["sell_price"]) + "ペラ")
                    j += 1
            
            if j == 0:
                print("所持しているアイテムに売れるものはありません。")
            elif j > 0:
                print("所持金："+str(money).rjust(6)+"ペラ")
            act = int(input('1. 売却, 2. 消耗品を見る, 3. 武器などを見る, 4. 終わる。>>>'))
            if act == 4:
                inventory = show
                mode = end_shop()
                return mode, money, inventory
            elif act == 3:
                print("車載品を表示します。")
                next_operation()
                inventory = show
                page = "weapon"
                show = shop_weapon
            elif act == 2:
                print("消耗品を表示します。")
                inventory = show
                next_operation()
                page = "item"
                show = shop_goods
            elif act == 1 and j == 0:
                print("売れるアイテムがないので売却は出来ません。")
                next_operation()
            elif act != 1:
                print("error message!")
                next_operation()
            elif j != 0:
                money, inventory = item_sell(money, inventory)
                next_operation()


#mode = "shop"
#shop_main(mode, money, inventory)