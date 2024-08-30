# assuming that the whether two strings are complementary is not case sensitive
str1 = input("Enter the first string \n").lower()
str2 = input("Enter the second string \n").lower()

def is_complement(s1,s2):
    for i in range(len(s1)):
        if(s1[i] in s2):
            return False
    return True

if(is_complement(str1,str2)):
    print("The strings are complementary")
else:
    print("The strings are not complementary")