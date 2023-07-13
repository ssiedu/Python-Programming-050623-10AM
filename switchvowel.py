ch=input("Enter any character :")
match ch.lower():
    case 'a'|'e'|'i'|'u'|'o':
        print("Vowel")
    case _:
        print("Consonant")
