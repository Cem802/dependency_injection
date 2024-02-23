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
    def __init__(self, model, view):
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

def main():
    config = Configuration("settings.json")
    logger = Logger()
    model = NameModel("")
    view = NameView()
    controller = NameController(model, view)
    controller.run()

if __name__ == "__main__":
    main()
