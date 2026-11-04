import string
alpha=[c for c in string.ascii_uppercase if c!='J']
for name,a in (('J-less',alpha),('full',list(string.ascii_uppercase))):
    groups=[[4,5,9,13,5,13],[7,5,11,9,5,2,19,5,13],[2,17,1,20,19,9,7,1,12]]
    print(name,' '.join(''.join(a[n-1] for n in g) for g in groups))
