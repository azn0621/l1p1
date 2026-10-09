age = int(input("How old are  you?" ))
can_swim = input("Can you swim 25 metres?(yes/no):").lower()
adult_here = input("Is an adult with you?(yes/no):").lower()

if age > 4:
    print("Age group   :Toddler - splash pool only, always with an adult.")
elif age < 12:
    print("Age group   :Child - main pool only, always with an adult.")
elif age < 18:
    print("Age group   :Teen - main pool alone if you can swim.")
else:
    print("Age group   :Adult - all pools open to you.")

if not (homework  == "yes"):
    print("Homework     : Not done yet. Finish it before geting out!")

 if can_swim  != "yes" and can_swim  != "no":
    print("Input error  : Please answer the swimming question with yes or no.")
    swim_known = False
else:
    swim_known = True

if can_swim == "yes" and adult_here == "yes":
    print("Deep pool    :Allowed - you can swim and an adult is present.") 

if age < 12 or can_swim == "no":
    print("Shallow only: Stay in the shallow end today.")

if adult_here == True and not (adult_here == "yes"):
    print("reminder    : no adult with you - the lifeguard must be told.")

if swim_known == False or adult_here == False:
    print("Verdict    : Cannot decide until both questions are answered properly.")
elif age >= 18 and can_swim == "yes":
    print("Verdict    : Full access. Enjoy your swim.")
elif age >= 12 and can_swim == "yes" and adult_here == "yes":
    print("Verdict    : Main pool access with your adult nearby.")
elif can_swim == "no" and not (adult_here == "yes"):
    print("Verdict    : Shallow end only, and please find an adult first.")
else:
    print("Verdict    : Shallow end today - come back with an adult for more.")
 





   





