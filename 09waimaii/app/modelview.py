from flask_admin.contrib.sqla import ModelView

class BaseModelview(ModelView):
    def getinfo(self):
        return "this is another model"