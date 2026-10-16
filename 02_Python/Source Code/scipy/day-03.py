# from scipy import optimize
# import numpy as np
# from scipy.optimize import curve_fit
# import matplotlib.pyplot as plt
# from scipy.optimize import linprog
# from scipy.interpolate import interp1d, CubicSpline


# # def f(x):
# #     return (x - 3)**2 + 5

# # def rosenbrock(params):
# #     x, y = params
# #     return (1-x)**2 + 100*(y - x**2)**2

# # result = optimize.minimize(f, x0=0)
# # print(result.x)
# # print(result.fun)
# # print(result.success)

# # result = optimize.minimize(rosenbrock, x0=[0,0])
# # print(result.x)

# # result = optimize.minimize(f, x0=0, bounds=[(-10,1)])
# # print(result.x)

# # result = optimize.minimize(rosenbrock, x0=[0,0], method='Nelder-Mead')




# # def exp_decay(x, a, b, c):
# #     return a * np.exp(-b * x) + c

# # np.random.seed(0)
# # x_data = np.linspace(0, 4, 50)
# # y_data = exp_decay(x_data, 2.5, 1.3, 0.5) + np.random.normal(0, 0.2, 50)

# # popt, pcov = curve_fit(exp_decay, x_data, y_data, p0=[1,1,1])
# # a_fit, b_fit, c_fit = popt
# # print(f"Fitted: a={a_fit:.2f}, b={b_fit:.2f}, c={c_fit:.2f}")

# # perr = np.sqrt(np.diag(pcov))
# # print(f"Uncertainty: ±{perr}")

# # plt.scatter(x_data, y_data, alpha=0.6, label='Data')
# # plt.plot(x_data, exp_decay(x_data, *popt), 'r-', linewidth=2, label='Fitted curve')
# # plt.legend()
# # plt.show()

# # def g(x):
# #     return x**3 - x - 2

# # def supply_minus_demand(price):
# #     supply = 50 * price - 100
# #     demand = 500 - 30 * price
# #     return supply - demand

# # result = optimize.root(g, x0=1)
# # print(result.x)
      
# # root_value = optimize.brentq(g, a=1, b=2)
# # print(root_value)

# # equilibrium_price = optimize.brentq(supply_minus_demand, a=0, b=50)
# # print(f"Equilibrium price: {equilibrium_price:.2f}")

# # c = [-3, -5]
# # A_ub = [[1,0], [0,2], [3,2]]
# # b_ub = [4, 12, 18]

# # result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(0,None), (0,None)])

# # print(f"Optimal units — Product A: {result.x[0]:.1f}, Product B: {result.x[1]:.1f}")
# # print(f"Maximum profit: {-result.fun:.2f}")

# hours = np.array([0, 4, 8, 12, 16, 20, 24])
# temps = np.array([15, 13, 18, 25, 23, 18, 15])

# linear_interp = interp1d(hours, temps, kind='linear')
# print(linear_interp(10))

# cubic_interp = interp1d(hours, temps, kind='cubic')
# print(cubic_interp(10))

# spline = CubicSpline(hours, temps)
# fine_hours = np.linspace(0, 24, 200)
# smooth_temps = spline(fine_hours)

# plt.scatter(hours, temps, color='black', zorder=5, label='Measured')
# plt.plot(fine_hours, linear_interp(fine_hours), '--', label='Linear')
# plt.plot(fine_hours, smooth_temps, label='Cubic Spline')
# plt.legend()
# plt.show()

# safe_interp = interp1d(hours, temps, kind='linear', fill_value='extrapolate')

from scipy.optimize import linprog, minimize, curve_fit, brentq
from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt

def calibration_curve(V, L, k, V0):
    return L / (1 + np.exp(-k * (V - V0)))

np.random.seed(4)
voltage = np.linspace(0, 10, 40)
true_pressure = calibration_curve(voltage, 100, 1.2, 5)
measured_pressure = true_pressure + np.random.normal(0, 3, len(voltage))

c = [-40, -90]
A_ub = [[4,8], [3,2], [1,0]]
b_ub = [400, 180, 80]

result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(0,None),(0,None)])
print(f"Chairs: {result.x[0]:.1f}, Tables: {result.x[1]:.1f}")
print(f"Max profit: ₹{-result.fun:.2f}")

popt, pcov = curve_fit(calibration_curve, voltage, measured_pressure, p0=[100,1,5])
print(f"Fitted: L={popt[0]:.1f}, k={popt[1]:.2f}, V0={popt[2]:.2f}")

logged_hours = np.array([0,3,6,9,12,15,18,21,24])
logged_temps = np.array([12,10,14,22,27,26,21,15,12])

spline = CubicSpline(logged_hours, logged_temps)
all_hours = np.arange(0, 24.5, 0.5)
interpolated_temps = spline(all_hours)
