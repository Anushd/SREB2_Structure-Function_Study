from modeller import *

env = environ()
aln = alignment(env)

m = model(env, file='1u19', model_segment=('FIRST:'+'A', 'LAST:'+'A'))
aln.append_model(m, atom_files='1u19', align_codes='1u19'+'A')

aln.malign()
aln.malign3d()
aln.compare_structures()
aln.id_table(matrix_file='family.mat')
env.dendrogram(matrix_file='family.mat', cluster_cut=-1.0)
