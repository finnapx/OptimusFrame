from time import time

def b1(fc):
    if fc < 280:
        b1 = 0.85
    elif 560 >= fc >= 280:
        b1 = 0.85 - 0.2 / 280 * (fc - 280)
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

def aLst(dI, dL, dS, nI, nL, nS):
    aS = aCir(dS) * nS
    aL = aCir(dL) * nL
    aI = aCir(dI) * nI
    aLst = [aS]
    for i in range(nL):
        aLst.append(aL)
    aLst.append(aI)
    return aLst

def yLst(dp, h, nL):
    yLst = [dp]
    for i in range(1, nL + 1):
        yi = round((h - yLst[i - 1] - dp) / (nL + 2 - i) + yLst[i - 1], 0)
        yLst.append(int(yi))
    yLst.append(h - dp)
    return yLst

def eiLst(c, eu, yLst):
    eiLst = []
    for i in yLst:
        eiLst.append(round(eu * (c - i) / c, 5))
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
    psSum = 0
    for i in range(len(fsLst)):
        psSum += fsLst[i] * aLst[i]
    return round(psSum / 1000, 2)

def pc(b, b1, c, fc):
    return round(0.85 * b1 * fc * b * c / 1000, 2)

def pn(pc, ps):
    return round(pc + ps, 2)

def phiPn(phi, pn):
    return round(phi * pn, 2)

def pnMax(aLst, b, fc, fy, h):
    return round((0.85 * fc * h * b + sum(aLst) * fy) / 1000, 2)

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

def cuanMin(fc, fy):
    return round(max((fc * 0.1) ** 0.5 / (4 * fy), 14 / fy), 5)

def cuanMax(b1, eu, ey, fc, fy):
    return round(0.75 * 0.85 * b1 * eu / (eu + ey) * fc / fy, 5)

def cPn(aLst, b, b1, es, eu, ey, fc, fy, h, pnB, yLst):
    c1 = 0.1
    c2 = 4 * h
    pnB = round(pnB, 1)
    Pn = abs(pnB) + 0.1
    PnMax = pnMax(aLst, b, fc, fy, h)
    PnMin = pnMin(aLst, fy)
    if pnB >= PnMax:
        pnB = PnMax
    elif pnB - 1 <= PnMin:
        pnB = PnMin
        c = 0
        Pn = pnB
    i = 0
    lim = 20
    while abs(pnB - Pn) > 0.001:
        c = (c1 + c2) / 2
        eiL = eiLst(c, eu, yLst)
        fsL = fsLst(eiL, es, ey, fy)
        Pc = pc(b, b1, c, fc)
        Ps = ps(aLst, fsL)
        Pn = round(pn(Pc, Ps), 1)
        if Pn > pnB:
            c2 = c
        else:
            c1 = c
        c = round(c, 2)
        i += 1
        if i == lim:
            break
    return c

def cPnMax(b1, dp, h):
    return max(h / b1, 3 * (h - dp))

def resumen(aLst, b, b1, c, dp, es, eu, ey, fc, fy, h, yLst):
    if c < 0.1:
        c = 0.1
    eiL = eiLst(c, eu, yLst)
    eT = et(c, dp, eu, h)
    fsL = fsLst(eiL, es, ey, fy)
    fsLpr = fsLst(eiL, es, ey, fy * 1.25)
    psL = psLst(aLst, fsL)
    psLpr = psLst(aLst, fsLpr)
    Phi = phi(eu, eT, ey)
    Pc = pc(b, b1, c, fc)
    Ps = ps(aLst, fsL)
    PsPr = ps(aLst, fsLpr)
    Pn = pn(Pc, Ps)
    Ppr = pn(Pc, PsPr)
    PhiPn = phiPn(Phi, Pn)
    PnMax = pnMax(aLst, b, fc, fy, h)
    if PhiPn > PnMax * 0.65 * 0.8:
        PhiPn = round(PnMax * 0.65 * 0.8, 2)
    CMax = cPn(aLst, b, b1, es, eu, ey, fc, fy, h, PnMax, yLst)
    if c > CMax:
        c = CMax
    Mc = mc(c, Pc, h)
    Ms = ms(fsL, h, psL, yLst)
    MsPr = ms(fsLpr, h, psLpr, yLst)
    Mn = mn(Mc, Ms)
    Mpr = mn(Mc, MsPr)
    if Mn == 0:
        PhiMn = 0.01
    else:
        PhiMn = phiMn(Mn, Phi)
    e = round((Mn/Pn), 3)
    return [c, e, eT, Phi, Ppr, Pn, PhiPn, Mpr, Mn, PhiMn]

