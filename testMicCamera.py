import random
import re
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import face_recognition
import cv2
import 
#import socket
import time
UDP_IP = "192.168.254.34"
UDP_PORT = 5005

MSG = "Open Door"
THRESH = 0

WORDS = ["FIND OWNER", "OPENDOOR", "OPEN"]

def initialize_camera():
	# start the FPS counter
    # initialize the video stream and allow the camera sensor to warm up
    
    print("starting video stream...")
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(0.5)
    fps = FPS().start()
    return vs, fps
def movement(centerEntity,areaEntity):
	#if face is left of center of the frame
	#entityChosen = ((t,r,b,l),n,(r-l)*(b-t))
	diffFaceCenter = centerEntity[0] - CENTER[0]
	print("diff: ", diffFaceCenter)
	if abs(diffFaceCenter) > THRESHOLD:
		if diffFaceCenter < 0:
			return ("moving left")
		elif diffFaceCenter >0:
			return ("moving right")
	elif areaEntity < DISTAREATHRESH:
		return('moving forward')
	else:
		return('stopped')

def handle(text, mic, data,detector):
    """
        Responds to user-input, typically speech text, by telling a joke.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    mic.say("Identifying.")

    # sock = connect_to_door()
    vs, fps = initialize_camera()
    FramesProcessed = 0
    OpenDoor = False
    
        # loop over frames from the video file stream
    while True: # major loop
        # grab the frame from the threaded video stream and resize it
        # to 500px (to speedup processing)
        frame = vs.read()
        frame = cv2.resize(frame,RESOLUTION,cv2.INTER_AREA)
		
        # convert the input frame from (1) BGR to grayscale (for face
        # detection) and (2) from BGR to RGB (for face recognition)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # detect faces in the grayscale frame
        rects = detector.detectMultiScale(gray, scaleFactor=1.1, 
            minNeighbors=5, minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE)
        # OpenCV returns bounding box coordinates in (x, y, w, h) order
        # but we need them in (top, right, bottom, left) order, so we
        # need to do a bit of reordering
        boxes=[]
        for (x, y, w, h) in rects:
			# calculate bounding box area
			# if area greater than AREATHRESH add bounding box
			# this helps improve facial detection accuracy
            if w*h > AREATHRESH:
               boxes.append((y, x + w, y + h, x))
        #print("boxes:" ,boxes)
        # compute the facial embeddings for each face bounding box
        encodings = face_recognition.face_encodings(rgb, boxes)
        names = []

        # loop over the facial embeddings
        for encoding in encodings:
            # attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(data['encodings'],
                encoding)
            name = "Unknown"

            # check to see if we have found a match
            if True in matches:
                # find the indexes of all matched faces then initialize a
                # dictionary to count the total number of times each face
                # was matched
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                # loop over the matched indexes and maintain a count for
                # each recognized face face
                for i in matchedIdxs:
                    name = data["names"][i]

                    counts[name] = counts.get(name, 0) + 1

                # determine the recognized face with the largest number
                # of votes (note: in the event of an unlikely tie Python
                # will select first entry in the dictionary)
                name = max(counts, key=counts.get)
                # update the list of names
                names.append(name)
        similarEntity = []
        CandidateEntity = None
        #determine the entity to follow 
        if not names:
           cv2.imshow("Frame", frame)
           key = cv2.waitKey(1) & 0xFF
           fps.update()
           continue
        if OWNER in names:
            mic.say("Found the Owner")
            similarEntity = [((t,r,b,l),n,(r-l)*(b-t)) for ((t,r,b,l),n)  in zip(boxes, names) if OWNER == n]
            simEnt_sorted = sorted(similarEntity,key=lambda x: x[-1],reverse=True)
            CandidateEntity = simEnt_sorted[0]	
        else:

            similarEntity = [((t,r,b,l),n,(r-l)*(b-t)) for ((t,r,b,l),n)  in zip(boxes, names)]
            simEnt_sorted = sorted(similarEntity,key=lambda x: x[-1],reverse=True)
            CandidateEntity = simEnt_sorted[0] # (dimensionsTup, name, area)
        t,r,b,l = CandidateEntity[0]
        centerEntity = ((l+r)//2,(b+t)//2)
        robo_movement = movement(centerEntity,CandidateEntity[-1])
        

        
        cv2.circle(frame,CENTER,5,(255,0,0),2)
            #centerpt1 = ((left+right)//2,(bottom+top)//2)
        cv2.circle(frame,centerEntity,5,(255,0,0),2)
            
        cv2.rectangle(frame, (l, t), (r, b),(255,0,0), 2)
        y = t - 15 if t - 15 > 15 else t + 15
        cv2.putText(frame, CandidateEntity[1], (l, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (255,0,0), 2)
            
            #cv2.putText(frame, 'AREA: %d'%((right-left)*(bottom-top)), (left, bottom+20), cv2.FONT_HERSHEY_SIMPLEX,0.75, color, 2)

        # display the image to our screen
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

        # update the FPS counter
        fps.update()
        if (robo_movement == 'stopped'):
            if (text in WORDS):
                mic.say("Found")
                break

    # stop the timer and display FPS information

    fps.stop()
    print("elapsed time: {:.2f}".format(fps.elapsed()))
    print("approx. FPS: {:.2f}".format(fps.fps()))
    
    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()

def isValid(text):
    """
        Returns True if the input is related to jokes/humor.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    Valid = bool(re.search(r'\bfind owner\b', text, re.IGNORECASE))
    return Valid
