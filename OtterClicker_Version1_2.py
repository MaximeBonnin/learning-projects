# GUI for Otter clicker game

# import otter_clicker # doesnt work? why not??
from tkinter import *
import os.path

def lvlup_cost(ID, lvl):
    cost = 10 * ID * 2 + 10 * ID * lvl**(1+ lvl/2)
    cost= round(cost, ndigits=2)
    return cost

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Otter clicker")

        self.multi = 1
        self.total_fish = 0
        self.upgrades = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fish_counter = IntVar()
        self.total_fish, self.upgrades, self.multi = self.load()
        self.fish_counter.set(self.total_fish)

        self.buttons = []

        self.label = Label(master, text="Click and get fish for the otters!", bg="brown")
        self.label.pack()
        self.reset_btn = Button(master, text="Reset (No benefit yet)", command=self.reset_save)
        self.reset_btn.pack()
        self.save_btn = Button(master, text="Save", command=self.save)
        self.save_btn.pack()


        self.fish_frame = Frame(master, bg="blue")
        self.fish_frame.pack(side=LEFT, fill=BOTH)


        self.img_fish = PhotoImage(file="fish.png").subsample(3,3)
        self.fish = Button(self.fish_frame,
                           text="TOTAL FISH:\n{}\n Multiplier: {}".format(str(self.fish_counter.get()), self.multi),
                           command=self.fish, bg="light blue", image=self.img_fish, compound = BOTTOM)
        self.fish.pack(side=LEFT)

        self.otter_frame = Frame(master, bg="dark green")
        self.otter_frame.pack(side=RIGHT, fill=Y)

        # self.upgrade1_counter = IntVar()
        # self.upgrade1_counter.set(upgrade_lvls[0])
        # self.otter1 = Button(self.otter_frame, text="Otter 1 lvl: {}\n Next upgrade cost: {}".format(self.upgrade1_counter.get(), lvlup_cost(1, self.upgrade1_counter.get())), command=lambda: self.upgrade(1), bg="light green")
        # self.otter1.pack()
        for i in range(1,14):
            # print(i, self.upgrades)
            # self.upgrades[i] = IntVar
            # self.upgrades[i].set(0)
            # self.upgrades.append(0)
            self.make_button(i)

        self.save()

    def make_button(self, ID):
        name = "Otter {}".format(ID)
        x = Button(self.otter_frame, text=name, command=lambda: self.upgrade(ID), bg="light green")
        self.buttons.append(x)
        self.buttons[ID-1].pack()
        self.buttons[ID-1].configure(text="{} lvl: {}\nNext upgrade cost:{}".format(name,self.upgrades[ID-1], lvlup_cost(ID, self.upgrades[ID-1])))

    def fish(self):
        # print("Clicked for fish!")
        self.fish_counter.set(self.fish_counter.get() + self.multi)
        # print(self.fish_counter.get())          # this changes the local counter but not global
        self.total_fish = self.fish_counter.get() + self.multi
        self.fish.configure(text="TOTAL FISH:\n{}\n Multiplier: {}".format(str(self.fish_counter.get()),self.multi))


    def upgrade(self, ID):
        # ID = 1
        # print("1 otter being upgraded!")
        # check fish and pay if affordable
        if self.total_fish > lvlup_cost(ID, self.upgrades[ID-1]):
            self.total_fish = self.total_fish - lvlup_cost(ID, self.upgrades[ID-1])
            self.fish_counter.set(self.total_fish)
            self.fish.configure(text="TOTAL FISH:\n{}\n Multiplier: {}".format(str(self.fish_counter.get()),self.multi))

            # do lvlup
            self.upgrades[ID-1] += 1

            self.buttons[ID-1].configure(text="Otter {} lvl: {}\n Next upgrade cost: {}".format(ID, self.upgrades[ID-1], lvlup_cost(ID, self.upgrades[ID-1])))

            # increase multiplier
            self.multi += round(ID/2 * self.upgrades[ID-1], 2)
            # global
            self.save()

        else:
            print("Not enough fish for upgrade! {} needed.".format(lvlup_cost(ID, self.upgrades[ID])))

    def reset_save(self):
        self.total_fish = 0
        self.upgrades = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.multi = 1
        self.fish_counter.set(0)
        save_data = "{}\n{}\n{}".format(self.total_fish, self.upgrades, self.multi)
        with open('gamesave.txt', 'w') as gamesave:
            gamesave.write(save_data)

        # save is now reset, need to update GUI
        self.fish.configure(text="TOTAL FISH:\n{}\n Multiplier: {}".format(str(self.fish_counter.get()), self.multi))
        for ID in range(1,14):
            self.buttons[ID - 1].configure(
                text="Otter {} lvl: {}\n Next upgrade cost: {}".format(ID, self.upgrades[ID - 1],
                                                                       lvlup_cost(ID, self.upgrades[ID - 1])))

    def save(self):
        save_data = "{}\n{}\n{}".format(self.total_fish, self.upgrades, self.multi)
        with open('gamesave.txt', 'w') as gamesave:
            gamesave.write(save_data)

    def load(self):
        if os.path.isfile('gamesave.txt'):
            with open('gamesave.txt', 'r') as gamesave:
                save_data = gamesave.read()
                save_data = save_data.split("\n")
                save_data[0] = float(save_data[0])
                save_data[1] = save_data[1][1:len(save_data[1]) - 1]
                save_data[1] = save_data[1].split(", ")
                for i in range(0, len(save_data[1])):
                    save_data[1][i] = int(save_data[1][i])
                save_data[2] = float(save_data[2])
                return save_data
        else:
            new_file = open('gamesave.txt', 'x')
            new_file.close()
            return self.total_fish, self.upgrades, self.multi

        # TODO autoclicking!






root = Tk()
root.geometry("500x500")
my_gui = GUI(root)
root.mainloop()