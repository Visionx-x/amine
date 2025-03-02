from panda3d.core import Point3
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.environment = self.loader.loadModel("models/environment")
        self.environment.reparentTo(self.render)

        # Scale and position the model.
        self.environment.setScale(0.25, 0.25, 0.25)
        self.environment.setPos(-8, 42, 0)

        # Load a simple boy model (you need to have a model file)
        self.boy = self.loader.loadModel("models/boy")  # Replace with your model path
        self.boy.reparentTo(self.render)
        self.boy.setScale(0.1, 0.1, 0.1)
        self.boy.setPos(0, 10, 0)

        # Load a laptop model (you need to have a model file)
        self.laptop = self.loader.loadModel("models/laptop")  # Replace with your model path
        self.laptop.reparentTo(self.render)
        self.laptop.setScale(0.1, 0.1, 0.1)
        self.laptop.setPos(0, 9, -0.1)

        # Add a task to animate the boy typing
        self.taskMgr.add(self.animate_typing, "animate_typing")

    def animate_typing(self, task):
        # Simple animation logic (you can replace this with actual animation)
        self.boy.setH(self.boy.getH() + 1)  # Rotate the boy slightly
        return Task.cont

app = MyApp()
app.run()
