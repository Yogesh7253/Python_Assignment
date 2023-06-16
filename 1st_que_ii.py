import json
dict1 = {'Haryana':'Chandigarh','Maharashtra':'Mumbai','Karnataka':'Bangluru','Rajasthan':'Jaipur','Uttar Pradesh':'Lucknow','Gujarat':'Gandhinagar','Goa':'Panaji'}
file = open(r"C:\Users\Hp\OneDrive\Desktop\Edyoda Practice\Edyoda Python Assignment 6\assignment_7_file.json","w")
json.dump(dict1,file)