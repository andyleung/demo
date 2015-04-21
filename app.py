# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/map')
def draw_map():
    max = 100
    ip_info = [{'count':100, 'latitude': 37.385999999999996, 'ip': '8.8.8.8', 'longitude': -122.0838}, 
               {'count':90, 'latitude': 22.283299999999997, 'ip': '210.6.10.86', 'longitude': 114.14999999999998}, 
               {'count':80, 'latitude': 22.283299999999997, 'ip': '210.6.10.96', 'longitude': 114.14999999999998}, 
               {'count':70, 'latitude': 42.362599999999986, 'ip': '173.223.93.192', 'longitude': -71.0843}, 
               {'count':60, 'latitude': 33.78659999999999, 'ip': '199.181.132.249', 'longitude': -118.2987}, 
               {'count':50, 'latitude': 38.0, 'ip': '12.130.132.30', 'longitude': -97.0}, 
               {'count':40, 'latitude': 42.362599999999986, 'ip': '184.87.96.38', 'longitude': -71.0843}, 
               {'count':30, 'latitude': 37.33940000000001, 'ip': '190.93.245.88', 'longitude': -121.89500000000001}, 
               {'count':20, 'latitude': 42.362599999999986, 'ip': '184.87.102.189', 'longitude': -71.0843}, 
               {'count':10, 'latitude': 1.3667000000000087, 'ip': '103.20.93.129', 'longitude': 103.80000000000001}, 
               {'count':100, 'latitude': 42.362599999999986, 'ip': '173.223.92.93', 'longitude': -71.0843}, 
               {'count':90, 'latitude': 42.362599999999986, 'ip': '173.223.84.229', 'longitude': -71.0843}, 
               {'count':80, 'latitude': 26.022199999999998, 'ip': '72.52.4.91', 'longitude': -80.1496}, 
               {'count':70, 'latitude': 42.362599999999986, 'ip': '173.223.86.54', 'longitude': -71.0843}, 
               {'count':100, 'latitude': 37.39609999999999, 'ip': '205.204.96.3', 'longitude': -121.96170000000001}, 
               {'count':50, 'latitude': 22.283299999999997, 'ip': '203.80.97.19', 'longitude': 114.14999999999998}, 
               {'count':50, 'latitude': 22.25, 'ip': '203.145.76.30', 'longitude': 114.16669999999999}, 
               {'count':30, 'latitude': 22.283299999999997, 'ip': '219.76.111.57', 'longitude': 114.14999999999998}, 
               {'count':80, 'latitude': 22.25, 'ip': '202.126.57.188', 'longitude': 114.16669999999999}, 
               {'count':40, 'latitude': 22.25, 'ip': '203.83.94.198', 'longitude': 114.16669999999999}, 
               {'count':60, 'latitude': 26.022199999999998, 'ip': '72.52.4.120', 'longitude': -80.1496}, 
               {'count':50, 'latitude': -27.0, 'ip': '144.140.108.23', 'longitude': 133.0}, 
               {'count':10, 'latitude': -6.1743999999999915, 'ip': '114.4.66.58', 'longitude': 106.82940000000004}, 
               {'count':40, 'latitude': 1.2931000000000097, 'ip': '203.116.221.170', 'longitude': 103.85579999999999}, 
               {'count':50, 'latitude': 1.2931000000000097, 'ip': '203.126.100.19', 'longitude': 103.85579999999999 }]
    return render_template('map.html', info=ip_info, max=max)  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)


