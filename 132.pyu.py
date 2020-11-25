postalCode = {
    "A":"Newfoundland", "B":"Nova Scotia", "C":"Prince Edward Island", \
    "E":"New Brunswick", "G":"Quebec", "H":"Quebec", "J":"Quebec", "K":"Ontario",\
    "L":"Ontario", "M":"Ontario", "N":"Ontario", "P":"Ontario",\
    "R":"Manitoba", "S":"Saskatchewan", "T":"Alberta", "V":"British Columba",\
    "X":"Nunavut or Northwest Territories", "Y":"Yukon"
}

p = input()
p=p.upper()
if (p[0] not in postalCode) or not ("0" <= p[1] <= "9"):
    print("This is not a valid POSTAL CODE")
else:
    address = ""
if p[1] == "0":
    address = "a rural"
else:
    address = "an urban"
print(f"That postal code is corresponds to {address} address in ",f"{postalCode[p[0]]}.")