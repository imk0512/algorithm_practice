N,X,Y = map(int,input().split())

def changeRed(red):
    if(red > 1):

        blue = [[red]*X]
        jue = {
            'red':red - 1,
            'blue':blue
        }
        return jue
    else :
        return {}

def changeBlue(blue):
    if(blue > 1):
        blues = [[blue]*Y]
        jue = {
            'red':blue,
            'blue':blue
        }
        return jue
    else :
        return {}

