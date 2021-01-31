import numpy as np

class Tiles:
    def __init__(self,name,width,distanceLimit,distanceMinimum,slipstream):
        self.name = name
        self.width = width
        self.distanceLimit = distanceLimit
        self.distanceMinimum = distanceMinimum
        self.slipstream = slipstream

start_2 = Tiles("start_2",2,None,None,True)
start_2_noslip = Tiles("start_2",2,None,None,False)
start_3 = Tiles("start_3",3,None,None,True)
track_2 = Tiles("track_2",2,None,None,True)
track_2_noslip = Tiles("track_2",2,None,None,False)
track_3 = Tiles("track_3",3,None,None,True)
finish = Tiles("finish",2,None,None,True)
finish_uphill = Tiles("finish_uphill",2,5,None,False)
cobble_1 = Tiles("cobble_1",1,None,None,False)
cobble_2 = Tiles("cobble_2",2,None,None,False)
uphill = Tiles("uphill",2,5,None,False)
downhill = Tiles("downhill",2,None,5,True)
downhill_noslip = Tiles("downhill",2,None,5,False)
feed = Tiles("feed",3,None,4,True)

class Pieces:
    def __init__(self,name,tile_array):
        self.name = name
        self.tile_array = tile_array
        self.length = len(tile_array)

    def apply_weather(self,weather):
        """
        Creates a weather array for a piece
        Length of returned array is equal to number of tiles in piece
        This is done to fit with attributes() function of Racecourse class
        """
        self.weather_array = self.length*[weather]

white_1 = Pieces("white_1",[start_3,start_3,start_3,start_3,track_3,track_3])
black_1 = Pieces("black_1",[start_3,start_3,start_3,start_3,start_3,track_3])
white_2 = Pieces("white_2",[track_3,track_3,track_3,track_3,track_3,track_2])
black_2 = Pieces("black_2",6*[track_2])
white_3 = Pieces("white_3",[feed,feed,feed,feed,feed,track_2])
black_3 = Pieces("black_3",[track_2,track_2,cobble_1,cobble_1,cobble_2,cobble_1])
white_4 = Pieces("white_4",white_3.tile_array)
black_4 = Pieces("black_4",[cobble_1,cobble_2,cobble_1,cobble_1,track_2,track_2])
white_5 = Pieces("white_5",[cobble_1,cobble_2,cobble_1,cobble_2,cobble_1,cobble_1])
black_5 = Pieces("black_5",[cobble_1,cobble_1,track_2,track_2,track_2,track_2])
white_6 = Pieces("white_6",[cobble_1,cobble_1,cobble_2,cobble_1,cobble_1,cobble_1])
black_6 = Pieces("black_6",[cobble_1,cobble_1,cobble_1,cobble_2,cobble_1,track_2])
white_7 = Pieces("white_7",[track_2,track_2,cobble_1,cobble_1,cobble_2,cobble_1])
black_7 = Pieces("black_7",[cobble_1,cobble_2,cobble_1,track_2,track_2,track_2])
white_8 = Pieces("white_8",[track_2,track_2,track_2,cobble_1,cobble_2,cobble_1])
black_8 = Pieces("black_8",[cobble_1,cobble_1,cobble_2,cobble_1,cobble_1,track_2])
white_9 = Pieces("white_9",[feed,feed,track_2])
black_9 = Pieces("black_9",[track_3,track_3,track_2])
A = Pieces("A",[start_2,start_2,start_2,start_2,track_2,track_2])
a = Pieces("a",[start_2,start_2,start_2,start_2,start_2,track_2])
B = Pieces("B",[downhill,downhill,downhill,downhill,track_2,track_2])
b = Pieces("b",black_2.tile_array)
C = Pieces("C",[track_2,track_2,track_2,uphill,uphill,uphill])
c = Pieces("c",black_2.tile_array)
D = Pieces("D",[uphill,uphill,uphill,uphill,uphill,downhill])
d = Pieces("d",black_2.tile_array)
E = Pieces("E",[uphill,uphill])
e = Pieces("e",2*[track_2])
F = Pieces("F",[downhill,downhill,downhill,track_2,track_2,track_2])
f = Pieces("f",black_2.tile_array)
G = Pieces("G",E.tile_array)
g = Pieces("g",e.tile_array)
H = Pieces("H",[downhill,downhill])
h = Pieces("h",e.tile_array)
I = Pieces("I",e.tile_array)
i = Pieces("i",e.tile_array)
J = Pieces("J",e.tile_array)
j = Pieces("j",e.tile_array)
K = Pieces("K",E.tile_array)
k = Pieces("k",e.tile_array)
L = Pieces("L",[uphill,uphill,uphill,downhill,downhill,downhill])
l = Pieces("l",black_2.tile_array)
M = Pieces("M",[track_2,track_2,uphill,uphill,uphill,uphill])
m = Pieces("m",black_2.tile_array)
N = Pieces("N",6*[uphill])
n = Pieces("n",black_2.tile_array)
O = Pieces("O",E.tile_array)
o = Pieces("o",e.tile_array)
P = Pieces("P",H.tile_array)
p = Pieces("p",e.tile_array)
Q = Pieces("Q",E.tile_array)
q = Pieces("q",e.tile_array)
R = Pieces("R",E.tile_array)
r = Pieces("r",e.tile_array)
S = Pieces("S",e.tile_array)
s = Pieces("s",e.tile_array)
T = Pieces("T",e.tile_array)
t = Pieces("t",e.tile_array)
U = Pieces("U",[uphill,uphill,finish_uphill,finish_uphill,finish_uphill,finish_uphill])
u = Pieces("u",[track_2,track_2,finish,finish,finish,finish])

