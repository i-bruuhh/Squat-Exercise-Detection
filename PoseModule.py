"""
Pose Module
By: Computer Vision Zone
Website: https://www.computervision.zone/
"""
import cv2
import mediapipe as mp
import numpy  as np


class PoseDetector:
    """
    Estimates Pose points of a human body using the mediapipe library.
    """

    def __init__(self, mode=False, smooth=True,
                 detectionCon=0.5, trackCon=0.5):
    
    # with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        """
        :param mode: In static mode, detection is done on each image: slower
        :param upBody: Upper boy only flag
        :param smooth: Smoothness Flag
        :param detectionCon: Minimum Detection Confidence Threshold
        :param trackCon: Minimum Tracking Confidence Threshold
        """

        self.mode = mode
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

   
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(static_image_mode=self.mode,
                                     smooth_landmarks=self.smooth,
                                     min_detection_confidence=self.detectionCon,
                                     min_tracking_confidence=self.trackCon)
        


    def findPose(self, img, draw=True):
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img


    def hipL(self):
        try:
            landmarks = self.results.pose_landmarks.landmark
            hipL = [landmarks[self.mpPose.PoseLandmark.LEFT_HIP.value].x,landmarks[self.mpPose.PoseLandmark.LEFT_HIP.value].y]
            return hipL
        except:
            pass

    def hipR(self):
        try:
            landmarks = self.results.pose_landmarks.landmark
            hipR = [landmarks[self.mpPose.PoseLandmark.RIGHT_HIP.value].x,landmarks[self.mpPose.PoseLandmark.RIGHT_HIP.value].y]
            return hipR
        except:
            pass

    # ************************************************

        
    def kneeL(self):
        try:
            landmarks = self.results.pose_landmarks.landmark
            knee = [landmarks[self.mpPose.PoseLandmark.LEFT_KNEE.value].x,landmarks[self.mpPose.PoseLandmark.LEFT_KNEE.value].y]
            return knee
        except:
            pass
    def kneeR(self):
        try:
            landmarks = self.results.pose_landmarks.landmark
            kneeR = [landmarks[self.mpPose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[self.mpPose.PoseLandmark.RIGHT_KNEE.value].y]
            return kneeR
        except:
            pass

    # ************************************************

    def ankleL(self):
        try:
            landmarks = self.results.pose_landmarks.landmark
            ankle = [landmarks[self.mpPose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[self.mpPose.PoseLandmark.LEFT_ANKLE.value].y]
            return ankle
        except:
            pass

    def ankleR(self):
        try:
            landmarks = self.results.pose_landmarks.landmark
            ankleR = [landmarks[self.mpPose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[self.mpPose.PoseLandmark.RIGHT_ANKLE.value].y]
            return ankleR
        except:
            pass


    def calculate_angle(self,a,b,c):
        a = np.array(a) # First
        b = np.array(b) # Mid
        c = np.array(c) # End
    
        radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians*180.0/np.pi)
    
        if angle >180.0:
            angle = 360-angle
        return angle
    