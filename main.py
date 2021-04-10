import argparse
import os
from pathlib import Path
import random
from randomiser import Randomiser
import sys
import yaml


class Main():

    ifilepath = ''
    iabsfilepath = ''
    ofilepath = ''
    oabsfilepath = ''
    n = 0
    seed = 0
    basepath = Path(__file__).parent
    randomiser = None
    alg = 1
    

    def __init__(self):
        pass

    def parsearguments(self):
        parser = argparse.ArgumentParser(prog='KH2 Level Up Randomiser', description='Swaps level up values around')
        parser.add_argument('--seed', nargs='?', type=int, default=random.randint(0, 10000), help='set seed used by rng default uses a random number between (0, 10000) as seed)')
        parser.add_argument('-n', nargs='?', type=int, default=500, help='amount of random passes')
        parser.add_argument('--input', nargs='?', default='data/lvluptemplate.yml', help='set input file')
        parser.add_argument('--output', nargs='?', default='data/lvlup.yml', help="set output file")
        parser.add_argument('-a', nargs='?', type=int, default=1, help='set algoritm used 1 simple swap, 2 chaos mode')
        #switches to skip certain swap
        parser.add_argument('--ap', nargs='?', type=bool, default=0, help='set to 1 to skip AP point randomising')
        parser.add_argument('--df', nargs='?', type=bool, default=0, help='set to 1 to skip defense randomising')
        parser.add_argument('--xp', nargs='?', type=bool, default=0, help='set to 1 to skip Exp randomising')
        parser.add_argument('--lv', nargs='?', type=bool, default=0, help='set to 1 to skip lv randomising (not used?)')
        parser.add_argument('--mg', nargs='?', type=bool, default=0, help='set to 1 to skip magic randomising (broken?)')
        parser.add_argument('--sh', nargs='?', type=bool, default=0, help='set to 1 to skip shieldskill randomising')
        parser.add_argument('--st', nargs='?', type=bool, default=0, help='set to 1 to skip staffskill randomising')
        parser.add_argument('--str', nargs='?', type=bool, default=0, help='set to 1 to skip strenght randomising')
        parser.add_argument('--sw', nargs='?', type=bool, default=0, help='set to 1 to skip swordskill randomising')

        args = parser.parse_args()
        self.ifilepath = args.input
        self.ofilepath = args.output
        self.n = args.n
        self.seed = args.seed
        self.alg = args.a

        self.randomiser = Randomiser(args.ap, args.df, args.xp, args.lv, args.mg, args.sh, args.st, args.str, args.sw)
        

    def main(self):
        self.parsearguments()
        print('KH2 Level Up Randomiser V0.1 By Delta-47')

        #print(self.ifilepath)
        #print(self.basepath)
        #print(self.ofilepath)

        ##build absolute paths
        self.iabsfilepath = os.path.join(self.basepath, self.ifilepath)
        self.oabsfilepath = os.path.join(self.basepath, self.ofilepath)

        ##read template file
        print('Opening template file at: '+ self.iabsfilepath)
        with open(file=self.iabsfilepath, mode='r') as inputfile:
            data = yaml.full_load(inputfile)

        ##do randomisation

        self.randomiser.randomiser(data, self.seed, self.n, self.alg)

        ##write output file
        print('Writing file at: ' + self.oabsfilepath)
        with open(file=self.oabsfilepath, mode='w') as outputfile:
            yaml.dump(data, outputfile)
        
        inputfile.close()
        outputfile.close()
        
        print('Done')

Main().main()
