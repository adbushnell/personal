import pandas as pd

def get_trial_dates(df, training_duration='156w', forecast_horizon = '52w', stride='1w'):
    '''
    This function gives us the dates that we need to begin the time series analysis from, using a stride of one week
    We train using 3 years of data and forecast over one year. Our data progresses by one week intervals
    '''
    
    training_start     = df.index[0]
    training_end       = training_start + pd.Timedelta(training_duration)
    training_end_index = df.index.get_loc(training_end)
    #print(training_start, training_end)

    test_start_index  =  training_end_index+1
    test_start        = df.index[test_start_index]
    forecast_horizon  = pd.Timedelta(forecast_horizon)
    test_end          = test_start+pd.Timedelta(days=(forecast_horizon.days-1)) # 1 day forecast horizon: test_start==test_end

    df.index[0]
    dates = []

    stride = pd.Timedelta(stride)

    while test_end <= df.index[-1]:

        trial = {}
        trial['training_start'] = training_start
        trial['training_end']   = training_end
        trial['test_start']     = test_start
        trial['test_end']       = test_end
        dates.append(trial)

        training_start += stride
        training_end   += stride
        test_start     += stride
        test_end       += stride
    
    return dates, forecast_horizon