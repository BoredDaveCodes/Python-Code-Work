#Legislation
print("===============================================")
print("           Educational Legislational")
print("===============================================")
print("Welcome to Educational Legislational, where you learn about legislations, so you know what is against the laws, regulations and legislations in the UK!")
print("")
def thingyfortopicsndstuff():
    print("Legislation Topics:\n"
        "1. Health and Safety at Work Act\n"
        "2. Display Screen Equipment\n"
        "3. Computer Misuse Act\n"
        "4.Data Security and Protection Legislation\n"
        "5. Equality Act\n"
        "6. Copyrights, Designs and Patents Act\n")
    print("What topic would you like to learn about? (1 - 6)")
    topic = int(input("Topic: "))
    while True:
        if topic == 1:
            print("Health and Safety at Work Act:\n"
            "\n"
            "This regulated legislation is all about being safe at work or in a work enviroment.\n"
            "This means that employers must make sure that they provide staff with the training that they need to do their job that they have  been allocated, employees should also have the right equipment provided for them by their empolyer e.g. PPE \n"
            "Employers should also ensure an adequate welfare provision, and provide information, instruction and advice\n"
            "Although there are no legal actions that happen if you go against Health and Safety code in your work place or enviroment, if rules are broken it may result in injury to yourself or others, however, you may be reprimanded by your employer.")
            break
        if topic == 2:
            print("Display Screen equipment:\n"
            "This legislation outlines to the employer what they should provide at work if your main job is using a screen.\n"
            "You should also take breaks from your screen, as it may cause lasting eye damage.\n"
            "Employers may provide eye tests if being on a screen is your whole job, and they have to provide training and allow access to equipment that you may need to do your job.\n"
            "You and your employer must make sure that you reduce risks to employees health, such as cable being in the middle of the floor, which is a tripping hazard.\n"
            "Risks may include: Adequate training (e.g., Fire Safety Training), Making sure there is a safe working enviroment, and making sure safe working practices are being practiced.")
            break
        if topic == 3:
            print("The Computer Misuse act 1990:\n"
            "The computer misuse act are laws and legislations that ensure that theres is no tomfoolery or illegal practices happening with work devices or another persons devices.\n"
            "This means that if you were to use someones device without permisson, you may end up in prison or with a heafty fine, the same applies with unautorised access and being prepared to do damage. and unauthorised access and having done damage.\n"
            "This act allows both people and entities (e.g., businesses etc) to be prosecuted.")
            break
        if topic == 4:
            print("Data Security and Protection Legislation:\n"
            "These regulations, laws and regulations ensure that all data is protected for example:\n"
            "General Data Protection regulations ensure Lawfulness, Fairness, Transparency, Accuracy, Storage Limitations, Integrity, Confidentiality, and Accountability. This makes sure your data is safe and up to date, and it also ensures that you know what data is held.\n"
            "Data Proteciton Act:\n"
            "This act provides guidance under legislation as to what is expected: Protected, Private, Be transparent to users about their data, Keep it up-to-date.")
            break
        if topic == 5:
            print("Equality act:\n"
            "This act ensures that everybody is treated equally and ensures that employers ensure that they can provide access for everyone in the work place or space.\n"
            "The 9 protected Characteristics include: Age, Paternity/maternity status or leave, Marital/relationship status, Gender reassignment, Sex, Sexual oridentation, Disability, Race/Ethnicity, Religion/Belief.\n"
            "These characteristics are protected by law, meaning that discrimination that is targeted to these characteristics is illegal.\n"
            "There are also multiple types of discrimimation: Direct, indirect, harrassment and victimisation.\n"
            "Equity vs Equality:\n"
            "Equity - providing access to different resources based on needs so that everyone can have equal access to things.\n"
            "Equality - treating everybody equally.")
            break
        if topic == 6:
            print("Intellectual property:\n" \
            "This law protects property that is licenced so that people cannot steal it. However it is not an international law meaning that the licence will only be covered for the country you are in.\n" \
            "Copyright - this is a legal right that protects creative works e.g. art\n" \
            "Patent - a patent is a legal right that is granted to an inventor of a porduct, this allows the inventer to have control to stop people form using, making or selling it as their own.\n" \
            "There are many different laws and protective licences all around the world that are similar to these.")
            break
        if topic == " ":
            print("You need to enter a number 1 - 6!")
            continue 
        else:
            print("Nothing with this number!")
            break

thingyfortopicsndstuff()