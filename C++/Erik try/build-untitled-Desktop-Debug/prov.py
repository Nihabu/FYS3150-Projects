# -*- coding: utf-8 -*-
#AST1100 Hjemmeeksamen uke 1
#Oppg 1A.6
import random
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


number = 1  #Seeding-nummer
random.seed(number)

#Vekt satelitt:
m_sat = 1000      #kg
#Temperatur gass:
T = 10000             #Kelvin
#Boks lengde:
L = 10E-6          #meter
#Antall partikler i boksen:
N = int(50)
#Masse til gasspartikkel(hydrogen):
m = 1.67E-27     #kg
#Boltzmanns konstant:
k = 1.38064852E-23    #m^2*kg*s^-2*K^-1
#Gjennomsnittlig kinetisk energi analytisk:
K_anal = 1.5*k*T
#Abs av gjennomsnittlig hastighet analytisk:
v_mean_anal = np.sqrt(k*T/(m*np.pi))
#Standardavvik
sigma = np.sqrt((k*T/m))
#Gjennomsnittshastighet:
mean = 0
end_time = 10E-9
n = 1000
dt = end_time/float(n)
print dt
#dt = 1E-18
time = np.linspace(0, end_time, n)
position = np.zeros((N, 3, n))
velocity = np.zeros((N, 3, n))
v_sum = 0
#lokke som henter init hatighet og posisjon:
for i in xrange(N):
    for j in xrange(3):
        v = random.gauss(mean, sigma)
        velocity[i][j][0] = v
        x = random.uniform(0, L)
        position[i][j][0] = x
        print x

    v_len = np.linalg.norm(velocity[i])
    v_sum += v_len
    v_mean = v_sum/float(N)

for i in xrange(n-1):
    velocity[:, :, i+1] = velocity[:, :, i]
    for j in xrange(N):
        for k in xrange(3):
            position[j, k, i+1] = position[j, k, i] + dt*velocity[j, k, i+1]
        
            if position[j, k, i+1] < 0:
                velocity[j, k, i+1] = - velocity[j, k, i]
                position[j, k, i+1] = position[j, k, i] + dt*velocity[j, k, i+1]
            elif position[j, k, i+1] > L:
                velocity[j, k, i+1] = - velocity[j, k, i]
                position[j, k, i+1] = position[j, k, i] + dt*velocity[j, k, i+1]
K_num = 0.5*m*v_mean**2



print K_num
print K_anal



def plot():
    def update_lines(num, dataLines, lines) :
        for line, data in zip(lines, dataLines) :
            line.set_data(data[0:2, num-1:num])
            line.set_3d_properties(data[2,num-1:num])
        return lines

    # Attach 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    m = 100
     # number of particles you want to animate
    # the code demands a vector in shape (n, 3 N), 
    # where n is number of particles and N are number 
    # of iterations.
    # if your arrays are not in this shape, use 
    # pos = np.reshape(pos(n, 3, N))
    system = position # this is the positions of the particles
    # to be animated. In this code it comes in and array 
    # with configuration (n, 3, N) where N is the number 
    # of iterations.
    # creates animation data for all your different 
    # particles
    data = [i for i in range(N)]
    lines = [i for i in range(N)]
    for i in range(N):
        data[i] = [system[i]]
        lines[i] = [ax.plot(data[i][0][0,0:1], 
        data[i][0][1,0:1], data[i][0][2,0:1], 'o')[0]]

    # Set the axes properties
    ax.set_xlim3d([0.0, L])
    ax.set_xlabel('X')

    ax.set_ylim3d([0.0, L])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, L])
    ax.set_zlabel('Z')

    ax.set_title('3D Test')

    # Creating the Animation object
    ani = [i for i in range(N)] 
    for i in range(N):
        ani[i] = animation.FuncAnimation(fig, 
        update_lines, m, fargs=(data[i], lines[i]),
        interval=50, blit=False)
    plt.show()
    
plot()
            
