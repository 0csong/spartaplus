from flask import Flask, render_template,request
import requests

app = Flask(__name__)


@app.route('/')
def main():
    myname="sparta"
    return render_template("index.html",name=myname)


@app.route('/detail/<keyword>')
def detail(keyword):
    r = requests.get("https://owlbot.info/api/v4/dictionary/owl", headers={"Authorization": "Token fab3372dd6c05f5d404f0491bb9cefc79044663d"})
    result = r.json()
    print(result)
    word_receive = request.args.get("word_give") #여기서는 http://localhost:5000/detail?word_give=hi로 들어가면 print(hi)뜸
    print(word_receive)
    return render_template("detail.html",word=keyword)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)