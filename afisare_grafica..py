
from matplotlib.pyplot import *

import contorizare_persoane_none
import contorizare_persoane_light
import contorizare_persoane_extreme
import contorizare_persoame_heavy
import contorizare_persoane_moderate

# valorile pentru axa x
activity_level = ['none', 'light', 'moderate', 'heavy', 'extreme']

# valorile pentru axa y (numarul de persoane)
persoane_none = contorizare_persoane_none.search_none_word('none')
persoane_light = contorizare_persoane_light.search_light_word('light')
persoane_moderate = contorizare_persoane_moderate.search_moderate_word('moderate')
persoane_heavy = contorizare_persoame_heavy.search_heavy_word('heavy')
persoane_extreme = contorizare_persoane_extreme.search_extreme_word('extreme')

persoane = [persoane_none, persoane_light, persoane_moderate, persoane_heavy, persoane_extreme]

# reprezentare grafic
bar(activity_level, persoane, color = 'green', width=0.5)

# elemente grafic
xlabel('Activity level')
ylabel('Nr. persoane')
title('Grafic pentru monitorizarea activitatii')
show()
