print(r'''                                ,-.
                               ("O_)
                              / `-/
                             /-. /
                            /   )
                           /   /  
              _           /-. /
             (_)"-._     /   )
               "-._ "-'""( )/    
                   "-/"-._" `. 
                    /     "-.'._
                   /\       /-._"-._
    _,---...__    /  ) _,-"/    "-(_)
___<__(|) _   ""-/  / /   /
 '  `----' ""-.   \/ /   /
               )  ] /   /
       ____..-'   //   /                       )
   ,-""      __.,'/   /   ___                 /,
  /    ,--""/  / /   /,-""   """-.          ,'/
 [    (    /  / /   /  ,.---,_   `._   _,-','
  \    `-./  / /   /  /       `-._  """ ,-'
   `-._  /  / /   /_,'            ""--"
       "/  / /   /"         
       /  / /   /
      /  / /   /  o!O
     /  |,'   /  
    :   /    /
    [  /   ,'   "Blackadder"
    | /  ,'
    |/,-'
    P'
    ''')
print("Welcome to the 'Veil of Despair' the island of darkness!!💀")
print("Your Mission is to find the LEGENDARY PYTHON SWORD!!")

print("You are in middle of no where. Where do u wanna go?")
go = input("     Type \"left\",\"right\" or \"straight\"? \n    ->>").lower()

if go == "left":
    print("You are doomed by a demon")
elif go == "right":
    print("Suddenly a ghost came, and......")
    b = input("Do u want to process? Yes or No?\n->>").lower()
    if b == "yes":
        print("processing..........")
        a = input("Do you really wish to know what happen? press 'y' for Yes and 'n' for No\n->>")
    print("You Died. lol 😂")
else:
    print("You saw the sword on top of the mountain full of ghost")
    go = input("How do You want to go to top of that mountain? \n'sneak in' type a\n'keep walking🙄' type b\n-->")
    if go == "a":
        print("U are sneaking in front of ghosts? Are U sure? You died")
    else:
        print("That was bold but now u have to face the ghosts")
        n =input("Run and try to grab the sword. press 'a'\nfight the ghost bravely. type 'b'\n->>")
        if n == "a":
            print("Sorry you are not faster than ghost so You died")
        else:
            print("Are you sure want to fight ghost bare handed? What a fool")
print("Thanks for playing this lame game.")
print("")
play_again= input("Do U want to play again? yes or no?\n->>")
if play_again == "yes":
    print("You are in middle of no where. Where do u wanna go?")
    go = input("     Type \"left\",\"right\",\"straight\"or \"up\"? \n    ->>").lower()

    if go == "left":
        print("You are doomed by a demon")
    elif go == "right":
        print("Suddenly a ghost came, and......")
        b = input("Do u want to process? yes or no?")
        if b == "yes":
            print("processing..........")
            a = input("Do you really wish to know what happen? press 'y' for Yes and 'n' for No\n->>")
        print("You Died. lol 😂")
    elif go == "up":
        print("Well u can always fly u know...")
        n = input("Keep flying and grab the sword? type 'a'\n Again fight the ghosts bravely? type 'b'\n->> ")
        if n == "a":
            print("Congratulation You have the Legendary Python Sword")
        else:
            print("Well You died again!!")
    else:
        print("Well you already no what happened last time. Don't you?😜")
