from flask import Flask, jsonify, request
app = Flask(__name__)

languages = [{'name' : 'JavaScript'} , {'name' : 'Python'} , {'name' : 'Ruby'}]

@app.route('/' , methods = ['GET'])
def test():
	return jsonify({'message' : 'It works!!'})



# other functions

if __name__ == '__main__':
	app.run(debug = True , port = 8080)