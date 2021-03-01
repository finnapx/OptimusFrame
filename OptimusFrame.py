import matplotlib.pyplot as plt

def b1(fc):
    if 550 >= fc >= 280:
        b1 = round(0.85-0.05/70*(fc-280), 2)
    else: b1 = 0.85 if fc < 280 else 0.65
    return b1

def phi(eu, et, ey):
    if ey <= et <= (eu+ey):
        phi = round(0.65+0.25/eu*(et-ey), 2)
    else: phi = 0.65 if et < ey else 0.9
    return phi

def aCir(d): return round(0.007854*d**2, 3)

def aLstC(dEsq, dLat, nHor, nVer):
    a = round(aCir(dEsq)*2+nHor*aCir(dLat), 3)
    return [a]+[round(aCir(dLat)*2,3) for i in range(nVer)]+[a]

def yLstC(dp, h, nVer):
    yLst = [dp]
    for i in range(1, nVer + 1):
        yi = round((h-yLst[i-1]-dp)/(nVer+2-i)+yLst[i-1], 0)
        yLst.append(int(yi))
    return yLst+[h-dp]

def pmC(aLst, b, b1, c, es, eu, ey, fc, fy, h, yLst):
    eiLst = [round(eu*(c-i)/c, 5) for i in yLst]
    fsLst = [fy*abs(i)/i if abs(i)>ey else es*i for i in eiLst]
    psLst = [fsLst[i] * aLst[i] for i in range(len(aLst))]
    Pc, Ps = 0.85*b1*fc*b*c, sum(psLst)
    Mc = Pc/2*(h-0.85*c)
    Ms = sum((psLst[i]*(h/2-yLst[i]) for i in range(len(aLst))))
    return round((Pc+Ps)/1000, 2), round((Mc+Ms)/100000, 2)

def cPn(aLst, b, b1, dp, es, eu, ey, fc, fy, h, pnB, yLst):
    c1, c2 = 0, max(h/b1, 3*(h-dp))
    PnMax = round((0.85*fc*(h*b-sum(aLst))+sum(aLst)*fy)/1000, 2)
    PhiPnMax = PnMax*0.8*0.65
    PnMin, PhiPn, i = round((-sum(aLst)*fy)/1000, 2), pnB+1, 0
    if pnB > PnMin * 0.9:
        pnB = PhiPnMax if pnB >= PhiPnMax else pnB
        while abs(pnB-PhiPn) > 0.1 and i<15:
            c, i = round((c1+c2)/2, 3), i+1
            PMC = pmC(aLst, b, b1, c, es, eu, ey, fc, fy, h, yLst)
            eT = round(eu*abs(h-dp-c)/c, 4)
            Phi = phi(eu, eT, ey)
            PhiPn, PhiMn = (PMC[0]) * Phi, (PMC[1]) * Phi
            c2 = c if PhiPn > pnB else c2
            c1 = c if PhiPn < pnB else c1
    else: c, PhiPn, PhiMn = 0, PnMin * 0.9, 0
    return round(c, 2), round(PhiMn, 1), round(PhiPn, 1)

def cFind(aLst, b, b1, dp, es, eu, ey, fc, fy, h, mu, pu, yLst):
    pu, mu = round(abs(pu+0.01)/(pu+0.01)*0.01+pu, 2), round(mu, 1)
    e = 0 if abs(mu) < 0.1 else round(abs(mu)/pu, 3)
    PnMin = round((-sum(aLst) * fy) / 1000, 1)
    if e != 0 and pu > PnMin:
        i, c2, ex = 0, 0, e+0.001
        c1 = max(h/b1, 3*(h-dp)) if e > 0 else cPn(aLst, b, b1, dp, es, eu, ey, fc, fy, h, 0, yLst)[0]
        while abs(e-round(ex, 3)) > 0.001 and i<20:
            c, i = round((c1+c2)/2, 2), i+1
            PMC = pmC(aLst, b, b1, c, es, eu, ey, fc, fy, h, yLst)
            ex = (abs(PMC[1])) / (PMC[0])
            c1, c2 = c if ex < e else c1, c if ex > e else c2
        eT = round(eu*abs(h-dp-c)/c, 4)
        Phi = phi(eu, eT, ey)
        phipn, phimn = PMC[1]*Phi, PMC[0]*Phi
    elif pu < PnMin: c, phipn, phimn = 0, PnMin, 0
    elif e == 0:
        Pn = round((0.85*fc*(h*b-sum(aLst))+sum(aLst)*fy)/1000, 2)
        C = cPn(aLst, b, b1, dp, es, eu, ey, fc, fy, h, Pn, yLst)
        c, phipn, phimn = C[0], C[2], 0
    return c, round(phimn, 1), round(phipn, 1)

