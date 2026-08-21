from flask import Flask
app =Flask(__name__)
@app.route("/")
def home():
 
  # return "flask application running successful"
   return """     
       <html>
   <body>
      <h1>Hello RGUKT</h1>
      </body> 
</html>        


   """
if __name__==('__main__'):
        app.run('0.0.0.0',2000)
        # host,port
