temp = input("Please enter your data!! ") 
try: 
	with open('data.txt', 'w') as gfg: 
		gfg.write(temp) 
    print("Launching server...")
except Exception as e: 
	print("There is a problem", str(e)) 
#  Privately create the server...
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Data!"
      try:
        with open('data.txt', 'r') as file:
            text_content = file.read()
        return render_template('data.html', content=text_content)
    except FileNotFoundError:
         return "File not found."
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
