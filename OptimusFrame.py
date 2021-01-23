
def b1(fc):
    if fc < 280:
        b1 = 0.85
    elif 550 >= fc >= 280:
        b1 = 0.85 - 0.05 / 70 * (fc - 280)
    else:
        b1 = 0.65
    return round(b1, 3)


def et(c, dp, eu, h):
    return round(eu * abs(h - dp - c) / c, 4)


def phi(eu, et, ey):
    if et < ey:
        phi = 0.65
    elif ey <= et <= (eu + ey):
        phi = 0.65 + 0.25 / eu * (et - ey)
    elif et > (eu + ey):
        phi = 0.9
    return round(phi, 3)


def aCir(d):
    return round(0.007854 * d ** 2, 3)


def aLstC(dEsq, dLat, nHor, nVer):
    a1 = round(aCir(dEsq) * 2 + nHor * aCir(dLat), 3)
    ai = round(aCir(dLat) * 2, 3)
    aLst = [a1]
    for i in range(nVer):
        aLst.append(ai)
    aLst.append(a1)
    return aLst


def yLstC(dp, h, nVer):
    yLst = [dp]
    for i in range(1, nVer + 1):
        yi = round((h - yLst[i - 1] - dp) / (nVer + 2 - i) + yLst[i - 1], 0)
        yLst.append(int(yi))
    yLst.append(h - dp)
    return yLst


def eiLst(c, eu, yLst):
    if c < 0.01:
        c = 0.01
    eiLst = ((round(eu * (c - i) / c, 5) for i in yLst))
    return eiLst


def fsLst(eiLst, es, ey, fy):
    fsLst = []
    for i in eiLst:
        if i > ey:
            fs = fy
        elif -ey <= i <= ey:
            fs = es * i
        else:
            fs = -fy
        fsLst.append(round(fs, 2))
    return fsLst


def psLst(aLst, fsLst):
    psLst = []
    for i in range(len(fsLst)):
        psLst.append(fsLst[i] * aLst[i])
    return psLst


def ps(aLst, fsLst):
    psSum = round(sum(fsLst[i] * aLst[i] for i in range(len(fsLst))) / 1000, 2)
    return psSum


def pc(b, b1, c, fc):
    return round(0.85 * b1 * fc * b * c / 1000, 2)


def pn(pc, ps):
    return round(pc + ps, 2)


def phiPn(phi, pn):
    return round(phi * pn, 2)


def pnMax(aLst, b, fc, fy, h):
    return round((0.85 * fc * (h * b - sum(aLst)) + sum(aLst) * fy) / 1000, 2)


def phiPnMax(phi, pnMax):
    return round(phi * pnMax, 2)


def pnMin(aLst, fy):
    return round((-sum(aLst) * fy) / 1000, 2)


def phiPnMin(phi, pnMin):
    return round(phi * pnMin, 2)


def mc(c, pc, h):
    return round(pc / 2 * (h - 0.85 * c) / 100, 2)


def ms(fsLst, h, psLst, yLst):
    ms = 0
    for i in range(len(fsLst)):
        ms = ms + psLst[i] * (h / 2 - yLst[i])
    return round(ms / 100000, 2)


def mn(mc, ms):
    mn = mc + ms
    if mn < 0:
        mn = 0
    return round(mn, 2)


def phiMn(mn, phi):
    return round(phi * mn, 2)


def cPnMax(b1, dp, h):
    return max(h / b1, 3 * (h - dp))


def cPn(aLst, b, b1, dp, es, eu, ey, fc, fy, h, pnB, yLst):
    c1 = 0
    c2 = cPnMax(b1, dp, h)
    pnB = round(pnB, 1)
    PnMax = pnMax(aLst, b, fc, fy, h)
    PnMin = pnMin(aLst, fy)
    PhiPn = pnB + 1
    i = 0
    if pnB > PnMin * 0.9:
        if pnB >= PnMax * 0.8 * 0.65:
            pnB = PnMax * 0.8 * 0.65
        while abs(pnB - PhiPn) > 0.1:
            c = round((c1 + c2) / 2, 3)
            eiL = eiLst(c, eu, yLst)
            fsL = fsLst(eiL, es, ey, fy)
            eT = et(c, dp, eu, h)
            Phi = phi(eu, eT, ey)
            Pc = pc(b, b1, c, fc)
            Ps = ps(aLst, fsL)
            PhiPn = pn(Pc, Ps) * Phi
            if PhiPn > pnB:
                c2 = c
            else:
                c1 = c
            i += 1
            if i == 20:
                break
            Mc = mc(c, Pc, h)
            psL = psLst(aLst, fsL)
            Ms = ms(fsL, h, psL, yLst)
            PhiMn = (Mc + Ms) * Phi
    else:
        PhiPn = PnMin * 0.9
        c = 0
        PhiMn = 0
    if pnB >= PnMax * 0.8 * 0.65:
        PhiMn = 0
    return round(c, 2), round(PhiMn, 2), round(PhiPn, 2)


