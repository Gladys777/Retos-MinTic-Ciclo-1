import csv, json

def solucion():
    
    archivo=open('TESLA.csv')
    x=csv.reader(archivo)
    Date=[]
    Open=[]
    High=[]
    Low=[]
    Close=[]
    Adj_Close=[]
    Volume=[]
    
    next(x,None)
    for i in x:
        Date.append(i[0])
        Open.append(float(i[1]))
        High.append(float(i[2]))
        Low.append(float(i[3]))
        Close.append(float(i[4]))
        Adj_Close.append(float(i[5]))
        Volume.append(int(i[6]))
    
    archivo.close()
    x=len(Date)
    alza=[]
    Abs=[]
    s=[]
    for i in range(x):
        operacion=Close[i]-Open[i]
        Abs.append(abs(Close[i]-Adj_Close[i]))
        s.append(abs(Low[i]-High[i]))
        if operacion>0:
            alza.append('SUBE')
        elif operacion<0:
            alza.append('BAJA')
        elif operacion==0:
            alza.append('ESTABLE')
   
    with open('analisis_archivo.csv','w') as file:
        file.write('Fecha\tComportamiento de la accion\tAjuste Cuadratico de Close\n')
        for i in range(x):
            file.write('%s\t' % Date[i])
            file.write('%s\t' % alza[i])
            file.write('%s\n' % Abs[i])
        file.close()
    
    lista={}
    lowest=min(Open)
    highest=max(Close)
    mean=sum(Volume)/len(Volume)
    greatest=max(s)
    
    for i in range(x):
        if  Open[i]==lowest:
            lista['date_lowest_open']=Date[i]
            lista['lowest_open']=lowest
        if Close[i]==highest:
            lista['date_highest_close']=Date[i]
            lista['highest_close']=highest
        lista['mean_volume']=mean
        if s[i]==greatest:
            lista['date_greatest_difference']=Date[i]
            lista['greatest_difference']=greatest
    with open('detalles.json','w') as file:
        json.dump(lista,file)
    