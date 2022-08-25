#Trying to fin the address using ONLY string methods

Mary="From Rome-Italy, e-mail address maryling46@outlook.com"

Mary_email=Mary.find("@")
Mary_email_start=Mary.find("address ")

print(Mary_email) #42
print(Mary_email_start) #24
print(len("address "))#8
print(Mary[Mary_email_start+8:len(Mary)])