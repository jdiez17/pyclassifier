from pyclassifier import Classifier
import sys

c = Classifier.from_data(open('training.pckl'))

print c.identify(open(sys.argv[1]).read())

