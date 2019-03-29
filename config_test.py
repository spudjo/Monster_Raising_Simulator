import configparser

config = configparser.ConfigParser()
config.read('test.ini')
config_main = config['MAIN']

print(config_main['test'])


print(config_main['test2'])