def resumen(aLst, c, b, dp, h, eu, fy, fc, b1, es, ey, yLst):
    PnMax = round((0.85*fc*(h*b-sum(aLst))+sum(aLst)*fy)/1000, 2)
    CMax = cPn(aLst, b, b1, dp, es, eu, ey, fc, fy, h, PnMax, yLst)[0]
    PMC = pmC(aLst, b, b1, c, es, eu, ey, fc, fy, h, yLst)
    eT = round(eu*abs(h-dp-c)/c, 4)
    Phi = phi(eu, eT, ey)
    PMCpr = pmC(aLst, b, b1, c, es, eu, ey, fc, fy*1.25, h, yLst)
    return PMC[0]*Phi, PMC[0], PMCpr[0], PMC[1]*Phi, PMC[1], PMCpr[1]

def FU(pu, mu, pn, mn):
    if abs(mu) < 0.1: FU = abs(pu/(pn+0.01))
    else: FU = max(abs(pu/(pn+0.01)), abs(mu/(mn+0.01)))
    return round(FU * 100, 1)

def optimusCol(b1, dp, es, eu, ey, fc, fy, muC, puC, dList, hmax, cH, cS):
    minor = 9999999
    hmax = hmax if hmax>=30 else 30
    hList = [i for i in range(30, hmax+5,5)]
    lista = ([b, h] for b in hList for h in hList if b == h)
    cont=0
    for b, h in lista:
        nH = [i for i in range(int((b-2*dp)/15)-1, int(round((b-2*dp)/10, 0)), 1)]
        nV = nH
        listaND = ([j, k] for j in nH for k in nV if 10 <= (b-2*dp)/(j+1) <= 15 and
                   10 <= (h-2*dp)/(k+1) <= 15 and j == k)
        for j, k in listaND:
            listaDm = ([l, m] for l in dList for m in dList if m <= l >=16)
            for l, m in listaDm:
                ylist = yLstC(dp, h, k)
                alist = aLstC(l, m, j, k)
                cF = cFind(alist, b, b1, dp, es, eu, ey, fc, fy, h, muC, puC, ylist)
                fu = FU(puC, muC, cF[1], cF[2])
                aS = aCir(l)*4+aCir(m)*(2*j+2*k)
                cuan = round(aS/(b*h-aS), 5)
                cont+=1
                if fu < 90 and 0.01 <= cuan <= 0.06:
                    costo = round((aS*cS+(b*h-aS)*cH)/10000, 0)
                    if costo < minor:
                        minor, e = costo, round(cF[1]/(cF[2]+0.001), 3)
                        optimo = [minor,h,b,j,k,l,m,fu,cuan,cF[0],e,alist,ylist, cont, cF[1], cF[2], muC, puC]
    return optimo

def yLstV(h, dp):
    # se busca el minimo de niveles barras laterales complementarias
    blat = min(int((h-3*dp)/25), int((h-3*dp)/20)+1)
    # se crea lista con dos primeros niveles
    Y = [dp, 2*dp]
    #se agrega cada nivel de barras complementarias
    for i in range(blat):
        Y.append(round(Y[-1]+(h-3*dp)/(blat+1), 0))
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

#diámetros no pueden diferir en más de 1 diámetro de diferencia i-1<=j<=i+1
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

dList=[12, 16, 18, 22, 25, 28, 32, 36]

