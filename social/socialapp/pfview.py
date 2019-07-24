
tdays=31

wages=float(input("Enter wages per Day:"))
leavs=int(input('enter leavs in month'))

basic=(tdays-leavs)*wages

HRA=basic*0.1
DA=basic*0.05
PF=basic*0.12  
netsalary=basic+HRA+DA-PF
print(basic,HRA,DA,PF,netsalary)



def epf(basic,pf):
    pf=basic-4%
    return