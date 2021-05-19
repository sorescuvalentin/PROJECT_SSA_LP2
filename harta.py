import gmplot

apikey = 'AIzaSyCQdXI-unUeNyKdtGRHh-3CmfPrbPPWPIw'
Ghe_Baritiu = [45.7486502,21.1996101]
Arena_Aqua = [45.7697793,21.2665302]
Pod_Ghiroda = [45.76336992754513, 21.304165559088155]
Ion_Ionescu = [45.77793065225331, 21.242701583520894]
Giratie_Dumbravita = [45.807454271759276, 21.255572372978044]
Traian_Grozavescu = [45.75469102273072, 21.233656934261482]
Calea_Martirilor = [45.72116219409322, 21.236897877934215]
Bulevardul_Sudului = [45.73735925234307, 21.25001413723511]
Baader = [45.7625158890286, 21.244690829547448]
Institutul_Agronomic = [45.7831044183027, 21.219383420305363]
Solventul = [45.74740287821777, 21.190473813122704]
Calea_Torontalului = [45.7748539305855, 21.21402661182725]


gmap11 = gmplot.GoogleMapPlotter(45.748871, 21.208679, 15, apikey=apikey)
gmap11.draw('map.html')
gmap11.directions(Ghe_Baritiu,Arena_Aqua,edge_color="cyan", edge_width=5, face_color=None, face_alpha=None, clickable = False)
gmap11.draw('linia11.html')

gmapM11 = gmplot.GoogleMapPlotter(45.748871, 21.208679, 15, apikey=apikey)
gmapM11.draw('map.html')
gmapM11.directions(Ghe_Baritiu,Pod_Ghiroda,edge_color="cyan", edge_width=5, face_color=None, face_alpha=None, clickable = False)
gmapM11.draw('liniaM11.html')

gmap14 = gmplot.GoogleMapPlotter(45.748871, 21.208679, 15, apikey=apikey)
gmap14.draw('map.html')
gmap14.directions(Ghe_Baritiu,Ion_Ionescu,edge_color="cyan", edge_width=5, face_color=None, face_alpha=None, clickable = False)
gmap14.draw('linia14.html')

gmapM14 = gmplot.GoogleMapPlotter(45.748871, 21.208679, 15, apikey=apikey)
gmapM14.draw('map.html')
gmapM14.directions(Ghe_Baritiu,Giratie_Dumbravita,edge_color="cyan", edge_width=5, face_color=None, face_alpha=None, clickable = False)
gmapM14.draw('liniaM14.html')

gmap15 = gmplot.GoogleMapPlotter(45.748871, 21.208679, 15, apikey=apikey)
gmap15.draw('map.html')
gmap15.directions(Traian_Grozavescu,Calea_Martirilor,edge_color="cyan", edge_width=5, face_color=None, face_alpha=None, clickable = False)
gmap15.draw('linia15.html')

gmap16 = gmplot.GoogleMapPlotter(45.748871, 21.208679, 15, apikey=apikey)
gmap16.draw('map.html')
gmap16.directions(Bulevardul_Sudului, Traian_Grozavescu,edge_color="cyan", edge_width=5, face_color=None, face_alpha=None, clickable = False)
gmap16.draw('linia16.html')

gmap17 = gmplot.GoogleMapPlotter(45.748871, 21.208679, 15, apikey=apikey)
gmap17.draw('map.html')
gmap17.directions(Baader, Institutul_Agronomic,edge_color="cyan", edge_width=5, face_color=None, face_alpha=None, clickable = False)
gmap17.draw('linia17.html')

gmap18 = gmplot.GoogleMapPlotter(45.748871, 21.208679, 15, apikey=apikey)
gmap18.draw('map.html')
gmap18.directions(Solventul, Calea_Torontalului,edge_color="cyan", edge_width=5, face_color=None, face_alpha=None, clickable = False)
gmap18.draw('linia18.html')

