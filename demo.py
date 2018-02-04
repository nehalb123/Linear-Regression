from numpy import *

def error_func(c,m,points):
    totalerror=0
    for i in range(0,len(points)):
        x=points[i,0]
        y=points[i,1]
        totalerror+=(y-(m*x+c))**2
    return totalerror/float(len(points))

def step_gradient(c_current,m_current,points,alpha):
    #gradient descent
    c_gradient=0
    m_gradient=0
    N = float(len(points))
    for i in range(0,len(points)):
        x=points[i,0]
        y=points[i,1]
        c_gradient+= -(2/N)*(y-((m_current*x)+ c_current))
        m_gradient+= -(2/N)*x*(y-((m_current*x)+ c_current))
    new_c = c_current-(alpha*c_gradient)
    new_m = m_current-(alpha*m_gradient)
    return [new_c,new_m]

def gradient_descent_wrapper(points,initial_c,initial_m,alpha,iterations):
    c=initial_c
    m=initial_m

    for i in range(iterations):
        c,m = step_gradient(c,m,array(points),alpha)
    return [c,m]
def main():
  points=genfromtxt('data.csv',delimiter=',')
  #hyperparameters
  alpha = 0.0001  #learning rate
  #y=mx+c
  initial_c=0
  initial_m=0
  iterations=1000
  print "Starting gradient descent at c = {0}, m = {1}, error = {2}".format(initial_c, initial_m, error_func(initial_c, initial_m, points))
  print "Running..."
  [c,m]=gradient_descent_wrapper(points,initial_c,initial_m,alpha,iterations)
  print "After {0} iterations c = {1}, m = {2}, error = {3}".format(iterations, c, m, error_func(c, m, points))



if __name__ == "__main__":
  main()