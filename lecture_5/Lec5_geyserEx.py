# Lecture 5: Snuffler exercise functions 
# 
# author: Eva Eibl eva.eibl@uni-potsdam.de
# SS 2019: Module MGPW02
# 16.5.2019
# -----------------------------
import Lec5_geyserEx_functions as h
import matplotlib.pyplot as plt
julianday, evclass = h.read_snuffler_marker ('markers.txt', length=0)
julianday= np.sort (julianday)
plt.plot (julianday)
plt.show ()

# -- import the snuffler marker file, time in julian days --
h.read_snuffler_marker


# -- calculate the waiting time after eruption/ duration of bursts in minutes --  



# -- calculate mean time --



# -- plot waiting time after eruptions/ duration of bursts vs. time --
plot


# -- plot histogram of the intereruption times (1 h bins) -- 
hist













