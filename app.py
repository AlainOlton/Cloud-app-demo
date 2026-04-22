from flask import Flask
import os
import psutil 

app = Flask(__name__)

@app.route('/')
def home():
    return "Cloud App is Running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



@app.route('/metrics')
def metrics():
    cpu_usage = psutil.cpu_percent()
    status = "HEALTHY" if cpu_usage < 80 else "ALERT"
    return {
        "cpu_usage_percent": cpu_usage,
        "status": status
    }