#!/bin/bash env python3 
print("Hello there, may i know your name please!")
mess = input()
print("Nice to meet you ",mess,"!\nhow may i help you!\n")
print("""1> I have an issue, request a ticket.\n2> Book a meeting.\n3> Want Some Pizza !!! \n""")
cmd = int(input("Plese Type Here: "))
print("\n")
if cmd==1:
    print("Everyone has issue, just ignore and enjoy your life!")
elif cmd==2:
    print("Huh Sorry, No Meetings today...")
elif cmd==3:
    print("Go and bring it yourself and also don't forget to bring one for me :)")
elif cmd==4:
    print("You don't have permissions to leave .... okay")
else:
    print("What the hack you typed...")
