import matplotlib.pyplot as plt

def b1(fc):
    if 550 >= fc >= 280:
        b1 = round(0.85 - 0.05 / 70 * (fc - 280), 2)
    else: b1 = 0.85 if fc < 280 else 0.65
    return b1

def phi(eu, et, ey):
    if ey <= et <= (eu + ey):
        phi = round(0.65 + 0.25 / eu * (et - ey), 2)
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
    return yLst + [h-dp]

def pmC(aLst, b, b1, c, es, eu, ey, fc, fy, h, yLst):
    eiLst = [round(eu*(c-i)/c, 5) for i in yLst]
    fsLst = [fy*abs(i)/i if abs(i)>ey else es*i for i in eiLst]
    psLst = [fsLst[i] * aLst[i] for i in range(len(aLst))]
    Pc, Ps = 0.85*b1*fc*b*c, sum(psLst)
    Mc = Pc/2*(h-0.85*c)
    Ms = sum((psLst[i]*(h/2-yLst[i]) for i in range(len(aLst))))
    return round((Pc + Ps)/1000, 2), round((Mc + Ms)/100000, 2)

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
            eT = round(eu * abs(h - dp - c) / c, 4)
            Phi = phi(eu, eT, ey)
            PhiPn, PhiMn = (PMC[0]) * Phi, (PMC[1]) * Phi
            c2 = c if PhiPn > pnB else c2
            c1 = c if PhiPn < pnB else c1
    else: c, PhiPn, PhiMn = 0, PnMin * 0.9, 0
    return round(c, 2), round(PhiMn, 1), round(PhiPn, 1)

def cFind(aLst, b, b1, dp, es, eu, ey, fc, fy, h, mu, pu, yLst):
    pu = round(abs(pu + 0.01) / (pu + 0.01) * 0.01 + pu, 1)
    mu = round(mu, 1)
    e = round(abs(mu) / pu, 3)
    if abs(mu) < 0.1: e = 0
    PnMin = round((-sum(aLst) * fy) / 1000, 1)
    if e != 0 and pu > PnMin:
        i, c2, ex = 0, 0, e+0.001
        if e > 0:  c1 = max(h / b1, 3 * (h - dp))
        elif e < 0:
            c1 = cPn(aLst, b, b1, dp, es, eu, ey, fc, fy, h, 0, yLst)[0]
        while abs(e - ex) > 0.001 and i<20:
            c, i = round((c1 + c2) / 2, 2), i+1
            PMC = pmC(aLst, b, b1, c, es, eu, ey, fc, fy, h, yLst)
            ex = round((abs(PMC[1])) / (PMC[0]), 3)
            c1 = c if ex < e else c1
            c2 = c if ex > e else c2
        eT = round(eu * abs(h - dp - c) / c, 4)
        Phi = phi(eu, eT, ey)
        phipn, phimn = PMC[1]*Phi, PMC[0]*Phi
    elif pu < PnMin:
        c, phipn, phimn = 0, PnMin, 0
        eT = round(eu * abs(h - dp - c) / c, 4)
        Phi = phi(eu, eT, ey)
    elif e == 0:
        Pn = round((0.85*fc*(h*b-sum(aLst))+sum(aLst)*fy)/1000, 2)
        C = cPn(aLst, b, b1, dp, es, eu, ey, fc, fy, h, Pn, yLst)
        eT = round(eu * abs(h - dp - c) / c, 4)
        Phi = phi(eu, eT, ey)
        c, phipn, phimn = C[0], C[2]*Phi, 0
    return c, round(phimn, 1), round(phipn, 1)

def resumen(aLst, c, b, dp, h, eu, fy, fc, b1, es, ey, yLst):
    PnMax = round((0.85*fc*(h*b-sum(aLst))+sum(aLst)*fy)/1000, 2)
    CMax = cPn(aLst, b, b1, dp, es, eu, ey, fc, fy, h, PnMax, yLst)[0]
    PMC = pmC(aLst, b, b1, c, es, eu, ey, fc, fy, h, yLst)
    eT = round(eu * abs(h - dp - c) / c, 4)
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
    for b, h in lista:
        nH = [i for i in range(int((b-2*dp)/15)-1, int(round((b-2*dp)/10, 0)), 1)]
        nV = [i for i in range(int((h-2*dp)/15)-1, int(round((h-2*dp)/10, 0)), 1)]
        listaND = ([j, k] for j in nH for k in nV if 10 <= (b-2*dp)/(j+1) <= 15 and
                   10 <= (h-2*dp)/(k+1) <= 15)
        for j, k in listaND:
            ylist = yLstC(dp, h, k)
            listaDm = ([l, m] for l in dList for m in dList if m <= l)
            for l, m in listaDm:
                alist = aLstC(l, m, j, k)
                cF = cFind(alist, b, b1, dp, es, eu, ey, fc, fy, h, muC, puC, ylist)
                fu = FU(puC, muC, cF[1], cF[2])
                aS = aCir(l)*4+aCir(m)*(2*j+2*k)
                cuan = round(aS/(b*h-aS), 5)
                if fu < 90 and 0.01 <= cuan <= 0.06:
                    costo = round((aS*cS+(b*h-aS)*cH)/10000, 0)
                    if costo < minor:
                        minor, e = costo, round(cF[1]/(cF[2]+0.001), 3)
    return [minor, h, b,    j,    k,  l, m, fu, cuan, cF[0], e, alist, ylist]

