
import tkinter as tk
import time

class whc():
    def __init__(self):
        side="L"
        self.LeftSide=["vege","sheep","wolf"]
        self.boat=["human",side]
        self.RightSide=[]
    def DeBug_showAll(self):
        print(f"LeftSide = {self.LeftSide}\n")
        print(f"boat = {self.boat}\n")
        print(f"RightSide = {self.RightSide}\n")
    def BoatIsFull(self):
        if(len(self.boat)==3):
            return False
        else:
            return True
    def CheckLeftSide(self,name):
        #check LeftSide
        try:
            LeftSide_id = self.LeftSide.index(name)
            #print(f"LID = {LeftSide_id}")
            return LeftSide_id
        except ValueError:    
            LeftSide_id = -1
            #print(f"LID = {LeftSide_id}")
            return LeftSide_id
    def CheckRightSide(self,name):
        #check RightSide
        try:
            RightSide_id = self.RightSide.index(name)
            #print(f"RID = {RightSide_id}")
            return RightSide_id
        except ValueError:
            RightSide_id = -1
            #print(f"RID = {RightSide_id}")
            return RightSide_id
    def MoveBoat(self):
        if(self.boat[1]=="L"):
            self.boat[1]="R"
        elif(self.boat[1]=="R"):
            self.boat[1]="L"
    def MoveGood(self,name):
        LeftSide_id = self.CheckLeftSide(name)
        RightSide_id = self.CheckRightSide(name)
        #print("-------------------------------")
        if(self.BoatIsFull()):
            if(LeftSide_id != -1 and self.boat[1]=="L"):
                item = self.LeftSide.pop(LeftSide_id)
                self.boat.append(item)
                
            elif(RightSide_id != -1 and self.boat[1]=="R"):
                item = self.RightSide.pop(RightSide_id)
                self.boat.append(item)
        elif(LeftSide_id == -1 and RightSide_id==-1):
            #print("item in boat")   
            if(self.boat[1]=="L"):
                item = self.boat.pop()
                self.LeftSide.append(item)
            elif(self.boat[1]=="R"):
                item = self.boat.pop()
                self.RightSide.append(item)
    def CheckWin(self):
        counts = [self.RightSide.count(x) for x in ["vege","sheep","wolf"]]
        if (0 not in counts):
            print("WIN")
            return 3
        else:
            counts = [self.RightSide.count(x) for x in ["sheep","wolf"]]
            if(0 not in counts):
                if(self.boat[1]=="L"):
                    print("Fail sheep die")
                    return 1

            counts = [self.RightSide.count(x) for x in ["sheep","vege"]]
            if(0 not in counts):
                if(self.boat[1]=="L"):
                    print("Fail vege die")
                    return 2
            
            counts = [self.LeftSide.count(x) for x in ["sheep","wolf"]]
            if(0 not in counts):
                if(self.boat[1]=="R"):
                    print("Fail sheep die")
                    return 1

            counts = [self.LeftSide.count(x) for x in ["sheep","vege"]]
            if(0 not in counts):
                if(self.boat[1]=="R"):
                    print("Fail vege die")
                    return 2

def Animation_Item():
    if("vege" in game.boat and game.boat[1]=="L"):
        background_Canvas.move(vegetable_icon_id,20,0)
        win.update()
    elif("vege" in game.boat and game.boat[1]=="R"):
        background_Canvas.move(vegetable_icon_id,-20,0)
        win.update()
    elif("sheep" in game.boat and game.boat[1]=="L"):
        background_Canvas.move(sheep_icon_id,20,0)
        win.update()
    elif("sheep" in game.boat and game.boat[1]=="R"):
        background_Canvas.move(sheep_icon_id,-20,0)
        win.update()
    elif("wolf" in game.boat and game.boat[1]=="L"):
        background_Canvas.move(wolf_icon_id,20,0)
        win.update()
    elif("wolf" in game.boat and game.boat[1]=="R"):
        background_Canvas.move(wolf_icon_id,-20,0)
        win.update()

def Button_moveBoat():
    transport.config(command=None)
    if(game.boat[1]=="L"):
        for i in range(10):
            Animation_Item()
            background_Canvas.move(human_icon_id,20,0)
            win.update()
            time.sleep(0.05)
            pass
        game.MoveBoat()
    elif(game.boat[1]=="R"):
        for i in range(10):
            Animation_Item()
            background_Canvas.move(human_icon_id,-20,0)
            win.update()
            time.sleep(0.05)
        game.MoveBoat()
    Label_gameMessage(game.CheckWin())
    transport.config(command=Button_moveBoat)

def Button_moveVegetable():
    if(game.BoatIsFull()):
        if("vege" in game.LeftSide and game.boat[1]=="L"):
            game.MoveGood("vege")
            background_Canvas.move(vegetable_icon_id,105,-10)
            win.update()
            time.sleep(0.05)
        elif("vege" in game.RightSide and game.boat[1]=="R"):
            game.MoveGood("vege")
            background_Canvas.move(vegetable_icon_id,-145,-10)
            win.update()
            time.sleep(0.05)
    else:
        if("vege" in game.boat and game.boat[1]=="L"):
            game.MoveGood("vege")
            background_Canvas.move(vegetable_icon_id,-105,10)
            win.update()
        elif("vege" in game.boat and game.boat[1]=="R"):
            game.MoveGood("vege")
            background_Canvas.move(vegetable_icon_id,145,10)
            win.update()
    Label_gameMessage(game.CheckWin())
