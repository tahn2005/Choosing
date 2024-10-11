import numpy as np
import matplotlib.pyplot as plt

def choose(a, b):
    num = 1
    if b == 0 or a == b:
        return 1
    for i in range(a, a - b, -1):
        num *= i
    den = 1
    for i in range(1, b + 1):
        den *= i
    return num // den

def main():
    committee = [0.0] * 6
    for i in range(6):
        EE = choose(12, i)
        CS = choose(8, 5 - i)
        committee[i] = (EE * CS) / choose(20, 5)

    return committee

if __name__ == "__main__":
    result = main()
    
    for time, value in enumerate(result):
        print(f"f({time}) = {value:.4f}")

    time_values = np.arange(len(result))  
    plt.plot(time_values, result, marker='o', label='P(Cx)', color='blue')

    plt.xlabel('x')
    plt.ylabel('P(Cx)')
    plt.title('EE & CS Committee')
    plt.axhline(0, color='black', linewidth=0.5, ls='--') 
    plt.axvline(0, color='black', linewidth=0.5, ls='--')  
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()

    
    plt.show()
