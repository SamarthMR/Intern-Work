import dlib, cv2
import socket , zmq
import numpy as np

getface = dlib.get_frontal_face_detector()
# Get a front face detector with dlib
getlandmark= dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")
# Get a landmark predictor from the dat file to get 68 landmarks of the face


context= zmq.Context()
#Here we build the context for communication to server
socket = context.socket(zmq.REP)
#From the context we create a socket through which other clients will be connected 
socket.bind("tcp://127.0.0.1:9999")
#For the example purpose we are taking port 9999 and localhost ip for sake of demonstration
#So far we have set up connection which listens to the ip and binds with it.


# THIS FUNCTION SENDS THE FRAME IMAGE TO THE ENDPOINT
def send_array(socket, A, flags=0, copy=True, track=False):
    md = dict(
        dtype = str(A.dtype),
        shape = A.shape,
    )
    socket.send_json(md, flags|zmq.SNDMORE)
    return socket.send(A, flags, copy=copy, track=track)

# THIS FUNCTION RECIEVIES THE ARRAY SENT FROM ANOTHER END
def recv_array(socket, flags=0, copy=True, track=False):
    md = socket.recv_json(flags=flags)
    msg = socket.recv(flags=flags, copy=copy, track=track)
    A = np.frombuffer(msg, dtype=md["dtype"])

    return A.reshape(md['shape'])
    
frame = recv_array(socket)
# Recieve the cam frame from the client
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#Converted the frame to gray for detection
faces= getface(gray)
# Detect all the faces in the frame

#Loop over each face
for face in faces:
    x, y= face.left(), face.top()
    w, h= face.right()-x, face.bottom()-y
    #Get cordinates of the face along with length and width 
    frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(0,0,255),3)
    # Draw a rectangle over the detected face

    landmarks = getlandmark(gray, face)
    # Get all 68 points of face from the prdictor by passing the image and face 

    hx= landmarks.part(48).x-10
    hy= landmarks.part(51).y-10
    ww= landmarks.part(54).x-landmarks.part(48).x+10
    hh = landmarks.part(57).y- landmarks.part(51).y+10
    #Getting the cordinates of lips of the face taking +10 margin (Refer to figure in the mardown file for landmard positions)

    frame= cv2.rectangle(frame, (hx,hy),(hx+ww,hy+hh),(0,255,0),3)
    #Draw a rectangle over the lips
    
    hx= (landmarks.part(37).x+landmarks.part(40).x)//2
    hy= (landmarks.part(37).y+landmarks.part(40).y)//2
    radius = (landmarks.part(39).x-landmarks.part(36).x+10)//2
    # Getting the cordinates of the left eye and radius to draw the circle
    

    frame= cv2.circle(frame, (hx,hy),radius ,(0,255,255),3)
    # Drawing a circle around the left eye  

    hx= (landmarks.part(43).x+landmarks.part(46).x)//2
    hy= (landmarks.part(43).y+landmarks.part(46).y)//2
    radius= (landmarks.part(45).x-landmarks.part(42).x+10)//2
    # Getting the cordinates of the right eye and radius to draw the circle

    frame= cv2.circle(frame, (hx,hy),radius,(0,255,255),3)
    # Drawing a circle around the right eye  

send_array(socket,frame)