import math
import shop

def item_sort(item):
    n = len(item)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if item[j]["type"] < item[min_index]["type"]:
                min_index = j
                item[i], item[min_index] = item[min_index], item[i]
        for k in range(i+1, n):
            if item[j]["sort"] < item[min_index]["sort"]:
                min_index = j
                item[i], item[min_index] = item[min_index], item[i]
    return item

def item_use(item, member, equip, digger, select):



    return item, member, equip, digger




def status_main(item, member, equip, name, mode, digger):
    while mode == "status":
        print("＜所持品＞")
        item_amount = 0
        for i in range(len(item)):
            if item[i]["type"] == 0:
                if item[i]["possession_num"] > 0:
                    print(str(i+1).rjust(2), str(item[i]["name"]).ljust(7, "　") + str(item[i]["possession_num"]).rjust(2) + "個")
                    item_amount += 1
            elif item[i]["type"] == 1:
                print(str(i+1).rjust(2), str(item[i]["name"]).ljust(8, "　"), str(item[i]["heavy"][0]),)
                print("攻撃力："+str(item[i]["ATK"]), "命中率："+str(item[i]["HIT"]), "速さ："+str(item[i]["SPD"]), "弾数："+str(item[i]["AMM"]).rjust(2)+"/"+str(item[i]["CAP"]).rjust(2))
                if item[i]["element"] == "貫通":
                    print("属性：      / 貫 通 ")
                elif item[i]["element"] != "":
                    if item[i]["Target"] == "全体":
                        print("属性："+str(item[i]["element"]).rjust(3,"　")+"/ 全体攻撃 ")
                    if item[i]["ATK_time"] != []:
                        print("属性："+str(item[i]["element"]).rjust(3,"　")+"/ "+str(item[i]["ATK_time"][0])+"-"+str(item[i]["ATK_time"][1])+"回攻撃")
                item_amount += 1
            
        print()

        mass = 0
        for i in range(len(equip)):
            mass += equip[i]["heavy"][1]

        print("＜装備品＞ 重量：" + str(mass).rjust(2) + "/14")
        for i in range(len(equip)):
            if equip[i]["type"] == 1:
                print(str(equip[i]["name"]).ljust(8, "　"), str(equip[i]["heavy"][0]))
                print("攻撃力："+str(equip[i]["ATK"]), "命中率："+str(equip[i]["HIT"]), "速さ："+str(equip[i]["SPD"]), "弾数："+str(equip[i]["AMM"]).rjust(2)+"/"+str(equip[i]["CAP"]).rjust(2))
                if equip[i]["element"] == "貫通":
                    print("属性：      / 貫 通 ")
                elif equip[i]["element"] != "":
                    if equip[i]["Target"] == "全体":
                        print("属性："+str(equip[i]["element"]).rjust(3,"　")+"/ 全体攻撃 ")
                    if equip[i]["ATK_time"] != []:
                        print("属性："+str(equip[i]["element"]).rjust(3,"　")+"/ "+str(equip[i]["ATK_time"][0])+"-"+str(equip[i]["ATK_time"][1])+"回攻撃")
                else:
                    print("属性：  無  /       ")
        print()



        act = int(input("1. アイテムの使用 2. 車載品の取り付け 3. 車載品の取り外し 4.終わる>>>"))
        if act == 4:
            print("ステータス画面を閉じます。")
            shop.next_operation()
            mode = "main_menu"
        elif act == 3:
            print("番号と一緒に装備品の一覧を出して、また尋ねる(select = int(input))")
            shop.next_operation()
        elif act == 2 or act == 1:
            if item_amount == 0:
                print("選択可能なアイテムはありません。")
            else:
                select = str(input("使用or装備するアイテムの番号をきく。キャンセルする際は負の数を入れてください。>>>"))
                while select == "" or select != str(int(select)) or int(select) > len(item)-1 or int(select) != math.floor(int(select)):
                    print("入力された値に対応するアイテム・装備はありません。")
                    select = str(input("使用or装備するアイテムの番号を聴く。キャンセルする際は負の数を入れてください。>>>"))
                else:
                    select = int(select)
                
                if select < 0:
                    print("アイテムの使用・車載品の装備をキャンセルします。")
                elif select == math.floor(select):
                    if item[select]["possession_num"] > 0:
                        print("使用処理")
                        item, member, equip, digger = item_use(item, member, equip, digger)
                    else:
                        print("選択したアイテムを所持していません。")
        else:
            print("入力された値に対応する行動がありません。")



        




    return item, member, equip, mode, digger


