import folium # Biblioteca para criar mapas
import numpy as np # Biblioteca é para importar os dados de entrada
from folium.plugins import HeatMap
from folium.plugins import MiniMap

# Dados de entrada
dados = np.genfromtxt("cidades_visitadas.csv", delimiter = ",") # Trabalhando com um arquivo CSV, o delimitador é a vírgula

# Mapa
escala_de_cores = {0.2:"#A149FA" ,
                  0.4:"#3B44F6",
                  0.6:"#3EC70B",
                  1:"#F7EC09"} 
                  # 0.2 = até 20% a cor é #A149FA
                  # 0.4 = até 40% a cor é #3B44F6
                  # 0.6 = até 60% a cor é #3EC70B
                  # 1 = até 100% a cor é #F7EC09

mapa = folium.Map([51.2211179,4.443809068], zoom_start = 6, tiles = "OpenStreetMap") # o Primeiro argumento é o ponto central do mapa. O segundo é Zoom inicial. O terceiro é o tipo de background 

HeatMap(dados, gradient=escala_de_cores).add_to(mapa) # Cria um mapa de calor com base nos dados fornecidos

MiniMap(tile_layer="OpenStreetMap", position = "topright", toggle_display = True, zoom_level_fixed = 1).add_to(mapa) # Adiciona um minimapa no canto superior direito do mapa principal

mapa # Imprime o mapa


# ------------------------------------------

# + HeatMap(dados, gradient=escala_de_cores):

#   - Cria um mapa de calor com base nos dados fornecidos.
#   - dados: São as coordenadas de latitude, longitude e a intensidade do ponto.
#   - gradient=escala_de_cores: Define uma escala de cores para o mapa de calor com base na intensidade dos pontos. A variável escala_de_cores é um dicionário que associa diferentes intervalos de intensidade a cores específicas.

# + .add_to(mapa): Adiciona o mapa de calor criado à instância do mapa principal (mapa).

# + MiniMap(tile_layer="cartodbpositron", position="topright", toggle_display=True, zoom_level_fixed=1):

#   - Cria um minimapa que exibe uma visão geral do mapa principal.
#   - tile_layer="cartodbpositron": Define o estilo do mapa base para o minimapa.
#   - position="topright": Posiciona o minimapa no canto superior direito do mapa principal.
#   - toggle_display=True: Permite alternar a exibição do minimapa.
#   - zoom_level_fixed=1: Fixa o nível de zoom do minimapa em 1, o que significa que ele manterá um zoom constante.

# + .add_to(mapa): Adiciona o minimapa à instância do mapa principal (mapa).