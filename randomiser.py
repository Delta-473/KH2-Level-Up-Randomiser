from level import Level
import random
import yaml

class Randomiser():

    seed = 0
    passes = 0
    r = random
    skipAp = False
    skipDef = False
    skipExp = False
    skipMag = False
    skipLvl = False
    skipSh = False
    skipSt = False
    skipStr = False
    skipsw = False

    def __init__(self, skipAp, skipDef, skipExp, skipMag, skipLvl, 
    skipSh, skipSt, skipStr, skipsw):
        self.skipAp = skipAp
        self.skipDef = skipDef
        self.skipExp = skipExp
        self.skipLvl = skipLvl
        self.skipMag = skipMag
        self.skipSh = skipSh
        self.skipSt = skipSt
        self.skipStr = skipStr
        self.skipsw = skipsw

    def storelevelvalue(self, l, level):
        level.ap = l['Ap']
        level.defence = l['Defense']
        level.exp = l['Exp']
        level.magic = l['Magic']
        level.shield = l['ShieldAbility']
        level.staff = l['StaffAbility']
        level.strength = l['Strength']
        level.sword = l['SwordAbility']

    def swapcore(self, yamldata):
        pass
    
    def simpleswap(self, yamldata):
        x = self.r.randint(1,99)
        y = self.r.randint(1,99)
        print(x)
        print(y)
        levelx = Level()
        levely = Level()

        for i,j in yamldata.items():
            foundx = False
            foundy = False
            for k,l in j.items():
                if x == l['Level']:
                    print('found x')
                    foundx = True
                    self.storelevelvalue(l, levelx)
                    t1 = l
                    print(t1)
                if y == l['Level']:
                    print('found Y')
                    foundy = True
                    self.storelevelvalue(l, levely)
                    t2 = l
                    print(t2)
                ##t1 is the level found with X and t2 is level found with Y and just swapping them
                if foundx == True and foundy == True:
                    if not self.skipAp:
                        t1['Ap'] = levely.ap
                        t2['Ap'] = levelx.ap
                    if not self.skipDef:
                        t1['Defense'] = levely.defence
                        t2['Defense'] = levelx.defence
                    if not self.skipExp:
                        t1['Exp'] = levely.exp
                        t2['Exp'] = levelx.exp
                    if not self.skipMag:
                        t1['Magic'] = levely.magic
                        t2['Magic'] = levelx.magic
                    if not self.skipLvl:
                        t1['Level'] = y
                        t2['Level'] = x
                    if not self.skipSh:
                        t1['ShieldAbility'] = levely.shield
                        t2['ShieldAbility'] = levelx.shield
                    if not self.skipSt:
                        t1['StaffAbility'] = levely.staff
                        t2['StaffAbility'] = levelx.staff
                    if not self.skipStr:
                        t1['Strength'] = levely.strength
                        t2['Strength'] = levelx.strength
                    if not self.skipsw:
                        t1['SwordAbility'] = levely.sword
                        t2['SwordAbility'] = levelx.sword
                    break




    #same as simple swap except that it will randomly allow certain values to change
    def chaosrandom(self, yamldata):
        x = self.r.randint(1,99)
        y = self.r.randint(1,99)
        print(x)
        print(y)
        levelx = Level()
        levely = Level()

        for i,j in yamldata.items():
            foundx = False
            foundy = False
            for k,l in j.items():
                if x == l['Level']:
                    print('found x')
                    foundx = True
                    self.storelevelvalue(l, levelx)
                    t1 = l
                    print(t1)
                if y == l['Level']:
                    print('found Y')
                    foundy = True
                    self.storelevelvalue(l, levely)
                    t2 = l
                    print(t2)
                ##t1 is the level found with X and t2 is level found with Y and just swapping them
                if foundx == True and foundy == True:
                    if self.r.randint(0,1) and not self.skipAp:
                        t1['Ap'] = levely.ap
                        t2['Ap'] = levelx.ap
                    if self.r.randint(0,1) and not self.skipDef:
                        t1['Defense'] = levely.defence
                        t2['Defense'] = levelx.defence
                    if self.r.randint(0,1) and not self.skipExp:
                        t1['Exp'] = levely.exp
                        t2['Exp'] = levelx.exp
                    if self.r.randint(0,1) and not self.skipMag:
                        t1['Magic'] = levely.magic
                        t2['Magic'] = levelx.magic
                    if self.r.randint(0,1) and not self.skipLvl:
                        t1['Level'] = y
                        t2['Level'] = x
                    if self.r.randint(0,1) and not self.skipSh:
                        t1['ShieldAbility'] = levely.shield
                        t2['ShieldAbility'] = levelx.shield
                    if self.r.randint(0,1) and not self.skipSt:
                        t1['StaffAbility'] = levely.staff
                        t2['StaffAbility'] = levelx.staff
                    if self.r.randint(0,1) and not self.skipStr:
                        t1['Strength'] = levely.strength
                        t2['Strength'] = levelx.strength
                    if self.r.randint(0,1) and not self.skipsw:
                        t1['SwordAbility'] = levely.sword
                        t2['SwordAbility'] = levelx.sword
                    break


    def randomiser(self, yamldata, seed, passes, alg):
        self.r.seed(seed)
        for i in range(passes):
            if alg == 1:
                self.simpleswap(yamldata)
            elif alg == 2:
                self.chaosrandom(yamldata)