import pandas as pd
def mae(y_true, y_hat):
    assert len(y_true) == len(y_hat)
    error = y_true - y_hat
    abs_error = error.abs()
    return abs_error.mean()

def rmse(y_true, y_hat):
    assert len(y_true) == len(y_hat)
    error = y_true - y_hat
    sq_error = error ** 2
    mean_sq_error = sq_error.mean()
    return mean_sq_error ** 0.5

def mape(y_true, y_hat):
    assert len(y_true) == len(y_hat)
    error = y_true - y_hat
    pct_error = 100*error/y_true
    ape = pct_error.abs()
    return ape.mean()

def mase(y_true, y_hat, benchmark):
    assert len(y_true) == len(y_hat)
    error = y_true - y_hat
    scaled_error = error/benchmark
    ase = scaled_error.abs()
    return ase.mean()

def benchmark_mae(y_train, forecast_horiz):
    y_pred = y_train[:-forecast_horiz] #y pred is delayed by h steps: the naive forecast
    benchmark = mae(pd.Series(y_train[forecast_horiz:]),pd.Series(y_pred))
    return benchmark