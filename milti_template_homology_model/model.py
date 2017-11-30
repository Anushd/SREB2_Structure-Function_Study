from modeller import *
from modeller.automodel import *

env = environ()
a = automodel(env, alnfile='align-mult.ali',
              knowns=('5u09A','5uenA'), sequence='qseq1',assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))
a.starting_model = 1
a.ending_model = 5
a.make()