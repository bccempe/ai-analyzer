class AppRepository:
    def __init__(self):
        self.apps = []

    def get_app(self, id: str) -> App:
        return App(id=id, name="App 1")

    def add_app(self, app: App):
        self.apps.append(app)

    def get_apps(self) -> list[App]:
        return self.apps