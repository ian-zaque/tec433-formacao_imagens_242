import cv2
import numpy as np

image_paths = ['America do Sul.tif', 'USA.tif', 'America Central.tif', 'Australia.tif', 
               'Canada.tif', 'Eurafrica leste.tif', 'Russia Central.tif', 'Sudeste Asia.tif']

intensidades_normalizadas = []

for path in image_paths:
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    _, image_binary = cv2.threshold(image, 127, 1, cv2.THRESH_BINARY)
    soma_intensidade = np.sum(image_binary)
    intensidade_normalizada = soma_intensidade / image_binary.size
    intensidades_normalizadas.append(intensidade_normalizada)

total_intensidade_normalizada = sum(intensidades_normalizadas)

for i, intensidade in enumerate(intensidades_normalizadas):
    percentual = (intensidade / total_intensidade_normalizada) * 100
    image_name = image_paths[i].replace('.tif', '')
    print(f'{image_name}: {percentual:.2f}% do consumo de energia total')