def cP(aLst, b, b1, dp, es, eu, ey, fc, fy, h, yLst):
    pnB = pnMax(aLst, b, fc, fy, h)
    c = cPn(aLst, b, b1, es, eu, ey, fc, fy, h, pnB, yLst)
    return resumen(aLst, b, b1, c, dp, es, eu, ey, fc, fy, h, yLst)

def cB(aLst, b, b1, dp, es, eu, ey, fc, fy, h, yLst):
    c = eu * (h - dp) / (eu + ey)
    return resumen(aLst, b, b1, c, dp, es, eu, ey, fc, fy, h, yLst)

def e5(aLst, b, b1, dp, es, eu, ey, fc, fy, h, yLst):
    c = eu * (h - dp) / (eu + 0.005)
    return resumen(aLst, b, b1, c, dp, es, eu, ey, fc, fy, h, yLst)

def fS(aLst, b, b1, dp, es, eu, ey, fc, fy, h, yLst):
    c = cPn(aLst, b, b1, es, eu, ey, fc, fy, h, 0, yLst)
    return resumen(aLst, b, b1, c, dp, es, eu, ey, fc, fy, h, yLst)

def tR(aLst, b, b1, dp, es, eu, ey, fc, fy, h, yLst):
    return resumen(aLst, b, b1, 0, dp, es, eu, ey, fc, fy, h, yLst)

def cFind(aLst, b, b1, dp, es, eu, ey, fc, fy, h, mu, pu, yLst):
    if pu == 0:
        pu = 0.01
    if mu == 0:
        mu = 0.01
    e = round(abs(mu)/pu, 3)
    cfs = cPn(aLst, b, b1, es, eu, ey, fc, fy, h, 0, yLst)
    ex = 0
    if e >= 0:
        PnMax = pnMax(aLst, b, fc, fy, h)
        ccp = cPn(aLst, b, b1, es, eu, ey, fc, fy, h, PnMax, yLst)
        if e > 0:
            c1 = ccp
            c2 = cfs
            i = 0
            MAX = 20
            while abs(e - ex) > 0.001:
                c = round((c1 + c2) / 2, 2)
                res = resumen(aLst, b, b1, c, dp, es, eu, ey, fc, fy, h, yLst)
                ex = res[1]
                if ex < e:
                    c1 = c
                elif ex > e:
                    c2 = c
                i += 1
                if i == MAX:
                    break
        elif e == 0:
            res = resumen(aLst, b, b1, ccp, dp, es, eu, ey, fc, fy, h, yLst)
    elif e < 0:
        resFs = resumen(aLst, b, b1, cfs, dp, es, eu, ey, fc, fy, h, yLst)
        resTr = resumen(aLst, b, b1, 0, dp, es, eu, ey, fc, fy, h, yLst)
        p1 = resTr[5]
        m1 = resTr[7]
        p2 = resFs[5]
        m2 = resFs[7]
        m = round((p2 - p1) / (m2 - m1), 2)
        phimn = round((p1 - m * m1) / (1 / e - m), 2)
        phipn = round(phimn / e, 2)
        c = cPn(aLst, b, b1, es, eu, ey, fc, fy, h, phipn/0.9, yLst)
        res = resumen(aLst, b, b1, c, dp, es, eu, ey, fc, fy, h, yLst)
    return res

def FU(pu, mu, cFound):
    if abs(mu) < 1:
        FU = abs(pu / cFound[6])
    else:
        FU = max(abs(pu / cFound[6]), abs(mu / cFound[9]))
    return round(FU * 100, 1)

def avs(dE, nRam, s):
    avs = aCir(dE) * nRam / s
    return avs

def vn(fc, nu, b, h, dp, avs):
    d = h - dp
    ag = b * h
    if nu == 0:
        vc = (fc / 10) ** 0.5 * 10 / 6 * b * d
    elif nu > 0:
        fact = (1 + (nu / (14 * ag * 10)))
        factLim = (1 + 0.29 * nu / (ag * 10)) ** 0.5
        if fact > factLim:
            fact = factLim
        vc = (fc / 10) ** 0.5 * 10 / 6 * b * d * fact
    else:
        fact = 1 + 0.29 * nu / (ag * 10)
        vc = (fc / 10) ** 0.5 * 10 / 6 * b * d * fact
        if vc < 0:
            vc = 0
    vs = avs * fy * d
    vsLim = 4 * (fc / 10) ** 0.5 * 10 / 6 * b * d
    if vs > vsLim:
        vs = vsLim
    return round((vc + vs) / 1000, 3)

def phiVn(vn, phiV):
    return round(vn * phiV, 2)

def aS(nS, dS, nL, dL, nI, dI):
    aS = (nS * aCir(dS) + 2 * nL * aCir(dL) + nI * aCir(dI))
    return aS

def aH(b, h, nS, dS, nL, dL, nI, dI):
    ah = b * h - aS(nS, dS, nL, dL, nI, dI)
    return ah

