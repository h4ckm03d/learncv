import argparse
import cv2

class LineFinder:
    PI=3.1415926

    def __init__(self):
        self.img = None
        self.lines=[]
        # accumulator resolution parameters
        self.delthaRho=1
        self.delthaTheta=PI/180.0

        # minimum number of votes that a line 
        # must receive before being considered
        self.minVote=10

        # min length for a line
        self.minLength=0.0

        # max allowed gap along the line
        self.maxGap=0.0;

        # distance to shift the drawn lines down when using a ROI
        self.shift=0
    
    def setAccResolution(self, dRho, dTheta):
        self.delthaRho = dRho
        self.delthaTheta = dTheta

    def setMinVote(self, minVote):
        self.minVote=minVote

    def setLineLengthAndGap(self, length, gap):
        self.minLength=length
        self.maxGap=gap

    def setShift(self, imgShift):
        self.shift=imgShift

    def findLines(self, binary):
        pass
    
    def drawDetectedLines(self, image, color):
        pass

    def removeLinesOfInconsistentOrientations(self, orientations, percentage, delta):
        pass

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    # ap.add_argument("-v", "--video", help= "Path to the video")
    ap.add_argument("-i", "--image", help= "Path to the image")
    ap.add_argument("-s", "--step", help= "Show Step")
    args = vars(ap.parse_args())

    vid = cv2.imread(args["image"])
    height, width, channels = image.shape
    
    print "width: %d pixels" % (image.shape[1])
    print "height: %d pixels" % (image.shape[0])
    print "channels: %d" % (image.shape[2])

    # TODO processing in every read from camera of video
    # 1. set the ROI for the image
    # 2. Display the image
    # 3. Canny algorithm
    # 4. Display Canny image
    # 5. Process hough transform
    #    Hough tranform for line detection with feedback
	#    Increase by 25 for the next frame if we found some lines.  
	#    This is so we don't miss other lines that may crop up in the next frame
	#    but at the same time we don't want to start the feed back loop from scratch. 
    # 6. Draw the lines
    # 7. Display the detected line image
    # 8. Create LineFinder instance
    # 9. Set probabilistic Hough parameters
    # 10.Detect lines
    # 11.bitwise AND of the two hough images
    # 12.Set probabilistic Hough parameters
    # 13.Writer the frame into the file