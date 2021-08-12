from facial_emotion_recognition import EmotionRecognition
import cv2

er = EmotionRecognition(device='cpu')


class Video(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret,frame = self.video.read()
        
        frame = er.recognise_emotion(frame, return_type='BGR')

        ret,jpg = cv2.imencode('.jpg',frame)
        return jpg.tobytes()