import numpy as np

class day:

    #feature vector
    date = [0,0,0] #year month day
    news_headlines = []
    week_prior_trend = 0

    #label
    delta_dow = 0 #if dow went up or down



    def set_date(self, date = [0,0,0]):
        self.date = date

    def set_news_headlines(self, news_headlines = []):
        self.news_headlines = news_headlines

    def set_week_prior_trend(self, values):
        projected_inc = day.fit_data(values)
         
    def fit_data(self,values):
        degree = 2
        x_axis = np.array([0,1,2,3,4,5,6])
        y_axis = np.array(values)
        z = np.polyfit(x_axis, y_axis, degree)

        poly = np.poly1d(z)

        projection = poly(7)

        delta_projection = projection  - values[6]

        breakpoint()
        return delta_projection




day = day()
data = [1,2,3,4,5,6,7]
day.set_week_prior_trend(data)
breakpoint()







