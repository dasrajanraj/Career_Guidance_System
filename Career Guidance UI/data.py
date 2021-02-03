#class 
enginner =["Sundar Pichai","Satya Nadella","Nagavara Ramaroa Narayana Murthy","RomaTheEngineer","tweetsoutloud","poornima","Jeffrey_Roe","dj_mckeown",]
teacher=["Teacher2Teacher","TeachtoLead","Jennfindleyblog","HeidiSongs","EdSurge","SBEducation","Educationweek"]
lawyer=["ABAJournal","BitterLawyer","GdnLaw","lawsocgazette","LegalPlanet","overlawyered"]
architect=["aianational","archinect","archicentral","subutcher","kadvacorp"]
police=["IPF_ORG","IPS_Association","DGPMaharashtra","DelhiPolice"]
politics=["narendramodi","ArvindKejriwal","arunjaitley","AmitShah","rajnathsingh","RahulGandhi"]
medical=["jayparkinson","EricTopol","Bob_Wachter","healthewoman","DrLindaMD","MotherinMed"]
actor=["aamirkhan","juniorbachchan","ajaydevgn","SrBachchan","akshaykumar","Riteishd","RanveerOfficial"]
entrepreneur=["RNTata2000","anandmahindra","SinghaniaGautam","NandanNilekani","RonnieScrewvala"]
scientist=["kinggary","starstryder","JFGariepy","BobMetcalfe"]
sports=["ImRo45","mVkohli","ImRaina","imjadeja","ImZaheer","Gvanderwiel","RobbieSavage8","themichaelowen","cesc4official","Cristiano"]
artist=["artistsmagazine","artistsnetwork","wcamag","pasteljournal"]
activist=["befeqe","BehrouzBoochani","LibyaLiberty","noansereiboth"]
writing=["Shteyngart","ejucole","JoyceCarolOates","paulocoelho","oedunthorne"]
security=["Troyhunt","e_kaspersky","StewartRoom","mikko","joshcorman","lutasecurity"]
hr=["trishmcfarlane","steveboese","thelance","billkutik","kris_dunn","beneubanks","robinschooling"]
bank=[ "Iamsamirarora", "rohitchauhan","Vivek_Investo", "trengriffin",  "jvembuna,AustinValue"]

def main(names):
    enginner_count=0
    lawyer_count=0
    teacher_count=0
    architect_count=0
    police_count=0
    politics_count=0
    medical_count=0
    actor_count=0
    entrepreneur_count=0
    scientist_count=0
    sports_count=0
    artist_count=0
    activist_count=0
    writing_count=0
    security_count=0
    hr_count=0
    bank_count=0
    total={}
    for name in names:
        if name in enginner:
            print("follows a engineer")
            enginner_count=enginner_count+1
        if name in lawyer:
            print("follows a lawyer")
            lawyer_count=lawyer_count+1
        if name in teacher:
            print("follows a teacher")
            teacher_count=teacher_count+1
        if name in architect:
            print("follows a architect")
            architect_count=architect_count+1
        if name in police:
            print("follows a police")
            police_count=police_count+1
        if name in politics:
            print("follows a politics")
            politics_count=politics_count+1
        if name in medical:
            print("follows a medical")
            medical_count=medical_count+1
        if name in actor:
            print("follows a actor")
            actor_count=actor_count+1
        if name in entrepreneur:
            print("follows a entrepreneur")
            entrepreneur_count=entrepreneur_count+1
        if name in scientist:
            print("follows a scientist")
            scientist_count=scientist_count+1
        if name in sports:
            print("follows a sports")
            sports_count=sports_count+1
        if name in artist:
            print("follows a artist")
            artist_count=artist_count+1
        if name in activist:
            print("follows a activist")
            activist_count=activist_count+1
        if name in writing:
            print("follows a writing")
            writing_count=writing_count+1
        if name in security:
            print("follows a security")
            security_count=security_count+1
        if name in hr:
            print("follows a hr")
            hr_count=hr_count+1
        if name in bank:
            print("follows a bank")
            bank_count=bank_count+1
    total["bank"]=bank_count
    total["enginner"]=enginner_count
    total["sports"]=sports_count
    total["lawyer"]=lawyer_count
    total["teacher"]=teacher_count
    total["architect"]=architect_count
    total["police"]=police_count
    total["politics"]=politics_count
    total["medical"]=medical_count
    total["actor"]=actor_count
    total["entrepreneur"]=entrepreneur_count
    total["scientist"]=scientist_count
    total["artist"]=artist_count
    total["activist"]=activist_count
    total["writing"]=writing_count
    total["security"]=security_count
    total["hr"]=hr_count
    sort_orders = sorted(total.items(), key=lambda x: x[1], reverse=True)
    Final_Occup=[sort_orders[0][0],sort_orders[1][0]]
    if total[sort_orders[0][0]] == 0:
        Final_Occup[0]='Null'
    if total[sort_orders[1][0]] == 0:
        Final_Occup[1]='Null'
    
    return Final_Occup
#name=["ImRo45","mVkohli","ImRaina","imjadeja","ImZaheer","RobbieSavage8","themichaelowen","starstryder","TeachtoLead"]
#total=main(name)
#print(total)
