def Pr_d(k: int, m: int, n: int) -> float:
    
    N = k + m + n
    
    return format(1 - (n/N * (n-1)/(N-1) + 0.25 * m/N * (m-1)/(N-1) + n/N * m/(N-1) * 0.5 + m/N * n/(N-1) * 0.5), ".5f")
    
    
    
print(Pr_d(25,16,29))
