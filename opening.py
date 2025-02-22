

def next_ope():
    input("▼")

def main():
    yes_no = ""
    while yes_no != "y":
        name = str(input("主人公の名前を入力してください。>>>"))
        print("主人公の名前は「"+ name + "」でよろしいですか？")
        yes_no = str(input("ゲームをはじめる場合は「y」を入力してください。>>>"))
        if yes_no == "y":
            print("ゲームをはじめます。")
            next_ope()
            print()
        else:
            print("再度、名前を入力してください。")
    return name




def choose_group(group):
    for i in range(3):
        print(str(i+1) + "." + group[i])
    choose = str(input("どの勢力に加わりますか？>>>"))
    while choose == "":
        choose = str(input("どの勢力に加わりますか？>>>"))
        if choose != "":
            choose = int(choose)
            if choose != 1 and choose != 2 and choose != 3: 
                print("入力された値に対応する勢力は存在しません。")
                print("再度、勢力選択に戻ります。")
                choose = ""
            else:
                print(str(group[choose-1]) + "に加わりました。" )
                next_ope()
                print()
                return group[choose-1]