def listadiam(A, b, dp, h, dList, v):
    amin = 10*A
    A/=2
    lista1 = listadiam1(A, b, dp, h, dList, v)
    lista2, asdf, minimos = [], [], []
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
        if lista3==[]:
            continue
        for j in range(len(lista2)):
            L2 = lista3[i]
            if 2*A>L1[4]+L2[4]:
                continue
            else:
                asdf+=[L1,L2]
                if L1[4]+L2[4]<amin:
                    amin=L1[4]+L2[4]
                    minimos=[L1, L2, round(amin, 2)]
    return minimos

def optimusVig(mpp, mnn, es, eu, ey, b1, fc, fy, dp, dList, hmax, bmax, ai, lo, cH, cS, v):
    minim = 99999999
    hmax, bmax = hmax if hmax>=25 else 25, bmax if bmax>=25 else 25
    hList = [i for i in range(25, hmax+5,5)]
    bList = [i for i in range(25, bmax+5,5)]
    lista = ([i, j] for i in hList if i >= lo/16 for j in bList if i >= j and j >= 0.4*i)
    for h, b in lista:
        A1 = areaV(mpp, b, b1, h, fc, fy, dp)
        A2 = areaV(mnn, b, b1, h, fc, fy, dp)
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
        ylst = list(yLstV(h, dp))
        ylstrev = [(h-i) for i in reversed(ylst)]
        aSLst = [L1[0][4], L1[1][4]]+[ai for i in range(len(ylst)-3)]+[lis[4]]
        alstrev = aSLst
        alstrev.reverse()
        cuanT = round(sum(aSLst)/(h*b-sum(aSLst)), 4)
        cumin = round(max(0.8/fy*(fc**0.5), 14/fy), 4)
        cuan1 = round(aSLst[0]/((b*(h-dp)-aSLst[0])), 4)
        cuan2 = round(2*aSLst[-1]/((b*(h-dp)-aSLst[-1])), 4)
        cpn = cPn(aSLst, b, b1, dp, es, eu, ey, fc, fy, h, 0, ylst)
        cpnrev = cPn(alstrev, b, b1, dp, es, eu, ey, fc, fy, h, 0, ylstrev)
        c, cond = cpn[0], False
        eT = round(eu*abs(h-dp-c)/c, 4)
        if 0.025 >= cuan1 >= cumin and 0.025 >= cuan2 >= cumin\
                and cpn[1] >= mnn and cpnrev[1] >= mpp:
            cond, costo = True, round((sum(aSLst)*cS+(h*b-sum(aSLst))*cH)/10000, 0)
            if costo < minim and cond != False:
                minim = costo
                FU = round(max(mnn/cpn[1], mpp/cpnrev[1]) * 100, 1)
                listaT = minim, h, b, aSLst, ylst, cuan1, cuan2*2, ylstrev, alstrev,c , abs(mnn), abs(mpp), L1, lis
    return listaT

def XYplotCurv(alst, b, h, dp, eu, fy, fc, b1, es, ey, ylst, ce, mu, pu, asd):
    PnMax = round((0.85*fc*(h*b-sum(alst))+sum(alst)*fy)/1000, 2)
    PnMaxPr = round(PnMax+sum(alst)*fy*0.25/1000, 2)
    PnMin, phiPnMin, PnMinPr = sum(alst)*-fy/1000, 0.9*sum(alst)*-fy/1000, 1.25*sum(alst)*-fy/1000
    C = [0]+[i/40*h for i in range(2, 41)]
    X1, X2, X3, Y1, Y2, Y3 = [0], [0], [0], [phiPnMin], [PnMin], [PnMinPr]
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
    plt.plot(X1, Y1, label='ØMn - ØPn', color='steelblue')
    plt.plot(X2, Y2, label='Mn - Pn', color='crimson')
    plt.plot(X3, Y3, label='Mpr - Ppr', color='forestgreen')
    plt.plot([mu], [pu], marker='x', markersize=10, color='red', label='Mu - Pu', lw='1')
    res1 = resumen(alst, ce, b, dp, h, eu, fy, fc, b1, es, ey, ylst)
    plt.plot([0, mu], [0, pu], ls='--', color='black')
    plt.plot([mu, res1[3]], [pu, res1[0]], ls='--', color='gray')
    plt.xlabel('Mn[tonf-m]')
    plt.xlim([0, max(X3)+0.1])
    plt.ylabel('Pn[tonf]')
    plt.title(asd)
    plt.legend()
    plt.grid()
    plt.show()
    return 0

