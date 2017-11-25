from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='1u19', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1u19A', atom_files='1u19.pdb')
aln.append(file='qseq1.ali', align_codes='qseq1')
aln.align2d()
aln.write(file='qseq1-1u19A.ali', alignment_format='PIR')
aln.write(file='qseq1-1u19A.pap', alignment_format='PAP', alignment_features='INDICES HELIX BETA')
