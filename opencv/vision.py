from google.cloud import vision
import os
import io
import time

start_time = time.time()

path = 'C:/Users/lukas/Desktop/vision_key.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=path
client = vision.ImageAnnotatorClient()

path = './Resources/Photos/lady.jpg'
with io.open(path, 'rb') as image_file:
        content = image_file.read()

image = vision.Image(content=content)
response = client.face_detection(image=image)
likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

for face in response.face_annotations:
        # likelihood = vision.Likelihood(face.joy_likelihood)
        # vertices = ['(%s,%s)' % (v.x, v.y) for v in face.bounding_poly.vertices]
        # print('Face surprised:', likelihood.name)
        # print('Face bounds:', ",".join(vertices))
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
        print('sorrow: {} \n'.format(likelihood_name[face.sorrow_likelihood]))

print("--- %s seconds ---" % (time.time() - start_time))
print('DONE')