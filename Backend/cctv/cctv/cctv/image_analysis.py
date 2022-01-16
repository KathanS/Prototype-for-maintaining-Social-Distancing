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
    psn = [0 for i in range(n)]

    for ind,i in enumerate(dis):
        for j in i:
            if j!=None and j<thre:
                sn+=1
                psn[ind] = 1
    
    psnLoc = []
    
    for i in range(n):
        if psn[i]==1:
            psnLoc.append((locs[i][0],locs[i][1],locs[i][2],locs[i][3]))

    return psnLoc
    
def queueLimit(avgTime, locs, remTime):
    num_persons = remTime//avgTime
    sortArr = []
    for i in locs:
        sortArr.append(i[1])
    sortArr.sort()
    return (num_persons, sortArr[num_persons])

def triangleCams(locs1, locs2):
    ylim = 0.55
    sortArr = []
    for i in locs:
        sortArr.append(i[0])
    sortArr.sort()
    i = 0
    while sortArr[i]<0.55:
        i+=1
    i+=len(locs2)
    return i
