from json import load, dump
import os

os.system("cls")
files = os.listdir(os.getcwd())
files = [file for file in files if os.path.isfile(file)]


stone_files=""
for file in files:
    if file.endswith(".sz"):
        stone_files+= file + "\n"

if stone_files=="": print("-- Please create a file ending in .sz and add code to it. --");exit()
stone_files=stone_files.split("\n")
if stone_files[-1]=="": del stone_files[-1]
if len(stone_files)>1:
    choice_text=""
    for i in range(len(stone_files)):
        choice_text += f"{i+1} | {stone_files[i]}\n"
    print(choice_text+"-- Which file do you want to use? --")
    chosen_file=stone_files[int(input(""))-1]
else:
    chosen_file=stone_files[0]


try: containers = load(open("starting_containers.json"))
except FileNotFoundError: dump({"0" : 3,"1":3}, open("starting_containers.json", "w"), indent=4);print("\n-- Please edit the containers in starting_containers.json and restart the program. --");exit()
sz_code = open(chosen_file).read().split("\n")
line = 0

def test(container):
    if containers[container] >= 1:
        return True
    else:
        return False
def end():
    dump(containers, open("containers.json", "w"), indent=4)
    print("\n-- Done! Results in containers.json --")
    exit()
if not "end" in open(chosen_file).read():print(f"\n-- {chosen_file} doesnt have an end // wont run --");exit()
while True:
    cl = sz_code[line].split(" ")
    try: command = cl[-2]
    except IndexError: command = cl[-1]
    if command == "tst":
        if test(cl[-1]):
            line = line + 1
        else:
            line = line + 2
    elif command == "jmp":
        line = int(cl[-1])
    elif command == "dec":
        containers[cl[-1]] -= 1
        line = line + 1
    elif command == "inc":
        containers[cl[-1]] += 1
        line = line + 1
    elif command == "end" or command == "hlt":
        end()
