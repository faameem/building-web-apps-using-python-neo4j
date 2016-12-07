'''
Created on 15-Mar-2015

@author: sagupta
'''
from test import *



if __name__ == '__main__':
    baseTestsuite = unittest.TestLoader().loadTestsFromTestCase(TestingGraph)
    nodeTestsuite = unittest.TestLoader().loadTestsFromTestCase(TestingNodes)
    pathTestsuite = unittest.TestLoader().loadTestsFromTestCase(TestingPaths)
    baseTestsuite.addTest(nodeTestsuite)
    baseTestsuite.addTest(pathTestsuite)
    
    unittest.TextTestRunner(verbosity=2).run(baseTestsuite)
    