#Play Wordle at: https://www.nytimes.com/games/wordle/index.html

def countLetterFrequency(lst):
    output = [{}, {}, {}, {}, {}]
    recommendWord = ""

    for word in lst:
        for i in range(5):
            if word[i] in output[i]:
                output[i][word[i]]+=1
            else:
                output[i][word[i]]=1
    
    #Sort each dictionary by count in descending order
    for i in range(5):
        output[i] = dict(sorted(output[i].items(), key=lambda item: item[1], reverse=True))
        statement = f"Index {i + 1}: "
        for j, (letter, count) in enumerate(output[i].items()):
            if j == 0: #Record the most likely word for next round by frequency
                recommendWord += letter
            elif j == 3: #Print out the top 3 for references
                break
            statement += f"{letter}: {count}, "
        print(statement[0:-2])
    
    print("\n!Recommendation: the next word should be similar to: "+recommendWord)



#Change the path where you stored Wordle.txt
with open('Wordle.txt') as f:
    
    words = f.read().rstrip().split()
    n = len(words)
    flag = ""
    round = 0

    greyletters = [] 
    yellowletters = []
    yellowpos = []
    greenletters = []
    greenpos = []

    while(flag==""):
        print("\n********** This is round: ",round," **********")

        #CA #OL
        grey = input("Enter grey letters(e.g.CARES):")
        #R2S4
        yellow = input("Enter yellow letters and positions(e.g.C0A1R2E3S4):")
        #E3 #S0R4
        green = input("Enter green letters and positions(e.g.S0A1D2L3Y4):")

        print("\n********** Confirm the letters **********")
        greyletters.extend(grey)
        print("greyletters are: ", greyletters)
        #even index for letters
        yellowletters.extend(yellow[::2])
        #odd index for positions
        yellowpos.extend(yellow[1::2])
        print("yellowletters are: ", yellowletters, yellowpos)
        #even index for letters
        greenletters.extend(green[::2])
        #odd index for positions
        greenpos.extend(green[1::2])
        print("greenletters are: ", greenletters, greenpos)

        print("\n********** Confirm the statements **********")
        greystatement = ""
        for j in range(len(greyletters)):
            greystatement+= "'"+greyletters[j]+"' in words[i] or "
        print("greystatement is: " + greystatement[0:-4])

        narrowstatement = ""
        yellowstatement = ""
        for k in range(len(yellowletters)):
            narrowstatement+= "'"+yellowletters[k]+"' in words[i] and "
            yellowstatement+= "words[i]["+yellowpos[k]+"] == '"+yellowletters[k]+"' or "
        print("yellowstatement is: " + yellowstatement[0:-4])

        greenstatement = ""
        for m in range(len(greenletters)):
            greenstatement+= "words[i]["+greenpos[m]+"] == '"+greenletters[m]+"' and "
        print("greenstatement is: " + narrowstatement + greenstatement[0:-5])

        lst = []
        for i in range(n-1):
            #print(words[i][0])
            #lst.append(words[i][0])

            #Grey
            #'C' in words[i] or 'A' in words[i]
            #'C' in words[i] or 'A' in words[i] or 'O' in words[i] or 'L' in words[i]
            if eval(greystatement[0:-4]):
                pass

            #Yellow
            #words[i][2] == 'R' or words[i][4] == 'S'
            #words[i][2] == 'R' or words[i][4] == 'S'
            elif eval(yellowstatement[0:-4]):
                pass

            #Green
            #'R' in words[i] and 'S' in words[i] and words[i][3] == 'E'
            #'R' in words[i] and 'S' in words[i] and words[i][3] == 'E' and words[i][0] == 'S' and words[i][4] == 'R'
            else:
                if greenstatement=="":
                    #print(words[i])
                    lst.append(words[i])
                else:
                    if eval(narrowstatement + greenstatement[0:-5]):
                        # print(words[i])
                        lst.append(words[i])
                    else:
                        pass
        #['DOSER', 'ESKER', 'ESTER', 'HOSER', 'LOSER', 'LUSER', 'MISER', 'MUSER', 'NOSER', 'OSIER', 'POSER', 'RESEE', 'RESET', 'RESEW', 'RISEN', 'RISER', 'ROSED', 'ROSET', 'SEDER', 'SEFER', 'SEVER', 'SEWER', 'SEXER', 'SHEER', 'SHIER', 'SHOER', 'SHYER', 'SIDER', 'SIKER', 'SILER', 'SIVER', 'SIXER', 'SIZER', 'SKEER', 'SKIER', 'SKYER', 'SLEER', 'SLIER', 'SLYER', 'SNEER', 'SOBER', 'SOGER', 'SOLER', 'SOWER', 'SPEER', 'SPIER', 'SPUER', 'STEER', 'SUBER', 'SUPER', 'SWEER', 'SYKER', 'SYVER', 'USHER', 'WISER']
        #['SEDER', 'SEFER', 'SEVER', 'SEWER', 'SEXER', 'SHEER', 'SHIER', 'SHYER', 'SIDER', 'SIKER', 'SIVER', 'SIXER', 'SIZER', 'SKEER', 'SKIER', 'SKYER', 'SNEER', 'SPEER', 'SPIER', 'SPUER', 'STEER', 'SUBER', 'SUPER', 'SWEER', 'SYKER', 'SYVER']
        print("\n********** Filtered results **********")
        print(lst)
        # Index 1: S: 35, R: 7, E: 2
        # Index 2: O: 11, I: 10, E: 8
        # Index 3: S: 16, E: 7, I: 5
        # Index 4: E: 55
        # Index 5: R: 49, T: 2, E: 1
        print("\n********** Stats **********")
        countLetterFrequency(lst)
        #words=lst
        if lst == []:
            print("Probably put wrong positions for letters, try again!")
            print("greyletters are: ", greyletters)
            print("yellowletters are: ", yellowletters, yellowpos)
            print("greenletters are: ", greenletters, greenpos)
            break

        flag = input("\nDid you get it right? (Yes: Type anything to terminate!, No: Press Enter Key):")
        if flag == "":
            print("Don't give up!")
        else:
            print("Congratulations!")

        round+=1



