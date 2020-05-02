import os

class Configuration():

    @property
    def plt_output(self):
        return os.environ.get('PLT_OUTPUT')

    @property
    def save_plt(self):
        env = os.environ.get('PLT_OUTPUT')
        if env is None:
            return False
        else:
            return True

    @property
    def headless(self):
        env = os.environ.get('HEADLESS')
        if env is None:
            return False # default to not headless.
        else:
            return True

    def __repr__(self):
        return "Configuration()"

    def __str__(self):
        return f'Headless: {self.headless} \nSave Plot: {self.save_plt}\nPlot Output: {self.plt_output}\n'


config = Configuration()
print(config)

def load_configuration():
    return config