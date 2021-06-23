import requests
      f = requests.get('https://api.openweathermap.org/data/2.5/weather?q=warangal&appid=2656dcc588455cf9f21251815987aa9d')

       with open('weather_report.txt','w')as f:
           f.write(r.text)

