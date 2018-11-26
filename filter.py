from PIL import Image, ImageDraw
import face_recognition
import cv2
import numpy as np
import time

def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
 
    while True:
        ret_val, img = cam.read()
        small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_landmarks_list = face_recognition.face_landmarks(img)
           
        for face_landmarks in face_landmarks_list:
            pil_image = Image.fromarray(img)
                
            d = ImageDraw.Draw(pil_image, 'RGBA')
            for i in range(len(face_landmarks['top_lip'])):
                d.polygon(face_landmarks['left_eye'][2]+face_landmarks['left_eye'][3] + face_landmarks['top_lip'][i], fill=(0, 100, 100, 100))
            for j in range(len(face_landmarks['top_lip'])):
                d.polygon(face_landmarks['right_eye'][2]+face_landmarks['right_eye'][3]+ face_landmarks['top_lip'][j],fill=(0, 100, 100, 100))
            for k in range(len(face_landmarks['chin'])):
                d.polygon(face_landmarks['nose_bridge'][2] +face_landmarks['nose_bridge'][1]+ face_landmarks['chin'][k], fill=(0,0,100,100))
            for i in range(5,len(face_landmarks['chin'])-4):
                d.polygon(face_landmarks['bottom_lip'][4] + face_landmarks['bottom_lip'][3] + face_landmarks['chin'][i], fill = (100,0,50,100))
            d.line(face_landmarks['chin'], fill = (200,200,200,200),width = 7)
            d.polygon(face_landmarks['top_lip'], fill=(100, 0, 100, 200))
            d.polygon(face_landmarks['bottom_lip'], fill=(100, 0, 100, 200))
            img = np.asarray(pil_image)
                           
        if mirror: 
            
            img = cv2.flip(img, 1)
        cv2.imshow('Video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print(face_landmarks_list)
            break
        
    cam.release()
    cv2.destroyAllWindows()
def main():
    show_webcam(mirror = True)
if __name__ == '__main__':
    main()

    
 
