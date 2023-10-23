from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')
@app.route('/Analysis')
def Analysis():
    return render_template('Analysis.html')
@app.route('/About_us')
def About_us():
    return render_template('About_us.html')
@app.route('/RRH')
def RRH():
    return render_template('RRH.html')
@app.route('/ARH')
def ARH():
    return render_template('ARH.html')
@app.route('/Events')
def Events():
    return render_template('Events.html')
@app.route('/Post',  methods=['POST'])
def post_event():
    if request.method == 'POST':
        # Handle the form submission here
        # You can add your code to process the form data
        return "Event Posted", render_template('Post.html')
    
@app.route('/Requst_Ride')
def Requst_Ride():
    return render_template('Requst_Ride.html')
@app.route('/Accept_Ride')
def Accept_Ride():
    return render_template('Accept_Ride.html')
@app.route('/EH')
def EH():
    return render_template('EH.html')

@app.route('/Profile')
def Profile():
    return render_template('Profile.html')
@app.route('/UpdateProfile')
def UpdateProfile():
    return render_template('UpdateProfile.html')
@app.route('/SISU')
def SISU():
    return render_template('SISU.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/f_pass')
def f_pass():
    return render_template('f_pass.html')
if __name__ == '__main__':
    app.run(debug=True)