class Racecourse:
    def __init__(self,name,piece_array,weather):

        weather = np.array(weather) #Make np array for easy matrix manipulation
        self.name = name
        self.route = []
        self.piece_array = []
        self.weather_array = []

        for piece in piece_array:
            if piece.name in weather[:,0]:
                loc = np.where(weather[:,0]==piece.name)[0][0] #Find location of tile in weather input
                w = weather[loc,1] #Return corresponding weather
                piece.apply_weather(w)
            else:
                piece.apply_weather(None)

            self.route.extend(piece.tile_array)
            self.weather_array.extend(piece.weather_array) #Note, weather separate array from route
        for piece in piece_array:
            self.piece_array.extend(len(piece.tile_array)*[piece.name])
        self.length = len(self.route)
        ind = 0 
        while ind < self.length:
            piece = self.route[ind].name
            if (piece == "uphill" or piece == "cobble_1" or piece == "cobble_2") and (self.route[ind-1].name == "track_2"):
                self.route[ind-1] = track_2_noslip
            elif (piece == "uphill" or piece == "cobble_1" or piece == "cobble_2") and (self.route[ind-1].name == "downhill"):
                self.route[ind-1] = downhill_noslip
            elif (piece == "uphill" or piece == "cobble_1" or piece == "cobble_2") and (self.route[ind-1].name == "start_2"):
                self.route[ind-1] = start_2_noslip
            ind += 1

    def attributes(self):
        """
        Returns attributes of each tile of the stage as full list in format
        [name, width, min distance, distance limit, slipstream (boolean), weather]
        No inputs, returns attributes of every attribute in a matrix
        """
        atts = []
        i = 0
        while i < self.length:
            tile = self.route[i]
            tileWeather = self.weather_array[i]
            atts.append([tile.name,tile.width,tile.distanceMinimum,tile.distanceLimit,tile.slipstream,tileWeather])
            i += 1
        return atts

#An example stage build and how its attributes are returned
#stage_18 = Racecourse("stage_18",[a,black_2,h,white_4,L,o,p,c,white_5,black_6,r,white_3,g,q,J,k,s,t,e,I,U],[["black_2","wet"],["black_6","crosswind"]])
#stage_18.attributes()


