import cv2 

def draw_circle(path, cX, cY, pX, pY, filename):
    path = 'kites.jpg'
    image = cv2.imread(path)
    #print(image==None)
    center_coordinates = (int(cX*pX), int(cY*pY))
    radius = 20
    color = (0, 0, 255)
    thickness = 2
    image = cv2.circle(image, center_coordinates, radius, color, thickness)
    #cv2.imshow("1", image)
    cv2.imwrite(filename, image)
    
def draw_all(path, locs, pX, pY, filename):
    for i in locs:
        x = (i[1]+i[3])/2
        y = (i[0]+i[2])/2
        draw_circle(path, x, y, pX, pY, filename)


if __name__=='__main__':
    for i in locs:
        x = (i[1]+i[3])/2
        y = (i[0]+i[2])/2
        draw_circle(path, x, y, pX, pY, filename)