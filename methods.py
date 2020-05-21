class Calculation:
    """Approximate solution of f(x)=0 by Newton's, secant and chord methods.

       Parameters
       ----------
       f : function
           Function for which we are searching for a solution f(x)=0.
       Df : function
           Derivative of f(x).
       x0, x1 : number
           The interval in which to search for a solution.
       epsilon : number
           Stopping criteria is abs(f(x)) < epsilon.
       -------
       """

    def __init__(self, function):
        self.function = function

    def newton(self, Df, x0: complex or float or int, epsilon: float or int) -> complex or None:
        xn = x0
        flag = True
        count = 0
        while flag:
            fxn = self.function(xn)
            count += 1
            if abs(fxn) < epsilon:
                print('Found solution after', count, 'iterations.')
                return xn
            Dfxn = Df(xn)
            if Dfxn == 0:
                print('Zero derivative.')
                return None
            xn = xn - fxn / Dfxn

    def secant(self, x0: complex or float or int, x1: complex or float or int,
               epsilon: float or int) -> complex or None:
        count = 0
        while abs(x1 - x0) > epsilon:
            tmp = x1
            try:
                x1 = x1 - (x1 - x0) * self.function(x1) / (self.function(x1) - self.function(x0))
            except ZeroDivisionError as e:
                print(e)
                return None
            x0 = tmp
            count += 1

        print('Found solution after', count, 'iterations.')
        return x1

    def chord(self, x0: float or int, x1: float or int, epsilon: float or int) -> complex or None:
        iteration = 0
        while True:
            try:
                xn = x0 - self.function(x0) * (x1 - x0) / (self.function(x1) - self.function(x0))
            except ZeroDivisionError as e:
                print(e)
                return None

            fxn = self.function(xn)
            iteration += 1
            if abs(fxn) <= epsilon:
                print(f'Found solution after {iteration} iterations.')
                return xn
            elif self.function(x0).real * fxn.real < 0:
                x0 = x0
                x1 = xn
            elif self.function(x1).real * fxn.real < 0:
                x0 = xn
                x1 = x1
            elif fxn == 0:
                print(f"Found exact solution after {iteration} iterations")
                return xn
            else:
                print("Chord method fails.")
                return None
