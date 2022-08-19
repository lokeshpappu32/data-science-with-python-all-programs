import re
text="python are g1ulareexpressions."
#ans=re.search("ula",text)
#ans=re.findall("re",text)
#ans=re.findall("[a-z]",text)
    #output:['i', 'h', 'e', 'l', 'l', 'o', 'y', 'o', 'u', 'a', 'r', 'e', 'l', 'e', 'a', 'r', 'n', 'i', 'n', 'g', 'p', 'y', 't', 'h', 'o', 'n', 'r', 'e', 'g', 'u', 'l', 'a', 'r', 'e', 'x', 'p', 'r', 'e', 's', 's', 'i', 'o', 'n', 's']
#ans=re.findall("[A-Z]",text)
#ans=re.findall("\d",text)
#ans=re.findall("\s",text)
#ans=re.findall("[rse]",text)
#ans=re.sub("are","ARE",text)

#ans=re.search("s.*",text)
ans=re.split("python",text)#divides the given string from given pattern
print(ans)
