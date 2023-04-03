#!/usr/bin/python3
################################################################################
# TUPLES (example-code-2-5.py)
################################################################################
# Two-element tuple
t2 = ('TCAG', 'UCAG')
print('Tuple t2 = {}, {}'.format(t2,type(t2)))
# One-element tuple
t1 = ('GCGA',)
print('Tuple t1 = {}'.format(t1))
# Not a tuple
tnot = ('GCGAA')
print('Tuple or not? tnot = {}, {}'.format(tnot,type(tnot)))
# Tuple function creates tuple containing elements of sequence
tseq = tuple('TCAG')
print("Tuple function on TCAG: {}".format(tseq))
trange = tuple(range(1,10))
print("Tuple range: {}".format(trange))