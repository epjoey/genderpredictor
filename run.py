#!/usr/bin/env python
import csv
from genderPredictor import genderPredictor
import pprint

gp = genderPredictor()
gp.trainAndTest()

results = {
    'numAnalyzed' : 0,
    'numMaleAnalyzed': 0,
    'numFemaleAnalyzed': 0,
    'numCorrect' : 0,
    'numMaleCorrect' : 0,
    'numFemaleCorrect' : 0,
    'percentageCorrect': {
        'M': 0,
        'F': 0,
        'total': 0
    }
}

with open('names.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        results['numAnalyzed'] += 1;
        
        gender = gp.classify(row[0])
        
        if gender == 'M':
            results['numMaleAnalyzed'] += 1;
        elif gender == 'F':
            results['numFemaleAnalyzed'] += 1;
        
        if gender == row[1]:
            results['numCorrect'] += 1
            if gender == 'M':
                results['numMaleCorrect'] += 1;
            elif gender == 'F':
                results['numFemaleCorrect'] += 1;


results['percentageCorrect'] = {
    'M': float(results['numMaleCorrect']) / float(results['numMaleAnalyzed']),
    'F': float(results['numFemaleCorrect']) / float(results['numFemaleAnalyzed']),
    'total': float(results['numCorrect']) / float(results['numAnalyzed'])
}

#print json.loads(results)
with open('output.txt', 'wt') as out:
    pprint.pprint(results, stream=out)