def cFind(aLst, b, b1, dp, es, eu, ey, fc, fy, h, mu, pu, yLst):
    pu = round(abs(pu + 0.01) / (pu + 0.01) * 0.01 + pu, 1)
    mu = round(mu, 1)
    e = round(abs(mu) / pu, 3)
    if abs(mu) < 0.01:
        e = 0
    ex = e + 0.1
    PnMin = pnMin(aLst, fy)
    if e != 0 and pu > PnMin:
        i = 0
        if e > 0:
            c1 = cPnMax(b1, dp, h)
            c2 = 0
        elif e < 0:
            c1 = cPn(aLst, b, b1, dp, es, eu, ey, fc, fy, h, 0, yLst)[0]
            c2 = 0
        while abs(e - ex) > 0.001:
            c = round((c1 + c2) / 2, 2)
            eiL = eiLst(c, eu, yLst)
            fsL = fsLst(eiL, es, ey, fy)
            psL = psLst(aLst, fsL)
            Pc = pc(b, b1, c, fc)
            Ps = ps(aLst, fsL)
            Mc = mc(c, Pc, h)
            Ms = ms(fsL, h, psL, yLst)
            Mn = mn(Mc, Ms)
            Pn = pn(Pc, Ps)
            ex = round((abs(Mn)) / Pn, 3)
            if ex < e:
                c1 = c
            elif ex > e:
                c2 = c
            i += 1
            if i == 20:
                break
        eT = et(c, dp, eu, h)
        Phi = phi(eu, eT, ey)
        phipn = phiPn(Phi, Pn)
        phimn = phiMn(Mn, Phi)
    elif pu < PnMin:
        c = 0
        phipn = PnMin
        phimn = 0
        eT = et(c, dp, eu, h)
        Phi = 0.9
    elif e == 0:
        Pn = pnMax(aLst, b, fc, fy, h) * 0.8 * 0.65
        C = cPn(aLst, b, b1, dp, es, eu, ey, fc, fy, h, Pn, yLst)
        c = C[0]
        phipn = C[1]
        phimn = 0
        eT = et(c, dp, eu, h)
        Phi = 0.65
    return c, phimn, phipn, eT, Phi


def FU(pu, mu, cFound):
    if abs(mu) < 0.1:
        FU = abs(pu / (cFound[2]+0.01))
    else:
        FU = max(abs(pu / (cFound[2] + 0.01)), abs(mu / (cFound[1]+0.01)))
    return round(FU * 100, 1)


fc=250
fy=4200
b1=b1(fc)
eu=0.003
ey=0.002
es=2100000
cH=60000
cS=23550000
dp=5
h = 60
b = 30


# se debería llamar a una función de área de acero para evitar calcularla más de una vez
def cosLC(b, h, dEsq, dLat, nHor, nVer, cH, cS):
    aS = aCir(dEsq) * 4 + aCir(dLat) * (2 * nHor + 2 * nVer)
    costo = (aS * cS + (b * h - aS) * cH) / 10000
    return round(costo, 0)


def cuantiaC(b, h,  dEsq, dLat, nHor, nVer):
    aS = aCir(dEsq) * 4 + aCir(dLat) * (2 * nHor + 2 * nVer)
    cuantia = aS/(b * h - aS)
    return round(cuantia, 5)


def supListC(b, h, dp):
    hMin = int(1 + (b - 2 * dp) / 15)
    hMax = int(round(1 + (b - 2 * dp) / 10, 0))
    nHor = []
    for i in range(hMin - 2, hMax - 1, 1):
        nHor.append(i)
    return nHor


def latListC(b, h, dp):
    vMin = int(1 + (h - 2 * dp) / 15)
    vMax = int(round(1 + (h - 2 * dp) / 10, 0))
    nVer = []
    for i in range(vMin - 2, vMax - 1, 1):
        nVer.append(i)
    return nVer


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


def cuminV(fc, fy):
    return round(max(0.8 / fy * (fc ** 0.5), 14 / fy), 4)


# def cumaxV(b1, fc, fy):
#     return round(min(0.025, 0.31875 * b1 * fc / fy), 4)


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


def reverV(A):
    B = A
    B.reverse()
    return B


