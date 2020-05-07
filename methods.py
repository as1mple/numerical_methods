class Calculation:
    def __init__(self, function):
        self.function = function

    def newton(self, Df, x0, epsilon, max_iter):
        """Approximate solution of f(x)=0 by Newton's method.

        Parameters
        ----------
        Function for which we are searching for a solution f(x)=0.
        Df : function
            Derivative of f(x).
        x0 : number
            Initial guess for a solution f(x)=0.
        epsilon : number
            Stopping criteria is abs(f(x)) < epsilon.
        max_iter : integer
            Maximum number of iterations of Newton's method.
        """
        xn = x0
        for n in range(0, max_iter):
            fxn = self.function(xn)
            if abs(fxn) < epsilon:
                print('Found solution after', n, 'iterations.')
                return xn
            Dfxn = Df(xn)
            if Dfxn == 0:
                print('Zero derivative. No solution found.')
                return None
            xn = xn - fxn / Dfxn
        print('Exceeded maximum iterations. No solution found.')
        return None

    def secant(self, a, b, N):
        """Approximate solution of f(x)=0 on interval [a,b] by the secant method.

        Parameters
        ----------
            The function for which we are trying to approximate a solution f(x)=0.
        a,b : numbers
            The interval in which to search for a solution. The function returns
            None if f(a)*f(b) >= 0 since a solution is not guaranteed.
        N : (positive) integer
            The number of iterations to implement.
        ----------
        """

        if self.function(a) * self.function(b) >= 0:
            print("Secant method fails.")
            return None
        a_n = a
        b_n = b
        for n in range(1, N + 1):
            m_n = a_n - self.function(a_n) * (b_n - a_n) / (self.function(b_n) - self.function(a_n))
            f_m_n = self.function(m_n)
            if self.function(a_n) * f_m_n < 0:
                a_n = a_n
                b_n = m_n
            elif self.function(b_n) * f_m_n < 0:
                a_n = m_n
                b_n = b_n
            elif f_m_n == 0:
                print("Found exact solution.")
                return m_n
            else:
                print("Secant method fails.")
                return None
        return a_n - self.function(a_n) * (b_n - a_n) / (self.function(b_n) - self.function(a_n))

    def chord(self, x_prev, x_curr, e):
        x_next = 0

        flag = True
        while flag:
            tmp = x_next
            x_next = x_curr - self.function(x_curr) * (x_prev - x_curr) / (
                    self.function(x_prev) - self.function(x_curr))
            x_prev = x_curr
            x_curr = tmp
            flag = abs(x_next - x_curr) > e
        return x_next
