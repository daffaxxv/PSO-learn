import numpy as np
import matplotlib.pyplot as plt

def optimize(yd, time,swarm_size = np.array([3,100]), bound = np.array([0,1]), c1 = float(2), c2 = float(2), vel_init = float(.1), weight = float(.5), etol = float(1e-3), maxiter = 200, show_fig = True):
    # particle is the amount of unknown variable that wanted to estimate
    # swarm is the amount of total particle
    yd = np.tile(yd,(swarm_size[1],1)).T
    # initialization for first iter
    lb = bound[0]
    ub = bound[1]
    swarmpart = np.random.uniform(low = lb, high = ub, size = swarm_size)
    swarmvel = np.ones(swarm_size)*vel_init
    tot_cost = []
    # first cost fun
    for i in range(maxiter):
        yi = myfun(swarmpart,time)
        cost = np.sqrt(np.sum((yd-yi)**2,axis = 0)/len(time)) #change which one is fit with the case
        current_best = np.amin(cost)
        tot_cost.append(cost)
        if i == 0:
            best_cost = current_best
            best_particle = cost
            x_best = swarmpart
            gbest = np.tile(swarmpart[:,np.where(cost == best_cost)[0][0]],(swarm_size[1],1)).T 
        else:
            if current_best < best_cost:
                best_cost = current_best
                gbest = np.tile(swarmpart[:,np.where(cost == best_cost)[0][0]],(swarm_size[1],1)).T 
            for j in range(swarm_size[1]):
                if cost[j] < best_particle[j]:
                    best_particle [j] = cost[j]
                    x_best[:,j] = swarmpart[:,j]

        swarmvel = weight*swarmvel + c1*(np.random.rand())*(x_best-swarmpart) + c2*(np.random.rand())*(gbest-swarmpart)
        swarmpart = swarmpart + swarmvel
    
    if show_fig == True:
        y = myfun(swarmpart, time)
        figure = plt.figure(figsize = (6,4), dpi = 200)
        plt.plot(yd[:,0], label = 'target')
        plt.plot(np.array(y)[:,0], label = 'estimation')
        plt.grid(alpha = .5)
        plt.title('Comparison between target and estimation')
        plt.legend(loc = 'upper center')
        plt.xlabel('$x$')
        plt.ylabel('$f(x)$')

        figure = plt.figure(figsize = (6,4), dpi = 200)
        plt.scatter(np.tile(np.arange(len(tot_cost)),(len(tot_cost[0]),1)).T,tot_cost, s=1)
        plt.grid(alpha = .5)
        plt.title('Cost for each iter')
        plt.xlabel('$iter$')
        plt.ylabel('$RMSE$')
    
    return swarmpart[:,0]

def myfun(particle , time):
    y=[]
    for t in time:
        y.append(np.array(particle[0]*t**2+particle[1]*t+particle[2]).T)

    return y