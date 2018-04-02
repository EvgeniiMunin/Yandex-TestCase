def ttest_ind_cust(a, b):
    a = np.array(a)
    b = np.array(b)
    
    # degrees of freedom
    df = len(a) + len(b) - 2
    
    # standard deviation
    s = sqrt((a.std(ddof=1)**2*(len(a) - 1) + b.std(ddof=1)**2*(len(b) - 1)) / df)
    
    # t-statistic
    t = (a.mean() - b.mean()) / (s * np.sqrt(1/len(a) + 1/len(b)))
    
    # two-tail p-value
    p = 2*(1 - sts.t.cdf(t, df=df))
    
    return t, p