def cosL(b, h, nS, dS, nL, dL, nI, dI, cH, cS):
    costo = (aS(nS, dS, nL, dL, nI, dI) * cS +
             aH(b, h, nS, dS, nL, dL, nI, dI) * cH)/10000
    return costo

def cuantia(b, h, nS, dS, nL, dL, nI, dI):
    cuantia = aS(nS, dS, nL, dL, nI, dI) / aH(b, h, nS, dS, nL, dL, nI, dI)
    return round(cuantia, 5)

def rangBar(b, h, dp):
    hMin = int(1 + (b - 2 * dp) / 15)
    hMax = int(round(1 + (b - 2 * dp) / 10, 0))
    vMin = int(1 + (h - 2 * dp) / 15)
    vMax = int(round(1 + (h - 2 * dp) / 10, 0))
    # print(hMin, hMax, vMin, vMax)
    return [hMin, hMax, vMin, vMax]

def diamList(fc, fy, b1, eu, ey, b, h, dp, dList):
    rang = rangBar(b, h, dp)
    cumin = cuanMin(fc, fy)
    cumax = cuanMax(b1, eu, ey, fc, fy)
    nBMin = rang[0] * 2 + (rang[2] - 2) * 2
    nBMax = rang[1] * 2 + (rang[3] - 2) * 2
    # entrada b y h en cm, salida diámetro en mm
    dMax = int(
        ((cumax * b * h * 127.324) / (nBMin * (1 + cumax))) ** 0.5)
    # coeficiente 127.324 = 4 * 100 / pi()
    dMin = int(round(
        ((cumin * b * h * 127.324) / (nBMax * (1 + cumin))) ** 0.5, 0))
    i = 0
    list = []
    while dList[i] < dMax:
        if dList[i] >= dMin:
            list.append(dList[i])
            if i < len(dList):
                i += 1
            else:
                break
        else:
            i += 1
    return list

def supList(b, h, dp):
    rang = rangBar(b, h, dp)
    nS = range(rang[0], rang[1] + 1, 1)
    return nS

def latList(b, h, dp):
    rang = rangBar(b, h, dp)
    nL = range(rang[2] - 2, rang[3] - 1, 1)
    return nL

tinicial = time()
# mu = input('ingrese momento último')
# pu = input('ingrese carga última')
mu = 30
pu = 144
dp = 5
es = 2100000
fc = 250
fy = 4200
cH = 60000
cS = 23550000
ey = 0.002
eu = 0.003
b1 = b1(fc)
lList = [30, 40, 50, 60, 70, 80, 90, 100, 110]
dList = [16, 18, 22, 25, 28, 32, 36]
dList.append(dList[-1] * 9)
b = 40
h = 120
nS = supList(b, h, dp)
# for i in nS:
#     print(i)
# nL = latList(b, h, dp)
# for i in nL:
#     print(i)

""" Cálculo de columna óptima"""

def sizeLims(b1, dp, es, eu, ey, fc, fy, mu, pu, dList, lList):
    b = h
    m2 = len(lList)
    n2 = len(dList) - 1

    # cFound = cFind(aLst, b, b1, dp, es, eu, ey, fc, fy, h, mu, pu, yLst)
    # fu = FU(pu, mu, cFound)
    # print(fu)

    return 0

sizeLims(b1, dp, es, eu, ey, fc, fy, mu, pu, dList, lList)

# sumRang = 0
# diam = 0
# for i in lList:
#     for j in lList:
#         if i <= j:
#             rang = rangBar(i, j, dp)
#             sumRang += (rang[1] - rang[0] + 1) * (rang[3] - rang[2] + 1)
#             diam += len(diamList(fc, fy, b1, eu, ey, i, j, dp, dList))
# costo = cosL(b, h, nS, dS, nL, dL, nI, dI, cH, cS)
# dE = 10
# nr = 2
# s = 15
# nu = 0
# avs = avs(dE, nr, s)
# vn = vn(fc, nu, b, h, dp, avs)
# phiV = 0.6
# phiVn = phiVn(vn, phiV)
# aLst = aLst(dI, dL, dS, nI, nL, nS)
# yLst = yLst(dp, h, nL)
# cFound = cFind(aLst, b, b1, dp, es, eu, ey, fc, fy, h, mu, pu, yLst)
# print(cFound)
# FU = FU(pu, mu, cFound)
# print(FU)
# print(phiVn)
tiempo = round(time() - tinicial, 5)
print("tiempo de ejecución = " + str(tiempo) + " segundos")
# cumin = cuanMin(fc, fy)
# cumax = cuanMax(b1, eu, ey, fc, fy)
# print(costo)
#
# dList = [16, 18, 22, 25, 28, 32, 36]
# areas = []
# for i in dList:
#     areas.append(aCir(i))
# print(areas)
