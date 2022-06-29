#https://www.nytimes.com/games/wordle/index.html

#change the path where you stored Wordle.txt
with open('/Users/mona/Downloads/Wordle/Wordle.txt') as f:
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
        print("**********This is round: ",round," **********")

        #CAES BITH PXY WN /
        grey = input("Enter grey letters(e.g.CARES):")
        #R2 / / / /
        yellow = input("Enter yellow letters and positions(e.g.C0A1R2E3S4):")
        #/ R1 O2 D0 L4
        green = input("Enter green letters and positions(e.g.S0A1D2L3Y4):")

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

        greystatement = ""
        for j in range(len(greyletters)):
            greystatement+= "'"+greyletters[j]+"' in words[i] or "
        print("greystatement is: " + greystatement[0:-4])

        yellowstatement = ""
        for k in range(len(yellowletters)):
            yellowstatement+= "words[i]["+yellowpos[k]+"] == '"+yellowletters[k]+"' or "
        print("yellowstatement is: " + yellowstatement[0:-4])

        greenstatement = ""
        for m in range(len(greenletters)):
            greenstatement+= "words[i]["+greenpos[m]+"] == '"+greenletters[m]+"' and "
        print("greenstatement is: " + greenstatement[0:-5])

        lst = []
        for i in range(n-1):
            #print(words[i][0])
            #lst.append(words[i][0])

            #Grey
            #'C' in words[i] or 'A' in words[i] or 'E' in words[i] or 'S' in words[i]
            #'C' in words[i] or 'A' in words[i] or 'E' in words[i] or 'S' in words[i] or 'B' in words[i] or 'I' in words[i] or 'T' in words[i] or 'H' in words[i]
            #'C' in words[i] or 'A' in words[i] or 'E' in words[i] or 'S' in words[i] or 'B' in words[i] or 'I' in words[i] or 'T' in words[i] or 'H' in words[i] or 'P' in words[i] or 'X' in words[i] or 'Y' in words[i]
            #'C' in words[i] or 'A' in words[i] or 'E' in words[i] or 'S' in words[i] or 'B' in words[i] or 'I' in words[i] or 'T' in words[i] or 'H' in words[i] or 'P' in words[i] or 'X' in words[i] or 'Y' in words[i] or 'W' in words[i] or 'N' in words[i]
            ##'C' in words[i] or 'A' in words[i] or 'E' in words[i] or 'S' in words[i] or 'B' in words[i] or 'I' in words[i] or 'T' in words[i] or 'H' in words[i] or 'P' in words[i] or 'X' in words[i] or 'Y' in words[i] or 'W' in words[i] or 'N' in words[i]
            if eval(greystatement[0:-4]):
                pass

            #Yellow
            #words[i][2] == 'R'
            #words[i][2] == 'R'
            #words[i][2] == 'R'
            #words[i][2] == 'R'
            #words[i][2] == 'R'
            elif eval(yellowstatement[0:-4]):
                pass

            #Green
            #
            #words[i][1] == 'R'
            #words[i][1] == 'R' and words[i][2] == 'O'
            #words[i][1] == 'R' and words[i][2] == 'O' and words[i][0] == 'D'
            #words[i][1] == 'R' and words[i][2] == 'O' and words[i][0] == 'D' and words[i][4] == 'L'
            else:
                if greenstatement=="":
                    #print(words[i])
                    lst.append(words[i])
                else:
                    if eval(greenstatement[0:-5]):
                        #print(words[i])
                        lst.append(words[i])
                    else:
                        pass
        #['BHOOT', 'BIDDY', 'BIDON', 'BIFFO', 'BIFFY', 'BIFID', 'BIGGY', 'BIGHT', 'BIGLY', 'BIGOT', 'BIJOU', 'BILBO', 'BILBY', 'BILGY', 'BILLY', 'BIMBO', 'BINDI', 'BINGO', 'BINGY', 'BINIT', 'BIONT', 'BIPOD', 'BITOU', 'BITTY', 'BIVVY', 'BIZZO', 'BIZZY', 'BLIMP', 'BLIMY', 'BLIND', 'BLING', 'BLINI', 'BLINK', 'BLINY', 'BLITZ', 'BLOND', 'BLOOD', 'BLOOM', 'BLOOP', 'BLOWN', 'BLOWY', 'BLUDY', 'BLUFF', 'BLUID', 'BLUNK', 'BLUNT', 'BLURB', 'BLURT', 'BOBBY', 'BOBOL', 'BOFFO', 'BOGGY', 'BOING', 'BOINK', 'BOLIX', 'BOMBO', 'BONGO', 'BONNY', 'BOOBY', 'BOODY', 'BOOFY', 'BOOGY', 'BOOKY', 'BOOMY', 'BOONG', 'BOORD', 'BOOTH', 'BOOTY', 'BOOZY', 'BOTHY', 'BOTTY', 'BOUGH', 'BOULT', 'BOUND', 'BOURD', 'BOURG', 'BOURN', 'BOVID', 'BRILL', 'BRING', 'BRINK', 'BRINY', 'BRITH', 'BRITT', 'BROGH', 'BROIL', 'BROMO', 'BROND', 'BROOD', 'BROOK', 'BROOL', 'BROOM', 'BROTH', 'BROWN', 'BRUGH', 'BRUIN', 'BRUIT', 'BRUNG', 'BRUNT', 'BUBBY', 'BUDDY', 'BUFFI', 'BUFFO', 'BUFFY', 'BUGGY', 'BUILD', 'BUILT', 'BULGY', 'BULKY', 'BULLY', 'BUMBO', 'BUMPH', 'BUMPY', 'BUNDH', 'BUNDT', 'BUNDU', 'BUNDY', 'BUNGY', 'BUNJY', 'BUNKO', 'BUNNY', 'BUNTY', 'BUPPY', 'BUTTY', 'BUTUT', 'BUTYL', 'BUXOM', 'BUZZY', 'DHOBI', 'DHOLL', 'DHOTI', 'DHUTI', 'DIDDY', 'DIGHT', 'DIGIT', 'DILDO', 'DILLI', 'DILLY', 'DIMLY', 'DINGO', 'DINGY', 'DINKY', 'DIPPY', 'DITTO', 'DITTY', 'DITZY', 'DIVOT', 'DIVVY', 'DIXIT', 'DIZZY', 'DJINN', 'DOBBY', 'DOBRO', 'DODDY', 'DODGY', 'DOGGO', 'DOGGY', 'DOHYO', 'DOILT', 'DOILY', 'DOING', 'DOLLY', 'DOLOR', 'DONKO', 'DONNY', 'DONOR', 'DONUT', 'DOODY', 'DOOLY', 'DOOMY', 'DOORN', 'DOOZY', 'DOTTY', 'DOUBT', 'DOUGH', 'DOWDY', 'DOWLY', 'DOWNY', 'DOWRY', 'DOYLY', 'DRIFT', 'DRILL', 'DRILY', 'DRINK', 'DRIPT', 'DROID', 'DROIL', 'DROIT', 'DROLL', 'DRONY', 'DROOB', 'DROOG', 'DROOK', 'DROOL', 'DROOP', 'DROPT', 'DROUK', 'DROWN', 'DRUID', 'DRUNK', 'DRUXY', 'DRYLY', 'DUBBO', 'DUDDY', 'DUING', 'DULLY', 'DUMBO', 'DUMKY', 'DUMMY', 'DUMPY', 'DUNGY', 'DUNNO', 'DUNNY', 'DUOMI', 'DUOMO', 'DUPLY', 'DUPPY', 'DYING', 'FIBRO', 'FIFTH', 'FIFTY', 'FIGHT', 'FILLO', 'FILLY', 'FILMI', 'FILMY', 'FILTH', 'FILUM', 'FINNY', 'FIORD', 'FITLY', 'FIXIT', 'FIZZY', 'FJORD', 'FLIMP', 'FLING', 'FLINT', 'FLIRT', 'FLITT', 'FLONG', 'FLOOD', 'FLOOR', 'FLORY', 'FLOUR', 'FLOUT', 'FLOWN', 'FLUFF', 'FLUID', 'FLUKY', 'FLUMP', 'FLUNG', 'FLUNK', 'FLUOR', 'FLURR', 'FLUTY', 'FLUYT', 'FLYBY', 'FOGGY', 'FOLIO', 'FOLKY', 'FOLLY', 'FONDU', 'FONLY', 'FOODY', 'FOOTY', 'FOUND', 'FOUNT', 'FOUTH', 'FOWTH', 'FRILL', 'FRITH', 'FRITT', 'FRITZ', 'FRIZZ', 'FROND', 'FRONT', 'FRORN', 'FRORY', 'FROTH', 'FROWN', 'FROWY', 'FRUIT', 'FRUMP', 'FUBBY', 'FUDDY', 'FUFFY', 'FUGGY', 'FUGIO', 'FUGLY', 'FULLY', 'FUNDI', 'FUNDY', 'FUNGI', 'FUNGO', 'FUNKY', 'FUNNY', 'FUTON', 'FUZIL', 'FUZZY', 'GHOUL', 'GHYLL', 'GIBLI', 'GIDDY', 'GIGOT', 'GILLY', 'GILPY', 'GIMPY', 'GINNY', 'GINZO', 'GIPON', 'GIPPO', 'GIPPY', 'GIZMO', 'GLIFF', 'GLIFT', 'GLINT', 'GLITZ', 'GLOBI', 'GLOBY', 'GLOGG', 'GLOOM', 'GLOOP', 'GLORY', 'GLOUT', 'GLUON', 'GLYPH', 'GOBBI', 'GOBBO', 'GOBBY', 'GODLY', 'GOING', 'GOLDY', 'GOLLY', 'GOMBO', 'GONIF', 'GONOF', 'GONZO', 'GOOBY', 'GOODY', 'GOOFY', 'GOOKY', 'GOOLD', 'GOOLY', 'GOONY', 'GOOPY', 'GOORY', 'GOPIK', 'GOURD', 'GOUTY', 'GOYIM', 'GRIFF', 'GRIFT', 'GRILL', 'GRIMY', 'GRIND', 'GRIOT', 'GRIPT', 'GRIPY', 'GRITH', 'GRODY', 'GROIN', 'GROOF', 'GROOM', 'GROUF', 'GROUP', 'GROUT', 'GROWL', 'GROWN', 'GRUFF', 'GRUMP', 'GRUNT', 'GRYPT', 'GUILD', 'GUILT', 'GUIMP', 'GUIRO', 'GULFY', 'GULLY', 'GULPH', 'GULPY', 'GUMBO', 'GUMMY', 'GUNDY', 'GUNGY', 'GUNKY', 'GUNNY', 'GUPPY', 'GUTTY', 'GUYOT', 'GYNNY', 'GYPPO', 'GYPPY', 'HIGHT', 'HIKOI', 'HILLO', 'HILLY', 'HILUM', 'HIMBO', 'HINKY', 'HINNY', 'HIPLY', 'HIPPO', 'HIPPY', 'HOBBY', 'HOING', 'HOKKU', 'HOKUM', 'HOLLO', 'HOLLY', 'HOLON', 'HONGI', 'HONKY', 'HONOR', 'HOODY', 'HOOKY', 'HOOLY', 'HOORD', 'HOOTY', 'HOPPY', 'HOTLY', 'HOTTY', 'HOUFF', 'HOUGH', 'HOUND', 'HOURI', 'HOWDY', 'HOWFF', 'HUBBY', 'HUDUD', 'HUFFY', 'HUGGY', 'HULKY', 'HULLO', 'HULLY', 'HUMID', 'HUMOR', 'HUMPH', 'HUMPY', 'HUNKY', 'HUZZY', 'HYDRO', 'HYING', 'HYOID', 'IDIOM', 'IDIOT', 'IDYLL', 'IGLOO', 'ILIUM', 'ILLTH', 'IMIDO', 'IMINO', 'IMMIT', 'IMMIX', 'IMPLY', 'IMPOT', 'INDOL', 'INDOW', 'INDRI', 'INFIX', 'INGOT', 'INION', 'INORB', 'INPUT', 'INTIL', 'INTRO', 'INURN', 'INWIT', 'IODID', 'IODIN', 'IPPON', 'IRING', 'IROKO', 'IRONY', 'IVORY', 'JIFFY', 'JIGGY', 'JIGOT', 'JIMMY', 'JIMPY', 'JINGO', 'JINNI', 'JOINT', 'JOKOL', 'JOLLY', 'JOLTY', 'JOMON', 'JONTY', 'JOTTY', 'JOTUN', 'JOWLY', 'JUGUM', 'JUMBO', 'JUMBY', 'JUMPY', 'JUNKY', 'JUNTO', 'JUPON', 'JUTTY', 'KHOUM', 'KIBBI', 'KIDDO', 'KIDDY', 'KIGHT', 'KIKOI', 'KILIM', 'KILTY', 'KIMBO', 'KINDY', 'KININ', 'KINKY', 'KITTY', 'KLONG', 'KLOOF', 'KLUTZ', 'KNOLL', 'KNOUT', 'KNOWN', 'KNURL', 'KNURR', 'KOKUM', 'KOMBU', 'KONBU', 'KONDO', 'KOOKY', 'KOORI', 'KOTOW', 'KRILL', 'KROON', 'KRUBI', 'KUDZU', 'KUKRI', 'KULFI', 'KYLIN', 'KYLIX', 'LIBRI', 'LIGHT', 'LIKIN', 'LIMBI', 'LIMBO', 'LIMBY', 'LIMIT', 'LINDY', 'LINGO', 'LINGY', 'LININ', 'LINKY', 'LINNY', 'LINTY', 'LINUM', 'LINUX', 'LIPID', 'LIPIN', 'LIPPY', 'LITHO', 'LIVID', 'LIVOR', 'LOBBY', 'LOFTY', 'LOGGY', 'LOGIN', 'LOGOI', 'LOGON', 'LOLLY', 'LOLOG', 'LOOBY', 'LOONY', 'LOOPY', 'LOORD', 'LOPPY', 'LOTTO', 'LOUGH', 'LOUND', 'LOURY', 'LOWLY', 'LOWND', 'LOWRY', 'LUMMY', 'LUMPY', 'LUNGI', 'LUPIN', 'LUVVY', 'LYING', 'LYMPH', 'MHORR', 'MIDDY', 'MIDGY', 'MIFFY', 'MIFTY', 'MIGHT', 'MILKO', 'MILKY', 'MILOR', 'MILTY', 'MILTZ', 'MINGY', 'MINIM', 'MINNY', 'MINOR', 'MINTY', 'MIXUP', 'MIZZY', 'MOBBY', 'MODII', 'MOGGY', 'MOGUL', 'MOHUR', 'MOLDY', 'MOLLY', 'MOLTO', 'MOMMY', 'MONDO', 'MONGO', 'MONTH', 'MONTY', 'MOODY', 'MOOLI', 'MOOLY', 'MOONY', 'MOORY', 'MOPPY', 'MOTHY', 'MOTIF', 'MOTOR', 'MOTTO', 'MOTTY', 'MOULD', 'MOULT', 'MOUND', 'MOUNT', 'MOURN', 'MOUTH', 'MUDDY', 'MUDIR', 'MUFTI', 'MUGGY', 'MUHLY', 'MUJIK', 'MUMMY', 'MUNGO', 'MUNTU', 'MUTON', 'MUZZY', 'MYOID', 'MYOPY', 'MYTHI', 'MYTHY', 'NIDOR', 'NIFFY', 'NIFTY', 'NIGHT', 'NIHIL', 'NIMBI', 'NINNY', 'NINON', 'NINTH', 'NIPPY', 'NITID', 'NITON', 'NITRO', 'NITRY', 'NITTY', 'NOBBY', 'NOBLY', 'NODDY', 'NOHOW', 'NOILY', 'NOINT', 'NOMOI', 'NONNY', 'NONYL', 'NOOIT', 'NOOKY', 'NOTUM', 'NOULD', 'NOUNY', 'NOVUM', 'NOWTY', 'NUBBY', 'NUDDY', 'NUDZH', 'NUNNY', 'NUTTY', 'NYING', 'NYLON', 'NYMPH', 'OBIIT', 'OBOLI', 'ODDLY', 'ODIUM', 'ODOUR', 'OGGIN', 'OHING', 'OLOGY', 'ONION', 'ONIUM', 'OOBIT', 'OOMPH', 'OOTID', 'OPING', 'OPIUM', 'ORBIT', 'ORIBI', 'ORLON', 'ORLOP', 'ORPIN', 'ORTHO', 'OUBIT', 'OUGHT', 'OUNDY', 'OUTBY', 'OUTDO', 'OUTGO', 'OUTRO', 'OVOID', 'OVOLI', 'OVOLO', 'OWING', 'OXBOW', 'OXLIP', 'PHLOX', 'PHONO', 'PHONY', 'PHOTO', 'PHPHT', 'PIGGY', 'PIGHT', 'PIGMY', 'PIING', 'PIKUL', 'PILOT', 'PILOW', 'PILUM', 'PINGO', 'PINKO', 'PINKY', 'PINNY', 'PINON', 'PINOT', 'PINTO', 'PINUP', 'PIONY', 'PIPIT', 'PIPPY', 'PIPUL', 'PITHY', 'PITON', 'PIVOT', 'PLING', 'PLINK', 'PLONG', 'PLONK', 'PLOOK', 'PLOTZ', 'PLOUK', 'PLUFF', 'PLUMB', 'PLUMP', 'PLUMY', 'PLUNK', 'POBOY', 'PODDY', 'PODGY', 'POILU', 'POIND', 'POINT', 'POLIO', 'POLLY', 'POLYP', 'POMMY', 'PONGO', 'PONGY', 'PONTY', 'PONZU', 'POOFY', 'POORI', 'POORT', 'POOVY', 'POPPY', 'POTIN', 'POTOO', 'POTTO', 'POTTY', 'POUFF', 'POULP', 'POULT', 'POUND', 'POUPT', 'POUTY', 'POWIN', 'POWND', 'POWNY', 'POYNT', 'POYOU', 'POZZY', 'PRILL', 'PRIMI', 'PRIMO', 'PRIMP', 'PRIMY', 'PRINK', 'PRINT', 'PRION', 'PRIOR', 'PRIVY', 'PROIN', 'PROLL', 'PROMO', 'PRONG', 'PRONK', 'PROOF', 'PROUD', 'PROUL', 'PROWL', 'PROXY', 'PROYN', 'PRUNT', 'PUDDY', 'PUDGY', 'PUDOR', 'PUFFY', 'PUGGY', 'PUGIL', 'PULIK', 'PULLI', 'PULMO', 'PULPY', 'PUNJI', 'PUNKY', 'PUNNY', 'PUNTO', 'PUNTY', 'PUPIL', 'PUPPY', 'PUTID', 'PUTON', 'PUTTI', 'PUTTO', 'PUTTY', 'PYGMY', 'PYLON', 'PYOID', 'QUBIT', 'QUIFF', 'QUILL', 'QUILT', 'QUINO', 'QUINT', 'QUIPO', 'QUIPU', 'QUIRK', 'QUIRT', 'QUOIF', 'QUOIN', 'QUOIT', 'QUOLL', 'QUONK', 'QUOTH', 'RHINO', 'RHODY', 'RHOMB', 'RHUMB', 'RIBBY', 'RIDGY', 'RIFTY', 'RIGHT', 'RIGID', 'RIGOL', 'RIGOR', 'RINDY', 'RITZY', 'ROBIN', 'ROBOT', 'ROGUY', 'ROILY', 'RONDO', 'RONIN', 'ROOFY', 'ROOKY', 'ROOMY', 'ROOPY', 'ROOTY', 'ROTON', 'ROTOR', 'ROUGH', 'ROUND', 'ROUPY', 'ROUTH', 'ROWDY', 'ROWND', 'ROWTH', 'ROZIT', 'RUBBY', 'RUBIN', 'RUDDY', 'RUGBY', 'RUGGY', 'RUING', 'RUMBO', 'RUMLY', 'RUMMY', 'RUMOR', 'RUMPO', 'RUMPY', 'RUNNY', 'RUNTY', 'RUTIN', 'RUTTY', 'THIGH', 'THILK', 'THILL', 'THING', 'THINK', 'THIOL', 'THIRD', 'THIRL', 'THOFT', 'THOLI', 'THONG', 'THORN', 'THORO', 'THORP', 'THOWL', 'THUMB', 'THUMP', 'THUNK', 'THURL', 'THYMI', 'THYMY', 'TIDDY', 'TIGHT', 'TIGON', 'TILLY', 'TILTH', 'TIMBO', 'TIMID', 'TIMON', 'TINNY', 'TINTY', 'TIPPY', 'TITTY', 'TITUP', 'TIZZY', 'TODDY', 'TOFFY', 'TOING', 'TOLLY', 'TOLYL', 'TOMMY', 'TONDI', 'TONDO', 'TOOTH', 'TOPHI', 'TOPOI', 'TOTTY', 'TOUGH', 'TOUZY', 'TOWNY', 'TOWZY', 'TOXIN', 'TOYON', 'TRIFF', 'TRIGO', 'TRILD', 'TRILL', 'TRIOL', 'TRIOR', 'TRIPY', 'TROLL', 'TROMP', 'TRONK', 'TROOP', 'TROOZ', 'TROTH', 'TROUT', 'TRUGO', 'TRULL', 'TRULY', 'TRUMP', 'TRUNK', 'TRUTH', 'TUBBY', 'TUFTY', 'TUKTU', 'TULIP', 'TUMID', 'TUMMY', 'TUMOR', 'TUMPY', 'TUNNY', 'TUPIK', 'TUTOR', 'TUTTI', 'TUTTY', 'TWILL', 'TWILT', 'TWINK', 'TWINY', 'TWIRL', 'TWIRP', 'TWIXT', 'TYING', 'TYIYN', 'TYPTO', 'UHURU', 'ULMIN', 'UMPTY', 'UNBID', 'UNBOX', 'UNDID', 'UNDUG', 'UNFIT', 'UNFIX', 'UNGOD', 'UNGOT', 'UNGUM', 'UNHIP', 'UNIFY', 'UNION', 'UNITY', 'UNKID', 'UNLID', 'UNLIT', 'UNMIX', 'UNPIN', 'UNTIL', 'UNTIN', 'UNWIT', 'UNWON', 'UNZIP', 'UPBOW', 'UPDRY', 'UPLIT', 'URUBU', 'VIGIL', 'VIGOR', 'VILLI', 'VINYL', 'VIOLD', 'VIVID', 'VIZIR', 'VIZOR', 'VODOU', 'VODUN', 'VOLTI', 'VOMIT', 'VOULU', 'VOZHD', 'VROOM', 'VROUW', 'VUGGY', 'VUGHY', 'VULGO', 'VUTTY', 'VYING', 'WHIFF', 'WHIFT', 'WHILK', 'WHINY', 'WHIPT', 'WHIRL', 'WHIRR', 'WHITY', 'WHIZZ', 'WHOMP', 'WHOOF', 'WHOOP', 'WHOOT', 'WHORL', 'WHORT', 'WHUMP', 'WIDDY', 'WIDOW', 'WIDTH', 'WIFTY', 'WIGGY', 'WIGHT', 'WILLY', 'WIMPY', 'WINDY', 'WINGY', 'WITHY', 'WITTY', 'WOFUL', 'WOLLY', 'WOMBY', 'WOMYN', 'WONGI', 'WONKY', 'WOODY', 'WOOFY', 'WOOLD', 'WOOLY', 'WOOTZ', 'WOOZY', 'WOULD', 'WOUND', 'WRING', 'WRONG', 'WROOT', 'WROTH', 'WRUNG', 'WRYLY', 'XYLOL', 'XYLYL', 'YIPPY', 'YMOLT', 'YOBBO', 'YOGIN', 'YOKUL', 'YOLKY', 'YOMIM', 'YOUNG', 'YOURN', 'YOURT', 'YOUTH', 'YRIVD', 'YUKKY', 'YUMMO', 'YUMMY', 'YUPON', 'YUPPY', 'ZHOMO', 'ZIMBI', 'ZINGY', 'ZINKY', 'ZIPPO', 'ZIPPY', 'ZIZIT', 'ZLOTY', 'ZOMBI', 'ZOOID', 'ZOOTY', 'ZOPPO', 'ZUZIM', 'ZYGON']
        #['DROLL', 'DRONY', 'DROOG', 'DROOK', 'DROOL', 'DROOP', 'DROUK', 'DROWN', 'DRUNK', 'DRUXY', 'DRYLY', 'FROND', 'FRORN', 'FRORY', 'FROWN', 'FROWY', 'FRUMP', 'GRODY', 'GROOF', 'GROOM', 'GROUF', 'GROUP', 'GROWL', 'GROWN', 'GRUFF', 'GRUMP', 'KROON', 'ORLON', 'ORLOP', 'PROLL', 'PROMO', 'PRONG', 'PRONK', 'PROOF', 'PROUD', 'PROUL', 'PROWL', 'PROXY', 'PROYN', 'VROOM', 'VROUW', 'WRONG', 'WRUNG', 'WRYLY']
        #['DROLL', 'DROOG', 'DROOK', 'DROOL', 'DROUK', 'DROWN', 'FROND', 'FRORN', 'FROWN', 'GROOF', 'GROOM', 'GROUF', 'GROWL', 'GROWN', 'KROON', 'VROOM', 'VROUW', 'WRONG']
        #['DROLL', 'DROOG', 'DROOK', 'DROOL', 'DROUK', 'DROWN', 'DRUNK']
        #['DROLL', 'DROOL']
        print(lst)
        #words=lst
        if lst == []:
            print("Probably put wrong positions for letters, try again!")
            print("greyletters are: ", greyletters)
            print("yellowletters are: ", yellowletters, yellowpos)
            print("greenletters are: ", greenletters, greenpos)
            break

        flag = input("Did you get it right? (Yes: Type anything to terminate!, No: Press Enter Key):")
        if flag == "":
            print("Don't give up!")
        else:
            print("Congratulations!")

        round+=1





#Calculation of frequency

    ### letter = max(lst,key = lst.count)
    ### print(letter)

    # frequency = {}
    # for item in lst:
    #     if item in frequency:
    #         frequency[item] +=1
    #     else:
    #         frequency[item] =1
    # #print(frequency)

    # sortedf = {k:v for k,v in sorted(frequency.items(), key = lambda item: item[1], reverse = True)}
    # print(sortedf)

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