'''
Kozlowski, L.P. IPC – Isoelectric Point Calculator. Biol Direct 11, 55 (2016). https://doi.org/10.1186/s13062-016-0159-9
http://fields.scripps.edu/DTASelect/20010710-pI-Algorithm.pdf
'''
def isoelectric_point(protein_seq):
    AspNumber,GluNumber,CysNumber,TyrNumber,HisNumber,LysNumber,ArgNumber=0,0,0,0,0,0,0
    for x in protein_seq:
        if x=='D':
            AspNumber+=1
        if x=='E':
            GluNumber+=1
        if x=='C':
            CysNumber+=1
        if x=='Y':
            TyrNumber+=1
        if x=='H':
            HisNumber+=1
        if x=='K':
            LysNumber+=1
        if x=='R':
            ArgNumber+=1
    net_charge=0.0
    qn1,qn2,qn3,qn4,qn5,qp1,qp2,qp3,qp4=0,0,0,0,0,0,0,0,0
    pH=6.5
    pHprev=0.0
    pHnext=14.0
    x=0.0
    E=0.01
    temp=0.0
    while True:
        qn1=-1/(1+pow(10,(3.65-pH)))
        qn2=-AspNumber/(1+pow(10,(3.9-pH)))
        qn3=-GluNumber/(1+pow(10,(4.07-pH)))
        qn4=-CysNumber/(1+pow(10,(8.18-pH)))
        qn5=-TyrNumber/(1+pow(10,(10.46-pH)))
        qp1=HisNumber/(1+pow(10,(pH-6.04)))
        qp2=1/(1+pow(10,(pH-8.2)))
        qp3=LysNumber/(1+pow(10,(pH-10.54)))
        qp4=ArgNumber/(1+pow(10,(pH-12.48)))
        net_charge=qp1+qp2+qp3+qp4+qn1+qn2+qn3+qn4+qn5
        if pH>=14.0:
            print('pH greater than 14.00')
            break
        if net_charge<0:
            temp=pH
            pH=pH-((pH-pHprev)/2)
            pHnext=temp
        else:
            temp=pH
            pH= pH + ((pHnext-pH)/2)
            pHprev=temp
        if ((pH-pHprev<E) and (pHnext-pH<E)):
            break
    return pH

