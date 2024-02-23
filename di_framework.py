from injector import Injector, inject, Provider, singleton

class NameModel:
    def __init__(self, name):
        self.name = name

    def get_greeting(self):
        return f"Hello, {self.name}!"
    
class NameView:
    def display_greeting(self, greeting):
        print(greeting)
    
    def prompt_for_name(self):
        return input("What is your name? ")
    
class NameController:
    @inject
    def __init__(self, model: NameModel, view: NameView):
        self.model = model
        self.view = view
    
    def run(self):
        name = self.view.prompt_for_name()
        self.model.name = name
        greeting = self.model.get_greeting()
        self.view.display_greeting(greeting)

class Configuration:
    def __init__(self, settings_file):
        pass

class Logger:
    def info(self, message):
        print(f"INFO: {message}")

    def error(self, message):
        print(f"ERROR: {message}")

def configure(binder):
    binder.bind(NameModel, to=NameModel(''), scope=singleton)
    binder.bind(NameView, to=NameView, scope=singleton)

def main():
    config = Configuration("settings.json")
    logger = Logger()
    injector = Injector(configure)
    controller = injector.get(NameController)
    controller.run()

if __name__ == "__main__":
    main()
