size=5
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper_line = "-e-"
right= ""
left= "" 

for i in range(1,size):
    line = (2*(size-i)-1)*"-" + upper_line +(2*(size-i)-1)*"-"
    upper_line = left+ "-" +(alphabet[size-i])+"-"+alphabet[size-i-1]+"-"+ (alphabet[size-i])+"-"+right
    right =(alphabet[size-i])+"-"+ right
    left = left + "-" + (alphabet[size-i])

    print(line)