import os
import numpy as np
import cv2
import pickle
from PIL import Image
from local_settings import BASE_DIR


class RecognizationService:
    face_cascade = cv2.CascadeClassifier(r'C:\BFR\biometric_face_recognition\common\recognizer\cascades\haarcascade_frontalface_alt2.xml')
    # current_photo_path = os.path.join(BASE_DIR, "C:\\BFR\\biometric_face_recognition\\media\\images\\current_photo\\current_photo.png")
    current_photo_path = r'C:\BFR\biometric_face_recognition\media\images\current_photo\current_photo.jpg'
    # user_photos_dir = os.path.join(BASE_DIR, "media\\images\\users")
    user_photos_dir = r'C:\BFR\biometric_face_recognition\media\images\users'

    @classmethod
    def make_photo(cls, camera=0):
        """Makes photo from camera and save it"""
        cap = cv2.VideoCapture(camera, cv2.CAP_DSHOW)
        ret, frame = cap.read()
        res = cv2.imwrite(cls.current_photo_path, frame)
        cap.release()
        cv2.destroyAllWindows()
        return res

    @classmethod
    def face_training(cls):
        people = ['user_1', 'user_2']
        features = []
        labels = []

        for person in people:
            path = os.path.join(cls.user_photos_dir, person)
            label = people.index(person)
            for img in os.listdir(path):
                img_path = os.path.join(path, img)

                img_array = cv2.imread(img_path)
                if img_array is None:
                    continue

                gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
                faces_rect = cls.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

                for (x, y, w, h) in faces_rect:
                    faces_roi = gray[y:y + h, x:x + w]
                    features.append(faces_roi)
                    labels.append(label)

        print('Training done')

        features = np.array(features, dtype='object')
        labels = np.array(labels)

        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.train(features, labels)
        face_recognizer.save(r'C:\BFR\biometric_face_recognition\common\recognizer\neural_network\face_trained.yml')

    @classmethod
    def face_recognition(cls):
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read(r'C:\BFR\biometric_face_recognition\common\recognizer\neural_network\face_trained.yml')

        img = cv2.imread(cls.current_photo_path)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Person', gray)

        # Detect the face in the image
        faces_rect = cls.face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces_rect:
            faces_roi = gray[y:y + h, x:x + w]

            label, confidence = face_recognizer.predict(faces_roi)
            if confidence > 60:
                print(f'Recognized user id: {label}. Confidence: {confidence}')
            else:
                print(f'User doesent recognized. Confidence: {confidence}')
                label = 'Unknown user'
            cv2.putText(img, "id: " + str(label), (20, 20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=1)

        cv2.imshow('Detected Face', img)
        cv2.waitKey(0)

    @classmethod
    def test(cls):
        print(BASE_DIR)
        face_cascade = cv2.CascadeClassifier(
            'C:\\BFR\\biometric_face_recognition\\common\\cascades\\haarcascade_frontalface_alt2.xml')
        cap = cv2.VideoCapture(0)

        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

            for (x, y, w, h) in faces:
                print(x, y, w, h)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]
                img_item = "current_image.png"
                cv2.imwrite(img_item, roi_gray)

            cv2.imshow('frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()


# RecognizationService.make_photo()
# RecognizationService.face_training()
RecognizationService.face_recognition()
