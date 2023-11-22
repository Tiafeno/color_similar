# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import math
from Services.colors import get_colors
from airium import Airium

def rgb_distance(color1, color2):
    # Convertir les codes couleurs en valeurs RGB
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)

    # Calculer la distance euclidienne
    distance = math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)
    return distance


def group_colors_by_reference(reference_colors, color_list, similarity_threshold):
    grouped_colors = {ref_color: [] for ref_color in reference_colors}
    used_colors = set()

    # Assigner chaque couleur à un groupe en fonction de la similarité
    for color in color_list:
        closest_ref_color = min(reference_colors, key=lambda ref_color: rgb_distance(ref_color, color))

        # Vérifier la similarité et l'absence de répétition de couleur dans la liste groupée
        if (
            rgb_distance(closest_ref_color, color) < similarity_threshold
            and color not in used_colors
        ):
            grouped_colors[closest_ref_color].append(color)
            used_colors.add(color)

    return grouped_colors


def similar_colors(reference_color, color_list, similarity_threshold):
    # Filtrer les couleurs similaires en fonction du seuil de similarité
    similar_colors_list = [color for color in color_list if rgb_distance(reference_color, color) < similarity_threshold]
    return similar_colors_list


if __name__ == '__main__':
    a = Airium()
    reference_colors = [
        "#CC8723",
        "#0EEA76",
        "#D51D25",
        "#1956D8",
        "#D570B3",
        "#0B4725",
        "#E424CF",
        "#EFEFF2",
        "#EEEB1D",
        "#81C3CA",
        "#D6C98E",
        "#251677",
        "#D9A4C2",
        "#19B8D7",
        "#CFDABA",
        "#BEE3DC",
    ]

    color_list = []
    similarity_threshold = 70  # Ajustez ce seuil selon vos besoins
    for attribute in get_colors(): # Récuperer la liste des couleurs dans la base de donnée
        if len(attribute.value[1:]) == 6:
            color_list.append(attribute.value)

    a('<!DOCTYPE html>')
    with a.html(lang="en"):
        with a.head():
            a.meta(charset="utf-8")
            a.title(_t="Color Similar")
        with a.body():
            with a.div(kclass="all_color", style="margin-bottom: 4em"):
                for attr_color in color_list:
                    a.div(
                        style="background-color: %s; height: 40px; margin-right: 5px; display:inline-block" % (
                            attr_color),
                        _t=attr_color)
            with a.div(kclass='main_header'):
                with a.div(kclass='color', style="margin-bottom: 2em"):

                    grouped_colors = group_colors_by_reference(reference_colors, color_list, similarity_threshold)
                    for ref_color, colors in grouped_colors.items():
                        with a.div(style="padding-bottom: .5em"):
                            a.div(style="background-color: %s; width: 50px; height: 50px; border: 1px solid" % (
                                ref_color), _t="")
                            for color in colors:
                                a.div(style="background-color: %s;  height: 40px; display:inline-block" % (color),
                                      _t=color)

    # Casting the file to a string to extract the value
    html = str(a)
    with open('color_similar.html', 'wb') as f:
        f.write(bytes(html, encoding='utf8'))
        f.close()
