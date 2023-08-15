from flask import Flask,render_template



FAI=Flask(__name__)

@FAI.route("/wish")

def wish():
    return " HI HELLO FLASK"
@FAI.route("/first")
def first():
    return render_template('first.html',Name='MESSI',Age=35)


if __name__=='__main__':
    FAI.run(debug=True)