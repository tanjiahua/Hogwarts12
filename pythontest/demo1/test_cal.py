import sys

sys.path.append('../../')


from pythontest.demo.cal import Calc


class TestCal:
    def test_add(self):
        self.calc = Calc()
        res = self.calc.add(1,2)
        print(res)
        assert 3 == res

    def test_div(self):
        self.calc = Calc()
        res = self.calc.div(6,3)
        print(res)
        assert 2 == res
