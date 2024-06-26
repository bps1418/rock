#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:37:12 2024

@author: bhanu
"""

import cv2

cam = cv2.VideoCapture(0)

while True:
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_RGBA2GRAY)
        blur = cv2.GaussianBlur(diff, (5,5),0)
        _,thresh = cv2.threshold(blur, 20,255,cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh,None, iterations=3)
        contours,_ = cv2.findContours(dilated, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame1, contours,-1,(0,255,255),2)

        if cv2.waitKey(10) == ord('q'):
            break
        cv2.imshow('My Cam', frame1)
        