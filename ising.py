import numpy.random as rand
import matplotlib.pyplot as plt

import numpy as np

def init_lattice(lattice_size):
    return np.ones((lattice_size,lattice_size))

init_lattice(50)


#get neighbor list
def neighborlist(x,y, lattice_size, lattice):
    right= ((x+1)%lattice_size, y)
    left=   ((x-1),y)
    top =   (x,(y-1))
    down=   (x,(y+1) % lattice_size)
    
    return [lattice[right[0],right[1]], lattice[left[0],left[1]], lattice[top[0],top[1]], lattice[down[0], down[1]]]



#used to calculate total energy
def tot_ener(lattice, lattice_size):
    energy=0
    for i in range(lattice_size):
        for j in range(lattice_size):
            s=lattice[i,j]
            neibr= np.sum(neighborlist(i,j,lattice_size, lattice))
            energy += -1*neibr*s
            
    return energy
    

def montecarlostep(lattice,beta):
    energy1 =tot_ener(lattice, lattice_size)
    for i in range(len(lattice)):
        for j in range(len(lattice)):
            a=np.random.randint(0,len(lattice))
            b=np.random.randint(0, len(lattice))
            lattice[a,b]=1-lattice[a,b]
            energy2=tot_ener(lattice, lattice_size)
            diff= energy2-energy1
            if diff<0:
                lattice[a,b]= lattice[a,b]
            elif np.random.uniform(0,1)< np.exp(-beta* diff):
                lattice[a,b]=lattice[a,b]
            elif np.random.uniform(0,1)>np.exp(-beta* diff):
                lattice[a,b]=1-lattice[a,b]
                

    

#mainbody function
lattice_size=50
lattice = init_lattice(lattice_size)   #make lattice

nsweep=5000
temp=2

step_energy=[]

#montecarlo evolution of the initial lattice
for i in range(nsweep):
    montecarlostep(lattice,1/temp)
    step_energy.append(tot_ener(lattice,lattice_size))

plt.plot(step_energy)
plt.show()
