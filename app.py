from flask import Flask, request, render_template

app = Flask(__name__)

logged_ips = []

@app.route("/")
def index():
    
    client_ip = request.remote_addr
    
   
    if client_ip not in logged_ips:
        logged_ips.append(client_ip)
    
  
    return render_template("index.html", ip=client_ip, logged_ips=logged_ips)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
