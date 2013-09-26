# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 18:00:44 2013

@author: NotMark
"""

import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos

theta = np.linspace(0, pi, 500)
r_sin = [sin(3*t) for t in theta]
r_cos = [cos(t) for t in theta]

dr_sin = np.diff(r_sin).tolist()
dr_cos = np.diff(r_cos).tolist()

dr_sin.append(0)
dr_cos.append(0)



ax = plt.subplot(211, polar=True)
ax2 = plt.subplot(212, polar=False)

ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.spines['bottom'].set_position(('data', 0))

ax.plot(theta, r_cos)

plt.xticks([0, pi/4.0, pi/2.0, 3.0*pi/4.0, pi],
           [r'$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/2$', r'$\pi$'])
ax2.plot(theta, r_cos)

ax.grid(True)
ax2.grid(True)

plt.show()