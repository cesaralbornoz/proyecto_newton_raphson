import math

def derivada(f, h = 0.02):

    def _(x):
        return (f(x + h) - f(x))/h

    return _

def newton_raphson(f, x, ER, N):
    i=0
    er=100
    xx=x
    d=derivada(f)
    while (i<N) and (er>ER):
        xxx=xx-(f(xx)/d(xx))
        er= abs((xxx-xx)/xxx)
        xx=xxx
        print ("Iteracion:",i, "Error:", er, "Raiz:", xx)
        i=i+1
    return xx



if __name__ == "__main__":
    # Pruebe aquí su función.
    f=lambda x:math.sin(x)-(math.e**-x)
    newton_raphson(f,3.5,0.05,100)
    pass 
