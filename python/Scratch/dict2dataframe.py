# -*- coding: utf-8 -*-

import pandas as pd
from Sensors import GPS_VK172 as vk

dd = pd.DataFrame(columns=vk.format_GPGLL())
for i in range(10):
    d = vk.get_position()
    # fill dict d with keys for data fields and cooresponding data
    dd = dd.append(d, ignore_index=True)


print(dd)
