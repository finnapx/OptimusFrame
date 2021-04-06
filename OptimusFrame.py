import matplotlib.pyplot as plt

tabla = {
    'head': [
        ['fila', 'perfil', 'combo', 'nodo', 'axial', 'corte', 'momento'],
        ['[kg]', '[kg]', '[kg-m]']
    ],
    'body': [
        ['COL', 1, '1.4 D', 'i', 83310.57, -3518.34, -3901.6325],
        ['j', 74805.57, -3518.34, 6653.387900000001],
        ['COL', 1, '1.2 D + L', 'i', 101635.11, -5166.32, -5724.1502],
        ['j', 94345.11, -5166.32, 9774.8033],
        ['COL', 1, '1.2 D + 1.6 L', 'i', 119770.75, -6456.68, -7152.0865],
        ['j', 112480.75, -6456.68, 12217.9429],
        ['COL', 1, '1.2 D + 1.4 E + L', 'i', 60104.67, 23702.1, 75561.23610000001],
        ['j', 52814.67, 23702.1, 4454.9499],
        ['COL', 1, '1.2 D - 1.4 E + L', 'i', 143165.56, -34034.73, -87009.5365],
        ['j', 135875.56, -34034.73, 15094.65import matplotlib.pyplot as plt
import temp as t

tabla=t.tabla['body']

def filtroCV(combis, combi_e, combi_s, tab, largosV, largosC):

    bars1=[[tab[i-1]+tab[i] for j in range(2) if j==1]
            for i in range(len(tab)) if i%2!=0]
    bars2=[bars1[i][0] for i in range(len(bars1))]
    bars=[[bars2[i] for i in range(combis*j, combis*j+combis)]
            for j in range(int(len(bars2)/combis))]

    exc=[]
    for i in range(len(bars)):
        temp1=[]
        maxim=0
        for j in range(len(bars[0])):
            for k in range(len(bars[0][0])):
                if bars[i][j][4]/bars[i][j][6]>bars[i][j][8]/bars[i][j][10]:
                    pu=bars[i][j][4]
                    mu=bars[i][j][6]
                else:
                    pu=bars[i][j][8]
                    mu=bars[i][j][10]
                ex=mu/pu
                if ex>maxim:
                    maxim=ex
                    list1=[round(mu,1), round(pu,1), round(ex,3)]
        temp1.append(list1)
        exc.append(temp1)

    bars_e1=[bars2[i] for i in range(len(bars2)) if 'E' in bars2[i][2]]
    bars_s1=[bars2[i] for i in range(len(bars2)) if 'E' not in bars2[i][2]]
    bars_e=[[bars_e1[i] for i in range(combi_e*j, combi_e*j+combi_e)]
            for j in range(int(len(bars_e1)/combi_e))]
    bars_s=[[bars_s1[i] for i in range(combi_s*j, combi_s*j+combi_s)]
            for j in range(int(len(bars_s1)/combi_s))]
    col_e=[[bars_e[j][i] for i in range(0, combi_e)] for j in range(len(bars_e))
            if bars_e[j][0][0]=='COL']
    col_s=[[bars_s[j][i] for i in range(0, combi_s) if bars_s[j][i][2]!='1.2 D + L']
            for j in range(len(bars_s)) if bars_s[j][0][0]=='COL']

    col_dl=[[bars_s[j][i] for i in range(0, combi_s) if bars_s[j][i][2]=='1.2 D + L']
            for j in range(len(bars_s)) if bars_s[j][0][0]=='COL']
    vig_e=[[bars_e[j][i] for i in range(0, combi_e)]
            for j in range(len(bars_e)) if bars_e[j][0][0]=='VIGA']
    vig_s=[[bars_s[j][i] for i in range(0, combi_s)if bars_s[j][i][2]!='1.2 D + L']
            for j in range(len(bars_s)) if bars_s[j][0][0]=='VIGA']
    vig_dl=[[bars_s[j][i] for i in range(0, combi_s)if bars_s[j][i][2]=='1.2 D + L']
            for j in range(len(bars_s)) if bars_s[j][0][0]=='VIGA']

    maTrix_ij = lambda lista:[[[round(lista[k][j][i],1) for j in range(len(lista[0]))]
                               for i in [5,9]] for k in range(len(lista))]
    maxTrix_i = lambda lista:[[round(max([lista[k][j][i] for j in range(len(lista[0]))]),2)
                               for i in [4,5,6]] for k in range(len(lista))]
    minTrix_i = lambda lista:[[round(min([lista[k][j][i] for j in range(len(lista[0]))]),2)
                               for i in [4,5,6]] for k in range(len(lista))]
    maxTrix_j = lambda lista:[[round(max([lista[k][j][i] for j in range(len(lista[0]))]),2)
                               for i in [8,9,10]] for k in range(len(lista))]
    minTrix_j = lambda lista:[[round(min([lista[k][j][i] for j in range(len(lista[0]))]),2)
                               for i in [8,9,10]] for k in range(len(lista))]

    npisos, nbahias = len(col_e)-len(vig_e), int(len(vig_e)/(len(col_e)-len(vig_e)))


    forma_col = lambda lista, nbahias, npisos:[
        [lista[j] for j in range(i*(nbahias+1), (i+1)*(nbahias+1))] for i in range(npisos)]
    forma_vig = lambda lista, nbahias, npisos:[
        [lista[j] for j in range(i*(nbahias), (i+1)*(nbahias))] for i in range(npisos)]

    exc = forma_col(exc[:len(col_e)],nbahias, npisos)

    max_col_ei = forma_col(maxTrix_i(col_e),nbahias,npisos)
    max_col_si = forma_col(maxTrix_i(col_s),nbahias,npisos)
    max_col_dli = forma_col(maxTrix_i(col_dl),nbahias,npisos)

    min_col_ei = forma_col(minTrix_i(col_e),nbahias,npisos)
    min_col_si = forma_col(minTrix_i(col_s),nbahias,npisos)
    min_col_dli = forma_col(minTrix_i(col_dl),nbahias,npisos)

    max_col_ej = forma_col(maxTrix_j(col_e),nbahias,npisos)
    max_col_sj = forma_col(maxTrix_j(col_s),nbahias,npisos)
    max_col_dlj = forma_col(maxTrix_j(col_dl),nbahias,npisos)

    min_col_ej = forma_col(minTrix_j(col_e),nbahias,npisos)
    min_col_sj = forma_col(minTrix_j(col_s),nbahias,npisos)
    min_col_dlj = forma_col(minTrix_j(col_dl),nbahias,npisos)

    mat_col_e = forma_col(maTrix_ij(col_e),nbahias,npisos)
    mat_col_s = forma_col(maTrix_ij(col_s),nbahias,npisos)

    max_vig_ei = forma_vig(maxTrix_i(vig_e),nbahias,npisos)
    max_vig_si = forma_vig(maxTrix_i(vig_s),nbahias,npisos)
    max_vig_dli = forma_vig(maxTrix_i(vig_dl),nbahias,npisos)

    min_vig_ei = forma_vig(minTrix_i(vig_e),nbahias,npisos)
    min_vig_si = forma_vig(minTrix_i(vig_s),nbahias,npisos)
    min_vig_dli = forma_vig(minTrix_i(vig_dl),nbahias,npisos)

    max_vig_ej = forma_vig(maxTrix_j(vig_e),nbahias,npisos)
    max_vig_sj = forma_vig(maxTrix_j(vig_s),nbahias,npisos)
    max_vig_dlj = forma_vig(maxTrix_j(vig_dl),nbahias,npisos)

    min_vig_ej = forma_vig(minTrix_j(vig_e),nbahias,npisos)
    min_vig_sj = forma_vig(minTrix_j(vig_s),nbahias,npisos)
    min_vig_dlj = forma_vig(minTrix_j(vig_dl),nbahias,npisos)

    mat_vig_e = forma_vig(maTrix_ij(vig_e),nbahias,npisos)
    mat_vig_s = forma_vig(maTrix_ij(vig_s),nbahias,npisos)

    matCorte_col=[mat_col_e,mat_col_s]
    matCorte_vig=[mat_vig_e,mat_vig_s]

    #'axial', 'corte', 'momento'
    listaV=[]
    for i in range(len(max_vig_ei)):
        lista1=[]
        lista2=[]
        for j in range(len(max_vig_ei[i])):
            lista1=[[round(max_vig_si[i][j][1]/1000,2), round(max_vig_ei[i][j][1]/1000,2),
                     round(max(max_vig_ei[i][j][2],max_vig_si[i][j][2])/1000,2),
                     round(min(min_vig_ei[i][j][2],min_vig_si[i][j][2])/1000,2),round(max_vig_dli[i][j][1]/1000,2),
                     largosV[i][j],mat_vig_s[i][j][0],mat_vig_e[i][j][0]],
                    [round(max_vig_sj[i][j][1]/1000,2), round(max_vig_ej[i][j][1]/1000,2),
                     round(max(max_vig_ej[i][j][2],max_vig_sj[i][j][2])/1000,2),
                     round(min(min_vig_ej[i][j][2],min_vig_sj[i][j][2])/1000,2),round(max_vig_dlj[i][j][1]/1000,2),
                     largosV[i][j],mat_vig_s[i][j][1],mat_vig_e[i][j][1]]]
            lista2.append(lista1)
        listaV.append(lista2)
    listaC=[]
    for i in range(len(max_col_ei)):
        lista1=[]
        lista2=[]
        for j in range(len(max_col_ei[i])):

            lista1=[[round(max(max_col_ei[i][j][0], max_col_si[i][j][0])/1000,2),
                     round(min(min_col_ei[i][j][0], min_col_si[i][j][0])/1000,2), round(max_col_si[i][j][1]/1000,2),
                     round(max_col_ei[i][j][1]/1000,2), round(max(max_col_ei[i][j][2],max_col_si[i][j][2],
                                              abs(min_col_ei[i][j][2]),abs(min_col_si[i][j][2]))/1000,2),
                     largosC[i][j],mat_col_s[i][j][0],mat_col_e[i][j][0]],
                    [round(max(max_col_ej[i][j][0], max_col_sj[i][j][0])/1000,2),
                     round(min(min_col_ej[i][j][0], min_col_sj[i][j][0])/1000,2), round(max_col_sj[i][j][1]/1000,2),
                     round(max_col_ej[i][j][1]/1000,2), round(max(max_col_ej[i][j][2],max_col_sj[i][j][2],
                                              abs(min_col_ej[i][j][2]),abs(min_col_sj[i][j][2]))/1000,2),
                     largosC[i][j],mat_col_s[i][j][1],mat_col_e[i][j][1]]]
            lista2.append(lista1)
        listaC.append(lista2)
    # lista_aux=[listaC[-1][j][:6] for j in range(len(listaC[0]))]
    # return [listaV,listaVmax, listaC, listaCmax]
    return [listaV, listaC, exc]
    # return [listaV, listaC, exC, lista_aux]


# print(filtroCV(combis, combi_e, combi_s, tab, largosV, largosC))

def V2vig(x1, lo, vuLsti, vueLsti, vuLstj, vueLstj, vupr, vc, state):
    vc = vc if state==1 else 0
    v2Calc = lambda v1, v2, x1, lo: round(v1 - x1 * (v1 - v2) / lo, 1)
    vupr2 = v2Calc(vupr,-vupr,x1,lo)/0.75-vc
    vu2 = max([v2Calc(vuLsti[i],vuLstj[i], x1, lo) for i in range(len(vuLsti))])/0.75-vc
    vue2 = max([v2Calc(vueLsti[i],vueLstj[i], x1, lo) for i in range(len(vueLsti))])/0.6
    return round(max(vupr2,vu2, vue2),1)

def b1(fc):
    if 550 >= fc >= 280:
        return round(0.85-0.05/70*(fc-280), 2)
    else:
        return 0.85 if fc < 280 else 0.65

def et(h,eu,dp,c): return round(eu*abs(h-dp-c)/c, 4)

def aCir(d): return round(0.007854*d**2, 3)

def phi(eu,et,ey):
    if ey <= et <= (eu+ey):
        return round(0.65+0.25/eu*(et-ey), 2)
    else:
        return 0.65 if et < ey else 0.9

def aLstC(dEsq,dLat,nHor,nVer):
    a = round(aCir(dEsq)*2+nHor*aCir(dLat), 3)
    return [a]+[round(aCir(dLat)*2,3) for i in range(nVer)]+[a]

def yLstC(dp,h,nVer):
    yLst = [dp]
    for i in range(1,nVer+1):
        yi = round((h-yLst[i-1]-dp)/(nVer+2-i)+yLst[i-1],0)
        yLst.append(int(yi))
    yLst.append(h-dp)
    return yLst

def pmC(aLst,b,b1,c,es,eu,ey,fc,fy,h,yLst):
    eiLst = [round(eu*(c-i)/c, 5) for i in yLst]
    fsLst = [fy*abs(i)/i if abs(i)>ey else es*i for i in eiLst]
    psLst = [fsLst[i] * aLst[i] for i in range(len(aLst))]
    Pc = 0.85*b1*fc*b*c
    Ps = sum(psLst)
    Mc = Pc/2*(h-0.85*c)
    Ms = sum((psLst[i]*(h/2-yLst[i]) for i in range(len(aLst))))
    return [round((Pc+Ps)/1000, 2), round((Mc+Ms)/100000, 2)]

def cPn(aLst,b,b1,dp,es,eu,ey,fc,fy,h,pnB,yLst):
    c1 = 0
    c2 = max(h/b1, 3*(h-dp))
    PnMax = round((0.85*fc*(h*b-sum(aLst))+sum(aLst)*fy)/1000, 2)
    PhiPnMax = PnMax*0.8*0.65
    PnMin = round((-sum(aLst)*fy)/1000, 2)
    PhiPn = pnB+10
    i = 0
    if pnB > PnMin * 0.9:
        pnB = PhiPnMax if pnB >= PhiPnMax else pnB
        while abs(pnB-PhiPn) > 0.1 and i<15:
            c = round((c1+c2)/2,3)
            i += 1
            PMC = pmC(aLst,b,b1,c,es,eu,ey,fc,fy,h,yLst)
            eT = et(h,eu,dp,c)
            Phi = phi(eu,eT,ey)
            PhiPn = (PMC[0])*Phi
            PhiMn = (PMC[1])*Phi
            c2 = c if PhiPn > pnB else c2
            c1 = c if PhiPn < pnB else c1
    else:
        c = 0
        PhiPn = PnMin*0.9
        PhiMn = 0
        Phi = 0.9
    return [round(c, 2), abs(round(PhiMn, 1)), round(PhiPn, 1), Phi]

def cFind(aLst, b, b1, dp, es, eu, ey, fc, fy, h, mu, pu, yLst):
    mu = round(abs(mu),3)
    pu = round(pu,3)
    PhiPnMin = round((-sum(aLst)*fy)/1000*0.9,1)
    PhiPnMax = round((0.85*fc*(h*b-sum(aLst))+sum(aLst)*fy)*0.8*0.65/1000,1)
    if pu<PhiPnMin:
        pu = PhiPnMin
    if pu>PhiPnMax:
        pu = PhiPnMax
    elif abs(pu) <= 0.1:
        return cPn(aLst,b,b1,dp,es,eu,ey,fc,fy,h,0,yLst)
    e = min(mu/pu,999)
    i = 0
    c2 = 0
    ex = e+1
    c1 = h/b1 if e > 0 else cPn(aLst,b,b1,dp,es,eu,ey,fc,fy,h,0,yLst)[0]
    while abs(round(e,3)-ex) > 0.001 and i < 15:
        c = round((c1+c2)/2,2)
        i += 1
        PMC = pmC(aLst,b,b1,c,es,eu,ey,fc,fy,h,yLst)
        ex = round((abs(PMC[1]))/(PMC[0]),3)
        c1 = c if ex < e else c1
        c2 = c if ex > e else c2
    e = ex
    eT = round(eu*abs(h-dp-c)/c,4)
    Phi = phi(eu,eT,ey)
    asdf=pmC(aLst,b,b1,c,es,eu,ey,fc,fy,h,yLst)
    phipn = PMC[0]*Phi
    phimn = PMC[1]*Phi
    return [c,abs(round(phimn,1)),round(phipn,1), Phi, e, PhiPnMin, PhiPnMax]

def resumen(aLst, c, b, dp, h, eu, fy, fc, b1, es, ey, yLst):
    PMC = pmC(aLst, b, b1, c, es, eu, ey, fc, fy, h, yLst)
    eT = round(eu*abs(h-dp-c)/c, 4)
    Phi = phi(eu, eT, ey)
    PMCpr = pmC(aLst, b, b1, c, es, eu, ey, fc, fy*1.25, h, yLst)
    return [PMC[0]*Phi,PMC[0],PMCpr[0],PMC[1]*Phi,PMC[1],PMCpr[1]]

def FU(pu, mu, pn, mn):
    if abs(mu) < 0.1:
        return abs(pu/(pn+0.01))
    else:
        return max(abs(pu/(pn+0.01)), abs(mu/(mn+0.01)))

def yLstV(h, dp, db):
    # se busca el minimo de niveles barras laterales complementarias
    blat = min(int((h-2*dp-db/4)/25), int((h-2*dp-db/4)/20)+1)
    # se crea lista con dos primeros niveles (1/4*10=2.5 veces el diámetro mayor)
    Y = [dp, max(dp+db/4, 2*dp)]
    #se agrega cada nivel de barras complementarias
    for i in range(blat):
        Y.append(round(Y[-1]+(h-2*dp-db/4)/(blat+1), 0))
    # la función retorna la lista de posiciones de barras completa
    return Y + [h - dp] if Y[-1] < (h-dp) else Y

# función para el cálculo de área requerida asegurando et>=0.005
def areaV(mu, b, b1, h, fc, fy, dp):
    muu = round(mu/(0.9*0.85/100000*fc*b*(h-dp)**2), 3)
    muu = 0.5 if muu > 0.5 else muu
    ulim = round(0.375*b1*(1-0.1875*b1), 3)
    wp = 0 if muu < ulim else round((muu-ulim)/(1-dp/(h-dp)), 3)
    w = 0.375+wp if wp > 0 else round(1-(1-2*muu)**0.5, 3)
    return round(w*0.85*fc*b*(h-dp)/fy, 2)

def listadiam1(A, b, dp, h, dList, v):
    sup = [i for i in range(int(1+(b-2*dp)/15), 2+int((b-2*dp)/10))]
    listadiam = []
    for i in sup:
        n2 = int(i/2) if i>2 else 0
        n1 = i-n2
        for j in range(len(dList)):
            j = dList[j]
            if n2>0:
                for k in range(len(dList)):
                    k = dList[k]
                    if A<=n1*aCir(j)+n2*aCir(k) and j+v>=k>=j-v:
                        listadiam+=[[n1, j, n2, k, round(aCir(j)*n1+aCir(k)*n2, 2)]]
                    else:
                        continue
            else:
                if 1.2*A>=n1*aCir(j)>=A:
                    listadiam+=[[n1, j, n2, 0, round(n1*aCir(j), 2)]]
                else:
                    continue
    return listadiam

def listadiam(A, b, dp, h, dList, v):
    amin = 10*A
    A /= 2
    lista1 = listadiam1(A, b, dp, h, dList, v)
    lista2 = []
    minimos = []
    for i in range(len(lista1)):
        if lista1[i][4]<=1.2*A:
            lista2+=[lista1[i]]
        else:
            continue
    for i in range(len(lista2)):
        L1 = lista2[i]
        ar1= L1[4]
        ar2=round(2*A-ar1, 2)
        ar2 = ar2 if ar2>0 else 0
        lista3 = listadiam1(ar2, b, dp, h, dList, v)
        if lista3 == []:
            continue
        for j in range(len(lista2)):
            L2 = lista3[i]
            if 2*A>L1[4]+L2[4]:
                continue
            else:
                if L1[4]+L2[4]<amin:
                    amin = L1[4]+L2[4]
                    if L2[4]>L1[4]:
                        minimos = [L2, L1, round(amin, 2)]
                    else:
                        minimos = [L1, L2, round(amin, 2)]
    return minimos


def critVC(vigas,columnas):
    newcol=[]
    for i in range(len(vigas)-1):
        new=[]
        for j in range(len(vigas[0])):
            if i == 0:
                mc1=columnas[i][j]
                mc2=columnas[i+1][j]
                mv1=vigas[i][j][0]
                mc=mc1+mc2
                dif=1.2*mv1-mc
                if dif > 0:
                    columnas[i][j]=dif*mc1/(mc1+mc2)+mc1
                    columnas[i+1][j]=dif*mc2/(mc1+mc2)+mc2
            elif i == len(vigas[0])-1:
                mc1 = columnas[i][j]
                mc2 = columnas[i + 1][j]
                mv2 = vigas[i][j][1]
                mc = mc1 + mc2
                dif = 1.2 * mv2 - mc
                if dif > 0:
                    columnas[i][j] = dif * mc1 / (mc1 + mc2) + mc1
                    columnas[i+1][j] = dif * mc2 / (mc1 + mc2) + mc2
            else:
                mc1 = columnas[i][j]
                mc2 = columnas[i+1][j]
                mv1 = vigas[i][j][0]
                mv2 = vigas[i][j][1]
                mc = mc1 + mc2
                dif = 1.2 * (mv1+mv2) - mc
                if dif > 0:
                    columnas[i][j] = dif * mc1 / (mc1 + mc2) + mc1
                    columnas[i+1][j] = dif * mc2 / (mc1 + mc2) + mc2
        newcol.append(new)
    newcol.append(columnas[-1])
    return newcol

def extMat(lista, indice):
    mat1=[]
    for i in lista:
        mat2=[]
        for j in i:
            mat2.append(j[indice])
        mat1.append(mat2)
    return mat1

def replMat(lista1, lista2, indice):
    for i in range(len(lista2)):
        for j in range(len(lista2[i])):
            lista1[i][j][indice]=lista2[i][j]
    return lista1

def matElemV(lista, bmaxV, hmaxV, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, ai, deList, v):
    #se itera en la lista
    listaV = []
    for i in lista:
        # se filtra la lista por piso
        tempV=[]
        for j in i:
            elem = optimusVig(j[2],j[3],es,eu,ey,b1,fc,fy,dp,dList,hmaxV,bmaxV,ai,j[5],cH,cS,v)
            tempV.append(elem)
        listaV.append(tempV)
    return listaV

def Lramas(xList):
    lar=len(xList)
    lista = [xList[0]]
    if lar%2 == 0:
        rango = xList[-1]-xList[0]
        for i in range(1, lar-1):
            if xList[i]-lista[-1]==30:
                lista.append(xList[i])
            elif xList[i]-lista[-1]>30:
                lista.append(xList[i-1])
        lista.append(xList[-1])
        minram = int((len(lista)+1)/2)*2
        maxram = len(xList)
        rlist = [i for i in range(minram, maxram+1, 2)]
        listas = []
        for i in rlist:
            sep = round(rango/(i-1), 1)
            complist = [xList[0]]
            for _ in range(i-1):
                complist.append(sep+complist[-1])
            lista2 = [xList[0]]
            for j in range(1, len(complist)-1):
                dif=999
                for k in xList:
                    if abs(k-complist[j])<dif:
                        dif = abs(k-complist[j])
                        bar = k
                lista2.append(bar)
            lista2.append(xList[-1])
            listas.append(lista2)
    else:
        mid = int(lar/2)
        midL = xList[0:mid+1]
        rango=midL[-1]-midL[0]
        for i in range(1, len(midL)-1):
            if midL[i]-lista[-1]==30:
                lista.append(midL[i])
            elif midL[i]-lista[-1]>30:
                lista.append(midL[i-1])
        lista.append(midL[-1])
        if lista[-2]-(xList[0]+xList[-1])/2<=15:
            lista.remove(lista[-1])
        lista2 = []
        for j in reversed(lista):
            lista2.append(xList[-1]+xList[0]-j)
        lista+=lista2
        listas=[lista]
        minram=2
        maxram=len(xList)
        rlist=[i for i in range(minram, maxram+1)]
        for i in rlist:
            sep = round(rango/(i-1), 1)
            complist = [xList[0]]
            rango=xList[-1]-xList[0]
            for _ in range(i-1):
                complist.append(sep+complist[-1])
            lista2 = [xList[0]]
            for j in range(1, len(complist)-1):
                dif=999
                for k in xList:
                    if abs(k-complist[j])<dif:
                        dif = abs(k-complist[j])
                        bar = k
                lista2.append(bar)
            lista2.append(xList[-1])
            if rlist[0]==i:
                continue
            else:
                listas.append(lista2)
    listas2=[]
    for i in listas:
        borrar = 0
        for j in range(1, len(i)):
            if i[j]-i[j-1]>30:
                borrar=1
        if borrar!=1:
            listas2.append(i)
    return listas2

def estribosV(xList, ramas):
    Lestrib = []
    medio = xList[int(len(xList)/2)]
    for j in ramas:
        mid=int(len(j)/2)
        L1 = j[0:mid]
        if len(j)%2!=0:
            L2 = j[mid+1:]
            cond=1
        else:
            L2 = j[mid:]
            cond=0
        estribos=[[L1[i],L2[i]] for i in range(len(L1))]
        if cond==1:
            estribos+=[[medio]]
        Lestrib.append(estribos)
    return Lestrib

def ldC(fy,fc,db):
    return round(max(0.075*fy*0.1*db/(fc)**0.5, 0.0044*fy*0.1*db),1)

def ldV(db, fc, fy):
    if db<19:
        return 0.1*db*fy/(3.46*(fc)**0.5)
    else:
        return 0.1*db*fy/(4.4*(fc)**0.5)

def lempV(db, fc, fy):
    if db<19:
        ld = 0.1*db*fy/(6.6*(fc)**0.5)
    else:
        ld = 0.1*db*fy/(5.34*(fc)**0.5)
    return ld

def ldhV(fy, db, fc):
    return fy*db/(170*(fc)**0.5)

def lGanchoC(db, fc, fy, h, dp):
    if db<19:
        ld = round(max(0.1*db*fy/(3.46*(fc)**0.5), 2.5*db+10),1)
        return [round(ldC(fy,fc,db)+0.6*3.1416/4*db+ld,1), ld]
    else:
        ld = round(max(0.1*db*fy/(4.4*(fc)**0.5), 2.5*db+10))
        return [round(ldC(fy,fc,db)+0.6*3.1416/4*db+ld,1), ld]

def lGanchoV(fy, db, fc):
    return round(ldhV(fy,db,fc)+1.05*db-5,1)

def rematC(db, ldV, h, dp):
    return max(2.5*db+10, ldV+dp-h)

def aminV(fc,b,fy):
    return max(0.2*(fc)**0.5*b/fy,3.5*b/fy)

def countram(ramas):
    nramas=[]
    for i in ramas:
        nramas+=[len(i)]
    return nramas

def Lest(h, b, dp, de):
    return round((2*(h+b-4*dp+0.2*de)*10+6.75*de*3.1416+2*max(75, 6*de))/10, 2)

def Ltrab(h, dp, de):
    return round((3.75*de*3.1416+2*max(75, 6*de)+(h+0.2*de-dp)*10)/10, 2)

def vc(fc, b, h, dp):
    return round(0.53*(fc)**0.5*b*(h-dp)/1000, 2)

def ashS(h, b, dp, fc, fy):
    return round(max(0.3*((b*h)/((h-dp)*(b-dp)))*(fc/fy), 0.09*(h-dp)*fc/fy), 3)

def loCol(h, b, H):
    return round(max(h, b, H/6, 45), 1)

def lEmp(fy, db):
    return round(max(0.00073*fy*db if fy<= 4200 else (0.0013*fy-2.4)*db, 30),0)

#wo es corte y no carga distribuida
def vprV(h, b, l, mpr1, mpr2, wo):
    return 100*(mpr1+mpr2)/l + wo/50

def VcAx(Nu, fc, b, h, dp):
    return round(0.53*(1+Nu*1000/(140*h*b))*(fc)**0.5*b*(h-dp)/1000, 1)

def vsLim(fc, b, h, dp):
    return round(2.2*(fc)**0.5*b*(h-dp)/1000,2)

def sRotV(h, dp, db):
    return round(max(min(15, 0.6*db, (h-dp)/4),8), 1)

def sRotC(h, b, db, hx):
    return round(min(max(min(15,0.6*db,(10+(35-hx)/3)),8),10),1)

def sMax(fc, b, h, dp, sm):
    return min(round((h-dp)/4 if vc(fc, b, h, dp)>0.33*(h-dp)*b*(fc/10)**0.5 else (h-dp)/2, 2), sm)

def sEmp(h, dp):
    return round(min(10, (h-dp)/4), 1)

def sCol(db):
    return min(0.6*db, 15)

def cubEstV(h, dp, de, Le):
    lista1 = []
    lista2 = []
    for i in Le:
        if len(i)%2 == 0:
            b = i[1]-i[0]
            lista1 += [Lest(h, b, dp, de)]
        else:
            lista2 += [Ltrab(h, dp, de)]
    return [round((sum(lista1)+sum(lista2))*aCir(de) ,1), lista1, lista2]

def estribosC(xList):
    lista = []
    ramas = Lramas(xList)
    count = []
    for i in ramas:
        count.append(len(i))
        Lestrib = []
        temp = i
        while len(temp) > 0:
            if len(temp) >= 2:
                Lestrib.append([temp[0],temp[-1]])
                temp.remove(temp[0])
                temp.remove(temp[-1])
            elif len(temp) == 1:
                Lestrib.append([temp[0]])
                temp.remove(temp[0])
            else:
                break
        lista.append(Lestrib)
        Lestrib = []
    return lista, count

def xLst(sup, b, dp):
    mid = int(sup[0] / 2)
    if sup[2]%2==0:
        l1=[sup[1] for i in range(mid)]
        l2=[sup[3] for i in range(sup[2])]
    else:
        l1=[sup[1] for i in range(mid)]
        l2=[sup[3] for i in range(sup[2])]
    lista=l1+l2+l1
    xList=yLstC(dp, b, len(lista)-2)
    return lista, xList

#revisar

def minEstC(mpr1, mpr2, Nu, H, vu, vue, yList, deList, db, h, b, dp, fy, fc, cS):
    salida1, salida2, salida3 = 0, 0, 0
    H*=100
    vu = vu*1000
    vue = vue*1000
    mpr1*=100000
    mpr2*=100000
    Vc = VcAx(Nu, fc, b, h, dp)*1000
    vupr = round((mpr1+mpr2)/H,1)
    vupr1 = vupr if Nu*1000 < 0.05 * fc * (h * b) else vupr-Vc
    vupr2 = vupr-Vc
    vu1 = round(max((vu-Vc)/0.75, vue/0.6, vupr1/0.75),1)
    vslim = vsLim(fc, b, h, dp)*1000*1.1
    lo = loCol(h, b, H)
    vu2 = round(max((vu-Vc)/0.75, vue/0.6, (vupr1-Vc)/0.75), 1)
    s = round(sCol(db))
    estr = estribosC(yList)
    est = estr[0]
    nRam = estr[1]
    ramas = Lramas(yList)
    if len(ramas)>1:
        srotL = [int(sRotC(h, b, db, l)) for l in [min(k) for k in [[i[j]-i[j-1] for j in range(1,len(i))] for i in ramas]]]
    else:
        ramitas = ramas[0]
        aux1=[ramitas[i]-ramitas[i-1] for i in range(1,len(ramitas))]
        srotL =  [int(sRotC(h, b, db, max(aux1)))]

    sash = round(max(ashS(h, b, dp, fc, fy),aminV(fc,b,fy)), 3)

    s1L = [[i, j, k, l] for i in range(len(nRam)) for j in deList for l in deList if l <= j
           for k in range(8, min(int(sRotC(h, b, db, srotL[i])), int(round(100/((sash * 100 / (2 * aCir(j) + (nRam[i] - 2) * aCir(l)))-1), 1))+1))
           if vu1 <= round((2*aCir(j)+(nRam[i]-2)*aCir(l))*fy*(h-dp)/k, 1) <= vslim]

    if s1L==[]:
        return 0
    minimo = 99999999
    for i, j, k, l in s1L:
        ramas1 = est[i]
        l1 = Lest(h, ramas1[0][1]-ramas1[0][0], dp, j)
        l2 = sum([Lest(h, ramas1[m][1]-ramas1[m][0], dp, l) if len(ramas1[m])==2 else Ltrab(h, dp, l)
                  for m in range(1,len(ramas1))])
        s1 = int((lo-0.01)/k)+1
        costo = round(2*s1*(l1*aCir(j)+2*l2*aCir(l))*cS/1000000, 0)
        if costo<minimo:
            minimo=costo
            l2a = [Lest(h, ramas1[m][1] - ramas1[m][0], dp, l) if len(ramas1[m]) == 2 else Ltrab(h, dp, l)
                   for m in range(1, len(ramas1))]
            lram = ramas1
            lista1=[costo, nRam[i], j, k, l, s1, l1, l2a, l2, lram, lo]
            salida1=1
    l_rot = lista1[3]
    l_emp = lEmp(fy, db)
    # s2L = [[i, j, k, l] for i in range(len(nRam)) for j in deList for k in range(10, s+1) for l in deList
    #        if vu2<=round((2*aCir(j)+(nRam[i]-2)*aCir(l))*fy*(h-dp)/k, 1) <= vslim and l <= j]
    s2L = [[i, j, k, l] for i in range(len(nRam)) for j in deList for l in deList if l <= j
           for k in range(10, min(int(s), int(round(100/((sash * 100 / (2 * aCir(j) + (nRam[i] - 2) * aCir(l)))-1), 1)))+1)
           if vu2 <= round((2*aCir(j)+(nRam[i]-2)*aCir(l))*fy*(h-dp)/k, 1) <= vslim]
    if s2L==[]:
        return 0
    minimo = 99999999
    for i, j, k, l in s2L:
        ramas1 = est[i]
        l1 = Lest(h, ramas1[0][1] - ramas1[0][0], dp, j)
        l2 = sum([Lest(h, ramas1[m][1] - ramas1[m][0], dp, l) if len(ramas1[m]) == 2 else Ltrab(h, dp, l)
                  for m in range(1, len(ramas1))])
        s2 = int((H-2*lo-l_emp-0.01)/k)
        dist2 = H-2*lo-l_emp
        costo = round(s2*(l1*aCir(j)+2*l2*aCir(l))*cS/1000000, 0)
        if costo<minimo:
            minimo=costo
            l2a = [Lest(h, ramas1[m][1] - ramas1[m][0], dp, l) if len(ramas1[m]) == 2 else Ltrab(h, dp, l)
                   for m in range(1, len(ramas1))]
            lram = ramas1
            lista2=[costo, nRam[i], j, k, l, s2, l1, l2a, l2, lram, dist2]
            salida2=1
    semp = int(sEmp(h, dp))
    # s3L = [[i, j, k, l] for i in range(len(nRam)) for j in deList for k in range(8, semp+1) for l in deList
    #        if vu2<=round((2*aCir(j)+(nRam[i]-2)*aCir(l))*fy*(h-dp)/k, 1) <= vslim and l <= j]
    s3L = [[i, j, k, l] for i in range(len(nRam)) for j in deList for l in deList if l <= j
           for k in range(8, min(int(semp), int(round(100/((sash * 100 / (2 * aCir(j) + (nRam[i] - 2) * aCir(l)))-1), 1))+1))
           if vu2 <= round((2*aCir(j)+(nRam[i]-2)*aCir(l))*fy*(h-dp)/k, 1) <= vslim]
    if s3L==[]:
        return 0
    minimo = 99999999
    for i, j, k, l in s3L:
        ramas1 = est[i]
        l1 = Lest(h, ramas1[0][1] - ramas1[0][0], dp, j)
        l2 = sum([Lest(h, ramas1[m][1] - ramas1[m][0], dp, l) if len(ramas1[m]) == 2 else Ltrab(h, dp, l)
                  for m in range(1, len(ramas1))])
        s3 = int((l_emp-0.01)/k)+1
        costo = round(s3*(l1*aCir(j)+2*l2*aCir(l))*cS/1000000, 0)
        if costo < minimo:
            minimo = costo
            l2a = [Lest(h, ramas1[m][1] - ramas1[m][0], dp, l) if len(ramas1[m]) == 2 else Ltrab(h, dp, l)
                   for m in range(1, len(ramas1))]
            lram = ramas1
            lista3 = [costo, nRam[i], j, k, l, s3, l1, l2a, l2, lram, l_emp]
            salida3=1
    costo_total = lista1[0]+lista2[0]+lista3[0]
    # lista1 --> [costo, n° ramas, de_externo, espaciamiento, de_interno, n° estribos, largo1, largos2, largo_tot2, d_ramas, dist]
    # lista2 --> [costo, n° ramas, de_externo, espaciamiento, de_interno, n° estribos, largo1, largos2, largo_tot2, d_ramas, dist]
    # lista3 --> [costo, n° ramas, de_externo, espaciamiento, de_interno, n° estribos, largo1, largos2, largo_tot2, d_ramas, dist]
    salida=salida1+salida2+salida3
    if salida == 3:
        return [lista1,lista2,lista3,costo_total,vu1,vu2]
    else:
        return 0

def optimusCol(b1, dp, es, eu, ey, fc, fy, muC, muCmin, puCmin, puCmax, dList, hmax, hmin, cH, cS, H, vu, vue, deList, iguales):
    salida=0
    minor = 9999999
    hmin = hmin if hmin >= 30 else 30
    hmax = hmax if hmax>=30 else 30
    hList = [i for i in range(hmin, hmax+5,5)]
    lista = ([b, h] for b in hList for h in hList if b == h)
    for b, h in lista:
        nH = [i for i in range(int((b-2*dp)/15)-1, int(round((b-2*dp)/10, 0)), 1)]
        nV = nH
        listaND = ([j, k] for j in nH for k in nV if 10 <= (b-2*dp)/(j+1) <= 15 and
                   10 <= (h-2*dp)/(k+1) <= 15 and j == k)
        for j, k in listaND:
            if iguales == 0:
                listaDm = ([l, m] for l in dList for m in dList if m <= l >=16)
            else:
                listaDm = ([l, m] for l in dList for m in dList if m == l >= 16)
            for l, m in listaDm:
                ylist = yLstC(dp, h, k)
                alist = aLstC(l, m, j, k)
                cF = cFind(alist, b, b1, dp, es, eu, ey, fc, fy, h, muC, puCmax, ylist)
                cF2 = cFind(alist, b, b1, dp, es, eu, ey, fc, fy, h, muCmin, puCmin, ylist)
                fu = round(FU(puCmax, muC, cF[2], cF[1])*100,1)
                fu2 = round(FU(puCmin, muCmin, cF2[2], cF2[1])*100,1)
                aS = aCir(l)*4+aCir(m)*(2*j+2*k)
                cuan = round(aS/(b*h), 5)
                mpr1 = max(pmC(alist, b, b1, cF[0], es, eu, ey, fc, fy*1.25, h, ylist)[1],
                           pmC(alist, b, b1, cF2[0], es, eu, ey, fc, fy*1.25, h, ylist)[1])
                mpr2 = mpr1
                #agregar a entrada H, vu, vue, deList
                if fu < 95 and fu2 < 95 and 0.01 <= cuan <= 0.06:
                    corte1 = minEstC(mpr1, mpr2, muC, H, vu, vue, ylist, deList, min(l, m), h, b, dp, fy, fc, cS)
                    if corte1 != 0:
                        costo1 = round((aS*cS+(b*h-aS)*cH)/10000, 0)*(corte1[2][10]+H*100)/100
                        costo2 = corte1[3]
                        costo = costo1+costo2
                        if costo < minor:
                            # corte = minEstC(mpr1, mpr2, muC, H, vu, vue, ylist, deList, min(l, m), h, b, dp, fy, fc, cS)
                            minor, e = costo, round(cF[1] / (cF[2] + 0.001), 3)
                            optimo = [minor, h, b, j, k, l, m, fu, fu2, cuan, cF[0], cF2[0], e, alist, ylist, cF[1],
                                      cF[2], muC, puCmax, puCmin, H, iguales, round(muCmin/puCmin,3), cF2[1], cF2[2], costo1, costo2, dp]
                            salida=1
                            corte=corte1
                    else:
                        continue
    if salida==1:
        return [optimo, corte]
    else:
        return 0

def minEstV(mpr1, mpr2, vuLsti,vueLsti,vuLstj,vueLstj, xList, deList, db, h, b, lo, dp, fy, fc, cS, wo, yLst):
    lo*=100
    Vc = vc(fc, b, h, dp)*1000
    vupr = round(vprV(h, b, lo, mpr1, mpr2,wo),3)*1000
    smax = sMax(fc, b, h, dp, 20)
    srot = int(sRotV(h, dp, db))
    sL1 = [i for i in range(8, int(srot)+1)]
    sL2 = [i for i in range(8, int(smax)+1)]
    vsL = vsLim(fc, b, h, dp)*1000*1.1
    ramas = Lramas(xList)
    est = estribosV(xList, ramas)
    nRam = countram(ramas)
    x1 = 2*h
    x2 = lo/2-2*h
    amin=aminV(fc,b,fy)
    Lout=[]
    for n in range(x1, x1 + 35, 5):
        xa1 = n
        xa2 = (x1 + x2) - xa1
        vsB1 = V2vig(0,lo,vuLsti,vueLsti,vuLstj,vueLstj,vupr,Vc,0)
        vsB2 = V2vig(xa1,lo,vuLsti,vueLsti,vuLstj,vueLstj,vupr,Vc,1)
        lista=[[i,j,k,l,m] for i in nRam for j in sL1 for k in deList for l in nRam
        for m in sL2 if vsB1/(fy*(h-dp))<=i*aCir(k)/j<=vsL/(fy*(h-dp))
        and vsB2/(fy*(h-dp))<=l*(aCir(k))/m<=vsL/(fy*(h-dp)) and i*aCir(k)>amin]
        minim = 999999999
        if lista!=[]:
            for i in lista:
                nr1, s1, de, nr2, s2 = i
                Lest1 = est[nRam.index(nr1)]
                Lest2 = est[nRam.index(nr2)]
                LestH = Ltrab(b, dp, de)
                ns1=int((xa1*2)/s1)
                ns2=int((xa2-0.01)*2/s2)+1
                nsH=ns1+ns2
                numH=len(yLst)-2
                cub1=cubEstV(h, dp, de, Lest1)
                cub2=cubEstV(h, dp, de, Lest2)
                mini = (cub1[0]*ns1+cub2[0]*ns2+LestH*nsH*numH)*cS/1000000
                X1 = xa1-5 if xa1 > 2*h else 2*h
                X2 = 2*((x1+x2)-X1)
                if mini < minim:
                    minim = round(mini, 2)
                    #[costo, dist rot, n° ramas, espaciamiento, n° estribos, dist de rotula al centro, n° ramas, espaciamiento, n° estribos, de]
                    Lout = [minim, X1, nr1, s1, ns1, X2, nr2, s2, ns2, de, vsB1, vsB2, cub1, cub2, nsH, numH, LestH]
    return Lout

def optimusVig(mpp,mnn,es,eu,ey,b1,fc,fy,dp,dList,dimV,ai,lo,cH,cS,v,allVu,deList,wo):
    di = (ai*200/3.1416)**0.5
    mnn=abs(mnn)
    salida=0
    minim = 999999999
    hmax = dimV[0] if dimV[0]>=30 else 30
    bmax = dimV[1] if dimV[1]>=25 else 25
    hmin = dimV[2] if dimV[2]<=30 else 30
    bmin = dimV[3] if dimV[3]<=25 else 25
    hList = [i for i in range(hmin, hmax+5,5)]
    bList = [i for i in range(bmin, bmax+5,5)]
    lista = ([i, j] for i in hList if i >= 100*lo/16 for j in bList if i >= j and j >= 0.4*i)
    for h, b in lista:
        A1 = areaV(mpp, b, b1, h, fc, fy, dp)
        # print(A1)
        A2 = areaV(mnn, b, b1, h, fc, fy, dp)
        # print(A2)
        L1 = listadiam(A1, b, dp, h, dList, v)
        if L1==[]:
            continue
        L2 = listadiam1(A2, b, dp, h, dList, v)
        mi1 = 10*A2
        lis=[]
        for i in range(len(L2)):
            L=L2[i]
            if L[4]<mi1:
                mi1=L[4]
                lis = L
        if lis==[]:
            continue
        db = max(L1[0][1], L1[0][3])
        db2 = max(L2[0][1], L2[0][3])
        gancho = round(lGanchoV(fy, db, fc),1)
        gancho2 = round(lGanchoV(fy, db2, fc), 1)
        gancho3 = round(lGanchoV(fy, di, fc),1)
        db12 = round(1.2*db,1)
        db122 = round(1.2 * db2, 1)
        nbarG = L1[0][0]+L1[0][2]+L1[1][0]+L1[1][2]+lis[0]+lis[2]
        traslp1=round(lempV(db, fc, fy),1)
        traslp2=round(lempV(db2, fc, fy),1)
        remate=round(ldC(fy,fc,db),1)
        remate2=round(ldC(fy,fc,db2),1)
        ylst = list(yLstV(h, dp, db))
        ylstrev = [(h-i) for i in reversed(ylst)]
        aSLst = [L1[0][4], L1[1][4]]+[ai for i in range(len(ylst)-3)]+[lis[4]]
        alstrev = [lis[4]]+[ai for i in range(len(ylst)-3)]+[L1[1][4], L1[0][4]]
        cuanT = round(sum(aSLst)/(h*b-sum(aSLst)), 4)
        cumin = round(max(0.8/fy*(fc**0.5), 14/fy), 4)
        cuan1 = round((aSLst[0]+aSLst[1])/((b*(h-dp))), 4)
        cuan2 = round(aSLst[-1]/((b*(h-dp))), 4)
        cpn = cPn(aSLst, b, b1, dp, es, eu, ey, fc, fy, h, 0, ylst)
        cpnrev = cPn(alstrev, b, b1, dp, es, eu, ey, fc, fy, h, 0, ylstrev)
        c = cpn[0]
        cond = False
        eT = round(eu*abs(h-dp-c)/c, 4)
        mpr1 = pmC(aSLst, b, b1, cpn[0], es, eu, ey, fc, fy * 1.25, h, ylst)[1]
        mpr2 = pmC(alstrev, b, b1, cpnrev[0], es, eu, ey, fc, fy * 1.25, h, ylstrev)[1]
        db = min([L1[0][1] if L1[0][1]>0 else 99
                 ,L1[0][3] if L1[0][3]>0 else 99
                 ,lis[1] if lis[1]>0 else 99
                 ,lis[3] if lis[3]>0 else 99])
        sup=L1[0]
        xlistV = xLst(sup, 30, 5)[1]
        FU = round(max(mnn / cpn[1], mpp / cpnrev[1]) * 100, 1)
        if 0.025 >= cuan1 >= cumin and 0.025 >= cuan2 >= cumin\
                and cpn[1] >= mnn and cpnrev[1] >= mpp and 85<=FU<=95:
            cond = True
            costo = round((sum(aSLst)*cS+(h*b-sum(aSLst))*cH)/10000, 0)
            if costo < minim and cond != False:
                minim = costo
                FU = round(max(mnn/cpn[1], mpp/cpnrev[1]) * 100, 1)
                listaT = [minim, h, b, aSLst, ylst, cuan1, cuan2, ylstrev, alstrev,c , round(abs(mnn),2),
                          round(abs(mpp),2), L1, lis, cpn[1], cpnrev[1], max(cpn[1],cpnrev[1]), lo, FU,
                          db2, gancho, db12, nbarG, traslp1, traslp2, remate, db122, remate2, gancho2, xlistV]
                corte = minEstV(mpr1,mpr2,allVu[0],allVu[1],allVu[2],allVu[3],xlistV,deList, db,h,  b, lo, dp, fy, fc, cS, wo, ylst)
                salida = 1
    if salida == 1:
        return [listaT, corte]
    else:
        return 0

def XYplotCurv(alst, b, h, dp, eu, fy, fc, b1, es, ey, ylst, ce, mu, pu, mn, pn, titulo):
    PnMax = round((0.85*fc*(h*b-sum(alst))+sum(alst)*fy)/1000, 2)
    PnMaxPr = round(PnMax+sum(alst)*fy*0.25/1000, 2)
    PnMin = sum(alst)*-fy/1000
    phiPnMin = 0.9*sum(alst)*-fy/1000
    PnMinPr = 1.25*sum(alst)*-fy/1000
    C = [0]+[i/50*h for i in range(2, 51)]
    X1 = [0]
    X2 = [0]
    X3 = [0]
    Y1 = [phiPnMin]
    Y2 = [PnMin]
    Y3 = [PnMinPr]
    for c in C[1::]:
        res = resumen(alst, c, b, dp, h, eu, fy, fc, b1, es, ey, ylst)
        X1.append(res[3])
        Y1.append(res[0])
        X2.append(res[4])
        Y2.append(res[1])
        X3.append(res[5])
        Y3.append(res[2])
    X1.append(0)
    X2.append(0)
    X3.append(0)
    Y1.append(Y1[-1])
    Y2.append(PnMax)
    Y3.append(PnMaxPr)
    fig = plt.figure(figsize=[4,6], dpi=200)
    plt.plot(X1, Y1, label='ØMn - ØPn', color='steelblue')
    plt.plot(X2, Y2, label='Mn - Pn', color='crimson')
    plt.plot(X3, Y3, label='Mpr - Ppr', color='forestgreen')
    plt.plot([mu], [pu], marker='x', markersize=10, color='red', label='Mu - Pu', lw='1')
    res1 = resumen(alst, ce, b, dp, h, eu, fy, fc, b1, es, ey, ylst)
    plt.plot([0, mu], [0, pu], ls='--', color='black')
    # plt.plot([mu, mn], [pu, pn], ls='--', color='gray')
    plt.xlabel('Mn[tonf-m]')
    plt.xlim([0, max(X3)+0.1])
    plt.ylabel('Pn[tonf]')
    plt.title(titulo)
    plt.legend()
    plt.grid()
    # plt.show()
    # fig.savefig(titulo)
    return 0


largosC=[[3,3,3,3],
         [3,3,3,3],
         [3,3,3,3],
         [3,3,3,3]]

largosV=[[7,7,7],
         [7,7,7],
         [7,7,7],
         [7,7,7]]

dimV = [[[65,40,25,25],[65,40,25,25],[65,40,25,25]],
        [[65,40,25,25],[65,40,25,25],[65,40,25,25]],
        [[65,40,25,25],[65,40,25,25],[65,40,25,25]],
        [[65,40,25,25],[65,40,25,25],[65,40,25,25]]]

nbahias=len(largosV[0])

def matElemV(lista, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, ai, deList, v):
    #se itera en la lista
    listaV = []
    for i in range(len(lista)):
        # se filtra la lista por piso
        tempV=[]
        for j in range(len(lista[0])):
            ultimo = 1 if i == len(lista)-1 else 0
            elem = optimusVig(lista[i][j][0],lista[i][j][1],es,eu,ey,b1,fc,fy,dp,dList,
                              lista[i][j][5],ai,lista[i][j][3],cH,cS,v,lista[i][j][4],deList,lista[i][j][2])
            cont=0
            while elem == 0 and cont<10:
                cont+=1
                lista[i][j][0]=lista[i][j][0]*1.1
                lista[i][j][1]=lista[i][j][1]*1.1
                elem = optimusVig(lista[i][j][0], lista[i][j][1], es, eu, ey, b1, fc, fy, dp, dList,
                                  lista[i][j][5], ai, lista[i][j][3], cH, cS, v, lista[i][j][4], deList, lista[i][j][2])
            tempV.append(elem)
        listaV.append(tempV)
    return listaV

cH, cS, b1, dp, es, ey, eu, fc, fy = 75000,7850000,0.85,5,2100000,0.002,0.003,250,4200
dList, deList = [16,18,22,25,28,32,36],[10,12]

def detVig(detvig, nbahias, hCol):
    # agregar lista de barras horizontales
    di = 8
    ai = 1
    contv = 0
    npisos=len(detvig)
    print("Reporte de diseño y cubicación de la estructura")
    print("\ncantidad pisos",npisos)
    print("cantidad vigas tipo por piso",len(detvig[0]), "\n\n")
    for i in detvig:
        for j in i:

            hcol=hCol[contv][0]

            """ Identificador """

            contv+=1
            print("Viga n° ",contv)
            print("Viga tipo del piso", contv,"\n\n")

            """Dimensiones"""

            print("Dimensiones\n")
            print("Largo : ", j[0][17], "[m]")
            print("Alto : ",j[0][1], "[cm]")
            print("Ancho : ",j[0][2], "[cm]\n")

            """Refuerzo longitudinal"""

            print("Refuerzo longitudinal\n")
            print("Armadura superior principal")
            numB2=" barras" if j[0][12][0][2]>1 else " barra"
            barr2 = "" if j[0][12][0][2]==0 else ", "+str(j[0][12][0][2])+str(numB2)+" Ø "+\
                                                 str(j[0][12][0][3])+"[mm] en la posición y = "+\
                                                 str(j[0][4][0])+" [cm], área = "+str(j[0][3][0])+" [cm2]"
            print(j[0][12][0][0],"barras Ø",j[0][12][0][1],"[cm]",barr2)
            print("Traslapo superior=", j[0][23], "cm")

            print("\nArmadura suplementaria")
            numB3 = " barras" if j[0][12][0][2] > 1 else " barra"
            barr3 = "" if j[0][12][1][2] == 0 else ", " + str(j[0][12][1][2])+str(numB3)+\
                                                   " Ø "+str(j[0][12][1][3])+"[mm] en la posición y = "+\
                                                   str(j[0][4][1])+" [cm], área = "+str(j[0][3][1])+" [cm2]"
            print(j[0][12][1][0], "barras Ø", j[0][12][1][1],"[cm]",barr3)
            if len(j[0][3])>3:
                print("\nArmadura lateral")
                for i in range(len(j[0][3])-3, len(j[0][3])-1):
                    print("2 barras Ø",di,"[mm] en la posición y = ",j[0][4][i],"cm, área = ",ai,"[cm2]")
            print("\nArmadura inferior principal")
            numB4 = " barras" if j[0][13][2] > 1 else " barra"
            barr4 = "" if j[0][13][2] == 0 else ", " + str(j[0][13][2])+str(numB3)+" Ø "+str(j[0][13][3])+\
                                                "[mm] en la posición y = "+str(j[0][4][-1])+" [cm], área = "+\
                                                str(j[0][3][-1])+" [cm2]"
            print(j[0][13][0], "barras Ø", j[0][13][1],"[cm]",barr4,"\n")


            """Cuantías"""

            print("\nCuantías")
            print("Superior = ",j[0][5])
            print("Inferior = ",j[0][6],"\n")


            print("Cubicación de acero en barras longitudinales.\n")

            print("Largos de suples : ")
            print("0.25lo : ", round(25*j[0][17],1),"[cm]")
            print("0.3lo : ",round(30*j[0][17],1),"[cm]")
            print("Ancho columnas : ", hcol, "[cm]")
            rem = 0 if contv < npisos else round(j[0][25]-j[0][21],1)
            lSupl = 2*(round(0.25 * j[0][17], 1)+j[0][20]/100)+(nbahias-1)*round(hcol/100+0.3*j[0][17],1)
            print("Longitud total de suples superiores : ",round(lSupl*100,1),"[cm]")
            print("Área de barras pertenecientes a suples : ",j[0][12][1][4],"[cm2]")
            print("Volumen de acero de suples : ",round(lSupl*100,1)*j[0][12][1][4],"[cm3]\n")


            Larm1 = round(2*j[0][20]+(j[0][23]+j[0][17]*100)*nbahias+(nbahias-1)*hcol,1)
            Larm2 = round(2*j[0][28]+(j[0][24]+j[0][17]*100)*nbahias+(nbahias-1)*hcol,1)
            print("Longitud de armadura superior : ",Larm1,"[cm]")
            print("Longitud de traslapo de armadura superior : ",j[0][23],"[cm]\n")
            print("Desarrollo total de remate de gancho : ",j[0][20],"[cm]")
            print("Área de barras de la armadura superior : ", j[0][12][0][4], "[cm2]")
            print("Volumen de acero de armadura superior : ",round(Larm1*j[0][12][0][4],1),"[cm3]\n")

            print("Longitud de armadura inferior : ", Larm2, "[cm]")
            print("Longitud de traslapo de armadura inferior : ", j[0][24], "[cm]")
            print("Desarrollo total de remate de gancho : ", j[0][27], "[cm]")
            print("Área de barras de la armadura superior : ", j[0][13][4], "[cm2]")
            print("Volumen de acero de armadura superior : ", round(Larm2*j[0][13][4],1),"[cm3]\n")


            print("Por simplificación del cálculo tendrá la misma longitud que la armadura superior.")
            print("Longitud de armadura lateral : ", Larm1, "[cm]")
            print("Longitud de traslapo de armadura lateral : ",j[0][23],"[cm]")
            print("Área de barras laterales : ", ai*(len(j[0][3])-3), "[cm2]")
            print("Volumen de acero de armadura lateral : ", round(Larm1*ai*(len(j[0][3])-3),1), "[cm3]")

            volLong = round((lSupl*100*j[0][12][1][4]+Larm1*j[0][12][0][4]+Larm2*j[0][13][4]+Larm1*ai*(len(j[0][3])-3))/1000000,3)

            pAs = 7850
            pesoLong = round(pAs*volLong,1)

            print("Volumen total del barras longitudinales en el piso : ",volLong,"[m3]")
            print("Peso del acero : ",pesoLong,"[kg]\n")


            """Refuerzo transversal"""

            print("Refuerzo transversal")
            print("\nZonas de rótula plástica, de 0 a",j[1][1],"[cm] y ",j[0][17]*100-j[1][1],"a",j[0][17]*100,"[cm]:")
            print("Diámetro : ",j[1][9],"[cm]")
            print("N° ramas : ",j[1][2])
            cont=0
            print("Estribos =",len(j[1][12][1]))
            for i in j[1][12][1]:
                cont+=1
                print("Largo de estribo n°",cont,"=",i,"[cm]")
            if j[1][12][2]!=[]:
                print("Traba central: si")
                print("Largo de traba =",j[1][12][2][0],"[cm]")
            else:
                print("Traba central: no")
            print("Espaciamiento : ",j[1][3],"[cm]")
            print("N° estribos : ",int(round(j[1][4]/2,0))," en cada extremo")
            print("Volumen de acero en zona de rótulas plásticas : ",)

            print("\nZonas central, de ",j[1][1],"a",j[0][17]*100-j[1][1],"[cm]:")
            print("Diámetro : ", j[1][9], "[cm]")
            print("N° ramas : ", j[1][6])
            cont=0
            for i in j[1][13][1]:
                cont+=1
                print("Largo de estribo n°",cont,"=",i,"[cm]")
            if j[1][13][2]!=[]:
                print("Traba central: si")
                print("Largo de traba =",j[1][13][2][0],"[cm]")
            else:
                print("Traba central: no")
            print("Espaciamiento : ", j[1][7],"[cm]")
            print("N° estribos : ", j[1][8],"\n")

            print("Trabas Horizontales")
            print("N° Trabas por estribo = ",j[1][15])
            print("N° de estribos donde va traba = ",j[1][14])
            print("Largo trabas = ",j[1][16],"[cm]")

            # listaT = [minim0, h1, b2, aSLst3, ylst4, cuan1 5, cuan2 6, ylstrev7, alstrev8, c9, round(abs(mnn), 2)10,
            #           round(abs(mpp), 2)11, L1 12, lis 13, cpn[1]14, cpnrev[1]15, max(cpn[1], cpnrev[1])16, lo17, FU18,
            #           db2 19, gancho20, db12 21, nbarG 22, traslp1 23, traslp2 24, remate25, db122 26, remate2 27, gancho2 28, xlistV 29]

            """Resultados"""

            print("Resultados\n")
            print("Flexión")
            print("ØMn+ = ", j[0][15], "[tf-m]")
            print("ØMn- = ", -j[0][14], "[tf-m]")
            print("F.U. mayor = ", j[0][18], "%\n")

            print("Corte")
            phiVn1 = round(aCir(j[1][9])*j[1][2]*fy*(j[0][1]-dp)/j[1][3],1)
            print("ØVn1 = ",round(phiVn1/1000,1), "[tf]")
            fuV1 = round(100*j[1][10]/(phiVn1),1)
            print("F.U.1 = ",fuV1, "%")
            phiVn2 = round(aCir(j[1][9])*j[1][6]*fy*(j[0][1]-dp)/j[1][7], 1)
            print("ØVn2 = ",round(phiVn2/1000,1), "[tf]")
            fuV2 = round(100*j[1][11]/phiVn2,1)
            print("F.U.2 = ",fuV2,"%\n")
            print("\n")
            input()

def detCol(detcol):

    print("\nNota: todas las columnas son simétricas, por lo tanto, su ancho y alto es igual.")
    print("Por otro lado, las trabas y/o estribos interiores perpendiculares al eje x se replican al eje y")
    cont = 0
    npisos = len(detcol)
    ncol = len(detcol[0])
    for i in detcol:
        for j in i:

            """ Identificador """

            cont+=1
            piso=npisos if cont%npisos==0 else cont%npisos
            tipo = 2 if cont>npisos else 1

            print("\n\nColumna n° ",cont)
            print("Piso N°",piso)
            print("Tipo",tipo,"\n\n")

            """Dimensiones"""

            print("Dimensiones\n")
            print("Largo : ", j[0][20], "[m]")
            print("Alto : ",j[0][1], "[cm]")
            print("Ancho : ",j[0][2], "[cm]\n")

            """Refuerzo longitudinal"""

            print("Refuerzo longitudinal\n")
            list = []
            if j[0][21]!=1:
                print("Armadura superior")
                if j[0][3]>0:
                    print("2 barras Ø",j[0][5],"[mm] y",j[0][3],"barras Ø",j[0][6],"[mm] en la posición y =",j[0][14][0],
                          "[cm], área =",j[0][13][0],"[cm2]")
                else:
                    print("2 barras Ø",j[0][5],"[mm] en la posición y =",j[0][14][0],"[cm], área =",j[0][13][0],"[cm2]")
            else:
                print(2+j[0][3],"barras Ø",j[0][5],"[mm] en la posición y =",j[0][14][0],"[cm], área =",j[0][13][0],"[cm2]")
            if j[0][4]>0:
                for i in range(j[0][4]):
                    print("2 barras Ø",j[0][6],"[mm] en la posición y =",j[0][14][i+1],"[cm], área =",j[0][13][i+1],"[cm2]")
            if j[0][21]!=1:
                print("Armadura superior")
                if j[0][3]>0:
                    print("2 barras Ø",j[0][5],"[mm] y",j[0][3],"barras Ø",j[0][6],
                          "[mm] en la posición y =",j[0][14][-1],"[cm], área =",j[0][13][-1],"[cm2]")
                else:
                    print("2 barras Ø",j[0][5],"[mm] en la posición y =",j[0][14][-1],"[cm], área =",j[0][13][-1],"[cm2]")
            else:
                print(2+j[0][3],"barras Ø",j[0][5],"[mm] en la posición y =",j[0][14][-1],"[cm], área =",j[0][13][-1],"[[cm]2]")

            """Cuantía"""

            print("\nCuantía = ",j[0][9],"\n\n")

            """Uniones y remates"""
            print("Uniones y remates\n")

            if piso!=npisos and piso>1:
                if cont>npisos:
                    print("Columna para zonas centrales\n")
                    print("Para unión superior\n")
                    ldc = ldC(fy, fc, j[0][5])
                    print("Longitud de empalme unión viga-columna = ", ldc, "cm\n")
                    print("Para unión inferior\n")
                    print("Longitud de gancho-remate = ", lG, "[cm]")
                    ldc = ldC(fy, fc, j[0][5])
                else:
                    print("Columna para zonas laterales\n")
                    print("Para unión superior\n")
                    ldc = ldC(fy, fc, j[0][5])
                    print("Longitud de empalme unión viga-columna = ", ldc, "[cm]\n")
                    lG = lGanchoC(j[0][5], fc, fy, j[0][1], dp)
                    print("Longitud de gancho-remate = ",lG,"[cm]")
                    print("Para unión inferior\n")
                    ldc = ldC(fy, fc, j[0][5])
                    print("Longitud de empalme unión viga-columna = ", ldc, "[cm]\n")

            elif piso==1:
                if cont>npisos:
                    print("Columna para zonas centrales\n")
                    print("Para unión superior\n")
                    ldc = ldC(fy, fc, j[0][5])
                    print("Longitud de empalme unión viga-columna = ", ldc, "[cm]\n")

                else:
                    print("Columna para zonas laterales\n")
                    print("Para unión superior\n")
                    ldc = ldC(fy, fc, j[0][5])
                    print("Longitud de empalme unión viga-columna = ", ldc, "[cm]\n")
                    lG = lGanchoC(j[0][5], fc, fy, j[0][1], dp)
                    print("Longitud de gancho-remate = ",lG,"[cm]")

            else:
                if cont>npisos:
                    print("Columna para zonas centrales\n")
                    print("Para unión superior\n")
                    lG = lGanchoC(j[0][5], fc, fy, j[0][1], dp)
                    print("Longitud de gancho-remate = ",lG,"[cm]")
                    print("Para unión inferior\n")
                    lG = lGanchoC(j[0][5], fc, fy, j[0][1], dp)
                    print("Longitud de gancho-remate = ", lG, "[cm]")
                else:
                    print("Columna para zonas laterales\n")
                    print("Para unión superior\n")
                    lG = lGanchoC(j[0][5], fc, fy, j[0][1], dp)
                    print("Longitud de gancho-remate = ",lG,"[cm]")
                    print("Para unión inferior\n")
                    ldc = ldC(fy, fc, j[0][5])
                    print("Longitud de empalme unión viga-columna = ", ldc, "[cm]\n")

            """Refuerzo transversal"""

            print("\n\nRefuerzo transversal\n")

            print("\nZonas de rótula plástica\n")

            print("\nUbicación : de 0 -",j[1][0][10],"[cm] y ",j[0][20]*100-j[1][0][10],"-",j[0][20]*100,"[cm]:")
            print("N° ramas : ",j[1][0][1])
            print("N° de estribos por extremo: ",j[1][0][5])
            print("Espaciamiento : ",j[1][0][3],"[cm]")
            print("\nRefuerzo exterior\n")
            print("Diámetro estribo exterior: ",j[1][0][2],"[cm]")
            print("Largo del estribo exterior",j[1][0][6],"[cm]")
            print("Ubicación entre ejes de barras horizontales: x =",j[1][0][9][0][0],"[cm] y x =",j[1][0][9][0][1],"[cm]")
            print("Ubicación entre ejes de barras verticales: y =",j[1][0][9][0][0],"[cm] e y =",j[1][0][9][0][1],"[cm]")
            if j[1][0][1]>2:
                print("\nRefuerzo interior\n")
                if j[1][0][1]%2!=0:
                    print("Diámetro de estribos y trabas interiores",j[1][0][4],"[cm]")
                    if len(j[1][0][7])-1>0:
                        for i in range(len(j[1][0][7])-1):
                            print("Largo estribo interior n°",i+1,"=",j[1][0][7][i],"[cm]")
                            print("Ubicación entre ejes de barras horizontales: x =", j[1][0][9][i+1][0], "[cm] y x =",
                                  j[1][0][9][i+1][1], "[cm]")
                            print("Ubicación entre ejes de barras verticales: y =", j[1][0][9][0][0], "[cm] e y =",
                                  j[1][0][9][0][1], "[cm]")
                    print("Largo de traba interior n°1 =",j[1][0][7][-1],"[cm]")
                    #Revisar
                    print("Ubicación entre ejes de barras horizontales: x =", j[1][0][9][-1][0], "[cm]")
                    print("Ubicación entre ejes de barras verticales: y =", j[1][0][9][0][0], "[cm] e y =",
                          j[1][0][9][0][1], "[cm]")
                else:
                    print("Diámetro de estribos interiores",j[1][0][4],"[cm]")
                    if len(j[1][0][7])-1>0:
                        for i in range(len(j[1][0][7])-1):
                            print("Largo estribo interior n°",i+1,"=",j[1][0][7][i],"[cm]")
                            print("Ubicación entre ejes de barras horizontales: x =", j[1][0][9][i + 1][0], "[cm] y x =",
                                  j[1][0][9][i + 1][1], "[cm]")
                            print("Ubicación entre ejes de barras verticales: y =", j[1][0][9][0][0], "[cm] e y =",
                                  j[1][0][9][0][1], "[cm]")
                    print("Largo de estribo interior n°", len(j[1][0][7]), "=", j[1][0][7][-1], "[cm]")
                    print("Ubicación entre ejes de barras horizontales: x =", j[1][0][9][-1][0], "[cm] y x =",
                          j[1][0][9][-1][1], "[cm]")
                    print("Ubicación entre ejes de barras verticales: y =", j[1][0][9][0][0], "[cm] e y =",
                          j[1][0][9][0][1], "[cm]")

            print("\n\nZona central\n")

            print("\nUbicación : de",j[1][0][10],"-",j[1][0][10]+round(j[1][1][10]/2,1),
                  "[cm] y de",j[0][20]*100-(j[1][0][10]+round(j[1][1][10]/2,1)),"-",j[0][20]*100-j[1][0][10],"[cm]")
            print("N° ramas : ", j[1][1][1])
            print("N° de estribos por extremo: ",int(round(j[1][1][5]/2,0)))
            print("Espaciamiento : ", j[1][1][3], "[cm]")
            print("\nRefuerzo exterior\n")
            print("Diámetro estribo exterior: ", j[1][1][2], "[cm]")
            print("Largo del estribo exterior", j[1][1][6], "[cm]")
            print("Ubicación entre ejes de barras horizontales: x =", j[1][1][9][0][0], "[cm] y x =", j[1][1][9][0][1],
                  "[cm]")
            print("Ubicación entre ejes de barras verticales: y =", j[1][1][9][0][0], "[cm] e y =", j[1][1][9][0][1],
                  "[cm]")
            if j[1][1][1] > 2:
                print("\nRefuerzo interior\n")
                if j[1][1][1] % 2 != 0:
                    print("Diámetro de estribos y trabas interiores", j[1][1][4], "[cm]")
                    if len(j[1][1][7]) - 1 > 0:
                        for i in range(len(j[1][1][7]) - 1):
                            print("Largo estribo interior n°", i + 1, "=", j[1][1][7][i], "[cm]")
                            print("Ubicación entre ejes de barras horizontales: x =", j[1][1][9][i + 1][0], "[cm] y x =",
                                  j[1][1][9][i + 1][1], "[cm]")
                            print("Ubicación entre ejes de barras verticales: y =", j[1][1][9][0][0], "[cm] e y =",
                                  j[1][1][9][0][1], "[cm]")
                    print("Largo de traba interior n°1 =", j[1][1][7][-1], "[cm]")
                    print("Ubicación entre ejes de barras horizontales: x =", j[1][0][9][-1][0], "[cm]")
                    print("Ubicación entre ejes de barras verticales: y =", j[1][1][9][0][0], "[cm] e y =",
                          j[1][1][9][0][1], "[cm]")
                else:
                    print("Diámetro de estribos interiores", j[1][1][4], "[cm]")
                    if len(j[1][1][7]) - 1 > 0:
                        for i in range(len(j[1][1][7]) - 1):
                            print("Largo estribo interior n°", i + 1, "=", j[1][1][7][i], "[cm]")
                            print("Ubicación entre ejes de barras horizontales: x =", j[1][1][9][i + 1][0], "[cm] y x =",
                                  j[1][1][9][i + 1][1], "[cm]")
                            print("Ubicación entre ejes de barras verticales: y =", j[1][1][9][0][0], "[cm] e y =",
                                  j[1][1][9][0][1], "[cm]")
                    print("Largo de estribo interior n°", len(j[1][1][7]), "=", j[1][1][7][-1], "[cm]")
                    print("Ubicación entre ejes de barras horizontales: x =", j[1][1][9][-1][0], "[cm] y x =",
                          j[1][1][9][-1][1], "[cm]")
                    print("Ubicación entre ejes de barras verticales: y =", j[1][1][9][0][0], "[cm] e y =",
                          j[1][1][9][0][1], "[cm]")

            print("\n\nEmpalme central\n")

            print("\nUbicación : de",j[1][0][10]+round(j[1][1][10]/2,1),"-",
                  j[0][20]*100-(j[1][0][10]+round(j[1][1][10]/2,1)),"[cm]")
            print("N° ramas : ", j[1][2][1])
            print("N° de estribos : ",j[1][2][5])
            print("Espaciamiento : ", j[1][2][3], "[cm]")
            print("\nRefuerzo exterior\n")
            print("Diámetro estribo exterior: ", j[1][2][2], "[cm]")
            print("Largo del estribo exterior", j[1][2][6], "[cm]")
            print("Ubicación entre ejes de barras horizontales: x =", j[1][2][9][0][0], "[cm] y x =", j[1][2][9][0][1],
                  "[cm]")
            print("Ubicación entre ejes de barras verticales: y =", j[1][2][9][0][0], "[cm] e y =", j[1][2][9][0][1],
                  "[cm]")
            if j[1][2][1] > 2:
                print("\nRefuerzo interior\n")
                if j[1][2][1] % 2 != 0:
                    print("Diámetro de estribos y trabas interiores", j[1][2][4], "[cm]")
                    if len(j[1][2][7]) - 1 > 0:
                        for i in range(len(j[1][2][7]) - 1):
                            print("\nLargo estribo interior n°", i + 1, "=", j[1][2][7][i], "[cm]")
                            print("Ubicación entre ejes de barras horizontales: x =", j[1][2][9][i+1][0], "[cm] y x =",
                                  j[1][2][9][i + 1][1], "[cm]")
                            print("Ubicación entre ejes de barras verticales: y =", j[1][2][9][0][0], "[cm] e y =",
                                  j[1][2][9][0][1], "[cm]")
                    print("\nLargo de traba interior n°1 =", j[1][2][7][-1], "[cm]")
                    print("Ubicación entre ejes de barras horizontales: x =", j[1][0][9][-1][0], "[cm]")
                    print("Ubicación entre ejes de barras verticales: y =", j[1][2][9][0][0], "[cm] e y =",
                          j[1][2][9][0][1], "[cm]")
                else:
                    print("Diámetro de estribos interiores", j[1][2][4], "[cm]")
                    if len(j[1][2][7]) - 1 > 0:
                        for i in range(len(j[1][2][7]) - 1):
                            print("\nLargo estribo interior n°", i + 1, "=", j[1][2][7][i], "[cm]")
                            print("Ubicación entre ejes de barras horizontales: x =", j[1][2][9][i+1][0], "[cm] y x =",
                                  j[1][2][9][i+1][1], "[cm]")
                            print("Ubicación entre ejes de barras verticales: y =", j[1][2][9][0][0], "[cm] e y =",
                                  j[1][2][9][0][1], "[cm]")
                    print("\nLargo de estribo interior n°", len(j[1][2][7]), "=", j[1][2][7][-1], "[cm]")
                    print("Ubicación entre ejes de barras horizontales: x =", j[1][0][9][-1][0], "[cm]")
                    print("Ubicación entre ejes de barras verticales: y =", j[1][2][9][0][0], "[cm] e y =",
                          j[1][2][9][0][1], "[cm]")

            """Resultados"""

            print("\n\nResultados\n")
            print("Flexión\n")
            print("Mayor excentricidad", round(j[0][22] * 100,1), "cm\n")
            print("Momentos\n")
            print("Mu_max = ", j[0][17], "[tf-m]")
            print("Momento nominal ajustado a Mu y Pu máximos")
            print("ØMn1 = ", j[0][15], "[tf-m]")
            print("Momento nominal ajustado a Mu máximo debido a mayor excentricidad:")
            print("ØMn2 = ", j[0][23], "[tf-m]\n")

            print("Cargas\n")
            print("Pu_max = ", j[0][18], "[tf]")
            print("Pu_min = ", j[0][19], "[tf]")
            print("Carga nominal que verifica Pu_max:")
            print("ØPn1 = ", j[0][16], "[tf]")
            print("Carga nominal que verifica Pu_min:")
            print("ØPn2 = ", j[0][24], "[tf]\n")
            print("F.U. 1 = ", j[0][7], "%")
            print("F.U. 2 = ", j[0][8], "%\n")

            print("Corte")

            print("\nCorte en zona de rótula plástica")
            phiVn1 = round((2*aCir(j[1][0][2])+aCir(j[1][0][4])*(j[1][0][1]-2))*fy*(j[0][1]-j[0][27])/j[1][0][3],1)
            print("ØVn1 = ",round(phiVn1/1000,1), "[tf]")
            fuV1 = round(100*j[1][4]/(phiVn1),1)
            print("F.U.1 = ",fuV1, "%\n")

            print("Corte en zona central")
            phiVn2 = round((2*aCir(j[1][1][2])+aCir(j[1][1][4])*(j[1][1][1]-2))*fy*(j[0][1]-j[0][27])/j[1][1][3],1)
            print("ØVn2 = ",round(phiVn2/1000,1), "[tf]")
            fuV2 = round(100*j[1][5]/phiVn2,1)
            print("F.U.2 = ",fuV2,"%\n")

            print("Corte en zona de empalme")
            phiVn3 = round((2*aCir(j[1][2][2])+aCir(j[1][2][4])*(j[1][2][1]-2))*fy*(j[0][1]-j[0][27])/j[1][2][3],1)
            print("ØVn3 = ",round(phiVn3/1000,1), "[tf]")
            fuV3 = round(100*j[1][5]/phiVn3,1)
            print("F.U.3 = ",fuV3,"%\n")
            print("\n")


def max_ind(lista,ind):
    temp=[]
    for i in range(len(lista)):
        maxim=0
        for j in range(len(lista[0])):
            if lista[i][j][ind]>maxim:
                maxim=lista[i][j][ind]
                list1=lista[i][j]
        temp.append(list1)
    return temp

def optimusFrame(tabla, largosC, largosV, dimV, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, deList, hColMax, hColMin):
    dList=[16,18,22,25,28,32,36]
    deList=[10,12]
    combis = 7
    combi_e = 4
    combi_s = 3
    tab = tabla
    filtro=filtroCV(combis, combi_e, combi_s, tab, largosV, largosC)
    listaV=filtro[0]
    listaC=filtro[1]
    exc_col=filtro[2]
    mpp1=[max([max([max(listaV[i][j][0][2], listaV[i][j][1][2]) for j in range(len(listaV[0]))])
                 for k in range(len(listaV[0][0]))]) for i in range(len(listaV))]
    mpp2=[[mpp1[j] for i in range(len(listaV[0]))] for j in range(len(listaV))]
    mpp3=[max(listaV[i][0][0][2], listaV[i][-1][1][2]) for i in range(len(listaV))]
    mnn1=[min([min([min(listaV[i][j][0][3], listaV[i][j][1][3]) for j in range(len(listaV[0]))])
                 for k in range(len(listaV[0][0]))]) for i in range(len(listaV))]
    mnn2=[[mnn1[j] for i in range(len(listaV[0]))] for j in range(len(listaV))]
    mnn3 = [max(listaV[i][0][0][3], listaV[i][-1][1][3]) for i in range(len(listaV))]
    allVuL = [[[listaV[i][j][0][6], listaV[i][j][0][7], listaV[i][j][1][6],
                listaV[i][j][1][7]] for j in range(len(listaV[0]))] for i in range(len(listaV))]
    wo1 = [max([max(listaV[i][j][0][4],listaV[i][j][1][4]) for j in range(len(listaV[0]))]) for i in range(len(listaV))]
    wo2 = [[wo1[j] for i in range(len(listaV[0]))] for j in range(len(listaV))]
    minLo = [min(i) for i in largosV]
    maxLo = [max(i) for i in largosV]
    lV = []
    for i in allVuL:
        a=[[],[],[],[]]
        a[0].append(max([i[j][0][0] for j in range(len(i))]))
        a[0].append(max([i[j][0][1] for j in range(len(i))]))
        a[1].append(max([i[j][1][0] for j in range(len(i))]))
        a[1].append(max([i[j][1][1] for j in range(len(i))]))
        a[1].append(min([i[j][1][2] for j in range(len(i))]))
        a[1].append(max([i[j][1][3] for j in range(len(i))]))
        a[2].append(min([i[j][2][0] for j in range(len(i))]))
        a[2].append(min([i[j][2][1] for j in range(len(i))]))
        a[3].append(min([i[j][3][0] for j in range(len(i))]))
        a[3].append(min([i[j][3][1] for j in range(len(i))]))
        a[3].append(min([i[j][3][2] for j in range(len(i))]))
        a[3].append(max([i[j][3][3] for j in range(len(i))]))
        lV.append(a)

    lV2=[[i for j in range(len(allVuL[0]))] for i in lV]
    listaVig = [[[mpp2[i][j],mnn2[i][j],wo2[i][j],largosV[i][j],lV2[i][j], dimV[i][j]]
       for j in range(len(listaV[0]))] for i in range(len(listaV))]
    listaVig2 = [[listaVig[i][0]] for i in range(len(listaVig))]
    detvig2=matElemV(listaVig2, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, 1, deList, 5)
    detvig = [[detvig2[j] for i in range(len(listaVig[0]))] for j in range(len(listaVig))]
    listaCol =[[[max(abs(listaC[i][j][0][k]), abs(listaC[i][j][1][k])) for k in range(6)]
                for j in range(len(listaC[0]))] for i in range(len(listaC))]
    exc_col=[[exc_col[i][j][0] for j in range(len(exc_col[0]))] for i in range(len(exc_col))]
    exc1=max_ind([[exc_col[i][0],exc_col[i][-1]]  for i in range(len(exc_col))],2)
    exc2 = max_ind([exc_col[i][1:-1] for i in range(len(exc_col))],2)
    tempCol = extMat(listaCol, 4)
    tempVig = [[[abs(listaVig[i][j][0]),abs(listaVig[i][j][1])]
                for j in range(len(listaVig[0]))] for i in range(len(listaVig))]
    colDef=replMat(listaCol,critVC(tempVig, tempCol),4)

    lC1 = []
    for i in range(len(colDef)):
        col1=[max(colDef[i][0][j],colDef[i][-1][j]) for j in range(len(colDef[0][0]))]+exc1[i]
        col2=[max([colDef[i][k][j] for k in range(len(colDef[0])-2)]) for j in range(len(colDef[0][0]))]+exc2[i]
        lC1.append([col1, col2])
    detcol=[]
    hmax1=hColMax
    hmax2=hmax1
    hmin1=hColMin
    hmin2=hmin1
    cont=0
    listC_bh1 = []
    listC_bh2 = []
    for j in range(len(lC1[0])):
        tempC=[]
        for i in range(len(lC1)):
            if j==0:
                cont+=1
                elem=optimusCol(b1, dp, es, eu, ey, fc, fy, lC1[i][j][4], round(lC1[i][j][7]/1000,1),
                                round(lC1[i][j][6]/1000,1), lC1[i][j][0], dList, hmax1, hmin1, cH,
                                cS, lC1[i][j][5], lC1[i][j][2], lC1[i][j][3], deList, 1)
                titulo = str("Columna tipo "+ str(j+1)+ " del piso " + str(i+1))
                XYplotCurv(elem[0][13], elem[0][2], elem[0][1], dp, eu, fy, fc, b1, es, ey, elem[0][14], elem[0][10], lC1[i][j][4], lC1[i][j][0], elem[0][15], elem[0][16], titulo)

                # optimusCol(b1, dp, es, eu, ey, fc, fy, muC, muCmin, puCmin, puCmax, dList, hmax, hmin, cH, cS, H, vu,
                #            vue, deList, iguales)

                # optimo = [minor0, h1, b2, j3, k4, l5, m6, fu7, fu2 8, cuan9, cF[0]10, cF2[0]11, e12,
                # alist13, ylist14, cF[1]15, cF[2]16, muC17, puCmax18, puCmin19, H20, iguales21, round(muCmin / puCmin, 3)22,
                # cF2[1]23, cF2[2]24, costo1 25, costo2 26, dp27]
                tempC.append(elem)
                hmax1=elem[0][1]
                hmin1=hmax1-5
                listC_bh1.append([elem[0][2],elem[0][1]])
            else:
                cont+=1
                elem = optimusCol(b1, dp, es, eu, ey, fc, fy, lC1[i][j][4], round(lC1[i][j][7] / 1000, 1),
                                  round(lC1[i][j][6] / 1000, 1), lC1[i][j][0], dList, hmax2, hmin2, cH, cS,
                                  lC1[i][j][5], lC1[i][j][2], lC1[i][j][3], deList, 1)
                # optimusCol(b1, dp, es, eu, ey, fc, fy, muC, muCmin, puCmin, puCmax, dList, hmax, hmin, cH, cS, H, vu,
                #            vue, deList, iguales)

                titulo = str("Columna tipo "+ str(j+1)+ " del piso " + str(i+1))
                XYplotCurv(elem[0][13], elem[0][2], elem[0][1], dp, eu, fy, fc, b1, es, ey, elem[0][14], elem[0][10],
                           lC1[i][j][4], lC1[i][j][0], elem[0][15], elem[0][16], titulo)
                hmax2=elem[0][1]
                hmin2=hmax2-5
                listC_bh2.append([elem[0][2],elem[0][1]])
                tempC.append(elem)
        detcol.append(tempC)
    listC_bh=[]
    cont=0
    for i in range(len(listaC)):
        for j in range(len(listaC[0])):
            if j==0 or j==len(listaC):
                cont+=1
                listC_bh.append((listC_bh1[i][0],listC_bh1[i][1]))
            else:
                cont += 1
                listC_bh.append((listC_bh1[i][0],listC_bh1[i][1]))
    listV_bh=[]
    cont=0
    for i in detvig:
        for j in i:
            cont+=1
            listV_bh.append((j[0][0][2],j[0][0][1]))
    # detCol(detcol)
    # print(detvig2)
    detVig(detvig2,nbahias,listV_bh)
    list_bh = listC_bh+listV_bh
    return [detcol,detvig2, list_bh]

hColMax, hColMin = 90, 30

from time import time
t1=time()
asd=optimusFrame(tabla, largosC, largosV, dimV, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, deList, hColMax, hColMin)
t2=time()-t1
print("tiempo de ejecución",round(t2,5),"segundos")
print(asd[0],"\n",asd[1])
# print(asd[2])
# cols = [[(0, asd[0][0][j][i][2], asd[0][0][j][i][0][1]) for i in range(asd[0])] for j in range(len(asd[0][0]))]
# print(cols)
# #
# listacolumnas1=[[[[393790.75, 70, 70, 4, 4, 18, 18, 91.0, 16.2, 0.01039, 18.46, 52.77, 0.608, [15.27, 5.09, 5.09, 5.09, 5.09, 15.27], [5, 17, 29, 41, 53, 65], 95.7, 157.4, 87.01, 143.17, 78.8, 3, 1, 0.152, 74.2, 488.6, 270953.75, 122837.0, 5], [[58037.0, 4, 10, 9, 10, 8, 260.21, [164.21], 164.21, [[5, 65], [29, 41]], 70], [39409.0, 4, 12, 11, 10, 9, 265.25, [164.21], 164.21, [[5, 65], [29, 41]], 105.0], [25391.0, 4, 10, 8, 10, 7, 260.21, [164.21], 164.21, [[5, 65], [29, 41]], 55.0], 122837.0, 56716.7, 56716.7]], [[378244.1, 65, 65, 4, 4, 18, 18, 51.9, 6.9, 0.01205, 23.04, 41.53, 0.442, [15.27, 5.09, 5.09, 5.09, 5.09, 15.27], [5, 16, 27, 38, 49, 60], 90.4, 204.7, 46.93, 106.09, 24.2, 3, 1, 0.198, 69.2, 349.0, 252980.1, 125264.0, 5], [[64853.0, 4, 12, 9, 10, 8, 245.25, [152.21], 152.21, [[5, 60], [27, 38]], 65], [36918.0, 4, 10, 10, 10, 11, 240.21, [152.21], 152.21, [[5, 60], [27, 38]], 115.0], [23493.0, 4, 10, 8, 10, 7, 240.21, [152.21], 152.21, [[5, 60], [27, 38]], 55.0], 125264.0, 99902.3, 52835.6]], [[300780.0, 60, 60, 3, 3, 18, 18, 75.8, 8.2, 0.01131, 14.09, 42.05, 0.648, [12.725, 5.09, 5.09, 5.09, 12.725], [5, 18, 30, 42, 55], 58.0, 89.5, 43.95, 67.72, 27.3, 3, 1, 0.15, 50.0, 332.9, 208243.0, 92537.0, 5], [[42454.0, 3, 12, 9, 10, 7, 225.25, [83.78], 83.78, [[5, 55], [30]], 60], [33356.0, 3, 12, 11, 10, 11, 225.25, [83.78], 83.78, [[5, 55], [30]], 125.0], [16727.0, 3, 10, 8, 10, 7, 220.21, [83.78], 83.78, [[5, 55], [30]], 55.0], 92537.0, 71404.4, 39933.3]], [[296559.0, 60, 60, 3, 3, 18, 18, 89.4, 3.4, 0.01131, 10.59, 58.86, 1.349, [12.725, 5.09, 5.09, 5.09, 12.725], [5, 18, 30, 42, 55], 47.9, 35.5, 42.82, 31.76, 16.5, 3, 1, 0.061, 29.4, 482.9, 208243.0, 88316.0, 5], [[38233.0, 3, 10, 8, 10, 8, 220.21, [83.78], 83.78, [[5, 55], [30]], 60], [33356.0, 3, 12, 11, 10, 11, 225.25, [83.78], 83.78, [[5, 55], [30]], 125.0], [16727.0, 3, 10, 8, 10, 7, 220.21, [83.78], 83.78, [[5, 55], [30]], 55.0], 88316.0, 50240.0, 31616.7]]], [[[420491.0, 70, 70, 5, 5, 18, 18, 79.0, 83.7, 0.01247, 25.81, 15.9, 0.462, [17.815, 5.09, 5.09, 5.09, 5.09, 5.09, 17.815], [5, 15, 25, 35, 45, 55, 65], 115.3, 249.3, 91.0, 197.01, 90.6, 3, 1, 0.886, 95.9, 108.3, 299052.0, 121439.0, 5], [[56172.0, 3, 12, 9, 10, 8, 265.25, [93.78], 93.78, [[5, 65], [35]], 70], [40692.0, 3, 12, 10, 12, 10, 265.25, [96.54], 96.54, [[5, 65], [35]], 105.0], [24575.0, 3, 12, 8, 10, 7, 265.25, [93.78], 93.78, [[5, 65], [35]], 55.0], 121439.0, 71591.1, 63516.7]], [[367089.1, 65, 65, 4, 4, 18, 18, 67.0, 87.9, 0.01205, 25.09, 12.72, 0.398, [15.27, 5.09, 5.09, 5.09, 5.09, 15.27], [5, 16, 27, 38, 49, 60], 87.8, 220.7, 58.78, 147.78, 56.3, 3, 1, 1.073, 68.7, 64.1, 252980.1, 114109.0, 5], [[53698.0, 4, 10, 9, 10, 8, 240.21, [152.21], 152.21, [[5, 60], [27, 38]], 65], [36918.0, 4, 10, 10, 10, 11, 240.21, [152.21], 152.21, [[5, 60], [27, 38]], 115.0], [23493.0, 4, 10, 8, 10, 7, 240.21, [152.21], 152.21, [[5, 60], [27, 38]], 55.0], 114109.0, 61050.0, 61050.0]], [[296559.0, 60, 60, 3, 3, 18, 18, 80.4, 61.3, 0.01131, 16.77, 13.66, 0.516, [12.725, 5.09, 5.09, 5.09, 12.725], [5, 18, 30, 42, 55], 63.5, 123.0, 51.05, 98.76, 51.0, 3, 1, 0.684, 56.9, 83.2, 208243.0, 88316.0, 5], [[38233.0, 3, 10, 8, 10, 8, 220.21, [83.78], 83.78, [[5, 55], [30]], 60], [33356.0, 3, 12, 11, 10, 11, 225.25, [83.78], 83.78, [[5, 55], [30]], 125.0], [16727.0, 3, 10, 8, 10, 7, 220.21, [83.78], 83.78, [[5, 55], [30]], 55.0], 88316.0, 49833.3, 49833.3]], [[296559.0, 60, 60, 3, 3, 18, 18, 94.1, 23.7, 0.01131, 11.68, 24.33, 0.966, [12.725, 5.09, 5.09, 5.09, 12.725], [5, 18, 30, 42, 55], 51.3, 53.1, 48.29, 49.73, 46.1, 3, 1, 0.338, 65.7, 194.5, 208243.0, 88316.0, 5], [[38233.0, 3, 10, 8, 10, 8, 220.21, [83.78], 83.78, [[5, 55], [30]], 60], [33356.0, 3, 12, 11, 10, 11, 225.25, [83.78], 83.78, [[5, 55], [30]], 125.0], [16727.0, 3, 10, 8, 10, 7, 220.21, [83.78], 83.78, [[5, 55], [30]], 55.0], 88316.0, 39716.7, 39716.7]]]]
# listavigas1= [[[[56077.0, 65, 35, [18.47, 14.73, 1, 15.98], [5, 12.0, 36.0, 60], 0.0158, 0.0076, [5, 29.0, 53.0, 60], [15.98, 1, 14.73, 18.47], 8.77, 32.52, 62.02, [[2, 28, 1, 28, 18.47], [2, 25, 1, 25, 14.73], 33.2], [2, 25, 1, 28, 15.98], 37.2, 65.7, 65.7, 7, 94.4, 32, 68.2, 33.6, 9, 139.3, 159.2, 55.8, 38.4, 63.8, 78.6, [5, 15, 25]], [133380.92, 155, 3, 15, 21, 390.0, 3, 20, 19, 12, 49885.0, 35957.3, [301.7, [175.25], [91.54]], [301.7, [175.25], [91.54]], 40, 2, 61.54]]], [[[61423.0, 65, 30, [20.36, 20.36, 1, 18.47], [5, 14.0, 37.0, 60], 0.0226, 0.0103, [5, 28.0, 51.0, 60], [18.47, 1, 20.36, 20.36], 10.53, 36.15, 66.67, [[2, 36, 0, 0, 20.36], [2, 36, 0, 0, 20.36], 40.72], [2, 28, 1, 28, 18.47], 43.3, 76.2, 76.2, 7, 87.5, 36, 89.1, 43.2, 7, 179.1, 179.1, 71.7, 43.2, 71.7, 89.1, [5, 25]], [134395.14, 155, 2, 11, 29, 390.0, 2, 15, 26, 12, 51797.2, 37849.5, [198.2, [175.25], []], [198.2, [175.25], []], 55, 2, 56.54]]], [[[54956.0, 60, 30, [20.36, 17.23, 1, 14.73], [5, 13.0, 34.0, 55], 0.0228, 0.0089, [5, 26.0, 47.0, 55], [14.73, 1, 17.23, 20.36], 9.29, 27.72, 58.05, [[2, 28, 1, 32, 20.36], [2, 28, 1, 25, 17.23], 37.59], [2, 25, 1, 25, 14.73], 32.6, 63.9, 63.9, 7, 90.8, 32, 78.6, 38.4, 9, 159.2, 159.2, 63.8, 38.4, 63.8, 78.6, [5, 15, 25]], [126771.53, 145, 3, 11, 27, 410.0, 3, 15, 27, 10, 47785.8, 34711.8, [191.5, [160.21], [83.78]], [191.5, [160.21], [83.78]], 54, 2, 53.78]]], [[[45636.0, 55, 30, [15.98, 15.98, 1, 9.82], [5, 12.0, 31.0, 50], 0.0213, 0.0065, [5, 24.0, 43.0, 50], [9.82, 1, 15.98, 15.98], 8.48, 16.47, 44.34, [[2, 25, 1, 28, 15.98], [2, 25, 1, 28, 15.98], 31.96], [2, 25, 0, 0, 9.82], 20.9, 48.4, 48.4, 7, 91.6, 25, 68.2, 33.6, 8, 139.3, 124.4, 55.8, 30.0, 49.8, 60.3, [5, 15, 25]], [117300.35, 135, 3, 11, 25, 430.0, 3, 16, 27, 10, 42365.5, 29912.3, [179.8, [150.21], [78.78]], [179.8, [150.21], [78.78]], 52, 2, 53.78]]]]
#
# listacolumnas2=[[[[393790.75, 70, 70, 4, 4, 18, 18, 91.0, 16.2, 0.01039, 18.46, 52.77, 0.608, [15.27, 5.09, 5.09, 5.09, 5.09, 15.27], [5, 17, 29, 41, 53, 65], 95.7, 157.4, 87.01, 143.17, 78.8, 3, 1, 0.152, 74.2, 488.6, 270953.75, 122837.0, 5], [[58037.0, 4, 10, 9, 10, 8, 260.21, [164.21], 164.21, [[5, 65], [29, 41]], 70], [39409.0, 4, 12, 11, 10, 9, 265.25, [164.21], 164.21, [[5, 65], [29, 41]], 105.0], [25391.0, 4, 10, 8, 10, 7, 260.21, [164.21], 164.21, [[5, 65], [29, 41]], 55.0], 122837.0, 56716.7, 56716.7]], [[378244.1, 65, 65, 4, 4, 18, 18, 51.9, 6.9, 0.01205, 23.04, 41.53, 0.442, [15.27, 5.09, 5.09, 5.09, 5.09, 15.27], [5, 16, 27, 38, 49, 60], 90.4, 204.7, 46.93, 106.09, 24.2, 3, 1, 0.198, 69.2, 349.0, 252980.1, 125264.0, 5], [[64853.0, 4, 12, 9, 10, 8, 245.25, [152.21], 152.21, [[5, 60], [27, 38]], 65], [36918.0, 4, 10, 10, 10, 11, 240.21, [152.21], 152.21, [[5, 60], [27, 38]], 115.0], [23493.0, 4, 10, 8, 10, 7, 240.21, [152.21], 152.21, [[5, 60], [27, 38]], 55.0], 125264.0, 99902.3, 52835.6]], [[300780.0, 60, 60, 3, 3, 18, 18, 75.8, 8.2, 0.01131, 14.09, 42.05, 0.648, [12.725, 5.09, 5.09, 5.09, 12.725], [5, 18, 30, 42, 55], 58.0, 89.5, 43.95, 67.72, 27.3, 3, 1, 0.15, 50.0, 332.9, 208243.0, 92537.0, 5], [[42454.0, 3, 12, 9, 10, 7, 225.25, [83.78], 83.78, [[5, 55], [30]], 60], [33356.0, 3, 12, 11, 10, 11, 225.25, [83.78], 83.78, [[5, 55], [30]], 125.0], [16727.0, 3, 10, 8, 10, 7, 220.21, [83.78], 83.78, [[5, 55], [30]], 55.0], 92537.0, 71404.4, 39933.3]], [[296559.0, 60, 60, 3, 3, 18, 18, 89.4, 3.4, 0.01131, 10.59, 58.86, 1.349, [12.725, 5.09, 5.09, 5.09, 12.725], [5, 18, 30, 42, 55], 47.9, 35.5, 42.82, 31.76, 16.5, 3, 1, 0.061, 29.4, 482.9, 208243.0, 88316.0, 5], [[38233.0, 3, 10, 8, 10, 8, 220.21, [83.78], 83.78, [[5, 55], [30]], 60], [33356.0, 3, 12, 11, 10, 11, 225.25, [83.78], 83.78, [[5, 55], [30]], 125.0], [16727.0, 3, 10, 8, 10, 7, 220.21, [83.78], 83.78, [[5, 55], [30]], 55.0], 88316.0, 50240.0, 31616.7]]], [[[420491.0, 70, 70, 5, 5, 18, 18, 79.0, 83.7, 0.01247, 25.81, 15.9, 0.462, [17.815, 5.09, 5.09, 5.09, 5.09, 5.09, 17.815], [5, 15, 25, 35, 45, 55, 65], 115.3, 249.3, 91.0, 197.01, 90.6, 3, 1, 0.886, 95.9, 108.3, 299052.0, 121439.0, 5], [[56172.0, 3, 12, 9, 10, 8, 265.25, [93.78], 93.78, [[5, 65], [35]], 70], [40692.0, 3, 12, 10, 12, 10, 265.25, [96.54], 96.54, [[5, 65], [35]], 105.0], [24575.0, 3, 12, 8, 10, 7, 265.25, [93.78], 93.78, [[5, 65], [35]], 55.0], 121439.0, 71591.1, 63516.7]], [[367089.1, 65, 65, 4, 4, 18, 18, 67.0, 87.9, 0.01205, 25.09, 12.72, 0.398, [15.27, 5.09, 5.09, 5.09, 5.09, 15.27], [5, 16, 27, 38, 49, 60], 87.8, 220.7, 58.78, 147.78, 56.3, 3, 1, 1.073, 68.7, 64.1, 252980.1, 114109.0, 5], [[53698.0, 4, 10, 9, 10, 8, 240.21, [152.21], 152.21, [[5, 60], [27, 38]], 65], [36918.0, 4, 10, 10, 10, 11, 240.21, [152.21], 152.21, [[5, 60], [27, 38]], 115.0], [23493.0, 4, 10, 8, 10, 7, 240.21, [152.21], 152.21, [[5, 60], [27, 38]], 55.0], 114109.0, 61050.0, 61050.0]], [[296559.0, 60, 60, 3, 3, 18, 18, 80.4, 61.3, 0.01131, 16.77, 13.66, 0.516, [12.725, 5.09, 5.09, 5.09, 12.725], [5, 18, 30, 42, 55], 63.5, 123.0, 51.05, 98.76, 51.0, 3, 1, 0.684, 56.9, 83.2, 208243.0, 88316.0, 5], [[38233.0, 3, 10, 8, 10, 8, 220.21, [83.78], 83.78, [[5, 55], [30]], 60], [33356.0, 3, 12, 11, 10, 11, 225.25, [83.78], 83.78, [[5, 55], [30]], 125.0], [16727.0, 3, 10, 8, 10, 7, 220.21, [83.78], 83.78, [[5, 55], [30]], 55.0], 88316.0, 49833.3, 49833.3]], [[296559.0, 60, 60, 3, 3, 18, 18, 94.1, 23.7, 0.01131, 11.68, 24.33, 0.966, [12.725, 5.09, 5.09, 5.09, 12.725], [5, 18, 30, 42, 55], 51.3, 53.1, 48.29, 49.73, 46.1, 3, 1, 0.338, 65.7, 194.5, 208243.0, 88316.0, 5], [[38233.0, 3, 10, 8, 10, 8, 220.21, [83.78], 83.78, [[5, 55], [30]], 60], [33356.0, 3, 12, 11, 10, 11, 225.25, [83.78], 83.78, [[5, 55], [30]], 125.0], [16727.0, 3, 10, 8, 10, 7, 220.21, [83.78], 83.78, [[5, 55], [30]], 55.0], 88316.0, 39716.7, 39716.7]]]]
# print(listacolumnas1==listacolumnas2)6599999998],
        ['COL', 1, '0.9 D + 1.4 E', 'i', 12026.35, 26606.62, 78777.194],
        ['j', 6558.85, 26606.62, -1042.6753999999999],
        ['COL', 1, '0.9 D - 1.4 E', 'i', 95087.24, -31130.2, -83793.57860000001],
        ['j', 89619.74, -31130.2, 9597.0313],
        ['COL', 2, '1.4 D', 'i', 127153.76, 231.63, 134.7818],
        ['j', 118648.76, 231.63, -560.0983],
        ['COL', 2, '1.2 D + L', 'i', 164005.09, 471.81, 336.93330000000003],
        ['j', 156715.09, 471.81, -1078.5025],
        ['COL', 2, '1.2 D + 1.6 L', 'i', 197014.79, 635.78, 469.7769],
        ['j', 189724.79, 635.78, -1437.5535],
        ['COL', 2, '1.2 D + 1.4 E + L', 'i', 165435.39, 38106.2, 90996.7256],
        ['j', 158145.39, 38106.2, -23321.870499999997],
        ['COL', 2, '1.2 D - 1.4 E + L', 'i', 162574.8, -37162.57, -90322.8591],
        ['j', 155284.8, -37162.57, 21164.8655],
        ['COL', 2, '0.9 D + 1.4 E', 'i', 83172.0, 37783.29, 90746.4378],
        ['j', 77704.5, 37783.29, -22603.431200000003],
        ['COL', 2, '0.9 D - 1.4 E', 'i', 80311.4, -37485.48, -90573.14689999999],
        ['j', 74843.9, -37485.48, 21883.304799999998],
        ['COL', 3, '1.4 D', 'i', 127153.76, -231.63, -134.7818],
        ['j', 118648.76, -231.63, 560.0983],
        ['COL', 3, '1.2 D + L', 'i', 164005.09, -471.81, -336.93330000000003],
        ['j', 156715.09, -471.81, 1078.5025],
        ['COL', 3, '1.2 D + 1.6 L', 'i', 197014.79, -635.78, -469.7769],
        ['j', 189724.79, -635.78, 1437.5535],
        ['COL', 3, '1.2 D + 1.4 E + L', 'i', 162574.8, 37162.57, 90322.8591],
        ['j', 155284.8, 37162.57, -21164.8655],
        ['COL', 3, '1.2 D - 1.4 E + L', 'i', 165435.39, -38106.2, -90996.7256],
        ['j', 158145.39, -38106.2, 23321.870499999997],
        ['COL', 3, '0.9 D + 1.4 E', 'i', 80311.4, 37485.48, 90573.14689999999],
        ['j', 74843.9, 37485.48, -21883.304799999998],
        ['COL', 3, '0.9 D - 1.4 E', 'i', 83172.0, -37783.29, -90746.4378],
        ['j', 77704.5, -37783.29, 22603.431200000003],
        ['COL', 4, '1.4 D', 'i', 83310.57, 3518.34, 3901.6325],
        ['j', 74805.57, 3518.34, -6653.387900000001],
        ['COL', 4, '1.2 D + L', 'i', 101635.11, 5166.32, 5724.1502],
        ['j', 94345.11, 5166.32, -9774.8033],
        ['COL', 4, '1.2 D + 1.6 L', 'i', 119770.75, 6456.68, 7152.0865],
        ['j', 112480.75, 6456.68, -12217.9429],
        ['COL', 4, '1.2 D + 1.4 E + L', 'i', 143165.56, 34034.73, 87009.5365],
        ['j', 135875.56, 34034.73, -15094.656599999998],
        ['COL', 4, '1.2 D - 1.4 E + L', 'i', 60104.67, -23702.1, -75561.23610000001],
        ['j', 52814.67, -23702.1, -4454.9499],
        ['COL', 4, '0.9 D + 1.4 E', 'i', 95087.24, 31130.2, 83793.57860000001],
        ['j', 89619.74, 31130.2, -9597.0313],
        ['COL', 4, '0.9 D - 1.4 E', 'i', 12026.35, -26606.62, -78777.194],
        ['j', 6558.85, -26606.62, 1042.6753999999999],
        ['COL', 5, '1.4 D', 'i', 62475.02, -4730.82, -7308.658399999999],
        ['j', 53970.02, -4730.82, 6883.79],
        ['COL', 5, '1.2 D + L', 'i', 76212.58, -6956.6, -10751.34],
        ['j', 68922.58, -6956.6, 10118.4546],
        ['COL', 5, '1.2 D + 1.6 L', 'i', 89810.12, -8697.57, -13443.4054],
        ['j', 82520.12, -8697.57, 12649.2925],
        ['COL', 5, '1.2 D + 1.4 E + L', 'i', 46333.15, 14638.11, 25426.3122],
        ['j', 39043.15, 14638.11, -18488.0276],
        ['COL', 5, '1.2 D - 1.4 E + L', 'i', 106092.02, -28551.31, -46928.9922],
        ['j', 98802.02, -28551.31, 38724.9368],
        ['COL', 5, '0.9 D + 1.4 E', 'i', 10283.08, 18553.47, 31479.229],
        ['j', 4815.58, 18553.47, -24181.188599999998],
        ['COL', 5, '0.9 D - 1.4 E', 'i', 70041.95, -24635.95, -40876.0754],
        ['j', 64574.45, -24635.95, 33031.7758],
        ['COL', 6, '1.4 D', 'i', 95373.23, 624.25, 1035.8644],
        ['j', 86868.23, 624.25, -836.8907],
        ['COL', 6, '1.2 D + L', 'i', 123017.57, 1120.26, 1835.5258999999999],
        ['j', 115727.57, 1120.26, -1525.2614],
        ['COL', 6, '1.2 D + 1.6 L', 'i', 147779.03, 1471.38, 2404.1111],
        ['j', 140489.03, 1471.38, -2010.0173000000002],
        ['COL', 6, '1.2 D + 1.4 E + L', 'i', 123975.89, 36631.7, 58778.3625],
        ['j', 116685.89, 36631.7, -51116.7331],
        ['COL', 6, '1.2 D - 1.4 E + L', 'i', 122059.25, -34391.17, -55107.3108],
        ['j', 114769.25, -34391.17, 48066.2104],
        ['COL', 6, '0.9 D + 1.4 E', 'i', 62269.68, 35912.74, 57608.749500000005],
        ['j', 56802.18, 35912.74, -50129.4729],
        ['COL', 6, '0.9 D - 1.4 E', 'i', 60353.04, -35110.13, -56276.9238],
        ['j', 54885.54, -35110.13, 49053.47059999999],
        ['COL', 7, '1.4 D', 'i', 95373.23, -624.25, -1035.8644],
        ['j', 86868.23, -624.25, 836.8907],
        ['COL', 7, '1.2 D + L', 'i', 123017.57, -1120.26, -1835.5258999999999],
        ['j', 115727.57, -1120.26, 1525.2614],
        ['COL', 7, '1.2 D + 1.6 L', 'i', 147779.03, -1471.38, -2404.1111],
        ['j', 140489.03, -1471.38, 2010.0173000000002],
        ['COL', 7, '1.2 D + 1.4 E + L', 'i', 122059.25, 34391.17, 55107.3108],
        ['j', 114769.25, 34391.17, -48066.2104],
        ['COL', 7, '1.2 D - 1.4 E + L', 'i', 123975.89, -36631.7, -58778.3625],
        ['j', 116685.89, -36631.7, 51116.7331],
        ['COL', 7, '0.9 D + 1.4 E', 'i', 60353.04, 35110.13, 56276.9238],
        ['j', 54885.54, 35110.13, -49053.47059999999],
        ['COL', 7, '0.9 D - 1.4 E', 'i', 62269.68, -35912.74, -57608.749500000005],
        ['j', 56802.18, -35912.74, 50129.4729],
        ['COL', 8, '1.4 D', 'i', 62475.02, 4730.82, 7308.658399999999],
        ['j', 53970.02, 4730.82, -6883.79],
        ['COL', 8, '1.2 D + L', 'i', 76212.58, 6956.6, 10751.34],
        ['j', 68922.58, 6956.6, -10118.4546],
        ['COL', 8, '1.2 D + 1.6 L', 'i', 89810.12, 8697.57, 13443.4054],
        ['j', 82520.12, 8697.57, -12649.2925],
        ['COL', 8, '1.2 D + 1.4 E + L', 'i', 106092.02, 28551.31, 46928.9922],
        ['j', 98802.02, 28551.31, -38724.9368],
        ['COL', 8, '1.2 D - 1.4 E + L', 'i', 46333.15, -14638.11, -25426.3122],
        ['j', 39043.15, -14638.11, 18488.0276],
        ['COL', 8, '0.9 D + 1.4 E', 'i', 70041.95, 24635.95, 40876.0754],
        ['j', 64574.45, 24635.95, -33031.7758],
        ['COL', 8, '0.9 D - 1.4 E', 'i', 10283.08, -18553.47, -31479.229],
        ['j', 4815.58, -18553.47, 24181.188599999998],
        ['COL', 9, '1.4 D', 'i', 41517.44, -5149.15, -7564.7628],
        ['j', 33012.44, -5149.15, 7882.6757],
        ['COL', 9, '1.2 D + L', 'i', 50616.34, -7552.31, -11105.5],
        ['j', 43326.34, -7552.31, 11551.4273],
        ['COL', 9, '1.2 D + 1.6 L', 'i', 59634.32, -9435.56, -13878.3505],
        ['j', 52344.32, -9435.56, 14428.336200000002],
        ['COL', 9, '1.2 D + 1.4 E + L', 'i', 33508.99, 8859.65, 5730.194],
        ['j', 26218.99, 8859.65, -20848.7658],
        ['COL', 9, '1.2 D - 1.4 E + L', 'i', 67723.7, -23964.27, -27941.193900000002],
        ['j', 60433.7, -23964.27, 43951.6204],
        ['COL', 9, '0.9 D + 1.4 E', 'i', 9582.43, 13101.8, 11972.632099999999],
        ['j', 4114.93, 13101.8, -27332.7588],
        ['COL', 9, '0.9 D - 1.4 E', 'i', 43797.14, -19722.13, -21698.755699999998],
        ['j', 38329.64, -19722.13, 37467.6275],
        ['COL', 10, '1.4 D', 'i', 63714.72, 106.72, 429.29220000000004],
        ['j', 55209.72, 106.72, 109.1337],
        ['COL', 10, '1.2 D + L', 'i', 82203.76, 351.45, 929.7013000000001],
        ['j', 74913.76, 351.45, -124.64540000000001],
        ['COL', 10, '1.2 D + 1.6 L', 'i', 98758.45, 507.43, 1266.7433],
        ['j', 91468.45, 507.43, -255.5584],
        ['COL', 10, '1.2 D + 1.4 E + L', 'i', 82775.3, 29899.47, 38649.1393],
        ['j', 75485.3, 29899.47, -51049.2658],
        ['COL', 10, '1.2 D - 1.4 E + L', 'i', 81632.23, -29196.57, -36789.7367],
        ['j', 74342.23, -29196.57, 50799.975099999996],
        ['COL', 10, '0.9 D + 1.4 E', 'i', 41531.0, 29616.62, 37995.4116],
        ['j', 36063.5, 29616.62, -50854.46309999999],
        ['COL', 10, '0.9 D - 1.4 E', 'i', 40387.93, -29479.41, -37443.4644],
        ['j', 34920.43, -29479.41, 50994.7778],
        ['COL', 11, '1.4 D', 'i', 63714.72, -106.72, -429.29220000000004],
        ['j', 55209.72, -106.72, -109.1337],
        ['COL', 11, '1.2 D + L', 'i', 82203.76, -351.45, -929.7013000000001],
        ['j', 74913.76, -351.45, 124.64540000000001],
        ['COL', 11, '1.2 D + 1.6 L', 'i', 98758.45, -507.43, -1266.7433],
        ['j', 91468.45, -507.43, 255.5584],
        ['COL', 11, '1.2 D + 1.4 E + L', 'i', 81632.23, 29196.57, 36789.7367],
        ['j', 74342.23, 29196.57, -50799.975099999996],
        ['COL', 11, '1.2 D - 1.4 E + L', 'i', 82775.3, -29899.47, -38649.1393],
        ['j', 75485.3, -29899.47, 51049.2658],
        ['COL', 11, '0.9 D + 1.4 E', 'i', 40387.93, 29479.41, 37443.4644],
        ['j', 34920.43, 29479.41, -50994.7778],
        ['COL', 11, '0.9 D - 1.4 E', 'i', 41531.0, -29616.62, -37995.4116],
        ['j', 36063.5, -29616.62, 50854.46309999999],
        ['COL', 12, '1.4 D', 'i', 41517.44, 5149.15, 7564.7628],
        ['j', 33012.44, 5149.15, -7882.6757],
        ['COL', 12, '1.2 D + L', 'i', 50616.34, 7552.31, 11105.5],
        ['j', 43326.34, 7552.31, -11551.4273],
        ['COL', 12, '1.2 D + 1.6 L', 'i', 59634.32, 9435.56, 13878.3505],
        ['j', 52344.32, 9435.56, -14428.336200000002],
        ['COL', 12, '1.2 D + 1.4 E + L', 'i', 67723.7, 23964.27, 27941.193900000002],
        ['j', 60433.7, 23964.27, -43951.6204],
        ['COL', 12, '1.2 D - 1.4 E + L', 'i', 33508.99, -8859.65, -5730.194],
        ['j', 26218.99, -8859.65, 20848.7658],
        ['COL', 12, '0.9 D + 1.4 E', 'i', 43797.14, 19722.13, 21698.755699999998],
        ['j', 38329.64, 19722.13, -37467.6275],
        ['COL', 12, '0.9 D - 1.4 E', 'i', 9582.43, -13101.8, -11972.632099999999],
        ['j', 4114.93, -13101.8, 27332.7588],
        ['COL', 13, '1.4 D', 'i', 20559.88, -6350.37, -6586.833299999999],
        ['j', 12054.88, -6350.37, 12464.2868],
        ['COL', 13, '1.2 D + L', 'i', 25022.76, -9343.24, -9697.4124],
        ['j', 17732.76, -9343.24, 18332.31],
        ['COL', 13, '1.2 D + 1.6 L', 'i', 29462.77, -11683.28, -12128.345500000001],
        ['j', 22172.77, -11683.28, 22921.491400000003],
        ['COL', 13, '1.2 D + 1.4 E + L', 'i', 18283.28, 285.92, -5294.8638],
        ['j', 10993.28, 285.92, -6152.6272],
        ['COL', 13, '1.2 D - 1.4 E + L', 'i', 31762.25, -18972.4, -14099.9609],
        ['j', 24472.25, -18972.4, 42817.2472],
        ['COL', 13, '0.9 D + 1.4 E', 'i', 6477.58, 5546.78, 168.1557],
        ['j', 1010.08, 5546.78, -16472.181399999998],
        ['COL', 13, '0.9 D - 1.4 E', 'i', 19956.55, -13711.54, -8636.9414],
        ['j', 14489.05, -13711.54, 32497.6931],
        ['COL', 14, '1.4 D', 'i', 32056.2, 1186.73, 1498.9201999999998],
        ['j', 23551.2, 1186.73, -2061.2666],
        ['COL', 14, '1.2 D + L', 'i', 41387.29, 2021.86, 2527.1816],
        ['j', 34097.29, 2021.86, -3538.3915],
        ['COL', 14, '1.2 D + 1.6 L', 'i', 49733.61, 2624.65, 3272.6173],
        ['j', 42443.61, 2624.65, -4601.3464],
        ['COL', 14, '1.2 D + 1.4 E + L', 'i', 41823.9, 23826.71, 23190.208599999998],
        ['j', 34533.9, 23826.71, -48289.926],
        ['COL', 14, '1.2 D - 1.4 E + L', 'i', 40950.68, -19783.0, -18135.845400000002],
        ['j', 33660.68, -19783.0, 41213.1431],
        ['COL', 14, '0.9 D + 1.4 E', 'i', 21044.17, 22567.75, 21626.618599999998],
        ['j', 15576.67, 22567.75, -46076.6345],
        ['COL', 14, '0.9 D - 1.4 E', 'i', 20170.95, -21041.96, -19699.435400000002],
        ['j', 14703.45, -21041.96, 43426.4346],
        ['COL', 15, '1.4 D', 'i', 32056.2, -1186.73, -1498.9201999999998],
        ['j', 23551.2, -1186.73, 2061.2666],
        ['COL', 15, '1.2 D + L', 'i', 41387.29, -2021.86, -2527.1816],
        ['j', 34097.29, -2021.86, 3538.3915],
        ['COL', 15, '1.2 D + 1.6 L', 'i', 49733.61, -2624.65, -3272.6173],
        ['j', 42443.61, -2624.65, 4601.3464],
        ['COL', 15, '1.2 D + 1.4 E + L', 'i', 40950.68, 19783.0, 18135.845400000002],
        ['j', 33660.68, 19783.0, -41213.1431],
        ['COL', 15, '1.2 D - 1.4 E + L', 'i', 41823.9, -23826.71, -23190.208599999998],
        ['j', 34533.9, -23826.71, 48289.926],
        ['COL', 15, '0.9 D + 1.4 E', 'i', 20170.95, 21041.96, 19699.435400000002],
        ['j', 14703.45, 21041.96, -43426.4346],
        ['COL', 15, '0.9 D - 1.4 E', 'i', 21044.17, -22567.75, -21626.618599999998],
        ['j', 15576.67, -22567.75, 46076.6345],
        ['COL', 16, '1.4 D', 'i', 20559.88, 6350.37, 6586.833299999999],
        ['j', 12054.88, 6350.37, -12464.2868],
        ['COL', 16, '1.2 D + L', 'i', 25022.76, 9343.24, 9697.4124],
        ['j', 17732.76, 9343.24, -18332.31],
        ['COL', 16, '1.2 D + 1.6 L', 'i', 29462.77, 11683.28, 12128.345500000001],
        ['j', 22172.77, 11683.28, -22921.491400000003],
        ['COL', 16, '1.2 D + 1.4 E + L', 'i', 31762.25, 18972.4, 14099.9609],
        ['j', 24472.25, 18972.4, -42817.2472],
        ['COL', 16, '1.2 D - 1.4 E + L', 'i', 18283.28, -285.92, 5294.8638],
        ['j', 10993.28, -285.92, 6152.6272],
        ['COL', 16, '0.9 D + 1.4 E', 'i', 19956.55, 13711.54, 8636.9414],
        ['j', 14489.05, 13711.54, -32497.6931],
        ['COL', 16, '0.9 D - 1.4 E', 'i', 6477.58, -5546.78, -168.1557],
        ['j', 1010.08, -5546.78, 16472.181399999998],
        ['VIGA', 17, '1.4 D', 'i', -1212.48, 12330.55, 13962.046299999998],
        ['j', -1212.48, -12434.28, 14325.1003],
        ['VIGA', 17, '1.2 D + L', 'i', -1790.28, 18132.53, 20526.143200000002],
        ['j', -1790.28, -18280.02, 21042.362999999998],
        ['VIGA', 17, '1.2 D + 1.6 L', 'i', -2240.89, 22670.62, 25661.348199999997],
        ['j', -2240.89, -22853.26, 26300.5863],
        ['VIGA', 17, '1.2 D + 1.4 E + L', 'i', -4365.66, 6481.52, -20971.3623],
        ['j', -4365.66, -29931.03, 61101.9431],
        ['VIGA', 17, '1.2 D - 1.4 E + L', 'i', 785.1, 29783.54, 62023.648799999995],
        ['j', 785.1, -6629.01, -19017.217099999998],
        ['VIGA', 17, '0.9 D + 1.4 E', 'i', -3354.82, -3724.23, -32521.9044],
        ['j', -3354.82, -19644.48, 49268.573200000006],
        ['VIGA', 17, '0.9 D - 1.4 E', 'i', 1795.93, 19577.79, 50473.1067],
        ['j', 1795.93, 3657.55, -30850.587000000003],
        ['VIGA', 18, '1.4 D', 'i', -819.85, 10841.25, 12729.1377],
        ['j', -819.85, -10841.25, 12729.1377],
        ['VIGA', 18, '1.2 D + L', 'i', -1141.83, 15417.5, 18128.3346],
        ['j', -1141.83, -15417.5, 18128.3346],
        ['VIGA', 18, '1.2 D + 1.6 L', 'i', -1405.29, 19092.5, 22458.9217],
        ['j', -1405.29, -19092.5, 22458.9217],
        ['VIGA', 18, '1.2 D + 1.4 E + L', 'i', -1141.83, 4238.46, -20998.289900000003],
        ['j', -1141.83, -26596.54, 57254.9592],
        ['VIGA', 18, '1.2 D - 1.4 E + L', 'i', -1141.83, 26596.54, 57254.9592],
        ['j', -1141.83, -4238.46, -20998.289900000003],
        ['VIGA', 18, '0.9 D + 1.4 E', 'i', -527.05, -4209.66, -30943.6075],
        ['j', -527.05, -18148.41, 47309.6416],
        ['VIGA', 18, '0.9 D - 1.4 E', 'i', -527.05, 18148.41, 47309.6416],
        ['j', -527.05, 4209.66, -30943.6075],
        ['VIGA', 19, '1.4 D', 'i', -1212.48, 12434.28, 14325.1003],
        ['j', -1212.48, -12330.55, 13962.046299999998],
        ['VIGA', 19, '1.2 D + L', 'i', -1790.28, 18280.02, 21042.362999999998],
        ['j', -1790.28, -18132.53, 20526.143200000002],
        ['VIGA', 19, '1.2 D + 1.6 L', 'i', -2240.89, 22853.26, 26300.5863],
        ['j', -2240.89, -22670.62, 25661.348199999997],
        ['VIGA', 19, '1.2 D + 1.4 E + L', 'i', 785.1, 6629.01, -19017.217099999998],
        ['j', 785.1, -29783.54, 62023.648799999995],
        ['VIGA', 19, '1.2 D - 1.4 E + L', 'i', -4365.66, 29931.03, 61101.9431],
        ['j', -4365.66, -6481.52, -20971.3623],
        ['VIGA', 19, '0.9 D + 1.4 E', 'i', 1795.93, -3657.55, -30850.587000000003],
        ['j', 1795.93, -19577.79, 50473.1067],
        ['VIGA', 19, '0.9 D - 1.4 E', 'i', -3354.82, 19644.48, 49268.573200000006],
        ['j', -3354.82, 3724.23, -32521.9044],
        ['VIGA', 20, '1.4 D', 'i', -418.33, 12452.58, 14448.5528],
        ['j', -418.33, -12312.25, 13957.4208],
        ['VIGA', 20, '1.2 D + L', 'i', -595.71, 18306.24, 21223.954500000003],
        ['j', -595.71, -18106.31, 20524.1993],
        ['VIGA', 20, '1.2 D + 1.6 L', 'i', -738.0, 22885.8, 26527.6429],
        ['j', -738.0, -22638.08, 25660.616800000003],
        ['VIGA', 20, '1.2 D + 1.4 E + L', 'i', -205.38, 5534.16, -24218.2216],
        ['j', -205.38, -30878.39, 64486.5823],
        ['VIGA', 20, '1.2 D - 1.4 E + L', 'i', -986.04, 31078.32, 66666.13070000001],
        ['j', -986.04, -5334.23, -23438.1837],
        ['VIGA', 20, '0.9 D + 1.4 E', 'i', 121.41, -4766.85, -36153.8207],
        ['j', 121.41, -20687.1, 52935.010700000006],
        ['VIGA', 20, '0.9 D - 1.4 E', 'i', -659.26, 20777.31, 54730.531500000005],
        ['j', -659.26, 4857.06, -34989.7554],
        ['VIGA', 21, '1.4 D', 'i', -935.86, 10841.25, 12691.2379],
        ['j', -935.86, -10841.25, 12691.2379],
        ['VIGA', 21, '1.2 D + L', 'i', -1364.52, 15417.5, 18069.2366],
        ['j', -1364.52, -15417.5, 18069.2366],
        ['VIGA', 21, '1.2 D + 1.6 L', 'i', -1701.94, 19092.5, 22383.856200000002],
        ['j', -1701.94, -19092.5, 22383.856200000002],
        ['VIGA', 21, '1.2 D + 1.4 E + L', 'i', -1364.52, 3032.21, -25279.2901],
        ['j', -1364.52, -27802.79, 61417.7633],
        ['VIGA', 21, '1.2 D - 1.4 E + L', 'i', -1364.52, 27802.79, 61417.7633],
        ['j', -1364.52, -3032.21, -25279.2901],
        ['VIGA', 21, '0.9 D + 1.4 E', 'i', -601.63, -5415.92, -35189.873700000004],
        ['j', -601.63, -19354.67, 51507.1796],
        ['VIGA', 21, '0.9 D - 1.4 E', 'i', -601.63, 19354.67, 51507.1796],
        ['j', -601.63, 5415.92, -35189.873700000004],
        ['VIGA', 22, '1.4 D', 'i', -418.33, 12312.25, 13957.4208],
        ['j', -418.33, -12452.58, 14448.5528],
        ['VIGA', 22, '1.2 D + L', 'i', -595.71, 18106.31, 20524.1993],
        ['j', -595.71, -18306.24, 21223.954500000003],
        ['VIGA', 22, '1.2 D + 1.6 L', 'i', -738.0, 22638.08, 25660.616800000003],
        ['j', -738.0, -22885.8, 26527.6429],
        ['VIGA', 22, '1.2 D + 1.4 E + L', 'i', -986.04, 5334.23, -23438.1837],
        ['j', -986.04, -31078.32, 66666.13070000001],
        ['VIGA', 22, '1.2 D - 1.4 E + L', 'i', -205.38, 30878.39, 64486.5823],
        ['j', -205.38, -5534.16, -24218.2216],
        ['VIGA', 22, '0.9 D + 1.4 E', 'i', -659.26, -4857.06, -34989.7554],
        ['j', -659.26, -20777.31, 54730.531500000005],
        ['VIGA', 22, '0.9 D - 1.4 E', 'i', 121.41, 20687.1, 52935.010700000006],
        ['j', 121.41, 4766.85, -36153.8207],
        ['VIGA', 23, '1.4 D', 'i', -1201.23, 12452.56, 14469.508899999999],
        ['j', -1201.23, -12312.27, 13978.4672],
        ['VIGA', 23, '1.2 D + L', 'i', -1790.93, 18303.58, 21248.8397],
        ['j', -1790.93, -18108.97, 20567.7196],
        ['VIGA', 23, '1.2 D + 1.6 L', 'i', -2247.72, 22881.55, 26556.681800000002],
        ['j', -2247.72, -22642.33, 25719.4254],
        ['VIGA', 23, '1.2 D + 1.4 E + L', 'i', -1310.75, 7935.71, -15553.902],
        ['j', -1310.75, -28476.84, 56340.061799999996],
        ['VIGA', 23, '1.2 D - 1.4 E + L', 'i', -2271.11, 28671.45, 58051.581399999995],
        ['j', -2271.11, -7741.1, -15204.6226],
        ['VIGA', 23, '0.9 D + 1.4 E', 'i', -292.03, -2362.65, -27500.914500000003],
        ['j', -292.03, -18282.9, 44758.4997],
        ['VIGA', 23, '0.9 D - 1.4 E', 'i', -1252.4, 18373.09, 46104.5688],
        ['j', -1252.4, 2452.84, -26786.1848],
        ['VIGA', 24, '1.4 D', 'i', -121.22, 10841.25, 12588.6806],
        ['j', -121.22, -10841.25, 12588.6806],
        ['VIGA', 24, '1.2 D + L', 'i', -120.52, 15417.5, 17915.8926],
        ['j', -120.52, -15417.5, 17915.8926],
        ['VIGA', 24, '1.2 D + 1.6 L', 'i', -130.5, 19092.5, 22191.2496],
        ['j', -130.5, -19092.5, 22191.2496],
        ['VIGA', 24, '1.2 D + 1.4 E + L', 'i', -120.52, 5184.56, -17899.4126],
        ['j', -120.52, -25650.44, 53731.1979],
        ['VIGA', 24, '1.2 D - 1.4 E + L', 'i', -120.52, 25650.44, 53731.1979],
        ['j', -120.52, -5184.56, -17899.4126],
        ['VIGA', 24, '0.9 D + 1.4 E', 'i', -77.93, -3263.57, -27722.582000000002],
        ['j', -77.93, -17202.32, 43908.02849999999],
        ['VIGA', 24, '0.9 D - 1.4 E', 'i', -77.93, 17202.32, 43908.02849999999],
        ['j', -77.93, 3263.57, -27722.582000000002],
        ['VIGA', 25, '1.4 D', 'i', -1201.23, 12312.27, 13978.4672],
        ['j', -1201.23, -12452.56, 14469.508899999999],
        ['VIGA', 25, '1.2 D + L', 'i', -1790.93, 18108.97, 20567.7196],
        ['j', -1790.93, -18303.58, 21248.8397],
        ['VIGA', 25, '1.2 D + 1.6 L', 'i', -2247.72, 22642.33, 25719.4254],
        ['j', -2247.72, -22881.55, 26556.681800000002],
        ['VIGA', 25, '1.2 D + 1.4 E + L', 'i', -2271.11, 7741.1, -15204.6226],
        ['j', -2271.11, -28671.45, 58051.581399999995],
        ['VIGA', 25, '1.2 D - 1.4 E + L', 'i', -1310.75, 28476.84, 56340.061799999996],
        ['j', -1310.75, -7935.71, -15553.902],
        ['VIGA', 25, '0.9 D + 1.4 E', 'i', -1252.4, -2452.84, -26786.1848],
        ['j', -1252.4, -18373.09, 46104.5688],
        ['VIGA', 25, '0.9 D - 1.4 E', 'i', -292.03, 18282.9, 44758.4997],
        ['j', -292.03, 2362.65, -27500.914500000003],
        ['VIGA', 26, '1.4 D', 'i', 6350.37, 12054.88, 12464.2868],
        ['j', 6350.37, -12709.95, 14757.060800000001],
        ['VIGA', 26, '1.2 D + L', 'i', 9343.24, 17732.76, 18332.31],
        ['j', 9343.24, -18679.79, 21646.8955],
        ['VIGA', 26, '1.2 D + 1.6 L', 'i', 11683.28, 22172.77, 22921.491400000003],
        ['j', 11683.28, -23351.11, 27045.6872],
        ['VIGA', 26, '1.2 D + 1.4 E + L', 'i', 15431.09, 10993.28, -6152.6272],
        ['j', 15431.09, -25419.27, 44338.363],
        ['VIGA', 26, '1.2 D - 1.4 E + L', 'i', 3255.39, 24472.25, 42817.2472],
        ['j', 3255.39, -11940.3, -1044.5721],
        ['VIGA', 26, '0.9 D + 1.4 E', 'i', 10170.23, 1010.08, -16472.181399999998],
        ['j', 10170.23, -14910.17, 32178.149500000003],
        ['VIGA', 26, '0.9 D - 1.4 E', 'i', -2005.46, 14489.05, 32497.6931],
        ['j', -2005.46, -1431.2, -13204.785600000001],
        ['VIGA', 27, '1.4 D', 'i', 5163.64, 10841.25, 12695.794199999998],
        ['j', 5163.64, -10841.25, 12695.794199999998],
        ['VIGA', 27, '1.2 D + L', 'i', 7321.38, 15417.5, 18108.504],
        ['j', 7321.38, -15417.5, 18108.504],
        ['VIGA', 27, '1.2 D + 1.6 L', 'i', 9058.62, 19092.5, 22444.3408],
        ['j', 9058.62, -19092.5, 22444.3408],
        ['VIGA', 27, '1.2 D + 1.4 E + L', 'i', 7321.38, 9114.62, -3951.563],
        ['j', 7321.38, -21720.38, 40168.571],
        ['VIGA', 27, '1.2 D - 1.4 E + L', 'i', 7321.38, 21720.38, 40168.571],
        ['j', 7321.38, -9114.62, -3951.563],
        ['VIGA', 27, '0.9 D + 1.4 E', 'i', 3319.49, 666.5, -13898.485],
        ['j', 3319.49, -13272.25, 30221.648999999998],
        ['VIGA', 27, '0.9 D - 1.4 E', 'i', 3319.49, 13272.25, 30221.648999999998],
        ['j', 3319.49, -666.5, -13898.485],
        ['VIGA', 28, '1.4 D', 'i', 6350.37, 12709.95, 14757.060800000001],
        ['j', 6350.37, -12054.88, 12464.2868],
        ['VIGA', 28, '1.2 D + L', 'i', 9343.24, 18679.79, 21646.8955],
        ['j', 9343.24, -17732.76, 18332.31],
        ['VIGA', 28, '1.2 D + 1.6 L', 'i', 11683.28, 23351.11, 27045.6872],
        ['j', 11683.28, -22172.77, 22921.491400000003],
        ['VIGA', 28, '1.2 D + 1.4 E + L', 'i', 3255.39, 11940.3, -1044.5721],
        ['j', 3255.39, -24472.25, 42817.2472],
        ['VIGA', 28, '1.2 D - 1.4 E + L', 'i', 15431.09, 25419.27, 44338.363],
        ['j', 15431.09, -10993.28, -6152.6272],
        ['VIGA', 28, '0.9 D + 1.4 E', 'i', -2005.46, 1431.2, -13204.785600000001],
        ['j', -2005.46, -14489.05, 32497.6931],
        ['VIGA', 28, '0.9 D - 1.4 E', 'i', 10170.23, 14910.17, 32178.149500000003],
        ['j', 10170.23, -1010.08, -16472.181399999998]
    ]
}

def filtroCV(combis, combi_e, combi_s, tab, largosV, largosC):

    bars1=[[tab[i-1]+tab[i] for j in range(2) if j==1]
            for i in range(len(tab)) if i%2!=0]
    bars2=[bars1[i][0] for i in range(len(bars1))]
    bars=[[bars2[i] for i in range(combis*j, combis*j+combis)]
            for j in range(int(len(bars2)/combis))]

    exc=[]
    for i in range(len(bars)):
        temp1=[]
        maxim=0
        for j in range(len(bars[0])):
            for k in range(len(bars[0][0])):
                if bars[i][j][4]/bars[i][j][6]>bars[i][j][8]/bars[i][j][10]:
                    pu=bars[i][j][4]
                    mu=bars[i][j][6]
                else:
                    pu=bars[i][j][8]
                    mu=bars[i][j][10]
                ex=mu/pu
                if ex>maxim:
                    maxim=ex
                    list1=[round(mu,1), round(pu,1), round(ex,3)]
        temp1.append(list1)
        exc.append(temp1)

    bars_e1=[bars2[i] for i in range(len(bars2)) if 'E' in bars2[i][2]]
    bars_s1=[bars2[i] for i in range(len(bars2)) if 'E' not in bars2[i][2]]
    bars_e=[[bars_e1[i] for i in range(combi_e*j, combi_e*j+combi_e)]
            for j in range(int(len(bars_e1)/combi_e))]
    bars_s=[[bars_s1[i] for i in range(combi_s*j, combi_s*j+combi_s)]
            for j in range(int(len(bars_s1)/combi_s))]
    col_e=[[bars_e[j][i] for i in range(0, combi_e)] for j in range(len(bars_e))
            if bars_e[j][0][0]=='COL']
    col_s=[[bars_s[j][i] for i in range(0, combi_s) if bars_s[j][i][2]!='1.2 D + L']
            for j in range(len(bars_s)) if bars_s[j][0][0]=='COL']

    col_dl=[[bars_s[j][i] for i in range(0, combi_s) if bars_s[j][i][2]=='1.2 D + L']
            for j in range(len(bars_s)) if bars_s[j][0][0]=='COL']
    vig_e=[[bars_e[j][i] for i in range(0, combi_e)]
            for j in range(len(bars_e)) if bars_e[j][0][0]=='VIGA']
    vig_s=[[bars_s[j][i] for i in range(0, combi_s)if bars_s[j][i][2]!='1.2 D + L']
            for j in range(len(bars_s)) if bars_s[j][0][0]=='VIGA']
    vig_dl=[[bars_s[j][i] for i in range(0, combi_s)if bars_s[j][i][2]=='1.2 D + L']
            for j in range(len(bars_s)) if bars_s[j][0][0]=='VIGA']

    maTrix_ij = lambda lista:[[[round(lista[k][j][i],1) for j in range(len(lista[0]))]
                               for i in [5,9]] for k in range(len(lista))]
    maxTrix_i = lambda lista:[[round(max([lista[k][j][i] for j in range(len(lista[0]))]),2)
                               for i in [4,5,6]] for k in range(len(lista))]
    minTrix_i = lambda lista:[[round(min([lista[k][j][i] for j in range(len(lista[0]))]),2)
                               for i in [4,5,6]] for k in range(len(lista))]
    maxTrix_j = lambda lista:[[round(max([lista[k][j][i] for j in range(len(lista[0]))]),2)
                               for i in [8,9,10]] for k in range(len(lista))]
    minTrix_j = lambda lista:[[round(min([lista[k][j][i] for j in range(len(lista[0]))]),2)
                               for i in [8,9,10]] for k in range(len(lista))]

    npisos, nbahias = len(col_e)-len(vig_e), int(len(vig_e)/(len(col_e)-len(vig_e)))


    forma_col = lambda lista, nbahias, npisos:[
        [lista[j] for j in range(i*(nbahias+1), (i+1)*(nbahias+1))] for i in range(npisos)]
    forma_vig = lambda lista, nbahias, npisos:[
        [lista[j] for j in range(i*(nbahias), (i+1)*(nbahias))] for i in range(npisos)]

    exc = forma_col(exc[:len(col_e)],nbahias, npisos)

    max_col_ei = forma_col(maxTrix_i(col_e),nbahias,npisos)
    max_col_si = forma_col(maxTrix_i(col_s),nbahias,npisos)
    max_col_dli = forma_col(maxTrix_i(col_dl),nbahias,npisos)

    min_col_ei = forma_col(minTrix_i(col_e),nbahias,npisos)
    min_col_si = forma_col(minTrix_i(col_s),nbahias,npisos)
    min_col_dli = forma_col(minTrix_i(col_dl),nbahias,npisos)

    max_col_ej = forma_col(maxTrix_j(col_e),nbahias,npisos)
    max_col_sj = forma_col(maxTrix_j(col_s),nbahias,npisos)
    max_col_dlj = forma_col(maxTrix_j(col_dl),nbahias,npisos)

    min_col_ej = forma_col(minTrix_j(col_e),nbahias,npisos)
    min_col_sj = forma_col(minTrix_j(col_s),nbahias,npisos)
    min_col_dlj = forma_col(minTrix_j(col_dl),nbahias,npisos)

    mat_col_e = forma_col(maTrix_ij(col_e),nbahias,npisos)
    mat_col_s = forma_col(maTrix_ij(col_s),nbahias,npisos)

    max_vig_ei = forma_vig(maxTrix_i(vig_e),nbahias,npisos)
    max_vig_si = forma_vig(maxTrix_i(vig_s),nbahias,npisos)
    max_vig_dli = forma_vig(maxTrix_i(vig_dl),nbahias,npisos)

    min_vig_ei = forma_vig(minTrix_i(vig_e),nbahias,npisos)
    min_vig_si = forma_vig(minTrix_i(vig_s),nbahias,npisos)
    min_vig_dli = forma_vig(minTrix_i(vig_dl),nbahias,npisos)

    max_vig_ej = forma_vig(maxTrix_j(vig_e),nbahias,npisos)
    max_vig_sj = forma_vig(maxTrix_j(vig_s),nbahias,npisos)
    max_vig_dlj = forma_vig(maxTrix_j(vig_dl),nbahias,npisos)

    min_vig_ej = forma_vig(minTrix_j(vig_e),nbahias,npisos)
    min_vig_sj = forma_vig(minTrix_j(vig_s),nbahias,npisos)
    min_vig_dlj = forma_vig(minTrix_j(vig_dl),nbahias,npisos)

    mat_vig_e = forma_vig(maTrix_ij(vig_e),nbahias,npisos)
    mat_vig_s = forma_vig(maTrix_ij(vig_s),nbahias,npisos)

    matCorte_col=[mat_col_e,mat_col_s]
    matCorte_vig=[mat_vig_e,mat_vig_s]

    #'axial', 'corte', 'momento'
    listaV=[]
    for i in range(len(max_vig_ei)):
        lista1=[]
        lista2=[]
        for j in range(len(max_vig_ei[i])):
            lista1=[[round(max_vig_si[i][j][1]/1000,2), round(max_vig_ei[i][j][1]/1000,2),
                     round(max(max_vig_ei[i][j][2],max_vig_si[i][j][2])/1000,2),
                     round(min(min_vig_ei[i][j][2],min_vig_si[i][j][2])/1000,2),round(max_vig_dli[i][j][1]/1000,2),
                     largosV[i][j],mat_vig_s[i][j][0],mat_vig_e[i][j][0]],
                    [round(max_vig_sj[i][j][1]/1000,2), round(max_vig_ej[i][j][1]/1000,2),
                     round(max(max_vig_ej[i][j][2],max_vig_sj[i][j][2])/1000,2),
                     round(min(min_vig_ej[i][j][2],min_vig_sj[i][j][2])/1000,2),round(max_vig_dlj[i][j][1]/1000,2),
                     largosV[i][j],mat_vig_s[i][j][1],mat_vig_e[i][j][1]]]
            lista2.append(lista1)
        listaV.append(lista2)
    listaC=[]
    for i in range(len(max_col_ei)):
        lista1=[]
        lista2=[]
        for j in range(len(max_col_ei[i])):
            #[vue, vu, .....]
            # round(max_col_dli[i][j][1] / 1000, 2)
            # round(max_col_dlj[i][j][1] / 1000, 2)
            lista1=[[round(max(max_col_ei[i][j][0], max_col_si[i][j][0])/1000,2),
                     round(min(min_col_ei[i][j][0], min_col_si[i][j][0])/1000,2), round(max_col_si[i][j][1]/1000,2),
                     round(max_col_ei[i][j][1]/1000,2), round(max(max_col_ei[i][j][2],max_col_si[i][j][2],
                                              abs(min_col_ei[i][j][2]),abs(min_col_si[i][j][2]))/1000,2),
                     largosC[i][j],mat_col_s[i][j][0],mat_col_e[i][j][0]],
                    [round(max(max_col_ej[i][j][0], max_col_sj[i][j][0])/1000,2),
                     round(min(min_col_ej[i][j][0], min_col_sj[i][j][0])/1000,2), round(max_col_sj[i][j][1]/1000,2),
                     round(max_col_ej[i][j][1]/1000,2), round(max(max_col_ej[i][j][2],max_col_sj[i][j][2],
                                              abs(min_col_ej[i][j][2]),abs(min_col_sj[i][j][2]))/1000,2),
                     largosC[i][j],mat_col_s[i][j][1],mat_col_e[i][j][1]]]
            lista2.append(lista1)
        listaC.append(lista2)
    # lista_aux=[listaC[-1][j][:6] for j in range(len(listaC[0]))]
    # return [listaV,listaVmax, listaC, listaCmax]
    return [listaV, listaC, exc]
    # return [listaV, listaC, exC, lista_aux]


# print(filtroCV(combis, combi_e, combi_s, tab, largosV, largosC))

def V2vig(x1, lo, vuLsti, vueLsti, vuLstj, vueLstj, vupr, vc, state):
    vc = vc if state==1 else 0
    v2Calc = lambda v1, v2, x1, lo: round(v1 - x1 * (v1 - v2) / lo, 1)
    vupr2 = v2Calc(vupr,-vupr,x1,lo)/0.75-vc
    vu2 = max([v2Calc(vuLsti[i],vuLstj[i], x1, lo) for i in range(len(vuLsti))])/0.75-vc
    vue2 = max([v2Calc(vueLsti[i],vueLstj[i], x1, lo) for i in range(len(vueLsti))])/0.6
    return round(max(vupr2,vu2, vue2),1)

def b1(fc):
    if 550 >= fc >= 280:
        return round(0.85-0.05/70*(fc-280), 2)
    else:
        return 0.85 if fc < 280 else 0.65

def et(h,eu,dp,c): return round(eu*abs(h-dp-c)/c, 4)

def aCir(d): return round(0.007854*d**2, 3)

def phi(eu,et,ey):
    if ey <= et <= (eu+ey):
        return round(0.65+0.25/eu*(et-ey), 2)
    else:
        return 0.65 if et < ey else 0.9

def aLstC(dEsq,dLat,nHor,nVer):
    a = round(aCir(dEsq)*2+nHor*aCir(dLat), 3)
    return [a]+[round(aCir(dLat)*2,3) for i in range(nVer)]+[a]

def yLstC(dp,h,nVer):
    yLst = [dp]
    for i in range(1,nVer+1):
        yi = round((h-yLst[i-1]-dp)/(nVer+2-i)+yLst[i-1],0)
        yLst.append(int(yi))
    yLst.append(h-dp)
    return yLst

def pmC(aLst,b,b1,c,es,eu,ey,fc,fy,h,yLst):
    eiLst = [round(eu*(c-i)/c, 5) for i in yLst]
    fsLst = [fy*abs(i)/i if abs(i)>ey else es*i for i in eiLst]
    psLst = [fsLst[i] * aLst[i] for i in range(len(aLst))]
    Pc = 0.85*b1*fc*b*c
    Ps = sum(psLst)
    Mc = Pc/2*(h-0.85*c)
    Ms = sum((psLst[i]*(h/2-yLst[i]) for i in range(len(aLst))))
    return [round((Pc+Ps)/1000, 2), round((Mc+Ms)/100000, 2)]

def cPn(aLst,b,b1,dp,es,eu,ey,fc,fy,h,pnB,yLst):
    c1 = 0
    c2 = max(h/b1, 3*(h-dp))
    PnMax = round((0.85*fc*(h*b-sum(aLst))+sum(aLst)*fy)/1000, 2)
    PhiPnMax = PnMax*0.8*0.65
    PnMin = round((-sum(aLst)*fy)/1000, 2)
    PhiPn = pnB+10
    i = 0
    if pnB > PnMin * 0.9:
        pnB = PhiPnMax if pnB >= PhiPnMax else pnB
        while abs(pnB-PhiPn) > 0.1 and i<15:
            c = round((c1+c2)/2,3)
            i += 1
            PMC = pmC(aLst,b,b1,c,es,eu,ey,fc,fy,h,yLst)
            eT = et(h,eu,dp,c)
            Phi = phi(eu,eT,ey)
            PhiPn = (PMC[0])*Phi
            PhiMn = (PMC[1])*Phi
            c2 = c if PhiPn > pnB else c2
            c1 = c if PhiPn < pnB else c1
    else:
        c = 0
        PhiPn = PnMin*0.9
        PhiMn = 0
        Phi = 0.9
    return [round(c, 2), abs(round(PhiMn, 1)), round(PhiPn, 1), Phi]

def cFind(aLst, b, b1, dp, es, eu, ey, fc, fy, h, mu, pu, yLst):
    mu = round(abs(mu),3)
    pu = round(pu,3)
    PhiPnMin = round((-sum(aLst)*fy)/1000*0.9,1)
    PhiPnMax = round((0.85*fc*(h*b-sum(aLst))+sum(aLst)*fy)*0.8*0.65/1000,1)
    if pu<PhiPnMin:
        pu = PhiPnMin
    if pu>PhiPnMax:
        pu = PhiPnMax
    elif abs(pu) <= 0.1:
        return cPn(aLst,b,b1,dp,es,eu,ey,fc,fy,h,0,yLst)
    e = min(mu/pu,999)
    i = 0
    c2 = 0
    ex = e+1
    c1 = h/b1 if e > 0 else cPn(aLst,b,b1,dp,es,eu,ey,fc,fy,h,0,yLst)[0]
    while abs(round(e,3)-ex) > 0.001 and i < 15:
        c = round((c1+c2)/2,2)
        i += 1
        PMC = pmC(aLst,b,b1,c,es,eu,ey,fc,fy,h,yLst)
        ex = round((abs(PMC[1]))/(PMC[0]),3)
        c1 = c if ex < e else c1
        c2 = c if ex > e else c2
    e = ex
    eT = round(eu*abs(h-dp-c)/c,4)
    Phi = phi(eu,eT,ey)
    asdf=pmC(aLst,b,b1,c,es,eu,ey,fc,fy,h,yLst)
    phipn = PMC[0]*Phi
    phimn = PMC[1]*Phi
    return [c,abs(round(phimn,1)),round(phipn,1), Phi, e, PhiPnMin, PhiPnMax]

def resumen(aLst, c, b, dp, h, eu, fy, fc, b1, es, ey, yLst):
    PMC = pmC(aLst, b, b1, c, es, eu, ey, fc, fy, h, yLst)
    eT = round(eu*abs(h-dp-c)/c, 4)
    Phi = phi(eu, eT, ey)
    PMCpr = pmC(aLst, b, b1, c, es, eu, ey, fc, fy*1.25, h, yLst)
    return [PMC[0]*Phi,PMC[0],PMCpr[0],PMC[1]*Phi,PMC[1],PMCpr[1]]

def FU(pu, mu, pn, mn):
    if abs(mu) < 0.1:
        return abs(pu/(pn+0.01))
    else:
        return max(abs(pu/(pn+0.01)), abs(mu/(mn+0.01)))

def yLstV(h, dp, db):
    # se busca el minimo de niveles barras laterales complementarias
    blat = min(int((h-2*dp-db/4)/25), int((h-2*dp-db/4)/20)+1)
    # se crea lista con dos primeros niveles (1/4*10=2.5 veces el diámetro mayor)
    Y = [dp, max(dp+db/4, 2*dp)]
    #se agrega cada nivel de barras complementarias
    for i in range(blat):
        Y.append(round(Y[-1]+(h-2*dp-db/4)/(blat+1), 0))
    # la función retorna la lista de posiciones de barras completa
    return Y + [h - dp] if Y[-1] < (h-dp) else Y

# función para el cálculo de área requerida asegurando et>=0.005
def areaV(mu, b, b1, h, fc, fy, dp):
    muu = round(mu/(0.9*0.85/100000*fc*b*(h-dp)**2), 3)
    muu = 0.5 if muu > 0.5 else muu
    ulim = round(0.375*b1*(1-0.1875*b1), 3)
    wp = 0 if muu < ulim else round((muu-ulim)/(1-dp/(h-dp)), 3)
    w = 0.375+wp if wp > 0 else round(1-(1-2*muu)**0.5, 3)
    return round(w*0.85*fc*b*(h-dp)/fy, 2)

def listadiam1(A, b, dp, h, dList, v):
    sup = [i for i in range(int(1+(b-2*dp)/15), 2+int((b-2*dp)/10))]
    listadiam = []
    for i in sup:
        n2 = int(i/2) if i>2 else 0
        n1 = i-n2
        for j in range(len(dList)):
            j = dList[j]
            if n2>0:
                for k in range(len(dList)):
                    k = dList[k]
                    if A<=n1*aCir(j)+n2*aCir(k) and j+v>=k>=j-v:
                        listadiam+=[[n1, j, n2, k, round(aCir(j)*n1+aCir(k)*n2, 2)]]
                    else:
                        continue
            else:
                if 1.2*A>=n1*aCir(j)>=A:
                    listadiam+=[[n1, j, n2, 0, round(n1*aCir(j), 2)]]
                else:
                    continue
    return listadiam

def listadiam(A, b, dp, h, dList, v):
    amin = 10*A
    A /= 2
    lista1 = listadiam1(A, b, dp, h, dList, v)
    lista2 = []
    minimos = []
    for i in range(len(lista1)):
        if lista1[i][4]<=1.2*A:
            lista2+=[lista1[i]]
        else:
            continue
    for i in range(len(lista2)):
        L1 = lista2[i]
        ar1= L1[4]
        ar2=round(2*A-ar1, 2)
        ar2 = ar2 if ar2>0 else 0
        lista3 = listadiam1(ar2, b, dp, h, dList, v)
        if lista3 == []:
            continue
        for j in range(len(lista2)):
            L2 = lista3[i]
            if 2*A>L1[4]+L2[4]:
                continue
            else:
                if L1[4]+L2[4]<amin:
                    amin = L1[4]+L2[4]
                    if L2[4]>L1[4]:
                        minimos = [L2, L1, round(amin, 2)]
                    else:
                        minimos = [L1, L2, round(amin, 2)]
    return minimos


def critVC(vigas,columnas):
    newcol=[]
    for i in range(len(vigas)-1):
        new=[]
        for j in range(len(vigas[0])):
            if i == 0:
                mc1=columnas[i][j]
                mc2=columnas[i+1][j]
                mv1=vigas[i][j][0]
                mc=mc1+mc2
                dif=1.2*mv1-mc
                if dif > 0:
                    columnas[i][j]=dif*mc1/(mc1+mc2)+mc1
                    columnas[i+1][j]=dif*mc2/(mc1+mc2)+mc2
            elif i == len(vigas[0])-1:
                mc1 = columnas[i][j]
                mc2 = columnas[i + 1][j]
                mv2 = vigas[i][j][1]
                mc = mc1 + mc2
                dif = 1.2 * mv2 - mc
                if dif > 0:
                    columnas[i][j] = dif * mc1 / (mc1 + mc2) + mc1
                    columnas[i+1][j] = dif * mc2 / (mc1 + mc2) + mc2
            else:
                mc1 = columnas[i][j]
                mc2 = columnas[i+1][j]
                mv1 = vigas[i][j][0]
                mv2 = vigas[i][j][1]
                mc = mc1 + mc2
                dif = 1.2 * (mv1+mv2) - mc
                if dif > 0:
                    columnas[i][j] = dif * mc1 / (mc1 + mc2) + mc1
                    columnas[i+1][j] = dif * mc2 / (mc1 + mc2) + mc2
        newcol.append(new)
    newcol.append(columnas[-1])
    return newcol

def extMat(lista, indice):
    mat1=[]
    for i in lista:
        mat2=[]
        for j in i:
            mat2.append(j[indice])
        mat1.append(mat2)
    return mat1

def replMat(lista1, lista2, indice):
    for i in range(len(lista2)):
        for j in range(len(lista2[i])):
            lista1[i][j][indice]=lista2[i][j]
    return lista1

def matElemV(lista, bmaxV, hmaxV, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, ai, deList, v):
    #se itera en la lista
    listaV = []
    for i in lista:
        # se filtra la lista por piso
        tempV=[]
        for j in i:
            elem = optimusVig(j[2],j[3],es,eu,ey,b1,fc,fy,dp,dList,hmaxV,bmaxV,ai,j[5],cH,cS,v)
            tempV.append(elem)
        listaV.append(tempV)
    return listaV

def Lramas(xList):
    lar=len(xList)
    lista = [xList[0]]
    if lar%2 == 0:
        rango = xList[-1]-xList[0]
        for i in range(1, lar-1):
            if xList[i]-lista[-1]==30:
                lista.append(xList[i])
            elif xList[i]-lista[-1]>30:
                lista.append(xList[i-1])
        lista.append(xList[-1])
        minram = int((len(lista)+1)/2)*2
        maxram = len(xList)
        rlist = [i for i in range(minram, maxram+1, 2)]
        listas = []
        for i in rlist:
            sep = round(rango/(i-1), 1)
            complist = [xList[0]]
            for _ in range(i-1):
                complist.append(sep+complist[-1])
            lista2 = [xList[0]]
            for j in range(1, len(complist)-1):
                dif=999
                for k in xList:
                    if abs(k-complist[j])<dif:
                        dif = abs(k-complist[j])
                        bar = k
                lista2.append(bar)
            lista2.append(xList[-1])
            listas.append(lista2)
    else:
        mid = int(lar/2)
        midL = xList[0:mid+1]
        rango=midL[-1]-midL[0]
        for i in range(1, len(midL)-1):
            if midL[i]-lista[-1]==30:
                lista.append(midL[i])
            elif midL[i]-lista[-1]>30:
                lista.append(midL[i-1])
        lista.append(midL[-1])
        if lista[-2]-(xList[0]+xList[-1])/2<=15:
            lista.remove(lista[-1])
        lista2 = []
        for j in reversed(lista):
            lista2.append(xList[-1]+xList[0]-j)
        lista+=lista2
        listas=[lista]
        minram=2
        maxram=len(xList)
        rlist=[i for i in range(minram, maxram+1)]
        for i in rlist:
            sep = round(rango/(i-1), 1)
            complist = [xList[0]]
            rango=xList[-1]-xList[0]
            for _ in range(i-1):
                complist.append(sep+complist[-1])
            lista2 = [xList[0]]
            for j in range(1, len(complist)-1):
                dif=999
                for k in xList:
                    if abs(k-complist[j])<dif:
                        dif = abs(k-complist[j])
                        bar = k
                lista2.append(bar)
            lista2.append(xList[-1])
            if rlist[0]==i:
                continue
            else:
                listas.append(lista2)
    listas2=[]
    for i in listas:
        borrar = 0
        for j in range(1, len(i)):
            if i[j]-i[j-1]>30:
                borrar=1
        if borrar!=1:
            listas2.append(i)
    return listas2

def estribosV(xList, ramas):
    Lestrib = []
    medio = xList[int(len(xList)/2)]
    for j in ramas:
        mid=int(len(j)/2)
        L1 = j[0:mid]
        if len(j)%2!=0:
            L2 = j[mid+1:]
            cond=1
        else:
            L2 = j[mid:]
            cond=0
        estribos=[[L1[i],L2[i]] for i in range(len(L1))]
        if cond==1:
            estribos+=[[medio]]
        Lestrib.append(estribos)
    return Lestrib

def ldC(fy,fc,db):
    return round(max(0.075*fy*0.1*db/(fc)**0.5, 0.0044*fy*0.1*db),1)

def ldV(db, fc, fy):
    if db<19:
        return 0.1*db*fy/(3.46*(fc)**0.5)
    else:
        return 0.1*db*fy/(4.4*(fc)**0.5)

def lempV(db, fc, fy):
    if db<19:
        ld = 0.1*db*fy/(6.6*(fc)**0.5)
    else:
        ld = 0.1*db*fy/(5.34*(fc)**0.5)
    return ld

def ldhV(fy, db, fc):
    return fy*db/(170*(fc)**0.5)

def lGanchoC(db, fc, fy, h, dp):
    if db<19:
        ld = round(max(0.1*db*fy/(3.46*(fc)**0.5), 2.5*db+10),1)
        return [round(ldC(fy,fc,db)+0.6*3.1416/4*db+ld,1), ld]
    else:
        ld = round(max(0.1*db*fy/(4.4*(fc)**0.5), 2.5*db+10))
        return [round(ldC(fy,fc,db)+0.6*3.1416/4*db+ld,1), ld]

def lGanchoV(fy, db, fc):
    return round(ldhV(fy,db,fc)+1.05*db-5,1)

def rematC(db, ldV, h, dp):
    return max(2.5*db+10, ldV+dp-h)

def aminV(fc,b,fy):
    return max(0.2*(fc)**0.5*b/fy,3.5*b/fy)

def countram(ramas):
    nramas=[]
    for i in ramas:
        nramas+=[len(i)]
    return nramas

def Lest(h, b, dp, de):
    return round((2*(h+b-4*dp+0.2*de)*10+6.75*de*3.1416+2*max(75, 6*de))/10, 2)

def Ltrab(h, dp, de):
    return round((3.75*de*3.1416+2*max(75, 6*de)+(h+0.2*de-dp)*10)/10, 2)

def vc(fc, b, h, dp):
    return round(0.53*(fc)**0.5*b*(h-dp)/1000, 2)

def ashS(h, b, dp, fc, fy):
    return round(max(0.3*((b*h)/((h-dp)*(b-dp)))*(fc/fy), 0.09*(h-dp)*fc/fy), 3)

def loCol(h, b, H):
    return round(max(h, b, H/6, 45), 1)

def lEmp(fy, db):
    return round(max(0.00073*fy*db if fy<= 4200 else (0.0013*fy-2.4)*db, 30),0)

#wo es corte y no carga distribuida
def vprV(h, b, l, mpr1, mpr2, wo):
    return 100*(mpr1+mpr2)/l + wo/50

def VcAx(Nu, fc, b, h, dp):
    return round(0.53*(1+Nu*1000/(140*h*b))*(fc)**0.5*b*(h-dp)/1000, 1)

def vsLim(fc, b, h, dp):
    return round(2.2*(fc)**0.5*b*(h-dp)/1000,2)

def sRotV(h, dp, db):
    return round(max(min(15, 0.6*db, (h-dp)/4),8), 1)

def sRotC(h, b, db, hx):
    return round(min(max(min(15,0.6*db,(10+(35-hx)/3)),8),10),1)

def sMax(fc, b, h, dp, sm):
    return min(round((h-dp)/4 if vc(fc, b, h, dp)>0.33*(h-dp)*b*(fc/10)**0.5 else (h-dp)/2, 2), sm)

def sEmp(h, dp):
    return round(min(10, (h-dp)/4), 1)

def sCol(db):
    return min(0.6*db, 15)

def cubEstV(h, dp, de, Le):
    lista1 = []
    lista2 = []
    for i in Le:
        if len(i)%2 == 0:
            b = i[1]-i[0]
            lista1 += [Lest(h, b, dp, de)]
        else:
            lista2 += [Ltrab(h, dp, de)]
    return [round((sum(lista1)+sum(lista2))*aCir(de) ,1), lista1, lista2]

def estribosC(xList):
    lista = []
    ramas = Lramas(xList)
    count = []
    for i in ramas:
        count.append(len(i))
        Lestrib = []
        temp = i
        while len(temp) > 0:
            if len(temp) >= 2:
                Lestrib.append([temp[0],temp[-1]])
                temp.remove(temp[0])
                temp.remove(temp[-1])
            elif len(temp) == 1:
                Lestrib.append([temp[0]])
                temp.remove(temp[0])
            else:
                break
        lista.append(Lestrib)
        Lestrib = []
    return lista, count

def xLst(sup, b, dp):
    mid = int(sup[0] / 2)
    if sup[2]%2==0:
        l1=[sup[1] for i in range(mid)]
        l2=[sup[3] for i in range(sup[2])]
    else:
        l1=[sup[1] for i in range(mid)]
        l2=[sup[3] for i in range(sup[2])]
    lista=l1+l2+l1
    xList=yLstC(dp, b, len(lista)-2)
    return lista, xList

#revisar

def minEstC(mpr1, mpr2, Nu, H, vu, vue, yList, deList, db, h, b, dp, fy, fc, cS):
    salida1, salida2, salida3 = 0, 0, 0
    H*=100
    vu = vu*1000
    vue = vue*1000
    mpr1*=100000
    mpr2*=100000
    Vc = VcAx(Nu, fc, b, h, dp)*1000
    vupr = round((mpr1+mpr2)/H,1)
    vupr1 = vupr if Nu*1000 < 0.05 * fc * (h * b) else vupr-Vc
    vupr2 = vupr-Vc
    vu1 = round(max((vu-Vc)/0.75, vue/0.6, vupr1/0.75),1)
    vslim = vsLim(fc, b, h, dp)*1000*1.1
    lo = loCol(h, b, H)
    vu2 = round(max((vu-Vc)/0.75, vue/0.6, (vupr1-Vc)/0.75), 1)
    s = round(sCol(db))
    estr = estribosC(yList)
    est = estr[0]
    nRam = estr[1]
    ramas = Lramas(yList)
    if len(ramas)>1:
        srotL = [int(sRotC(h, b, db, l)) for l in [min(k) for k in [[i[j]-i[j-1] for j in range(1,len(i))] for i in ramas]]]
    else:
        ramitas = ramas[0]
        aux1=[ramitas[i]-ramitas[i-1] for i in range(1,len(ramitas))]
        srotL =  [int(sRotC(h, b, db, max(aux1)))]

    sash = round(max(ashS(h, b, dp, fc, fy),aminV(fc,b,fy)), 3)

    s1L = [[i, j, k, l] for i in range(len(nRam)) for j in deList for l in deList if l <= j
           for k in range(8, min(int(sRotC(h, b, db, srotL[i])), int(round(100/((sash * 100 / (2 * aCir(j) + (nRam[i] - 2) * aCir(l)))-1), 1))+1))
           if vu1 <= round((2*aCir(j)+(nRam[i]-2)*aCir(l))*fy*(h-dp)/k, 1) <= vslim]

    if s1L==[]:
        return 0
    minimo = 99999999
    for i, j, k, l in s1L:
        ramas1 = est[i]
        l1 = Lest(h, ramas1[0][1]-ramas1[0][0], dp, j)
        l2 = sum([Lest(h, ramas1[m][1]-ramas1[m][0], dp, l) if len(ramas1[m])==2 else Ltrab(h, dp, l)
                  for m in range(1,len(ramas1))])
        s1 = int((lo-0.01)/k)+1
        costo = round(2*s1*(l1*aCir(j)+2*l2*aCir(l))*cS/1000000, 0)
        if costo<minimo:
            minimo=costo
            l2a = [Lest(h, ramas1[m][1] - ramas1[m][0], dp, l) if len(ramas1[m]) == 2 else Ltrab(h, dp, l)
                   for m in range(1, len(ramas1))]
            lram = ramas1
            lista1=[costo, nRam[i], j, k, l, s1, l1, l2a, l2, lram, lo]
            salida1=1
    l_rot = lista1[3]
    l_emp = lEmp(fy, db)
    # s2L = [[i, j, k, l] for i in range(len(nRam)) for j in deList for k in range(10, s+1) for l in deList
    #        if vu2<=round((2*aCir(j)+(nRam[i]-2)*aCir(l))*fy*(h-dp)/k, 1) <= vslim and l <= j]
    s2L = [[i, j, k, l] for i in range(len(nRam)) for j in deList for l in deList if l <= j
           for k in range(10, min(int(s), int(round(100/((sash * 100 / (2 * aCir(j) + (nRam[i] - 2) * aCir(l)))-1), 1)))+1)
           if vu2 <= round((2*aCir(j)+(nRam[i]-2)*aCir(l))*fy*(h-dp)/k, 1) <= vslim]
    if s2L==[]:
        return 0
    minimo = 99999999
    for i, j, k, l in s2L:
        ramas1 = est[i]
        l1 = Lest(h, ramas1[0][1] - ramas1[0][0], dp, j)
        l2 = sum([Lest(h, ramas1[m][1] - ramas1[m][0], dp, l) if len(ramas1[m]) == 2 else Ltrab(h, dp, l)
                  for m in range(1, len(ramas1))])
        s2 = int((H-2*lo-l_emp-0.01)/k)
        dist2 = H-2*lo-l_emp
        costo = round(s2*(l1*aCir(j)+2*l2*aCir(l))*cS/1000000, 0)
        if costo<minimo:
            minimo=costo
            l2a = [Lest(h, ramas1[m][1] - ramas1[m][0], dp, l) if len(ramas1[m]) == 2 else Ltrab(h, dp, l)
                   for m in range(1, len(ramas1))]
            lram = ramas1
            lista2=[costo, nRam[i], j, k, l, s2, l1, l2a, l2, lram, dist2]
            salida2=1
    semp = int(sEmp(h, dp))
    # s3L = [[i, j, k, l] for i in range(len(nRam)) for j in deList for k in range(8, semp+1) for l in deList
    #        if vu2<=round((2*aCir(j)+(nRam[i]-2)*aCir(l))*fy*(h-dp)/k, 1) <= vslim and l <= j]
    s3L = [[i, j, k, l] for i in range(len(nRam)) for j in deList for l in deList if l <= j
           for k in range(8, min(int(semp), int(round(100/((sash * 100 / (2 * aCir(j) + (nRam[i] - 2) * aCir(l)))-1), 1))+1))
           if vu2 <= round((2*aCir(j)+(nRam[i]-2)*aCir(l))*fy*(h-dp)/k, 1) <= vslim]
    if s3L==[]:
        return 0
    minimo = 99999999
    for i, j, k, l in s3L:
        ramas1 = est[i]
        l1 = Lest(h, ramas1[0][1] - ramas1[0][0], dp, j)
        l2 = sum([Lest(h, ramas1[m][1] - ramas1[m][0], dp, l) if len(ramas1[m]) == 2 else Ltrab(h, dp, l)
                  for m in range(1, len(ramas1))])
        s3 = int((l_emp-0.01)/k)+1
        costo = round(s3*(l1*aCir(j)+2*l2*aCir(l))*cS/1000000, 0)
        if costo < minimo:
            minimo = costo
            l2a = [Lest(h, ramas1[m][1] - ramas1[m][0], dp, l) if len(ramas1[m]) == 2 else Ltrab(h, dp, l)
                   for m in range(1, len(ramas1))]
            lram = ramas1
            lista3 = [costo, nRam[i], j, k, l, s3, l1, l2a, l2, lram, l_emp]
            salida3=1
    costo_total = lista1[0]+lista2[0]+lista3[0]
    # lista1 --> [costo, n° ramas, de_externo, espaciamiento, de_interno, n° estribos, largo1, largos2, largo_tot2, d_ramas, dist]
    # lista2 --> [costo, n° ramas, de_externo, espaciamiento, de_interno, n° estribos, largo1, largos2, largo_tot2, d_ramas, dist]
    # lista3 --> [costo, n° ramas, de_externo, espaciamiento, de_interno, n° estribos, largo1, largos2, largo_tot2, d_ramas, dist]
    salida=salida1+salida2+salida3
    if salida == 3:
        return [lista1,lista2,lista3,costo_total,vu1,vu2]
    else:
        return 0

def optimusCol(b1, dp, es, eu, ey, fc, fy, muC, muCmin, puCmin, puCmax, dList, hmax, hmin, cH, cS, H, vu, vue, deList, iguales):
    salida=0
    minor = 9999999
    hmin = hmin if hmin >= 30 else 30
    hmax = hmax if hmax>=30 else 30
    hList = [i for i in range(hmin, hmax+5,5)]
    lista = ([b, h] for b in hList for h in hList if b == h)
    for b, h in lista:
        nH = [i for i in range(int((b-2*dp)/15)-1, int(round((b-2*dp)/10, 0)), 1)]
        nV = nH
        listaND = ([j, k] for j in nH for k in nV if 10 <= (b-2*dp)/(j+1) <= 15 and
                   10 <= (h-2*dp)/(k+1) <= 15 and j == k)
        for j, k in listaND:
            if iguales == 0:
                listaDm = ([l, m] for l in dList for m in dList if m <= l >=16)
            else:
                listaDm = ([l, m] for l in dList for m in dList if m == l >= 16)
            for l, m in listaDm:
                ylist = yLstC(dp, h, k)
                alist = aLstC(l, m, j, k)
                cF = cFind(alist, b, b1, dp, es, eu, ey, fc, fy, h, muC, puCmax, ylist)
                cF2 = cFind(alist, b, b1, dp, es, eu, ey, fc, fy, h, muCmin, puCmin, ylist)
                fu = round(FU(puCmax, muC, cF[2], cF[1])*100,1)
                fu2 = round(FU(puCmin, muCmin, cF2[2], cF2[1])*100,1)
                aS = aCir(l)*4+aCir(m)*(2*j+2*k)
                cuan = round(aS/(b*h), 5)
                mpr1 = max(pmC(alist, b, b1, cF[0], es, eu, ey, fc, fy*1.25, h, ylist)[1],
                           pmC(alist, b, b1, cF2[0], es, eu, ey, fc, fy*1.25, h, ylist)[1])
                mpr2 = mpr1
                #agregar a entrada H, vu, vue, deList
                if fu < 95 and fu2 < 95 and 0.01 <= cuan <= 0.06:
                    corte1 = minEstC(mpr1, mpr2, muC, H, vu, vue, ylist, deList, min(l, m), h, b, dp, fy, fc, cS)
                    if corte1 != 0:
                        costo1 = round((aS*cS+(b*h-aS)*cH)/10000, 0)*(corte1[2][10]+H*100)/100
                        costo2 = corte1[3]
                        costo = costo1+costo2
                        if costo < minor:
                            # corte = minEstC(mpr1, mpr2, muC, H, vu, vue, ylist, deList, min(l, m), h, b, dp, fy, fc, cS)
                            minor, e = costo, round(cF[1] / (cF[2] + 0.001), 3)
                            optimo = [minor, h, b, j, k, l, m, fu, fu2, cuan, cF[0], cF2[0], e, alist, ylist, cF[1],
                                      cF[2], muC, puCmax, puCmin, H, iguales, round(muCmin/puCmin,3), cF2[1], cF2[2], costo1, costo2, dp]
                            salida=1
                            corte=corte1
                    else:
                        continue
    if salida==1:
        return [optimo, corte]
    else:
        return 0

def minEstV(mpr1, mpr2, vuLsti,vueLsti,vuLstj,vueLstj, xList, deList, db, h, b, lo, dp, fy, fc, cS, wo, yLst):
    lo*=100
    Vc = vc(fc, b, h, dp)*1000
    vupr = round(vprV(h, b, lo, mpr1, mpr2,wo),3)*1000
    smax = sMax(fc, b, h, dp, 20)
    srot = int(sRotV(h, dp, db))
    sL1 = [i for i in range(8, int(srot)+1)]
    sL2 = [i for i in range(8, int(smax)+1)]
    vsL = vsLim(fc, b, h, dp)*1000*1.1
    ramas = Lramas(xList)
    est = estribosV(xList, ramas)
    nRam = countram(ramas)
    x1 = 2*h
    x2 = lo/2-2*h
    amin=aminV(fc,b,fy)
    Lout=[]
    for n in range(x1, x1 + 35, 5):
        xa1 = n
        xa2 = (x1 + x2) - xa1
        vsB1 = V2vig(0,lo,vuLsti,vueLsti,vuLstj,vueLstj,vupr,Vc,0)
        vsB2 = V2vig(xa1,lo,vuLsti,vueLsti,vuLstj,vueLstj,vupr,Vc,1)
        lista=[[i,j,k,l,m] for i in nRam for j in sL1 for k in deList for l in nRam
        for m in sL2 if vsB1/(fy*(h-dp))<=i*aCir(k)/j<=vsL/(fy*(h-dp))
        and vsB2/(fy*(h-dp))<=l*(aCir(k))/m<=vsL/(fy*(h-dp)) and i*aCir(k)>amin]
        minim = 999999999
        if lista!=[]:
            for i in lista:
                nr1, s1, de, nr2, s2 = i
                Lest1 = est[nRam.index(nr1)]
                Lest2 = est[nRam.index(nr2)]
                LestH = Ltrab(b, dp, de)
                ns1=int((xa1*2)/s1)
                ns2=int((xa2-0.01)*2/s2)+1
                nsH=ns1+ns2
                numH=len(yLst)-2
                cub1=cubEstV(h, dp, de, Lest1)
                cub2=cubEstV(h, dp, de, Lest2)
                mini = (cub1[0]*ns1+cub2[0]*ns2+LestH*nsH*numH)*cS/1000000
                X1 = xa1-5 if xa1 > 2*h else 2*h
                X2 = 2*((x1+x2)-X1)
                if mini < minim:
                    minim = round(mini, 2)
                    #[costo, dist rot, n° ramas, espaciamiento, n° estribos, dist de rotula al centro, n° ramas, espaciamiento, n° estribos, de]
                    Lout = [minim, X1, nr1, s1, ns1, X2, nr2, s2, ns2, de, vsB1, vsB2, cub1, cub2, nsH, numH, LestH]
    return Lout

def optimusVig(mpp,mnn,es,eu,ey,b1,fc,fy,dp,dList,dimV,ai,lo,cH,cS,v,allVu,deList,wo):
    mnn=abs(mnn)
    salida=0
    minim = 999999999
    hmax = dimV[0] if dimV[0]>=30 else 30
    bmax = dimV[1] if dimV[1]>=25 else 25
    hmin = dimV[2] if dimV[2]<=30 else 30
    bmin = dimV[3] if dimV[3]<=25 else 25
    hList = [i for i in range(hmin, hmax+5,5)]
    bList = [i for i in range(bmin, bmax+5,5)]
    lista = ([i, j] for i in hList if i >= 100*lo/16 for j in bList if i >= j and j >= 0.4*i)
    for h, b in lista:
        A1 = areaV(mpp, b, b1, h, fc, fy, dp)
        # print(A1)
        A2 = areaV(mnn, b, b1, h, fc, fy, dp)
        # print(A2)
        L1 = listadiam(A1, b, dp, h, dList, v)
        if L1==[]:
            continue
        L2 = listadiam1(A2, b, dp, h, dList, v)
        mi1 = 10*A2
        lis=[]
        for i in range(len(L2)):
            L=L2[i]
            if L[4]<mi1:
                mi1=L[4]
                lis = L
        if lis==[]:
            continue
        db = max(L1[0][1], L1[0][3])
        db2 = max(L2[0][1], L2[0][3])
        gancho = round(lGanchoV(fy, db, fc),1)
        db12 = round(1.2*db,1)
        nbarG = L1[0][0]+L1[0][2]+L1[1][0]+L1[1][2]+lis[0]+lis[2]
        traslp1=round(lempV(db, fc, fy),1)
        traslp2=round(lempV(db2, fc, fy),1)
        remate=round(ldC(fy,fc,db),1)
        ylst = list(yLstV(h, dp, db))
        ylstrev = [(h-i) for i in reversed(ylst)]
        aSLst = [L1[0][4], L1[1][4]]+[ai for i in range(len(ylst)-3)]+[lis[4]]
        alstrev = [lis[4]]+[ai for i in range(len(ylst)-3)]+[L1[1][4], L1[0][4]]
        cuanT = round(sum(aSLst)/(h*b-sum(aSLst)), 4)
        cumin = round(max(0.8/fy*(fc**0.5), 14/fy), 4)
        cuan1 = round((aSLst[0]+aSLst[1])/((b*(h-dp))), 4)
        cuan2 = round(aSLst[-1]/((b*(h-dp))), 4)
        cpn = cPn(aSLst, b, b1, dp, es, eu, ey, fc, fy, h, 0, ylst)
        cpnrev = cPn(alstrev, b, b1, dp, es, eu, ey, fc, fy, h, 0, ylstrev)
        c = cpn[0]
        cond = False
        eT = round(eu*abs(h-dp-c)/c, 4)
        mpr1 = pmC(aSLst, b, b1, cpn[0], es, eu, ey, fc, fy * 1.25, h, ylst)[1]
        mpr2 = pmC(alstrev, b, b1, cpnrev[0], es, eu, ey, fc, fy * 1.25, h, ylstrev)[1]
        db = min([L1[0][1] if L1[0][1]>0 else 99
                 ,L1[0][3] if L1[0][3]>0 else 99
                 ,lis[1] if lis[1]>0 else 99
                 ,lis[3] if lis[3]>0 else 99])
        sup=L1[0]
        xlistV = xLst(sup, 30, 5)[1]
        FU = round(max(mnn / cpn[1], mpp / cpnrev[1]) * 100, 1)
        if 0.025 >= cuan1 >= cumin and 0.025 >= cuan2 >= cumin\
                and cpn[1] >= mnn and cpnrev[1] >= mpp and 85<=FU<=95:
            cond = True
            costo = round((sum(aSLst)*cS+(h*b-sum(aSLst))*cH)/10000, 0)
            if costo < minim and cond != False:
                minim = costo
                FU = round(max(mnn/cpn[1], mpp/cpnrev[1]) * 100, 1)
                listaT = [minim, h, b, aSLst, ylst, cuan1, cuan2, ylstrev, alstrev,c , round(abs(mnn),2),
                          round(abs(mpp),2), L1, lis, cpn[1], cpnrev[1], max(cpn[1],cpnrev[1]), lo, FU,
                          db2, gancho, db12, nbarG, traslp1, traslp2, remate]
                corte = minEstV(mpr1,mpr2,allVu[0],allVu[1],allVu[2],allVu[3],xlistV,deList, db,h,  b, lo, dp, fy, fc, cS, wo, ylst)
                salida = 1
    if salida == 1:
        return [listaT, corte]
    else:
        return 0

def XYplotCurv(alst, b, h, dp, eu, fy, fc, b1, es, ey, ylst, ce, mu, pu, mn, pn, titulo):
    PnMax = round((0.85*fc*(h*b-sum(alst))+sum(alst)*fy)/1000, 2)
    PnMaxPr = round(PnMax+sum(alst)*fy*0.25/1000, 2)
    PnMin = sum(alst)*-fy/1000
    phiPnMin = 0.9*sum(alst)*-fy/1000
    PnMinPr = 1.25*sum(alst)*-fy/1000
    C = [0]+[i/50*h for i in range(2, 51)]
    X1 = [0]
    X2 = [0]
    X3 = [0]
    Y1 = [phiPnMin]
    Y2 = [PnMin]
    Y3 = [PnMinPr]
    for c in C[1::]:
        res = resumen(alst, c, b, dp, h, eu, fy, fc, b1, es, ey, ylst)
        X1.append(res[3])
        Y1.append(res[0])
        X2.append(res[4])
        Y2.append(res[1])
        X3.append(res[5])
        Y3.append(res[2])
    X1.append(0)
    X2.append(0)
    X3.append(0)
    Y1.append(Y1[-1])
    Y2.append(PnMax)
    Y3.append(PnMaxPr)
    fig = plt.figure(figsize=[4,6], dpi=200)
    plt.plot(X1, Y1, label='ØMn - ØPn', color='steelblue')
    plt.plot(X2, Y2, label='Mn - Pn', color='crimson')
    plt.plot(X3, Y3, label='Mpr - Ppr', color='forestgreen')
    plt.plot([mu], [pu], marker='x', markersize=10, color='red', label='Mu - Pu', lw='1')
    res1 = resumen(alst, ce, b, dp, h, eu, fy, fc, b1, es, ey, ylst)
    plt.plot([0, mu], [0, pu], ls='--', color='black')
    # plt.plot([mu, mn], [pu, pn], ls='--', color='gray')
    plt.xlabel('Mn[tonf-m]')
    plt.xlim([0, max(X3)+0.1])
    plt.ylabel('Pn[tonf]')
    plt.title(titulo)
    plt.legend()
    plt.grid()
    # plt.show()
    # fig.savefig(titulo)
    return 0


largosC=[[3,3,3,3],
         [3,3,3,3],
         [3,3,3,3],
         [3,3,3,3]]

largosV=[[7,7,7],
         [7,7,7],
         [7,7,7],
         [7,7,7]]

dimV = [[[65,40,25,25],[65,40,25,25],[65,40,25,25]],
        [[65,40,25,25],[65,40,25,25],[65,40,25,25]],
        [[65,40,25,25],[65,40,25,25],[65,40,25,25]],
        [[65,40,25,25],[65,40,25,25],[65,40,25,25]]]

nbahias=len(largosV[0])

def matElemV(lista, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, ai, deList, v):
    #se itera en la lista
    listaV = []
    for i in range(len(lista)):
        # se filtra la lista por piso
        tempV=[]
        for j in range(len(lista[0])):
            ultimo = 1 if i == len(lista)-1 else 0
            elem = optimusVig(lista[i][j][0],lista[i][j][1],es,eu,ey,b1,fc,fy,dp,dList,
                              lista[i][j][5],ai,lista[i][j][3],cH,cS,v,lista[i][j][4],deList,lista[i][j][2])
            cont=0
            while elem == 0 and cont<10:
                cont+=1
                lista[i][j][0]=lista[i][j][0]*1.1
                lista[i][j][1]=lista[i][j][1]*1.1
                elem = optimusVig(lista[i][j][0], lista[i][j][1], es, eu, ey, b1, fc, fy, dp, dList,
                                  lista[i][j][5], ai, lista[i][j][3], cH, cS, v, lista[i][j][4], deList, lista[i][j][2])
            tempV.append(elem)
        listaV.append(tempV)
    return listaV

cH, cS, b1, dp, es, ey, eu, fc, fy = 75000,7850000,0.85,5,2100000,0.002,0.003,250,4200
dList, deList = [16,18,22,25,28,32,36],[10,12]

def detVig(detvig):
    # agregar lista de barras horizontales
    di = 8
    ai = 1
    contv = 0
    print("cantidad pisos",len(detvig))
    print("cantidad vigas tipo por piso",len(detvig[0]))
    for i in detvig:
        for j in i:

            """ Identificador """

            contv+=1
            print("Viga n° ",contv)
            print("Viga tipo del piso", contv,"\n\n")

            """Dimensiones"""

            print("Dimensiones\n")
            print("Largo : ", j[0][17], "m")
            print("Alto : ",j[0][1], "cm")
            print("Ancho : ",j[0][2], "cm\n")

            """Refuerzo longitudinal"""

            print("Refuerzo longitudinal\n")
            print("Armadura superior principal")
            numB2=" barras" if j[0][12][0][2]>1 else " barra"
            barr2 = "" if j[0][12][0][2]==0 else ", "+str(j[0][12][0][2])+str(numB2)+" Ø "+\
                                                 str(j[0][12][0][3])+"mm en la posición y = "+\
                                                 str(j[0][4][0])+" cm, área = "+str(j[0][3][0])+" cm2"
            print(j[0][12][0][0],"barras Ø",j[0][12][0][1],"mm",barr2)
            print("Traslapo superior=", j[0][23], "cm")

            print("\nArmadura suplementaria")
            numB3 = " barras" if j[0][12][0][2] > 1 else " barra"
            barr3 = "" if j[0][12][1][2] == 0 else ", " + str(j[0][12][1][2])+str(numB3)+\
                                                   " Ø "+str(j[0][12][1][3])+"mm en la posición y = "+\
                                                   str(j[0][4][1])+" cm, área = "+str(j[0][3][1])+" cm2"
            print(j[0][12][1][0], "barras Ø", j[0][12][1][1],"mm",barr3)
            if len(j[0][3])>3:
                print("\nArmadura lateral")
                for i in range(len(j[0][3])-3, len(j[0][3])-1):
                    print("2 barras Ø",di,"mm en la posición y = ",j[0][4][i],"cm, área = ",ai,"cm2")
            print("\nArmadura inferior principal")
            numB4 = " barras" if j[0][13][2] > 1 else " barra"
            barr4 = "" if j[0][13][2] == 0 else ", " + str(j[0][13][2])+str(numB3)+" Ø "+str(j[0][13][3])+\
                                                "mm en la posición y = "+str(j[0][4][-1])+" cm, área = "+\
                                                str(j[0][3][-1])+" cm2"
            print(j[0][13][0], "barras Ø", j[0][13][1],"mm",barr4,"\n")
            print("Traslapo inferior=", j[0][24], "cm\n")

            print("En zonas donde termina solo con columna\n")
            print("Desarrollo total de remate de gancho : ",j[0][20],"cm")
            print("Con desarrollo bajo la curva (12db) de: ",j[0][21],"cm\n")

            print("Lagos de suples\n")
            print("0.25lo = ", round(25*j[0][17],1),"cm")
            print("0.3lo = ",round(30*j[0][17],1),"cm\n")

            """Cuantías"""

            print("Cuantías")
            print("Superior = ",j[0][5])
            print("Inferior = ",j[0][6],"\n")

            """Refuerzo transversal"""

            print("Refuerzo transversal")
            print("\nZonas de rótula plástica, de 0 a",j[1][1],"cm y ",j[0][17]*100-j[1][1],"a",j[0][17]*100,"cm:")
            print("Diámetro : ",j[1][9],"mm")
            print("N° ramas : ",j[1][2])
            cont=0
            print("Estribos =",len(j[1][12][1]))
            for i in j[1][12][1]:
                cont+=1
                print("Largo de estribo n°",cont,"=",i,"cm")
            if j[1][12][2]!=[]:
                print("Traba central: si")
                print("Largo de traba =",j[1][12][2][0],"cm")
            else:
                print("Traba central: no")
            print("Espaciamiento : ",j[1][3],"cm")
            print("N° estribos : ",int(round(j[1][4]/2,0))," en cada extremo")
            print("\nZonas central, de ",j[1][1],"a",j[0][17]*100-j[1][1],"cm:")
            print("Diámetro : ", j[1][9], "mm")
            print("N° ramas : ", j[1][6])
            cont=0
            for i in j[1][13][1]:
                cont+=1
                print("Largo de estribo n°",cont,"=",i,"cm")
            if j[1][13][2]!=[]:
                print("Traba central: si")
                print("Largo de traba =",j[1][13][2][0],"cm")
            else:
                print("Traba central: no")
            print("Espaciamiento : ", j[1][7],"cm")
            print("N° estribos : ", j[1][8],"\n")

            print("Trabas Horizontales")
            print("N° Trabas por estribo = ",j[1][15])
            print("N° de estribos donde va traba = ",j[1][14])
            print("Largo trabas = ",j[1][16],"cm")

            """Resultados"""

            print("Resultados\n")
            print("Flexión")
            print("ØMn+ = ", j[0][15], "tf-m")
            print("ØMn- = ", -j[0][14], "tf-m")
            print("F.U. mayor = ", j[0][18], "%\n")

            print("Corte")
            phiVn1 = round(aCir(j[1][9])*j[1][2]*fy*(j[0][1]-dp)/j[1][3],1)
            print("ØVn1 = ",round(phiVn1/1000,1), "tf")
            fuV1 = round(100*j[1][10]/(phiVn1),1)
            print("F.U.1 = ",fuV1, "%")
            phiVn2 = round(aCir(j[1][9])*j[1][6]*fy*(j[0][1]-dp)/j[1][7], 1)
            print("ØVn2 = ",round(phiVn2/1000,1), "tf")
            fuV2 = round(100*j[1][11]/phiVn2,1)
            print("F.U.2 = ",fuV2,"%\n")
            print("\n")

def detCol(detcol):

    print("\nNota: todas las columnas son simétricas, por lo tanto, su ancho y alto es igual.")
    print("Por otro lado, las trabas y/o estribos interiores perpendiculares al eje x se replican al eje y")
    cont = 0
    npisos = len(detcol)
    ncol = len(detcol[0])
    for i in detcol:
        for j in i:

            """ Identificador """

            cont+=1
            piso=npisos if cont%npisos==0 else cont%npisos
            tipo = 2 if cont>npisos else 1

            print("\n\nColumna n° ",cont)
            print("Piso N°",piso)
            print("Tipo",tipo,"\n\n")

            """Dimensiones"""

            print("Dimensiones\n")
            print("Largo : ", j[0][20], "m")
            print("Alto : ",j[0][1], "cm")
            print("Ancho : ",j[0][2], "cm\n")

            """Refuerzo longitudinal"""

            print("Refuerzo longitudinal\n")
            list = []
            if j[0][21]!=1:
                print("Armadura superior")
                if j[0][3]>0:
                    print("2 barras Ø",j[0][5],"mm y",j[0][3],"barras Ø",j[0][6],"mm en la posición y =",j[0][14][0],
                          "cm, área =",j[0][13][0],"cm2")
                else:
                    print("2 barras Ø",j[0][5],"mm en la posición y =",j[0][14][0],"cm, área =",j[0][13][0],"cm2")
            else:
                print(2+j[0][3],"barras Ø",j[0][5],"mm en la posición y =",j[0][14][0],"cm, área =",j[0][13][0],"cm2")
            if j[0][4]>0:
                for i in range(j[0][4]):
                    print("2 barras Ø",j[0][6],"mm en la posición y =",j[0][14][i+1],"cm, área =",j[0][13][i+1],"cm2")
            if j[0][21]!=1:
                print("Armadura superior")
                if j[0][3]>0:
                    print("2 barras Ø",j[0][5],"mm y",j[0][3],"barras Ø",j[0][6],
                          "mm en la posición y =",j[0][14][-1],"cm, área =",j[0][13][-1],"cm2")
                else:
                    print("2 barras Ø",j[0][5],"mm en la posición y =",j[0][14][-1],"cm, área =",j[0][13][-1],"cm2")
            else:
                print(2+j[0][3],"barras Ø",j[0][5],"mm en la posición y =",j[0][14][-1],"cm, área =",j[0][13][-1],"cm2")

            """Cuantía"""

            print("\nCuantía = ",j[0][9],"\n\n")

            """Uniones y remates"""
            print("Uniones y remates\n")

            if piso!=npisos and piso>1:
                if cont>npisos:
                    print("Columna para zonas centrales\n")
                    print("Para unión superior\n")
                    ldc = ldC(fy, fc, j[0][5])
                    print("Longitud de empalme unión viga-columna = ", ldc, "cm\n")
                    print("Para unión inferior\n")
                    print("Longitud de gancho-remate = ", lG, "cm")
                    ldc = ldC(fy, fc, j[0][5])
                else:
                    print("Columna para zonas laterales\n")
                    print("Para unión superior\n")
                    ldc = ldC(fy, fc, j[0][5])
                    print("Longitud de empalme unión viga-columna = ", ldc, "cm\n")
                    lG = lGanchoC(j[0][5], fc, fy, j[0][1], dp)
                    print("Longitud de gancho-remate = ",lG,"cm")
                    print("Para unión inferior\n")
                    ldc = ldC(fy, fc, j[0][5])
                    print("Longitud de empalme unión viga-columna = ", ldc, "cm\n")

            elif piso==1:
                if cont>npisos:
                    print("Columna para zonas centrales\n")
                    print("Para unión superior\n")
                    ldc = ldC(fy, fc, j[0][5])
                    print("Longitud de empalme unión viga-columna = ", ldc, "cm\n")

                else:
                    print("Columna para zonas laterales\n")
                    print("Para unión superior\n")
                    ldc = ldC(fy, fc, j[0][5])
                    print("Longitud de empalme unión viga-columna = ", ldc, "cm\n")
                    lG = lGanchoC(j[0][5], fc, fy, j[0][1], dp)
                    print("Longitud de gancho-remate = ",lG,"cm")

            else:
                if cont>npisos:
                    print("Columna para zonas centrales\n")
                    print("Para unión superior\n")
                    lG = lGanchoC(j[0][5], fc, fy, j[0][1], dp)
                    print("Longitud de gancho-remate = ",lG,"cm")
                    print("Para unión inferior\n")
                    lG = lGanchoC(j[0][5], fc, fy, j[0][1], dp)
                    print("Longitud de gancho-remate = ", lG, "cm")
                else:
                    print("Columna para zonas laterales\n")
                    print("Para unión superior\n")
                    lG = lGanchoC(j[0][5], fc, fy, j[0][1], dp)
                    print("Longitud de gancho-remate = ",lG,"cm")
                    print("Para unión inferior\n")
                    ldc = ldC(fy, fc, j[0][5])
                    print("Longitud de empalme unión viga-columna = ", ldc, "cm\n")

            """Refuerzo transversal"""

            print("\n\nRefuerzo transversal\n")

            print("\nZonas de rótula plástica\n")

            print("\nUbicación : de 0 -",j[1][0][10],"cm y ",j[0][20]*100-j[1][0][10],"-",j[0][20]*100,"cm:")
            print("N° ramas : ",j[1][0][1])
            print("N° de estribos por extremo: ",j[1][0][5])
            print("Espaciamiento : ",j[1][0][3],"cm")
            print("\nRefuerzo exterior\n")
            print("Diámetro estribo exterior: ",j[1][0][2],"mm")
            print("Largo del estribo exterior",j[1][0][6],"cm")
            print("Ubicación entre ejes de barras horizontales: x =",j[1][0][9][0][0],"cm y x =",j[1][0][9][0][1],"cm")
            print("Ubicación entre ejes de barras verticales: y =",j[1][0][9][0][0],"cm e y =",j[1][0][9][0][1],"cm")
            if j[1][0][1]>2:
                print("\nRefuerzo interior\n")
                if j[1][0][1]%2!=0:
                    print("Diámetro de estribos y trabas interiores",j[1][0][4],"mm")
                    if len(j[1][0][7])-1>0:
                        for i in range(len(j[1][0][7])-1):
                            print("Largo estribo interior n°",i+1,"=",j[1][0][7][i],"cm")
                            print("Ubicación entre ejes de barras horizontales: x =", j[1][0][9][i+1][0], "cm y x =",
                                  j[1][0][9][i+1][1], "cm")
                            print("Ubicación entre ejes de barras verticales: y =", j[1][0][9][0][0], "cm e y =",
                                  j[1][0][9][0][1], "cm")
                    print("Largo de traba interior n°1 =",j[1][0][7][-1],"cm")
                    #Revisar
                    print("Ubicación entre ejes de barras horizontales: x =", j[1][0][9][-1][0], "cm")
                    print("Ubicación entre ejes de barras verticales: y =", j[1][0][9][0][0], "cm e y =",
                          j[1][0][9][0][1], "cm")
                else:
                    print("Diámetro de estribos interiores",j[1][0][4],"mm")
                    if len(j[1][0][7])-1>0:
                        for i in range(len(j[1][0][7])-1):
                            print("Largo estribo interior n°",i+1,"=",j[1][0][7][i],"cm")
                            print("Ubicación entre ejes de barras horizontales: x =", j[1][0][9][i + 1][0], "cm y x =",
                                  j[1][0][9][i + 1][1], "cm")
                            print("Ubicación entre ejes de barras verticales: y =", j[1][0][9][0][0], "cm e y =",
                                  j[1][0][9][0][1], "cm")
                    print("Largo de estribo interior n°", len(j[1][0][7]), "=", j[1][0][7][-1], "cm")
                    print("Ubicación entre ejes de barras horizontales: x =", j[1][0][9][-1][0], "cm y x =",
                          j[1][0][9][-1][1], "cm")
                    print("Ubicación entre ejes de barras verticales: y =", j[1][0][9][0][0], "cm e y =",
                          j[1][0][9][0][1], "cm")

            print("\n\nZona central\n")

            print("\nUbicación : de",j[1][0][10],"-",j[1][0][10]+round(j[1][1][10]/2,1),
                  "cm y de",j[0][20]*100-(j[1][0][10]+round(j[1][1][10]/2,1)),"-",j[0][20]*100-j[1][0][10],"cm")
            print("N° ramas : ", j[1][1][1])
            print("N° de estribos por extremo: ",int(round(j[1][1][5]/2,0)))
            print("Espaciamiento : ", j[1][1][3], "cm")
            print("\nRefuerzo exterior\n")
            print("Diámetro estribo exterior: ", j[1][1][2], "mm")
            print("Largo del estribo exterior", j[1][1][6], "cm")
            print("Ubicación entre ejes de barras horizontales: x =", j[1][1][9][0][0], "cm y x =", j[1][1][9][0][1],
                  "cm")
            print("Ubicación entre ejes de barras verticales: y =", j[1][1][9][0][0], "cm e y =", j[1][1][9][0][1],
                  "cm")
            if j[1][1][1] > 2:
                print("\nRefuerzo interior\n")
                if j[1][1][1] % 2 != 0:
                    print("Diámetro de estribos y trabas interiores", j[1][1][4], "mm")
                    if len(j[1][1][7]) - 1 > 0:
                        for i in range(len(j[1][1][7]) - 1):
                            print("Largo estribo interior n°", i + 1, "=", j[1][1][7][i], "cm")
                            print("Ubicación entre ejes de barras horizontales: x =", j[1][1][9][i + 1][0], "cm y x =",
                                  j[1][1][9][i + 1][1], "cm")
                            print("Ubicación entre ejes de barras verticales: y =", j[1][1][9][0][0], "cm e y =",
                                  j[1][1][9][0][1], "cm")
                    print("Largo de traba interior n°1 =", j[1][1][7][-1], "cm")
                    print("Ubicación entre ejes de barras horizontales: x =", j[1][0][9][-1][0], "cm")
                    print("Ubicación entre ejes de barras verticales: y =", j[1][1][9][0][0], "cm e y =",
                          j[1][1][9][0][1], "cm")
                else:
                    print("Diámetro de estribos interiores", j[1][1][4], "mm")
                    if len(j[1][1][7]) - 1 > 0:
                        for i in range(len(j[1][1][7]) - 1):
                            print("Largo estribo interior n°", i + 1, "=", j[1][1][7][i], "cm")
                            print("Ubicación entre ejes de barras horizontales: x =", j[1][1][9][i + 1][0], "cm y x =",
                                  j[1][1][9][i + 1][1], "cm")
                            print("Ubicación entre ejes de barras verticales: y =", j[1][1][9][0][0], "cm e y =",
                                  j[1][1][9][0][1], "cm")
                    print("Largo de estribo interior n°", len(j[1][1][7]), "=", j[1][1][7][-1], "cm")
                    print("Ubicación entre ejes de barras horizontales: x =", j[1][1][9][-1][0], "cm y x =",
                          j[1][1][9][-1][1], "cm")
                    print("Ubicación entre ejes de barras verticales: y =", j[1][1][9][0][0], "cm e y =",
                          j[1][1][9][0][1], "cm")

            print("\n\nEmpalme central\n")

            print("\nUbicación : de",j[1][0][10]+round(j[1][1][10]/2,1),"-",
                  j[0][20]*100-(j[1][0][10]+round(j[1][1][10]/2,1)),"cm")
            print("N° ramas : ", j[1][2][1])
            print("N° de estribos : ",j[1][2][5])
            print("Espaciamiento : ", j[1][2][3], "cm")
            print("\nRefuerzo exterior\n")
            print("Diámetro estribo exterior: ", j[1][2][2], "mm")
            print("Largo del estribo exterior", j[1][2][6], "cm")
            print("Ubicación entre ejes de barras horizontales: x =", j[1][2][9][0][0], "cm y x =", j[1][2][9][0][1],
                  "cm")
            print("Ubicación entre ejes de barras verticales: y =", j[1][2][9][0][0], "cm e y =", j[1][2][9][0][1],
                  "cm")
            if j[1][2][1] > 2:
                print("\nRefuerzo interior\n")
                if j[1][2][1] % 2 != 0:
                    print("Diámetro de estribos y trabas interiores", j[1][2][4], "mm")
                    if len(j[1][2][7]) - 1 > 0:
                        for i in range(len(j[1][2][7]) - 1):
                            print("\nLargo estribo interior n°", i + 1, "=", j[1][2][7][i], "cm")
                            print("Ubicación entre ejes de barras horizontales: x =", j[1][2][9][i+1][0], "cm y x =",
                                  j[1][2][9][i + 1][1], "cm")
                            print("Ubicación entre ejes de barras verticales: y =", j[1][2][9][0][0], "cm e y =",
                                  j[1][2][9][0][1], "cm")
                    print("\nLargo de traba interior n°1 =", j[1][2][7][-1], "cm")
                    print("Ubicación entre ejes de barras horizontales: x =", j[1][0][9][-1][0], "cm")
                    print("Ubicación entre ejes de barras verticales: y =", j[1][2][9][0][0], "cm e y =",
                          j[1][2][9][0][1], "cm")
                else:
                    print("Diámetro de estribos interiores", j[1][2][4], "mm")
                    if len(j[1][2][7]) - 1 > 0:
                        for i in range(len(j[1][2][7]) - 1):
                            print("\nLargo estribo interior n°", i + 1, "=", j[1][2][7][i], "cm")
                            print("Ubicación entre ejes de barras horizontales: x =", j[1][2][9][i+1][0], "cm y x =",
                                  j[1][2][9][i+1][1], "cm")
                            print("Ubicación entre ejes de barras verticales: y =", j[1][2][9][0][0], "cm e y =",
                                  j[1][2][9][0][1], "cm")
                    print("\nLargo de estribo interior n°", len(j[1][2][7]), "=", j[1][2][7][-1], "cm")
                    print("Ubicación entre ejes de barras horizontales: x =", j[1][0][9][-1][0], "cm")
                    print("Ubicación entre ejes de barras verticales: y =", j[1][2][9][0][0], "cm e y =",
                          j[1][2][9][0][1], "cm")

            """Resultados"""

            print("\n\nResultados\n")
            print("Flexión\n")
            print("Mayor excentricidad", round(j[0][22] * 100,1), "cm\n")
            print("Momentos\n")
            print("Mu_max = ", j[0][17], "tf-m")
            print("Momento nominal ajustado a Mu y Pu máximos")
            print("ØMn1 = ", j[0][15], "tf-m")
            print("Momento nominal ajustado a Mu máximo debido a mayor excentricidad:")
            print("ØMn2 = ", j[0][23], "tf-m\n")

            print("Cargas\n")
            print("Pu_max = ", j[0][18], "tf")
            print("Pu_min = ", j[0][19], "tf")
            print("Carga nominal que verifica Pu_max:")
            print("ØPn1 = ", j[0][16], "tf")
            print("Carga nominal que verifica Pu_min:")
            print("ØPn2 = ", j[0][24], "tf\n")
            print("F.U. 1 = ", j[0][7], "%")
            print("F.U. 2 = ", j[0][8], "%\n")

            print("Corte")

            print("\nCorte en zona de rótula plástica")
            phiVn1 = round((2*aCir(j[1][0][2])+aCir(j[1][0][4])*(j[1][0][1]-2))*fy*(j[0][1]-j[0][27])/j[1][0][3],1)
            print("ØVn1 = ",round(phiVn1/1000,1), "tf")
            fuV1 = round(100*j[1][4]/(phiVn1),1)
            print("F.U.1 = ",fuV1, "%\n")

            print("Corte en zona central")
            phiVn2 = round((2*aCir(j[1][1][2])+aCir(j[1][1][4])*(j[1][1][1]-2))*fy*(j[0][1]-j[0][27])/j[1][1][3],1)
            print("ØVn2 = ",round(phiVn2/1000,1), "tf")
            fuV2 = round(100*j[1][5]/phiVn2,1)
            print("F.U.2 = ",fuV2,"%\n")

            print("Corte en zona de empalme")
            phiVn3 = round((2*aCir(j[1][2][2])+aCir(j[1][2][4])*(j[1][2][1]-2))*fy*(j[0][1]-j[0][27])/j[1][2][3],1)
            print("ØVn3 = ",round(phiVn3/1000,1), "tf")
            fuV3 = round(100*j[1][5]/phiVn3,1)
            print("F.U.3 = ",fuV3,"%\n")
            print("\n")

def max_ind(lista,ind):
    temp=[]
    for i in range(len(lista)):
        maxim=0
        for j in range(len(lista[0])):
            if lista[i][j][ind]>maxim:
                maxim=lista[i][j][ind]
                list1=lista[i][j]
        temp.append(list1)
    return temp

def optimusFrame(tabla, largosC, largosV, dimV, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, deList, hColMax, hColMin):
    dList=[16,18,22,25,28,32,36]
    deList=[10,12]
    combis = 7
    combi_e = 4
    combi_s = 3
    tab = tabla['body']
    filtro=filtroCV(combis, combi_e, combi_s, tab, largosV, largosC)
    listaV=filtro[0]
    listaC=filtro[1]
    exc_col=filtro[2]
    mpp1=[max([max([max(listaV[i][j][0][2], listaV[i][j][1][2]) for j in range(len(listaV[0]))])
                 for k in range(len(listaV[0][0]))]) for i in range(len(listaV))]
    mpp2=[[mpp1[j] for i in range(len(listaV[0]))] for j in range(len(listaV))]
    mpp3=[max(listaV[i][0][0][2], listaV[i][-1][1][2]) for i in range(len(listaV))]
    mnn1=[min([min([min(listaV[i][j][0][3], listaV[i][j][1][3]) for j in range(len(listaV[0]))])
                 for k in range(len(listaV[0][0]))]) for i in range(len(listaV))]
    mnn2=[[mnn1[j] for i in range(len(listaV[0]))] for j in range(len(listaV))]
    mnn3 = [max(listaV[i][0][0][3], listaV[i][-1][1][3]) for i in range(len(listaV))]
    allVuL = [[[listaV[i][j][0][6], listaV[i][j][0][7], listaV[i][j][1][6],
                listaV[i][j][1][7]] for j in range(len(listaV[0]))] for i in range(len(listaV))]
    wo1 = [max([max(listaV[i][j][0][4],listaV[i][j][1][4]) for j in range(len(listaV[0]))]) for i in range(len(listaV))]
    wo2 = [[wo1[j] for i in range(len(listaV[0]))] for j in range(len(listaV))]
    minLo = [min(i) for i in largosV]
    maxLo = [max(i) for i in largosV]
    lV = []
    for i in allVuL:
        a=[[],[],[],[]]
        a[0].append(max([i[j][0][0] for j in range(len(i))]))
        a[0].append(max([i[j][0][1] for j in range(len(i))]))
        a[1].append(max([i[j][1][0] for j in range(len(i))]))
        a[1].append(max([i[j][1][1] for j in range(len(i))]))
        a[1].append(min([i[j][1][2] for j in range(len(i))]))
        a[1].append(max([i[j][1][3] for j in range(len(i))]))
        a[2].append(min([i[j][2][0] for j in range(len(i))]))
        a[2].append(min([i[j][2][1] for j in range(len(i))]))
        a[3].append(min([i[j][3][0] for j in range(len(i))]))
        a[3].append(min([i[j][3][1] for j in range(len(i))]))
        a[3].append(min([i[j][3][2] for j in range(len(i))]))
        a[3].append(max([i[j][3][3] for j in range(len(i))]))
        lV.append(a)

    lV2=[[i for j in range(len(allVuL[0]))] for i in lV]
    listaVig = [[[mpp2[i][j],mnn2[i][j],wo2[i][j],largosV[i][j],lV2[i][j], dimV[i][j]]
       for j in range(len(listaV[0]))] for i in range(len(listaV))]
    listaVig2 = [[listaVig[i][0]] for i in range(len(listaVig))]
    detvig2=matElemV(listaVig2, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, 1, deList, 5)
    detvig = [[detvig2[j] for i in range(len(listaVig[0]))] for j in range(len(listaVig))]
    listaCol =[[[max(abs(listaC[i][j][0][k]), abs(listaC[i][j][1][k])) for k in range(6)]
                for j in range(len(listaC[0]))] for i in range(len(listaC))]
    exc_col=[[exc_col[i][j][0] for j in range(len(exc_col[0]))] for i in range(len(exc_col))]
    exc1=max_ind([[exc_col[i][0],exc_col[i][-1]]  for i in range(len(exc_col))],2)
    exc2 = max_ind([exc_col[i][1:-1] for i in range(len(exc_col))],2)
    tempCol = extMat(listaCol, 4)
    tempVig = [[[abs(listaVig[i][j][0]),abs(listaVig[i][j][1])]
                for j in range(len(listaVig[0]))] for i in range(len(listaVig))]
    colDef=replMat(listaCol,critVC(tempVig, tempCol),4)

    lC1 = []
    for i in range(len(colDef)):
        col1=[max(colDef[i][0][j],colDef[i][-1][j]) for j in range(len(colDef[0][0]))]+exc1[i]
        col2=[max([colDef[i][k][j] for k in range(len(colDef[0])-2)]) for j in range(len(colDef[0][0]))]+exc2[i]
        lC1.append([col1, col2])
    detcol=[]
    hmax1=hColMax
    hmax2=hmax1
    hmin1=hColMin
    hmin2=hmin1
    cont=0
    listC_bh1 = []
    listC_bh2 = []
    for j in range(len(lC1[0])):
        tempC=[]
        for i in range(len(lC1)):
            if j==0:
                cont+=1
                elem=optimusCol(b1, dp, es, eu, ey, fc, fy, lC1[i][j][4], round(lC1[i][j][7]/1000,1),
                                round(lC1[i][j][6]/1000,1), lC1[i][j][0], dList, hmax1, hmin1, cH,
                                cS, lC1[i][j][5], lC1[i][j][2], lC1[i][j][3], deList, 1)
                titulo = str("Columna tipo "+ str(j+1)+ " del piso " + str(i+1))
                XYplotCurv(elem[0][13], elem[0][2], elem[0][1], dp, eu, fy, fc, b1, es, ey, elem[0][14], elem[0][10], lC1[i][j][4], lC1[i][j][0], elem[0][15], elem[0][16], titulo)

                # optimusCol(b1, dp, es, eu, ey, fc, fy, muC, muCmin, puCmin, puCmax, dList, hmax, hmin, cH, cS, H, vu,
                #            vue, deList, iguales)

                # optimo = [minor0, h1, b2, j3, k4, l5, m6, fu7, fu2 8, cuan9, cF[0]10, cF2[0]11, e12,
                # alist13, ylist14, cF[1]15, cF[2]16, muC17, puCmax18, puCmin19, H20, iguales21, round(muCmin / puCmin, 3)22,
                # cF2[1]23, cF2[2]24, costo1 25, costo2 26, dp27]
                tempC.append(elem)
                hmax1=elem[0][1]
                hmin1=hmax1-5
                listC_bh1.append([elem[0][2],elem[0][1]])
            else:
                cont+=1
                elem = optimusCol(b1, dp, es, eu, ey, fc, fy, lC1[i][j][4], round(lC1[i][j][7] / 1000, 1),
                                  round(lC1[i][j][6] / 1000, 1), lC1[i][j][0], dList, hmax2, hmin2, cH, cS,
                                  lC1[i][j][5], lC1[i][j][2], lC1[i][j][3], deList, 1)
                # optimusCol(b1, dp, es, eu, ey, fc, fy, muC, muCmin, puCmin, puCmax, dList, hmax, hmin, cH, cS, H, vu,
                #            vue, deList, iguales)

                titulo = str("Columna tipo "+ str(j+1)+ " del piso " + str(i+1))
                XYplotCurv(elem[0][13], elem[0][2], elem[0][1], dp, eu, fy, fc, b1, es, ey, elem[0][14], elem[0][10],
                           lC1[i][j][4], lC1[i][j][0], elem[0][15], elem[0][16], titulo)
                hmax2=elem[0][1]
                hmin2=hmax2-5
                listC_bh2.append([elem[0][2],elem[0][1]])
                tempC.append(elem)
        detcol.append(tempC)
    listC_bh=[]
    cont=0
    for i in range(len(listaC)):
        for j in range(len(listaC[0])):
            if j==0 or j==len(listaC):
                cont+=1
                listC_bh.append((listC_bh1[i][0],listC_bh1[i][1]))
            else:
                cont += 1
                listC_bh.append((listC_bh1[i][0],listC_bh1[i][1]))
    listV_bh=[]
    cont=0
    for i in detvig:
        for j in i:
            cont+=1
            listV_bh.append((j[0][0][2],j[0][0][1]))
    detCol(detcol)
    detVig(detvig2)
    list_bh = listC_bh+listV_bh
    return [detcol,detvig2, list_bh]

hColMax, hColMin = 90, 30

from time import time
t1=time()
asd=optimusFrame(tabla, largosC, largosV, dimV, cH, cS, b1, dp, es, ey, eu, fc, fy, dList, deList, hColMax, hColMin)
t2=time()-t1
print("tiempo de ejecución",round(t2,5),"segundos")

# cols = [[(0, asd[0][0][j][i][2], asd[0][0][j][i][0][1]) for i in range(asd[0])] for j in range(len(asd[0][0]))]
# print(cols)
# #
