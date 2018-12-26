from view.View import CLIView
from model.Model import Model
from model.db.Db import Db
from controller.ControllerTSU import ControllerTSU

def app(view):
    view.main_menu()
    app(view)
if __name__ == '__main__':
    db = Db()
    model = Model(db)
    controller = ControllerTSU(model)
    view = CLIView(model, controller)

    app(view)