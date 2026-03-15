string=input("Enter a string to count vowerls,consonants,digits,special characters = ")

countA=string[0:].count("a")+string[0:].count("A")
countE=string[0:].count("e")+string[0:].count("E")
countI=string[0:].count("i")+string[0:].count("I")
countO=string[0:].count("o")+string[0:].count("O")
countu=string[0:].count("U")+string[0:].count("U")

if(not ((string[0:]!="e" or string[0:]!="e") and (string[0:]!="i" or string[0:]!="I") and (string[0:]!="o" or string[0:]!="O") and (string[0:]!="u" or string[0:]!="U") and (string[0:]!="a" or string[0:]!="A")) ):
    print(f"{string[0:].count}")
    


total=countA+countE+countI+countO+countu




print(f"Vowels in a string ={total} ")
