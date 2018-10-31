"""
2.
"""
import unittest
from Q1 import Default


class QoneTest(unittest.TestCase):

    def setUp(self):
        self.default = Default()
        # 新建repetition()测试用例
        self.case1_li = [5, 12, 34, 57, 89, 101, 132, 158]
        self.case1_num = 15
        self.case2_li = [65714297, 66696598, 72697666, 73776167, 74715648, 74789469, 81705082, 88869408, 88885270, 84902742]
        self.case2_num = 88885270
        self.case3_li = [65843401, 65904344, 66755822, 66827392, 66846049, 67765639, 68775400, 68782284, 68852753, 68863638,
                         69755871, 69798283, 70690821, 70773445, 73698396, 74666469, 74673718, 74759503, 75659481, 75720364,
                         75751169, 75757534, 75771696, 75825114, 76717053, 76759609, 76857238, 77753875, 78742874, 79842136,
                         80662694, 80793718, 80908539, 81895868, 82752392, 82861389, 84831676, 84835102, 84888649, 85674921,
                         85828156, 86719739, 86747662, 87661619, 88670823, 88801230, 89667648, 89834678, 90678865, 87719914]
        self.case3_num = 88801230

    def test_repetition(self):
        self.assertFalse(self.default.repetition(self.case1_li, self.case1_num, 0, len(self.case1_li)))
        self.assertTrue(self.default.repetition(self.case2_li, self.case2_num, 0, len(self.case2_li)))
        self.assertTrue(self.default.repetition(self.case3_li, self.case3_num, 0, len(self.case3_li)))

if __name__ == '__main__':
    unittest.main()
