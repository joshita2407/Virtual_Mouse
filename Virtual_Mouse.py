import cv2                                                      
import mediapipe as mp      #this is used to detect the hand    
import pyautogui                                                
cap = cv2.VideoCapture(0)       #used to capture vedio from camera
hand_detector = mp.solutions.hands.Hands()      #detecting hand from frame
drawing_utils = mp.solutions.drawing_utils      #  drawing util used for hand marks             
screen_width, screen_height = pyautogui.size()  # used for getting the monitor sceen size                
index_y = 0                                                      
while True:                                                     
    _, frame = cap.read()       #used to capture the frame      
    frame = cv2.flip(frame, 1)      #used to flip the camera    
    frame_height, frame_width, _ = frame.shape()                  
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)      #cv2.cvtcolor is used to convert color from BGR to RGB
    output = hand_detector.process(rgb_frame)       #process hand from coverted frame
    hands = output.multi_hand_landmarks     #To store land mark value in this variable
    if hands:                                                   
        for hand in hands:                                      
            drawing_utils.draw_landmarks(frame, hand)       #used to point land marks on hand in screen
            landmarks = hand.landmark                           
            for id, landmark in enumerate(landmarks):           
                x = int(landmark.x*frame_width)     #converting cordinate to int
                y = int(landmark.y*frame_height)    #converting cordinate to int
                if id == 8:     #index finger tip               
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))     #used to highlight finger 
                    index_x = screen_width/frame_width*x    #used to make camera frame=monitor screen    
                    index_y = screen_height/frame_height*y  #used to make camera frame=monitor screen       
                if id == 4:     #thumb finger tip               
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x        #used to make camera frame=monitor screen    
                    thumb_y = screen_height/frame_height*y      #used to make camera frame=monitor screen    
                    print('outside', abs(index_y - thumb_y))        
                    if abs(index_y - thumb_y) < 20:                  
                        pyautogui.click()  #left click operation default                     
                        pyautogui.sleep(1)                      
                    elif abs(index_y - thumb_y) < 100:          
                        pyautogui.moveTo(index_x, index_y)      
    cv2.imshow('Virtual Mouse', frame)                          
    cv2.waitKey(1)                                              