from flask import Flask, render_template;
app = Flask(__name__)

@app.route("/")
def home():
    inStream = open("data_hw252.csv", 'r')                    
    data = inStream.read()
    inStream.close()

    def removeLineBr(a):
         pos = 0
         data = a[:]
         amount = data.count('(')
         while pos <= amount:
             a = data.find('(')
             data = data[: (a - 1)] + '-' + data[a:]
             data = data[: a] + '^' + data[a + 1:]
             pos += 1
         data = data.replace('^', '(')
         data = data[:126239]
         return data
    
    data = removeLineBr(data);
    #lines = data.split("\n")  
    return render_template("home.html", data = data, lines= data.split("\n"));


if __name__ == "__main__":
    app.debug = True
    app.run()
