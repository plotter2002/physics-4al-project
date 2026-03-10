import numpy as np 
import matplotlib.pyplot as plt
cardboard =np.loadtxt('cardboard1.txt', delimiter=',')
plastic= np.loadtxt('plastic1.txt', delimiter=',')
sandpaper= np.loadtxt('sandpaper1.txt', delimiter=',')

# numpy has a function that helps to read data files so we import it

# Read in data using np.loadtxt. It takes in two inputs, the path to the file and a delimiter. The delimiter in this case is ';'.

# This dataset has two columns
# The zeroth column is the x axis, and the first column is y axis
# Take all of the elements in the 0th column to create your x-axis array
time_millis = cardboard[:,0]
# The x_axis data is the elapsed time in milliseconds

# Take all of the elements in the 1st column to create your y-axis array
dist_cm = cardboard[:,1]
# The y_axis data is the distance in cm.
time_s = time_millis/1000

dist_m=dist_cm/100
plt.scatter(time_s,dist_m)

# Add axes labels
# Create a variable that starts from 0 and ends at the size of the array
array_index=np.arange(0,len(dist_m))
print(array_index)
# Plot the distance vs array index
 # plt.scatter(array_index, dist_m)

# Add axes labels




lower_index = 0
lower_time_limit = time_millis[lower_index]
print('The lower time cutoff is ' + str(lower_time_limit))


upper_index = 100
upper_time_limit = time_millis[upper_index]
print('The upper time cutoff is ' + str(upper_time_limit))

# Create new arrays for the time window and distance window that we care about
time_window = time_s[lower_index:upper_index]
dist_window = dist_m[lower_index:upper_index]

plt.plot(time_window, dist_window)

# Add axes labels



plt.plot(time_window, dist_window)
coeff_quad = np.polyfit(time_window, dist_window, 2)
y_fit=coeff_quad[0]*time_window**2+coeff_quad[1]*time_window+coeff_quad[2]

plt.plot(time_window,y_fit, label = 'Model')
plt.scatter(time_window, dist_window, label = 'Data')
plt.legend()
coeff_quad, cov_quad = np.polyfit(time_window, dist_window, 2, cov=True)

# Error in quadratic coefficient
quad_err = np.sqrt(cov_quad[0,0])
# Your x and y axes labels here
plt.xlabel("Time in milliseconds")
plt.ylabel("Distance in meters")
plt.title("Position vs time ultrasonic sensor")
plt.show()
print(quad_err)
#Title 
angle_rad = np.arcsin(2*coeff_quad[0]/-9.8)
# Convert the angle to degrees
angle_deg = angle_rad*180/np.pi

print(angle_deg, "degrees")
# Error in angle

# Recall quad_err is the error in "a"
# The formula is taken from the slides of lab 2A
angle_err_rad = (2/9.8)*(quad_err)/(np.sqrt(1-(2*coeff_quad[0]/9.8)**2))

# Convert to degrees
angle_err_deg = angle_err_rad*180/np.pi

print(angle_err_deg)
print(coeff_quad[0], " m/s^2")
print(quad_err)


