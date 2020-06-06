###Welcome to my ass


#
#Personal skills
#
smarts = 0

charisma = 0

endurance = 0





#Military skills
cbtskill = 0
plnskill = 0
intskill = 0
#Extra things
polgrace = 0
##Political grace, have you achieved enough to get policies pushed through


#Trackers for doing stuff with
battlestotal = 0
opstotal = 0
serviceyears = 0


traits = "None"
player_name = input("Enter your last name: ")
player_rank = "Recruit"
playerskill = "None"
print("Welcome " + str(player_rank) + " " + str(player_name))
input("")
background = input("""What is your background?:
A) I had an interest in science, entering and winning a few contests
B) I loved team sports, leading a regional team to victory
C) I joined Army Cadets, becoming a senior cadet leader
D) I volunteered with many charities and events
""")

if background == "A" or "a":
    print("Interesting")
    smarts =+ 30
    charisma =+ 5
    endurance =+ 10
    polgrace =+20
    traits == "Analyst"
    elseif: background == "B" or "b"
    print("Interesting")
    smarts =+ 5
    charisma =+ 10
    endurance =+ 30
    polgrace =+ 20
    traits == "Planner"
    elseif: background == "C" or "c"
    print("Interesting")
    smarts =+ 5
    charisma =+ 10
    endurance =+ 30
    polgrace =+ 153
traits == "Military Bearing"
print(player_rank, player_name, traits)
print(smarts, charisma, endurance, polgrace)
input("")
