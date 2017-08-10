#!/usr/bin/env python
# coding=utf-8

"""
Manipulation des triangles. Détection des triangle isocèle, rectange, équilatéral et quelconque.

- isocèle : 2 côté égaux
- équilatéral : 3 côtés égaux
- rectangle : pythagore a^2 = b^2 + C^2

"""


# ----------------------------------------------------------------------------------------------------------------------
class triangle:
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, a, b, c):
        """
        Creation d'un triangle basé sur 3 longueurs
        :param a: int
        :param b: int
        :param c: int
        """
        self._a = a
        self._b = b
        self._c = c

    # ------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        """
        Conversion d'un triangle en chaine de caractere
        :rtype: str
        :return: le texte décrivant le triangle
        """
        return "Triangle: %s, %s, %s" % (self._a, self._b, self._c)

    # ------------------------------------------------------------------------------------------------------------------
    def isIsocele(self):
        return self._a == self._b or self._a == self._c