def dBarV(A, b, dp, dList):
    sup = supListV(b, dp)
    minlist = [abs(sup[-1]*i*i/400*3.1416 - A) for i in dList]
    maxlist = [abs(sup[0]*i*i/400*3.1416 - A) for i in dList]
    minerr = min(minlist)
    maxerr = min(maxlist)
    ind1 = minlist.index(minerr)
    ind2 = maxlist.index(maxerr)
    if ind1 > 0:
        ind1 = ind1 - 1
    if ind2 < 7:
        ind2 = ind2 + 1
    listad = []
    for i in range(ind1, ind2+1):
        listad.append(dList[i])
    return listad, sup


def diamBarV(A, b, dp, h, lista):
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
            area = n1 * aCir(j) + n2 * aCir(k)
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
        w = round(1 - (1-2*u)**.5, 3)
    return w


def areaV(mu, b, b1, h, fc, fy, dp, dList):
    muu = U(mu, fc, b, h, 1.5 * dp)
    ulim = uLim(b1)
    wp = wP(b1, muu, 1.5 * dp / (h - 1.5 * dp))
    w = W(wp, muu)
    a = round(w * 0.85 * fc * b * (h - dp) / fy, 2)
    return a


def areaLstV(mnn, mpp, b, b1, fc, fy, h, dp, dList, ai):
    aN = areaV(mnn/0.95, b, b1, h, fc, fy, dp, dList)/2
    aP = areaV(mpp/0.95, b, b1, h, fc, fy, dp, dList)
    dBarN = dBarV(aN, b, dp, dList)
    dBarP = dBarV(aP, b, dp, dList)
    dlistN = diamBarV(aN, b, dp, h, dBarN)
    dlistP = diamBarV(aP, b, dp, h, dBarP)
    Y = yLstV(h, dp)
    alist = aLstV(round(dlistN[4], 3), round(dlistN[4], 3), 1, round(dlistP[4], 3), Y)
    return dlistN, dlistP, Y, alist


# asdf1 = areaLstV(58.7, 30.29, 30, 0.85, 250, 4200, 50, 5, [12, 16, 18, 22, 25, 28, 32, 36], 1)
asdf2 = areaV(58.7, 30, 0.85, 50, 250, 4200, 5, [12, 16, 18, 22, 25, 28, 32, 36])

#falta detalle de diametros en cada nivel para la salida, para ello se debe crear una matriz


def optimusVig(mpp, mnn, b1, fc, fy, dp, dList, lList, ai, lo, cH, cS):
    min = 99999999
    cont = 0
    lista = [[i, j] for i in lList if i >= lo/16 for j in lList if i >= j and j >= 0.4 * i]
    for i, j in lista:
        cont = 1 + cont
        aSLst = areaLstV(mnn, mpp, j, b1, fc, fy, i, dp, dList, ai)[3]
        aS = round(sum(aSLst), 2)
        aG = i * j - aS
        cuanT = round(aS/(aG - aS), 4)
        cumin = cuminV(fc, fy)
        cuan1 = round(aSLst[0] / ((j * (i - dp) - aSLst[0])), 4)
        cuan2 = round(aSLst[1] / ((j * (i - dp) - aSLst[1])), 4)
        cond = False
        if cuanT < 0.026 and cuan1 >= cumin and cuan2 >= cumin:
            cond = True
            costo = round(aS * cS + aG * cH, 0)
            if costo < min and cond != False:
                min = costo
                listaT = min, i, j, aS, aG, aSLst, cumin, cuan1, cuan2, cond, cont
    return listaT


#  funcion para enlistar diámetros en función de las cuantías y sección de hormigón


# Función para determinar medidas máximas y mínimas factibles


""" Cálculo de columna óptima"""


def optimusCol(b1, dp, es, eu, ey, fc, fy, muC, puC, dList, lList, cH, cS):
    minor = 9999999
    lista = ([i, a] for i in lList for a in lList if a == i)
    cont = 0
    for i, a in lista:
        b = i
        h = a
        nH = supListC(b, h, dp)
        nV = latListC(b, h, dp)
        listaND = ([j, k] for j in nH for k in nV if 10 <= (b - 2 * dp) / (j + 1) <= 15 and
                   10 <= (h - 2 * dp) / (k + 1) <= 15)
        for j, k in listaND:
            ylist = yLstC(dp, h, k)
            listaDm = ([l, m] for l in dList for m in dList if m <= l)
            for l, m in listaDm:
                cont = 1+cont
                alist = aLstC(l, m, j, k)
                cFound = cFind(alist, b, b1, dp, es, eu, ey, fc, fy, h, muC, puC, ylist)
                fu = FU(puC, muC, cFound)
                cuan = cuantiaC(b, h, l, m, j, k)
                if fu < 90 and 0.01 <= cuan <= 0.06:
                    costo = cosLC(b, h, l, m, j, k, cH, cS)
                    if costo < minor:
                        minor = costo
                        e = round(cFound[1] / (cFound[2] + 0.001), 3)
                        #        [costo, h, b, nHor, nVer, dEsq, dLat, FU, cuantia, C, e, cont]
                        optimo = [minor, h, b,    j,    k,  l, m, fu, cuan, cFound[0], e, cont]
    return optimo


