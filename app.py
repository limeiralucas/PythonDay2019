import falcon

class Resource:
    def on_get(self, req, resp):
        resp.body = '{"status": "ok"}'
        resp.status = falcon.HTTP_200


app = falcon.API()
app.add_route('/resource', Resource())