def Button_moveSheep():
    if(game.BoatIsFull()):
        if("sheep" in game.LeftSide and game.boat[1]=="L"):
            game.MoveGood("sheep")
            background_Canvas.move(sheep_icon_id,70,-10)
            win.update()
            time.sleep(0.05)
        elif("sheep" in game.RightSide and game.boat[1]=="R"):
            game.MoveGood("sheep")
            background_Canvas.move(sheep_icon_id,-110,-10)
            win.update()
            time.sleep(0.05)
    else:
        if("sheep" in game.boat and game.boat[1]=="L"):
            game.MoveGood("sheep")
            background_Canvas.move(sheep_icon_id,-70,10)
            win.update()
        elif("sheep" in game.boat and game.boat[1]=="R"):
            game.MoveGood("sheep")
            background_Canvas.move(sheep_icon_id,110,10)
            win.update()
    Label_gameMessage(game.CheckWin())
def Button_moveWolf():
    if(game.BoatIsFull()):
        if("wolf" in game.LeftSide and game.boat[1]=="L"):
            game.MoveGood("wolf")
            background_Canvas.move(wolf_icon_id,40,-10)
            win.update()
            time.sleep(0.05)
        elif("wolf" in game.RightSide and game.boat[1]=="R"):
            game.MoveGood("wolf")
            background_Canvas.move(wolf_icon_id,-70,-10)
            win.update()
            time.sleep(0.05)
    else:
        if("wolf" in game.boat and game.boat[1]=="L"):
            game.MoveGood("wolf")
            background_Canvas.move(wolf_icon_id,-40,10)
            win.update()
        elif("wolf" in game.boat and game.boat[1]=="R"):
            game.MoveGood("wolf")
            background_Canvas.move(wolf_icon_id,70,10)
            win.update()
    Label_gameMessage(game.CheckWin())

def Button_Reset():
    win.destroy()

game = whc()
#---------------
win = tk.Tk()#建立主視窗
#title
win.title("狼羊菜test")

#size
win.geometry("800x500")
win.resizable(False,False)

#icon
win.iconbitmap(".\picture\witch.ico") #ico

#color
win.config(background="#dff9fb")
#置頂
win.attributes("-topmost",0)

#image-------------------
background_Canvas = tk.Canvas(win,width=800,height=500,background="#dff9fb")
bd = tk.PhotoImage(file=".\picture\whc-background.gif")
background_Canvas.create_image(0,500,image=bd,anchor="sw")
background_Canvas.place(x=0,y=0)

human_icon = tk.PhotoImage(file=".\picture\human.png")
human_icon_id = background_Canvas.create_image(0,0,image=human_icon,anchor="sw")
background_Canvas.move(human_icon_id,270,300)

wolf_icon = tk.PhotoImage(file=".\picture\wolf.png")
wolf_icon_id = background_Canvas.create_image(0,0,image=wolf_icon,anchor="sw")
background_Canvas.move(wolf_icon_id,235,300)

sheep_icon = tk.PhotoImage(file=".\picture\sheep.png")
sheep_icon_id = background_Canvas.create_image(0,0,image=sheep_icon,anchor="sw")
background_Canvas.move(sheep_icon_id,200,300)

vegetable_icon = tk.PhotoImage(file=".\picture\\vegetable.png")
vegetable_icon_id = background_Canvas.create_image(0,0,image=vegetable_icon,anchor="sw")
background_Canvas.move(vegetable_icon_id,165,300)
#button
        
pixelVirtual = tk.PhotoImage(width=1, height=1)

transport = tk.Button(text="GO!",image=pixelVirtual,command=Button_moveBoat,compound="c",height=30,width=50)
wolf = tk.Button(text="狼",image=pixelVirtual,command=Button_moveWolf,compound="c",height=30,width=50)
sheep = tk.Button(text="羊",image=pixelVirtual,command=Button_moveSheep,compound="c",height=30,width=50)
cabbage = tk.Button(text="菜",image=pixelVirtual,command=Button_moveVegetable,compound="c",height=30,width=50)
reset = tk.Button(text="關閉",image=pixelVirtual,command=Button_Reset,compound="c",height=30,width=50)
'''
transport.pack(padx=5,side="left")
wolf.pack(padx=5,side="left")
goat.pack(padx=5,side="left")
cabbage.pack(padx=5,side="left")
'''
transport.place(y=50,x=210)
wolf.place(y=50,x=300)
sheep.place(y=50,x=400)
cabbage.place(y=50,x=500)
reset.place(y=50,x=600)
#----------
#pixelVirtual = tk.PhotoImage(width=1, height=1)
gameMessage = tk.Label(text="我是遊戲訊息",image=pixelVirtual,compound="c",height=30,relief="solid")
gameMessage.place(x=250,y=150)
def Label_gameMessage(status):
    if(status==1):
        gameMessage.config(text="失敗 綿羊被狼吃掉了 請重開遊戲",image=pixelVirtual,compound="c",height=200,width=400,relief="solid")
        gameMessage.place(x=160,y=50)
    elif(status==2):
        gameMessage.config(text="失敗 菜被綿羊吃掉了 請重開遊戲",image=pixelVirtual,compound="c",height=200,width=400,relief="solid")
        gameMessage.place(x=160,y=50)
    elif(status==3):
        gameMessage.config(text="恭喜你贏了！ 請重開遊戲",image=pixelVirtual,compound="c",height=30,relief="solid")
        gameMessage.place(x=250,y=150)
#main window

win.mainloop()#常駐主視窗
#*---

    