def gen2array(a):
    b = []
    for i in a:
        b.append(i)
    return b


def curvaC(optimo, eu, fy, fc, b1, es, ey):
    optimo=gen2array(optimo)
    c = optimo[9]
    b = optimo[2]
    h = optimo[1]
    nH = optimo[3]
    nV = optimo[4]
    dEsq = optimo[5]
    dLat = optimo[6]
    ylst = yLstC(dp, h, nV)
    alst = aLstC(dEsq, dLat, nH, nV)
    eiL = eiLst(c, eu, ylst)
    eiL=gen2array(eiL)
    eT = et(c, dp, eu, h)
    fsL = fsLst(eiL, es, ey, fy)
    fsLpr = fsLst(eiL, es, ey, fy * 1.25)
    psL = psLst(alst, fsL)
    psLpr = psLst(alst, fsLpr)
    Phi = phi(eu, eT, ey)
    Pc = pc(b, b1, c, fc)
    Ps = ps(alst, fsL)
    PsPr = ps(alst, fsLpr)
    Pn = pn(Pc, Ps)
    Ppr = pn(Pc, PsPr)
    PhiPn = phiPn(Phi, Pn)
    PnMax = pnMax(alst, b, fc, fy, h)
    if PhiPn > PnMax * 0.65 * 0.8:
        PhiPn = round(PnMax * 0.65 * 0.8, 2)
    CMax = cPn(alst, b, b1, dp, es, eu, ey, fc, fy, h, PnMax, ylst)
    if c > CMax[0]:
        c = CMax[0]
    Mc = mc(c, Pc, h)
    Ms = ms(fsL, h, psL, ylst)
    MsPr = ms(fsLpr, h, psLpr, ylst)
    Mn = mn(Mc, Ms)
    Mpr = mn(Mc, MsPr)
    if Mn == 0:
        PhiMn = 0.01
    else:
        PhiMn = phiMn(Mn, Phi)
    return PhiPn, Pn, Ppr, PhiMn, Mn, Mpr


from time import time
#
#
# muC = int(round(float(input('ingrese mu de columna (en Tf-m): ')), 0))
# puC = int(round(float(input('ingrese pu de columna (en Tf): ')), 0))
# Muvpos = round(float(input('ingrese momento positivo de la viga (en Tf): ')), 1)
# Muvneg = round(float(input('ingrese momento negativo de la viga (en Tf): ')), 1)
#
#
# VuC = int(round(float(input('ingrese vu de viga (en Tf): ')), 0))
dp = 5
es = 2100000
fc = 250
fy = 4200
cH = 60000
cS = 23550000
ey = 0.002
eu = 0.003
b1 = 0.85
lList = range(30, 110, 10)
dList = [12, 16, 18, 22, 25, 28, 32, 36]
tinicial = time()
# asdf = optimusVig(58.70, 30.29, 0.85, 250, 4200, 5, dList, lList, 1, 700, 60000, 23550000)
asdf = optimusVig(58.7, 30.29, 0.85, 250, 4200, 5, dList, lList, 1, 700, 6, 2355)
print(asdf)
optC = optimusCol(b1, dp, es, eu, ey, fc, fy, 30, 144, dList, lList, cH, cS)
print(optC)
curvac = curvaC(optC, eu, fy, fc, b1, es, ey)
print(curvac)
# print("\ncosto = ", str(optC[0]),"\nancho = ", str(optC[1]),"\nalto = ", str(optC[2]),
#     "\nnHor = ", str(optC[3]), "\nnVer = ", str(optC[4]), "\ndEsq = ", str(optC[5]), "\ndLat = ", str(optC[6]),
#       "\nfu = ", str(optC[7]), "\ncuan = ", str(optC[8]), "\nc = ", str(optC[9]), "\ne = ", str(optC[10]))
tiempo = round(time() - tinicial, 4)
print("tiempo de ejecución =", str(tiempo), "segundos")
#
