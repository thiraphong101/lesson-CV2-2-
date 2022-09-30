# USAGE
# python find_waldo.py --puzzle puzzle.png --waldo waldo.png

# import the necessary packages
import numpy as np
import imutils
import cv2

# load the puzzle and waldo images
puzzle = cv2.imread("puzzle.png")
waldo = cv2.imread("waldo.png")
(waldoHeight, waldoWidth) = waldo.shape[:2]

# find the waldo in the puzzle
result = cv2.matchTemplate(puzzle, waldo, cv2.TM_CCOEFF)
(_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)

# grab the bounding box of waldo and extract him from
# the puzzle image
topLeft = maxLoc
botRight = (topLeft[0] + waldoWidth, topLeft[1] + waldoHeight)
roi = puzzle[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]

# construct a darkened transparent 'layer' to darken everything
# in the puzzle except for waldo
mask = np.zeros(puzzle.shape, dtype = "uint8")
puzzle = cv2.addWeighted(puzzle, 0.25, mask, 0.75, 0)

# put the original waldo back in the image so that he is
# 'brighter' than the rest of the image
puzzle[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi
puzzle=cv2.resize(puzzle, (0,0), fx=0.4, fy=0.4) 
# display the images
cv2.imshow("Puzzle", puzzle)
cv2.imshow("Waldo", waldo)
cv2.waitKey(0)