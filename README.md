# PSO-learn
This is the best step where you can learn Particle Swarm Optimization (PSO) in python

## Files Inside
### 1. pso.py
- (optimize) The basis of PSO computation with RMSE as the cost function
  ```
  Input argument:
  - yd: Desired time series signal (1D)
  - swarm_size: size of swarm [vars, populations] (ND.Array)
  - bound: random number boundaries for swarm-population generation [lower bound, upper bound] (ND.Array)
  - vel_init: initiation coeff. of swarm velocity
  - c1, c2, weight: coefficient of swarm velocity update
  - maxiter: maximum iteration of optimization
  - etol: minimum estimation error (optimization termination parameter)
  - func: choosing the estimation function equation (string; 'linear', 'quadratic', 'cubic', 'fourier')
  - cost_fun: choosing the cost function (string; 'RMSE', 'MSE', 'MAE')
  - show_fig: showing estimation figure and iteration cost (boolean)
  ```
- (myfun) The function to estimate the true value using similar function (you can add manually)
  ```
  Estimation function:
  - linear (could be used as linear regression)(use swarm_size: [2,pop])
  - quadratic (use swarm_size: [3,pop])
  - cubic (use swarm_size: [4,pop])
  - fourier series (could be used for periodic signal)(be aware of swarm_size; [5,pop]: up to 2nd order, [7,pop]: up to 3rd order, and so on)
  ```
- (cost_cal) cost function that is used as the optimization parameter
  ```
  Cost function:
  - RMSE = Root Mean Squared Error
  - MSE = Mean Squared Error
  - MAE = Mean Absolute Error
  ```
### 2. pso_learning.ipynb
- Allows you to change the input, but don't forget to change the 'myfun' in pso.py to fit with your 'y' and use the most fitted cost_fun for your case

## Dependencies
- matplotlib
- numpy