def latListV(h, dp):
    vMin = int(1 + (h - 2 * dp) / 15)
    vMax = int(round(1 + (h - 2 * dp) / 10, 0))
    nVer = []
    for i in range(vMin, vMax + 1, 1):
        nVer.append(i)
    return nVer

def supListV(b, dp):
    hMin = int(1 + (b - 2 * dp) / 15)
    hMax = int(round(1 + (b - 2 * dp) / 10, 0))
    nHor = []
    for i in range(hMin, hMax + 1, 1):
        nHor.append(i)
    return nHor

def espc(xlist, esp):
    i=0
    espacio=0
    while xlist[i+1]-5<=esp and len(xlist)>i:
        i+=1
        espacio = xlist[i]-5
    return espacio

def ramList(xlist, esp):
    nram = int((xlist[-1] - xlist[0] - 0.01) / esp) + 2
    if len(xlist) % 2 == 0:
        nram += 1
    return nram, len(xlist)

def cuminV(fc, fy):
    return round(max(0.8 / fy * (fc ** 0.5), 14 / fy), 4)

def cuantNiv(b, h, aS, dp):
    return round(aS / (b * (h - dp) - aS), 4)

def cuantiaV(b, h, aS):
    return round(aS / (b * h - aS), 4)

def yLstV(h, dp):
    blat = min(int((h - 3 * dp) / 25), int((h - 3 * dp) / 20) + 1)
    Y = [dp, 2 * dp]
    for i in range(blat):
        Y.append(round(Y[-1] + (h - 3 * dp) / (blat + 1), 0))
    if Y[-1] < h - dp:
        Y.append(h - dp)
    return Y

def aLstV(a1, a2, ai, a3, yv):
    A = [a1, a2]
    for i in range(len(yv) - 3):
        A.append(ai)
    A.append(a3)
    return A

def dBarV(A, b, dp, dList):
    sup = supListV(b, dp)
    minlist = [abs(sup[-1] * i * i / 400 * 3.1416 - A) for i in dList]
    maxlist = [abs(sup[0] * i * i / 400 * 3.1416 - A) for i in dList]
    minerr = min(minlist)
    maxerr = min(maxlist)
    ind1 = minlist.index(minerr)
    ind2 = maxlist.index(maxerr)
    if ind1 > 1:
        ind1 = max(ind1 - 2, 0)
    if ind2 < 6:
        ind2 = min(ind2 + 2, 7)
    listad = []
    for i in range(ind1, ind2 + 1):
        listad.append(dList[i])
    return listad, sup

def diamBarV(A, b, fc, fy, dp, h, lista):
    min = 10 * A
    d1 = 0
    d2 = 0
    alist = ([j, k] for j in lista[0] for k in lista[0] if j>=k)
    cumin = cuminV(fc, fy)
    for i in lista[1]:
        if i - 2 * int(i / 2) > 0:
            n1 = int(i / 2)
            n2 = n1 + 1
        else:
            n1 = int(i / 2)
            n2 = int(i / 2)
        for j, k in alist:
            if n1 + n2 <= 2:
                j = k
            area = round(n1 * aCir(j) + n2 * aCir(k), 2)
            if abs(A - area):
                min = abs(A - area)
                d1 = j
                d2 = k
            diamlist = n1, d1, n2, d2, area
    return diamlist

def uLim(b1):
    return round(0.375 * b1 * (1 - 0.1875 * b1), 3)

def U(mu, fc, b, h, dp):
    d = h - dp
    # 0.00000765=0.9*0.85/100000
    muu = round(mu / (7.65e-06 * fc * b * d * d), 3)
    if muu > 0.5:
        muu = 0.5
    return muu

def delP(h, dp):
    return round(dp/(h - dp), 3)

