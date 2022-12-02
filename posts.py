import json

import database_gateway

class Posts:

    def create_record(self, args):

        dg = database_gateway.DatabaseGateway()

        query_string = "insert into posts (titulo, alias, descricao) values (%s, %s, %s)"
        data = (args["titulo"], args["alias"], args["descricao"])

        dg.db_execute(query_string, data)     

        return self.read_records(dg.lastrowid)

    def update_record(self, args, resource_id):

        dg = database_gateway.DatabaseGateway()

        query_string = "update posts set titulo = %s, alias = %s, descricao = %s where id = %s"

        data = (args["titulo"], args["alias"], args['descricao'], resource_id)

        dg.db_execute(query_string, data)     

        return self.read_records(resource_id)

    def delete_record(self, resource_id):

        dg = database_gateway.DatabaseGateway()

        query_string = "delete from posts where id = %s"

        data = (resource_id)

        dg.db_execute(query_string, data) 

        resp = ("Success",)

        json_object = json.dumps(resp)

        return json.dumps(json.loads(json_object), indent = 2)

    def read_records(self, resource_id):

        dg = database_gateway.DatabaseGateway()

        if resource_id == "" :
            query_string = "select * from posts"
        else:
            query_string = "select * from posts where id = '" + str(resource_id) + "'"

        resp = dg.db_query(query_string)     

        return resp