#Calculation of word frequency
    ## letter = max(lst,key = lst.count)
    ## print(letter)

    # frequency = {}
    # for item in lst:
    #     if item in frequency:
    #         frequency[item] +=1
    #     else:
    #         frequency[item] =1
    # #print(frequency)

    # sortedf = {k:v for k,v in sorted(frequency.items(), key = lambda item: item[1], reverse = True)}
    # print(sortedf)

# Output
#{'S': 1521, 'C': 888, 'B': 871, 'P': 821, 'T': 787, 'A': 715, 'M': 666, 'D': 650, 'R': 610, 'G': 608, 'F': 575, 'L': 551, 'H': 477, 'W': 402, 'K': 353, 'N': 317, 'E': 288, 'O': 257, 'V': 231, 'J': 191, 'U': 178, 'Y': 175, 'I': 157, 'Z': 97, 'Q': 76, 'X': 15}
#{'A': 2158, 'O': 2008, 'E': 1572, 'I': 1334, 'U': 1137, 'R': 908, 'L': 677, 'H': 525, 'N': 334, 'Y': 262, 'T': 232, 'P': 229, 'M': 175, 'C': 173, 'W': 158, 'K': 92, 'S': 89, 'D': 83, 'B': 79, 'G': 73, 'X': 53, 'V': 52, 'Z': 28, 'F': 23, 'Q': 14, 'J': 9}
#{'A': 1206, 'R': 1158, 'I': 1018, 'O': 960, 'N': 933, 'E': 847, 'L': 820, 'U': 642, 'T': 599, 'S': 510, 'M': 496, 'C': 373, 'D': 373, 'G': 351, 'P': 343, 'B': 315, 'W': 265, 'K': 253, 'V': 226, 'Y': 202, 'F': 168, 'Z': 136, 'X': 124, 'H': 107, 'J': 42, 'Q': 10}
#{'E': 2257, 'A': 1027, 'T': 878, 'I': 832, 'N': 758, 'L': 756, 'R': 695, 'O': 658, 'S': 502, 'K': 484, 'D': 451, 'G': 409, 'P': 406, 'M': 391, 'C': 389, 'U': 379, 'B': 227, 'F': 225, 'H': 224, 'V': 148, 'W': 126, 'Z': 119, 'Y': 98, 'J': 26, 'X': 11, 'Q': 1}
#{'S': 3805, 'E': 1477, 'Y': 1254, 'D': 807, 'T': 710, 'R': 656, 'A': 632, 'N': 512, 'L': 465, 'O': 365, 'H': 349, 'I': 253, 'K': 244, 'M': 179, 'P': 146, 'G': 135, 'C': 123, 'F': 80, 'X': 65, 'U': 63, 'W': 62, 'B': 55, 'Z': 31, 'V': 4, 'Q': 3, 'J': 2}

# S 1521 C 888 B 871
# A 2158 O 2008 E 1572
# A 1206 R 1158 I 1018
# E 2257 A 1027 T 878
# S 3805 E 1477 Y 1254

#CARES