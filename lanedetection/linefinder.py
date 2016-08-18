import cv2

class LineFinder:
    PI=3.1415926

    def __init__(self):
        self._img = None
        self._lines=[]
        # accumulator resolution parameters
        self._delthaRho=1
        self._delthaTheta=PI/180.0

        # minimum number of votes that a line 
        # must receive before being considered
        self._minVote=10

        # min length for a line
        self._minLength=0.0

        # max allowed gap along the line
        self._maxGap=0.0;

        # distance to shift the drawn lines down when using a ROI
        self._shift=0
    
    def setAccResolution(self, dRho, dTheta):
        self._delthaRho = dRho
        self._delthaTheta = dTheta

    def setMinVote(self, minVote):
        self._minVote=minVote

    def setLineLengthAndGap(self, length, gap):
        self._minLength=length
        self._maxGap=gap

    def setShift(self, imgShift):
        self._shift=imgShift

    def findLines(self, cv2.Mat):
        pass