def Lramas(xList, nram=0):
    lar=len(xList)
    lista = [xList[0]]
    if lar%2==0:
        rango=xList[-1]-xList[0]
        for i in range(1, len(xList)-1):
            if xList[i]-lista[-1]==30:
                lista.append(xList[i])
            elif xList[i]-lista[-1]>30:
                lista.append(xList[i-1])
        lista.append(xList[-1])
        minram = len(lista)
        maxram = len(xList)
        rlist=[i for i in range(minram, maxram+1, 2)]
        listas=[]
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
        minram=len(lista)
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
    return listas

def estribos(xList, ramas):
    mid=int(len(ramas)/2)
    L1 = ramas[0:mid]
    L2 = ramas[mid+1:]
    estribos=[[L1[i],L2[i]] for i in range(len(L1))]
    if ramas[mid] in xList:
        estribos+=[ramas[mid]]
    return estribos

def Lest(h, b, dp, de, db): return round((2*(h+b-4*dp)+3*3.1416*max(3*de, de+db)+2*max(75, 6*de))/100, 2)

def Ltrab(h, dp, de, db): return round((4*de+3.1416*max(3*de, de+db)+2*max(75, 6*de))/100, 2)  

def vueV(l, mpr1, mpr2): return (mpr1+mpr2)/l

# 'avs' = (Av / s)_nec = Vs / (fy * d)
def avs(av, fy, h, dp, vu): return vu/(fy*(h-dp))

def fest(avs, nRam): return round(100 * avs/nRam, 3)

def vS(fy, nRam, aEst, h, dp, s):
    return round(fy * nRam * aEst * (h-dp) / s, 2)

# se desprecia vc
def vReqV(vdl, vue):
    return 0.75 * (vdl + vue)

def corteV():
    pass

def vuV(mpr1, mpr2, lo, wo, vu1, vu2, fc, b, h, dp, de):
    ve = (mpr1 + mpr2) / lo + wo * lo / 2
    vc = 10 * (fc ** 0.5) * b * (h - dp) / 6
    vu = max(vu1 / .75 - vc, vu2 / .6)
    lmin = 2 * h
    vs1min = ve / .75

print(xList)
nramL = ramLst(xList)
print(nramL)
from time import time

dp, es, fc, fy, ey, eu, b1, cH, cS = 5, 2100000, 250, 4200, 0.002, 0.003, 0.85, 75000, 7850000
dList, estList = [12, 16, 18, 22, 25, 28, 32, 36], [10, 12, 16]
tinicial = time()
asdf = list(optimusVig(58.7, 30.29, 2100000, 0.003, 0.002, 0.85, 250, 4200, 5, dList, 75, 30, 1, 700, cH, cS, 5))
print(asdf)
optC = optimusCol(b1, dp, es, eu, ey, fc, fy, 30, 144, dList, 50, cH, cS)
print(optC)
tiempo = round(time() - tinicial, 4)
print("tiempo de ejecución =", str(tiempo), "segundos")
XYplotCurv(optC[11], optC[1], optC[2], dp, eu, fy, fc, b1, es, ey, optC[12], optC[9], optC[16], optC[17], 'Interacción de columna')
XYplotCurv(asdf[3], asdf[2], asdf[1], dp, eu, fy, fc, b1, es, ey, asdf[4], asdf[9], asdf[10], 0, 'Interacción de viga con momento negativo')
XYplotCurv(asdf[8], asdf[2], asdf[1], dp, eu, fy, fc, b1, es, ey, asdf[7], asdf[9], asdf[11], 0, 'Interacción de viga con momento positivo')
