from sklearn.linear_model import LinearRegression
def get_linear_fit(x_series,y_series):
    x = x_series.values.reshape(-1,1)
    y = y_series.values.reshape(-1,1)
    print(f'\tthere are {x.shape} points')
    lr = LinearRegression()
    lr = lr.fit(x, y)
    
    m = lr.coef_[0][0]
    c = lr.intercept_[0]    
    r_squared = lr.score(x,y)
    return m,c,r_squared
