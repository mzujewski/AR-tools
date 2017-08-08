import sys
sys.path.append('../')
import artools
artools = reload(artools)

import scipy as sp

from artools import calcDim


class Test1D:

    def test_1(self):
        # row vector
        x = sp.array([[1.0, 2.0, 3.0, 4.0]])
        assert (calcDim(x) == 1) is True


    def test_2(self):
        # column vector
        x = sp.array([[1.0, 2.0, 3.0, 4.0]]).T
        assert (calcDim(x) == 1) is True


    def test_3(self):
        # 1-D numpy array
        x = sp.array([1.0, 2.0, 3.0, 4.0])
        assert (calcDim(x) == 1) is True


class TestRand:

    def test_1a(self):

        Xs = sp.rand(10, 1)
        assert calcDim(Xs) == 1


    def test_1b(self):

        Xs = sp.rand(1, 10)
        assert calcDim(Xs) == 1


    def test_2(self):

        Xs = sp.rand(10, 2)
        assert calcDim(Xs) == 2


    def test_3(self):

        Xs = sp.rand(10, 3)
        assert calcDim(Xs) == 3


    def test_4(self):

        Xs = sp.rand(10, 4)
        assert calcDim(Xs) == 4