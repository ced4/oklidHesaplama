#Noktaların Tanımlanması:
#points’ adında bir liste oluşturun. Bu liste, 2D uzaydaki noktaları temsil eden demetler (tuple) içermelidir.
#Örneğin, ‘(x, y)’ noktası bir demet ‘(x, y)’ olarak temsil edilecektir.

import math
points = [(x1,y1), (x2,y2)]

#Öklid Mesafesi İçin Bir Fonksiyon Yazma:
#‘euclideanDistance’ adında bir fonksiyon tanımlayın. 
# Bu fonksiyon, iki demet (her biri bir noktayı temsil eder) almalı ve bu iki nokta arasındaki Öklid mesafesini döndürmelidir.

def euclideanDistance (x1,y1, x2,y2): 
    return math.sqrt ((x2 - x1)**2 + (y2 - y1)**2)

#Mesafelerin Hesaplanması:
#Bir döngü kullanarak, ‘points’ listesindeki her nokta çifti arasındaki Öklid mesafesini hesaplayın. 
# Bu mesafeleri ‘distances’ adında başka bir listede saklayın.

distances = []
for i in range(len(points)):
    for k in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[k]
        distances = euclideanDistance(x1, y1, x2, y2)
        distances.append(distances)

#Minimum Mesafenin Bulunması:

min_distance = min(distances)
print("Noktalar arasındaki minimum mesafe:", min_distance)
