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

def optimusCol(b1, dp, es, eu, ey, fc, fy, muC, puC, dList, lList, cH, cS):
    minor = 9999999
    lista = ([b, h] for b in lList for h in lList if b == h)
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

def espc(xlist, esp):
    i, espacio = 0, 0
    while xlist[i+1]-5<=esp and len(xlist)>i:
        i+=1
        espacio = xlist[i]-5
    return espacio

def vueV(l, mpr1, mpr2): return (mpr1+mpr2)/l

# 'avs' = (Av / s)_nec = Vs / (fy * d)
def avs(av, fy, h, dp, vu): return vu/(fy*(h-dp))

def fest(avs, nRam): return round(100 * avs/nRam, 3)

def limEst(h, dp, db, s):
    cond1, c1, cond2, c2 = min((h-dp)/4, 0.6*db, 15), [], min((h-dp)/2, 30), []
    for i in s:
        c1 += [i] if cond1 >= i else []
        c2 += [i] if cond2 >= i else []
    return c1, c2

def remrep(a):
    a.sort()
    return list(dict.fromkeys(a))

xList = [5, 15, 25, 35, 45]

def ramLst(xList):
    if xList[-1]-xList[0] <= 30:
        return [xList[0], xList[-1]]
    b = xList[-1]+xList[0]
    dist, ind = b/2-xList[0], int(len(xList)/2)
    rang1, estLst = xList[0:ind-1], []
    rang1.append(xList[ind])
    if len(xList)%2 == 0:
        c = ind-1
        while b/2-xList[c] <= 15:
            c -= 1
        c += 1
        estLst.append(xList[c])
        for i in range(c, -1, -1):
            if estLst[0]-xList[i] >= 30:
                if estLst[0]-xList[i] > 30:
                    estLst.insert(0, xList[i+1])
                else:
                    estLst.insert(0, xList[i])
        for i in range(len(estLst)-1, -1, -1):
            indx = len(xList)-1-xList.index(estLst[i])
            estLst.append(xList[indx])
        estLst.insert(0, xList[0])
        estLst.append(xList[-1])
        estLst = remrep(estLst)
    else:
        estLst1, estLst2, c = [], [], ind-1
        while b/2-xList[c] <= 15:
            c -= 1
        c += 1
        estLst1 += [xList[c]]
        estLst2 += [xList[ind]]
        for i in range(c, -1, -1):
            if estLst1[0]-xList[i] >= 30:
                if estLst1[0]-xList[i] > 30:
                    estLst1.insert(0, xList[i + 1])
                else:
                    estLst1.insert(0, xList[i])
        for i in range(c, -1, -1):
            if estLst2[0]-xList[i] >= 30:
                if estLst2[0]-xList[i] > 30:
                    estLst2.insert(0, xList[i + 1])
                else:
                    estLst2.insert(0, xList[i])
        for i in range(len(estLst) - 1, -1, -1):
            indx = len(xList)-1-xList.index(estLst[i])
            estLst1.append(xList[indx])
            estLst2.append(xList[indx])
        if len(estLst1) < len(estLst2):
            for i in range(len(estLst1)-1, -1, -1):
                indx = len(xList) - 1 - xList.index(estLst1[i])
                estLst1.append(xList[indx])
            estLst1.insert(0, xList[0])
            estLst1.append(xList[-1])
            estLst1 = remrep(estLst1)
            estLst = estLst1
            estLst1 = remrep(estLst1)
        else:
            for i in range(len(estLst2)-2, -1, -1):
                indx = len(xList) - 1 - xList.index(estLst2[i])
                estLst2.append(xList[indx])
            estLst2.insert(0, xList[0])
            estLst2.append(xList[-1])
            estLst2 = remrep(estLst2)
            estLst = estLst2
    return estLst

# print(ramLst(xList))

def vS(fy, nRam, aEst, h, dp, s):
    return round(fy * nRam * aEst * (h-dp) / s, 2)

# se desprecia vc
def vReqV(vdl, vue):
    return 0.75 * (vdl + vue)

def corteV():
    pass

from time import time

dp, es, fc, fy, ey, eu, b1, cH, cS = 5, 2100000, 250, 4200, 0.002, 0.003, 0.85, 75000, 7850000
lList, dList, estList = range(30, 110, 10), [12, 16, 18, 22, 25, 28, 32, 36], [10, 12, 16, 18, 22, 25]
tinicial = time()
asdf = list(optimusVig(58.7, 30.29, 2100000, 0.003, 0.002, 0.85, 250, 4200, 5, dList, 70, 40, 1, 700, cH, cS, 5))
print(asdf)
optC = optimusCol(b1, dp, es, eu, ey, fc, fy, 30, 144, dList, lList, cH, cS)
print(optC)
tiempo = round(time() - tinicial, 4)
print("tiempo de ejecución =", str(tiempo), "segundos")
XYplotCurv(optC[11], optC[1], optC[2], dp, eu, fy, fc, b1, es, ey, optC[12], optC[9], optC[16], optC[17], 'Interacción de columna')
XYplotCurv(asdf[3], asdf[2], asdf[1], dp, eu, fy, fc, b1, es, ey, asdf[4], asdf[9], asdf[10], 0, 'Interacción de viga con momento negativo')
XYplotCurv(asdf[8], asdf[2], asdf[1], dp, eu, fy, fc, b1, es, ey, asdf[7], asdf[9], asdf[11], 0, 'Interacción de viga con momento positivo')
print(cFind([20.36, 18.47, 1, 17.22], 30, 0.85, 5, 2100000, 0.003, 0.002, 250, 4200, 60, 58.8, 0.1, [5, 13, 34, 55]))
print(cPn([17.22, 1, 18.47, 20.36], 30, 0.85, 5, 2100000, 0.003, 0.002, 250, 4200, 60, 0, [5, 26, 47, 55]))
