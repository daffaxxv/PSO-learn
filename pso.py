import numpy as np
import matplotlib.pyplot as plt

def optimize(yd, time,swarm_size = np.array([3,100]), bound = np.array([-1,1]), vel_init = float(.1), c = np.array([float(2), float(2)]), weight = float(.5), etol = float(1e-3), maxiter = 200, func = 'quadratic', cost_fun = 'RMSE', show_fig = True):
    c1, c2 = c
    x_best = gbest = np.zeros(shape=swarm_size)
    if func == 'linear':
        print('Please make the swarm_size = [2,n]')
    elif func == 'quadratic':
        print('Please make the swarm_size = [3,n]')
    elif func == 'cubic':
        print('Please make the swarm_size = [4,n]')
    elif func == 'fourier':
        print('Please make the swarm_size = [odd number (not 1),n]')

    yd = np.tile(yd,(swarm_size[1],1)).T
    # particle is the amount of unknown variable that wanted to estimate
    # swarm is the amount of total particle
    # initialization for first iter
    lb = bound[0]
    ub = bound[1]
    swarmpart = np.random.uniform(low = lb, high = ub, size = swarm_size)
    swarmvel = np.ones(swarm_size)*vel_init
    tot_cost = []

    for i in range(maxiter):
        yi = myfun(swarmpart,time,func=func)
        cost = cost_cal(yd, yi, cost_fun = cost_fun)
        current_best = np.amin(cost)
        tot_cost.append(cost)

        if current_best > etol:

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
        y = myfun(swarmpart, time, func = func)
        figure = plt.figure(figsize = (4,2), dpi = 200)
        plt.plot(time, yd[:,0], linewidth = '.8')
        plt.plot(time, np.array(y)[:,0], linestyle = 'dashed', alpha = .7, color = 'red', linewidth = '.8')
        plt.grid(alpha = .5)
        plt.title('Comparison between target and estimation')
        plt.legend(['target', 'estimation'], loc = 'upper center', fontsize = 8, ncol = 2)
        plt.xlabel('$x$')
        plt.ylabel('$f(x)$')

        figure = plt.figure(figsize = (4,2), dpi = 200)
        plt.scatter(np.tile(np.arange(len(tot_cost)),(len(tot_cost[0]),1)).T,tot_cost, s=.5)
        plt.grid(alpha = .5)
        plt.title('Cost for each iter')
        plt.xlabel('$iter$')
        plt.ylabel('$cost$')
    
    return swarmpart[:,0]

def myfun(particle, time, func):
    y=[]
    if func == 'linear':
        for t in time:
            y.append(np.array(particle[0]*t*+particle[1]).T)
    elif func == 'quadratic':
        for t in time:
            y.append(np.array(particle[0]*t**2+particle[1]*t+particle[2]).T)
    elif func == 'cubic':
        for t in time:
            y.append(np.array(particle[0]*t**3+particle[1]*t**2+particle[2]*t+particle[3]).T)
    elif func == 'fourier':
        for t in time:
            temp = particle[0]
            n_count = int((particle.shape[0]-1)/2)
            for n in range(1,n_count+1):
                temp = temp + particle[n]*np.sin(n*t) + particle[n+n_count]*np.cos((n+n_count)*t)
            y.append(np.array(temp).T)

    return y

def cost_cal(yd, yi, cost_fun):
    n = len(yd[0])
    if cost_fun == 'RMSE':
        cost = np.sqrt(np.sum((yd-yi)**2, axis = 0)/n)
    elif cost_fun == 'MSE':
        cost = np.sum((yd-yi)**2, axis = 0)/n
    elif cost_fun == 'MAE':
        cost = np.sum(np.abs(yd-yi),axis = 0)/n
    return cost

