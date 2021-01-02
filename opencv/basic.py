import cv2 as cv
img_str = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAMCAgICAgMCAgIDAwMDBAYEBAQEBAgGBgUGCQgKCgkICQkKDA8MCgsOCwkJDRENDg8QEBEQCgwSExIQEw8QEBD/2wBDAQMDAwQDBAgEBAgQCwkLEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBD/wAARCAHgAoADAREAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDuUTgkkDAzUvXQ2Wg5GAQ7uSCTx6cf/XoasD1JVw68Ict90HjrTYkraiIMcnoanlTHcdgHkdKfLYdx+Fx8oI+tOxLJRjHC4xSaKbuhQxAyeT7CmlYQ4E4HGDTG2KAccNg56jmgSsiVMHjdigQ4F…
'
decoded_data = base64.b64decode(img_str)
np_data = np.fromstring(decoded_data,np.uint8)
img = cv.imdecode(np_data,cv.IMREAD_UNCHANGED)
cv.imshow("test", img)

    
# img = cv.imread('./Resources/Photos/park.jpg')
# cv.imshow('boston',img)

# #grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray boston', gray)

# #blur
# blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('blur boston', blur)

# #edge cascade
# canny= cv.Canny(blur, 125, 125)
# cv.imshow('edge boston', canny)

# #dalating de image
# dilated = cv.dilate(canny,(7,7),iterations=3)
# cv.imshow('dilated boston', dilated)

cv.waitKey(0)