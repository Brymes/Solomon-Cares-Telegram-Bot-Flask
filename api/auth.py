#!/usr/bin/python3

from http import HTTPStatus
from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_jwt
)
from jwt.exceptions import (
    InvalidTokenError,
    DecodeError
)


black_list = set()


class TokenResource(Resource):

    def post(self):

        json_data = request.get_json()

        # FIXME
        user_id = json_data.get('user_id')

        access_token = create_access_token(identity=user.user_id, fresh=True)
        refresh_token = create_refresh_token(identity=user_id)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }, HTTPStatus.OK


class RefreshResource(Resource):

    @jwt_required(refresh=True)
    def post(self):
        try:
            current_user = get_jwt_identity()

        except (InvalidTokenError, DecodeError):
            raise InvalidTokenError
        else:

            token = create_access_token(identity=current_user, fresh=False)

            return {'access_token': token}, HTTPStatus.OK


class RevokeResource(Resource):

    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']

        black_list.add(jti)

        return {'message': 'Successfully logged out'}, HTTPStatus.OK