def wP(ulim, u, delta):
    wp = round((u - ulim) / (1 - delta), 3)
    if u<ulim:
        wp=0
    return wp

def W(wp, u):
    if wp > 0:
        w = 0.375 + wp
    else:
        w = round(1 - (1 - 2 * u) ** 0.5, 3)
    return w

def areaV(mu, b, b1, h, fc, fy, dp, dList):
    muu = U(mu, fc, b, h, dp)
    ulim = uLim(b1)
    wp = wP(b1, muu, dp / (h - dp))
    w = W(wp, muu)
    a = round(w * 0.85 * fc * b * (h - dp) / fy, 2)
    return a

def areaLstV(mnn, mpp, b, b1, fc, fy, h, dp, dList, ai):
    aN = areaV(mnn, b, b1, h, fc, fy, dp, dList)/2
    aP = areaV(mpp, b, b1, h, fc, fy, dp, dList)
    dBarN = dBarV(aN, b, dp, dList)
    dBarP = dBarV(aP, b, dp, dList)
    dlistN = diamBarV(aN, b, fc, fy, dp, h, dBarN)
    dlistP = diamBarV(aP, b, fc, fy, dp, h, dBarP)
    Y = yLstV(h, dp)
    alist = aLstV(round(dlistN[4], 3), round(dlistN[4], 3), 1, round(dlistP[4], 3), Y)
    return dlistN, dlistP, Y, alist, aN, aP

def ylstRev(h, ylst):
    ylstrev = []
    for i in reversed(ylst):
        ylstrev.append(h - i)
    return ylstrev

def XYplotCurv(alst, b, h, dp, eu, fy, fc, b1, es, ey, ylst):
    PnMax = round((0.85 * fc * (h * b - sum(alst)) + sum(alst) * fy) / 1000, 2)
    PnMaxPr = round((0.85 * fc * (h * b - sum(alst)) + sum(alst) * fy * 1.25) / 1000, 2)
    PnMin = sum(alst) * -fy / 1000
    phiPnMin = 0.9 * PnMin
    PnMinPr = 1.25 * PnMin
    C = [0]
    X1 = [0]
    Y1 = [phiPnMin]
    X2 = [0]
    Y2 = [PnMin]
    X3 = [0]
    Y3 = [PnMinPr]
    CMax = cPn(alst, b, b1, dp, es, eu, ey, fc, fy, h, PnMax, ylst)
    for i in range(2, 41):
        C.append(i/40 * h)
    for c in C[1::]:
        res = resumen(alst, c, b, h, eu, fy, fc, b1, es, ey, ylst)
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
    plt.xlabel('Mn[tonf-m]')
    plt.ylabel('Pn[tonf]')
    plt.title("Curvas de interacción")
    plt.legend()
    plt.grid()
    plt.show()
    return 0

def optimusVig(mpp, mnn, es, eu, ey, b1, fc, fy, dp, dList, lList, ai, lo, cH, cS):
    min = 99999999
    cH = cH/10000
    cS = cS/10000
    lista = ([i, j] for i in lList if i >= lo / 16 for j in lList if i >= j and j >= 0.4 * i)
    for i, j in lista:
        h = i
        b = j
        ylst = list(yLstV(h, dp))
        ylstrev = ylstRev(h, ylst)
        aLst = areaLstV(mnn, mpp, b, b1, fc, fy, h, dp, dList, ai)
        aSLst = list(aLst[3])
        alstrev = aSLst
        alstrev.reverse()
        aS = round(sum(aSLst), 2)
        aG = h * b - aS
        cuanT = round(aS / (aG - aS), 4)
        cumin = cuminV(fc, fy)
        cuan1 = round(aSLst[0] / ((b * (h - dp) - aSLst[0])), 4)
        cuan2 = round(2 * aSLst[-1] / ((b * (h - dp) - aSLst[-1])), 4)
        cond = False
        asdf = cPn(aSLst, b, b1, dp, es, eu, ey, fc, fy, h, 0, ylst)
        asdfrev = cPn(alstrev, b, b1, dp, es, eu, ey, fc, fy, h, 0, ylstrev)
        c = asdf[0]
        eT = et(c, dp, eu, h)
        if 0.025 >= cuan1 >= cumin and\
                0.0125 >= cuan2 >= cumin and eT >= 0.005\
                and asdf[1] >= mnn and asdfrev[1] >= mpp:
            cond = True
            costo = round(aS * cS + aG * cH, 0)
            if costo < min and cond != False:
                min = costo
                mpr1 = cPn(alstrev, b, b1, dp, es, eu, ey, fc, 1.25 * fy, h, 0, ylstrev)[3]
                mpr2 = cPn(aSLst, b, b1, dp, es, eu, ey, fc, 1.25 * fy, h, 0, ylst)[3]
                FU = round(max(mnn / asdf[1], mpp / asdfrev[1]) * 100, 1)
                listaT = min, h, b, mpr1, mpr2, aSLst, ylst, cuan1, cuan2*2, ylstrev, alstrev, FU, aLst[0], aLst[1]
    return listaT

