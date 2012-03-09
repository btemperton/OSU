__author__ = 'benbo'
import logging
import re
import os



@staticmethod
def getUniqueValues(listOfValues):
    set = {}
    map(set.__setitem__, listOfValues, [])
    return set.keys()


class BlastHit:
    def __init__(self, queryId, subjectId, pctId, alnLength, qStart, qEnd, sStart, sEnd, evalue, bitscore):
        self.queryId = queryId
        self.subjectId = subjectId
        self.pctId = pctId
        self.alnLength = alnLength
        self.qStart = qStart
        self.qEnd = qEnd
        self.sStart = sStart
        self.sEnd = sEnd
        self.evalue = evalue
        self.bitscore = bitscore

class BlastUtility:
    @staticmethod
    def parseBlastOutput(outputFile):
        logging.debug('Parsing file %s' % (outputFile))
        f = open(outputFile, 'rU')
        hits = set()
        for line in f:
            if line.startswith('#'):
                continue
            line = line.strip()
            bits = line.split('\t')
            hits.add(bits[0], bits[1], bits[2], bits[3], bits[6], bits[7], bits[8], bits[9], bits[10], bits[11])
        f.close()
        return hits
