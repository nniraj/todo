from config import app
from flask_restful import Resource, Api

api = Api(app)

class TodoResource(Resource):
    pass


api.add_resource(TodoResource, '/posts/<int:post_id>')

if __name__ == "__main__":
    app.run(port=5002, debug=True)