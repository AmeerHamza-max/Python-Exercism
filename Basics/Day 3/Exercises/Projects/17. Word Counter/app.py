# It does not included spaces
string1=input("Enter a string = ")
counter=1
while  counter < len(string1)-1:
    
    if( string1[0:] == " "):
        continue
    else:
     counter=counter+1
print(counter)
    
