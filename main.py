output=""
text_1=""
text_2=""
text_3=""
vesion="0.01"
import os
while True:
    program=input(os.getlogin() + ">>")
    関数処理="待てよやめろ"
    関数=""
    i=0
    引数の有無=True
    if not program=="":
        関数処理=program[i]
        while not program[i]==" ":
            if program[i]=="":
                引数の有無=False
                break
            if 関数処理=="":
                引数の有無=False
                break
            if not 関数処理==" "or 関数処理=="":
                    関数=関数 + 関数処理
                    i=int(i)+1
                    try:
                        関数処理=str(program[i])
                    except:
                        #print(関数)
                        引数の有無=False
                        break
    #print(関数)
    引数=program
    if 引数の有無:
        for i in range(len(program) - (len(program) - len(関数) - 1)):
            引数=引数[1:]
    #print(引数)
    if 引数の有無:
        if 関数=="print":
            if 引数=="text_1":
                print(text_1)
            else:
                print(引数)
        if 関数=="input":
            output=input(引数)
        if 関数=="text_1":
            text_1=引数
        if 関数=="text_2":
            text_2=引数
        if 関数=="text_3":
            text_3=引数
    else:
        if 関数=="output":
            #print("input")
            print(output)
        if 関数=="vesion":
            print(vesion)
