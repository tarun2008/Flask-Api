from flask import Flask,request,jsonify
from star import final_star_list

app = Flask(__name__)

@app.route('/')
def index ():
    return jsonify({
        'data' : final_star_list,
        'message' : 'success'
    })
@app.route('/star')
def star ():
    name = request.args.get('name')
    star_data = next(item for item in final_star_list if item['name'] == name)
    return jsonify({
        'data' : star_data,
        'message' : 'success'
    })
if __name__  == '__main__' :
    app.run()   