def ramas(b, dp):
    dlibre = b - 2 * dp
    return int(dlibre / 35) + 2

def vueV(l, mpr1, mpr2):
    vue = (mpr1 + mpr2) / l
    return vue

# 'avs' = (Av / s)_nec = Vs / (fy * d)
def avs(av, fy, h, dp, vu):
    return vu/(fy * (h - dp))

def fest(avs, nRam):
    return round(100 * avs/nRam, 3)

def limEst(h, dp, db, s):
    d = h - dp
    cond1 = min(d / 4, 0.6 * db, 15)
    cond2 = min(d / 2, 30)
    c1 = []
    c2 = []
    for i in s:
        if cond1 >= i:
            c1.append(i)
        if cond2 >= i:
            c2.append(i)
        else:
            break
    return c1, c2

def remrep(a):
    a.sort()
    a = list(dict.fromkeys(a))
    return a

xList = [5, 15, 25, 35, 45]
# xList = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125]

def ramLst(xList):
    if xList[-1]-xList[0] <=30:
        return [xList[0], xList[-1]]
    b = xList[-1] + xList[0]
    mid = b / 2
    dist = mid - xList[0]
    larg = len(xList)
    ind = int(larg / 2)
    rang1 = xList[0:ind-1]
    rang1.append(xList[ind])
    estLst = []
    if larg % 2 == 0:
        c = ind-1
        while mid - xList[c] <= 15:
            c -= 1
        c += 1
        estLst.append(xList[c])
        for i in range(c, -1, -1):
            if estLst[0] - xList[i] >= 30:
                if estLst[0] - xList[i] > 30:
                    estLst.insert(0, xList[i+1])
                else:
                    estLst.insert(0, xList[i])
        for i in range(len(estLst) - 1, -1, -1):
            indx = len(xList)-1-xList.index(estLst[i])
            estLst.append(xList[indx])
        estLst.insert(0,xList[0])
        estLst.append(xList[-1])
        estLst = remrep(estLst)
    else:
        estLst1 = []
        estLst2 = []
        c = ind-1
        while mid - xList[c] <= 15:
            c -= 1
        c += 1
        estLst1.append(xList[c])
        estLst2.append(xList[ind])
        for i in range(c, -1, -1):
            if estLst1[0] - xList[i] >= 30:
                if estLst1[0] - xList[i] > 30:
                    estLst1.insert(0, xList[i + 1])
                else:
                    estLst1.insert(0, xList[i])
        for i in range(c, -1, -1):
            if estLst2[0] - xList[i] >= 30:
                if estLst2[0] - xList[i] > 30:
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

def vS(fy, nRam, aEst, h, dp, s):
    return round(fy * nRam * aEst * (h-dp) / s, 2)

# se desprecia vc
def vReqV(vdl, vue):
    return 0.75 * (vdl + vue)

def corteV():
    pass

from time import time

dp = 5
es = 2100000
fc = 250
fy = 4200
cH = 75000
cS = 7850000
ey = 0.002
eu = 0.003
b1 = 0.85
lList = range(30, 110, 10)
dList = [12, 16, 18, 22, 25, 28, 32, 36]
estList = [10, 12, 16, 18, 22, 25]
tinicial = time()
# asdf = optimusVig(58.7, 30.29, es, eu, ey, b1, fc, fy, dp, dList, lList, 1, 700, cH, cS)
# list(asdf)
# print(asdf)
optC = optimusCol(b1, dp, es, eu, ey, fc, fy, 30, 144, dList, lList, cH, cS)
print(optC)
tiempo = round(time() - tinicial, 4)
print("tiempo de ejecución =", str(tiempo), "segundos")
# XYplotCurv(optC[11], optC[1], optC[2], dp, eu, fy, fc, b1, es, ey, optC[12])
# XYplotCurv(asdf[5], asdf[2], asdf[1], dp, eu, fy, fc, b1, es, ey, asdf[6])
# XYplotCurv(asdf[10], asdf[2], asdf[1], dp, eu, fy, fc, b1, es, ey, asdf[9])
