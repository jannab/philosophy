import philosophy

def testGettingToPhilosophyLaw(numberOfTests):
    sumOfHops = 0
    numberOfSuccessfulTests = 0
    for testNumber in range(numberOfTests):
        numberOfHops = philosophy.getNumberOfHopsToPhilosophy()
        if numberOfHops is not None:
            sumOfHops += numberOfHops
            numberOfSuccessfulTests += 1
    printResult(numberOfTests, numberOfSuccessfulTests, sumOfHops)

def printResult(numberOfTests, numberOfSuccessfulTests, sumOfHops):
    print('Average Hops: ' + str(sumOfHops/numberOfSuccessfulTests))
    print('The "Getting to Philosophy" law was successful in '
            + str(100*numberOfSuccessfulTests/numberOfTests)
            + ' % of the cases.')

testGettingToPhilosophyLaw(100)
