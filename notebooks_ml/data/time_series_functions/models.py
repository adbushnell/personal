class DecompositionModel:
    def __init__(self, linear_model = None, monthly_model=None, daily_model=None, hourly_model=None):
        self.linear_model = linear_model
        self.monthly_model= monthly_model
        self.daily_model = daily_model
        self.hourly_model = hourly_model
        
    def predict(self, date_to_predict):
        yhat = 0.0 
        
        if self.linear_model is not None:
            x_timedelta = date_to_predict - self.linear_model[2]
            x = x_timedelta.days
            linear_yhat = self.linear_model[0] * x + self.linear_model[1]
            yhat += linear_yhat
            
        if self.monthly_model is not None:
            month = date_to_predict.month
            monthly_yhat = self.monthly_model[month]
            yhat += monthly_yhat
            
        if self.daily_model is not None:
            day = date_to_predict.hour
            daily_yhat = self.daily_model[day]
            yhat += daily_yhat

        if self.hourly_model is not None:
            hour = date_to_predict.hour
            hourly_yhat = self.hourly_model[hour]
            yhat += hourly_yhat
            
        return yhat
        
