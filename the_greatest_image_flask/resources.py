from flask_restful import Resource
from flask import jsonify


class ImageResource(Resource):
    def get(self):
        return jsonify({
            'img': 'test.png',
            'uuid': 'test-uuid'
        })

    def post(self, img_uuid):
        print(request.data['uuid'], request.data['response'])
        return jsonify({'message': 'success'})
