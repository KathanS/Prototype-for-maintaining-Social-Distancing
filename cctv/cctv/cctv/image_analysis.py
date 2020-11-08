import math

def people_locations(image_url):

    from clarifai.rest import ClarifaiApp

    app = ClarifaiApp(api_key='940c1262c8004ae5a8b4688ba80cff31')

    model = app.public_models.face_detection_model
    response = model.predict_by_url(url=image_url)

    locData = response['outputs'][0]['data']['regions']

    locs = []

    for i in locData:
        if i['data']['concepts'][0]['value']>0.8:
            d = i['region_info']['bounding_box']
            c = []
            c.append(d['top_row'])
            c.append(d['left_col'])
            c.append(d['bottom_row'])
            c.append(d['right_col'])
            locs.append(c)

    return locs

def socialDistance(locs, thre):
    cX = [(i[1] + i[3])/2 for i in locs]
    cY = [(i[0] + i[2])/2 for i in locs]

    dis = []

    n = len(locs)

    for i in range(n):
        darr = []
        for j in range(n):
            if i!=j:
                pd = math.sqrt((cX[i]-cX[j])**2 + (cY[i] - cY[j])**2)
                darr.append(pd)
            else:
                darr.append(None)
        dis.append(darr)

    sn = 0

    for i in dis:
        for j in i:
            if j!=None and j<thre:
                sn+=1

    return sn

locs = people_locations('https://previews.123rf.com/images/microstockasia/microstockasia1611/microstockasia161120865/69410827-three-indian-people-talking-together-and-laughing.jpg')

n = socialDistance(locs, 0.5)

print(n/2) # will print number of people who are not maintaining social distance