# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 21:08:06 2020

@author: romrobotics
"""

import numpy as np

def check_vector_span(set_of_vectors, vector_to_check):
    vector_of_scalars = np.asarray([None]*set_of_vectors.shape[0])
    try:
        vector_of_scalars = np.linalg.solve(set_of_vectors, vector_to_check)
        if not (vector_of_scalars is None):
            print("\nVector is within span.\nScalars in s:", vector_of_scalars)
    except Exception as exception_type:
        if str(exception_type) == "Singular matrix":
            print("\nNo single solution\nVector is NOT within span")
        else:
            print("\nUnexpected Exception Error:", exception_type)
    return vector_of_scalars

vw = np.array([ [1,2],[3,5] ])
t = np.array([4,11])
print("\nEquation 1:\n Matrix vw:", vw, "\nVectr t:", t, sep="\n")
solution = check_vector_span(vw, t)

vw2 = np.array([ [1,2],[2,4] ])
t2 = np.array([6,12])
print("\nEquation 1:\n Matrix vw:", vw2, "\nVectr t:", t2, sep="\n")
solution2 = check_vector_span(vw2, t2)

vw3 = np.array([ [1,2],[1,2] ])
t3 = np.array([6,10])
print("\nEquation 1:\n Matrix vw:", vw3, "\nVectr t:", t3, sep="\n")
solution3 = check_vector_span(vw3, t3)