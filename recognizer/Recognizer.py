import cv2 as cv
import numpy as np
import face_recognition
import os
import pickle

PATH = os.path.dirname(os.path.abspath(__file__))


class RecognizationService:
    current_image_path = fr'{PATH}\current_image\current_image.jpg'
    users_images_path = fr'{PATH}\images_base'
    encode_list_path = fr'{PATH}\face-encode_lsit.pickle'

    @classmethod
    def save_current_image(cls, user_id=1):
        old_loc = cls.current_image_path
        new_loc = fr'{PATH}\images_base\{user_id}.jpg'
        os.replace(old_loc, new_loc)
        cls.face_train()
        return True

    @classmethod
    def delete_image(cls, user_id):
        if not user_id:
            print('Ошибка удаления фото')
            return False
        image_path = fr'{PATH}\images_base\{user_id}.jpg'
        os.remove(image_path)
        return True

    @classmethod
    def make_photo(cls, camera=0):
        """Makes photo from camera and save it"""
        cap = cv.VideoCapture(camera, cv.CAP_DSHOW)
        ret, frame = cap.read()
        res = cv.imwrite(cls.current_image_path, frame)
        cap.release()
        cv.destroyAllWindows()

        faces_amount = len(face_recognition.face_locations(frame))
        if faces_amount != 1:
            print('There more than 1 face in the photo, making new one!')
            return False
            # cls.make_photo()
        else:
            print('[OK]\tPhoto taken!')
            return True

    @classmethod
    def face_train(cls):
        images = []

        # for root, dirs, files in os.walk(cls.users_images_path):
        #     for filename in files:
        #         img_path = os.path.join(root, filename)

        user_images_list = os.listdir(cls.users_images_path)

        for user_image in user_images_list:
            # current_user_image = cv.imread(fr'{cls.users_images_path}\{user_image}')
            current_user_image = face_recognition.load_image_file(fr'{cls.users_images_path}\{user_image}')
            images.append(current_user_image)

        encode_lsit = []
        for image in images:
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(image)[0]
            encode_lsit.append(encode)
        with open(cls.encode_list_path, 'wb') as f:
            pickle.dump(encode_lsit, f)
        print('[OK]\tTraining complete!')
        return True

    @classmethod
    def check_image(cls):
        images = []
        user_names_list = []
        user_images_list = os.listdir(cls.users_images_path)

        for user_image in user_images_list:
            current_user_image = cv.imread(f'{cls.users_images_path}/{user_image}')
            images.append(current_user_image)
            user_names_list.append(user_image.split('.')[0])

        with open(cls.encode_list_path, 'rb') as f:
            encode_list = pickle.load(f)

        image = face_recognition.load_image_file(cls.current_image_path)
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        faces_cur_frame = face_recognition.face_locations(image)
        encodes_cur_frame = face_recognition.face_encodings(image, faces_cur_frame)

        for encode_face, face_loc in zip(encodes_cur_frame, faces_cur_frame):
            matches = face_recognition.compare_faces(encode_list, encode_face)
            face_dist = face_recognition.face_distance(encode_list, encode_face)
            match_index = np.argmin(face_dist)

            if matches[match_index]:
                name = user_names_list[match_index].upper()
            else:
                name = None
            return name

