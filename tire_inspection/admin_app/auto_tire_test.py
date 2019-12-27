from cv2 import cv2
import numpy as np

class tire_testing:
    """
    Class containing all the tire testing function
    """
    def ink_test(self,location):
        """
        Function checks the ink spillage in tire
        Returns 0 or 1
        """
        frame = cv2.imread(location)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray,150,200,0)
        contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.fillPoly(frame,pts=[contours[17]],color=(0,0,0))
        cv2.fillPoly(frame,pts=[contours[34]],color=(0,0,0))
        cv2.fillPoly(frame,pts=[contours[44]],color=(0,0,0))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray,165,165,0)
        _, contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        count = 0
        for _ in contours:
            count = count + 1
        if count > 0:
            flag = 1
        else:
            flag = 0
        return flag
    
    def scorch_test(self,location):
        """
        Function checks the scorch in tire
        Returns 0 or 1
        """
        frame = cv2.imread(location)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        tot_area = 0
        _, thresh = cv2.threshold(gray,150,200,0)
        _,contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            tot_area = tot_area + area
        if tot_area > 2000 and tot_area < 2500:
            flag = 1
        else:
            flag = 0
        return flag
