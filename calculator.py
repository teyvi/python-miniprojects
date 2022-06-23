weight = input("Type Weight:")
unit = input ("(K)" or "(L)")
if unit.upper == "K"
   converted = weight/0.45
   print('Weight in Lbs:" + converted)
else:
    converted = weight * 0.45
    print("Weight in Kgs: "+ converted)   
