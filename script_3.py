from modeller import *
from modeller.automodel import *

env = environ()
a = automodel(env, alnfile='qseq1-mult.ali',
              knowns=('tseq1A','tseq2A','tseq3A'), sequence='qseq1')
a.starting_model = 1
a.ending_model = 5
a.make()