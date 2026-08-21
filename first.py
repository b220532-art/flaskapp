from flask import Flask
app =Flask(__name__)
@app.route("/")
def home():
   return "flask application running successful"
if __name__==('__main__'):
        app.run('0.0.0.0',2000)
        # host,port
        
