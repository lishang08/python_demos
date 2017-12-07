# coding=utf-8

import ConfigParser

'''
cf = ConfigParser.ConfigParser()

cf.read('test.conf')

secs = cf.sections()

print('sections:', secs, type(secs))

opts = cf.options('db')

print('options:', opts, type(opts))

kvs = cf.items('db')

print('db:', kvs, type(kvs))

#遍历字典
for k, v in kvs:
    print('{k}:{v}'.format(k=k, v=v))

#read by type
db_host = cf.get('db', 'db_host')
db_user = cf.get('db', 'db_user')
db_port = cf.get('db', 'db_port')
db_pass = cf.get('db', 'db_pass')

print(db_host)
print(db_user)
print(db_port)
print(db_pass)

#read int
threads = cf.getint("concurrent", "thread")
processors = cf.getint("concurrent", "processor")

print('db_host:', db_host)
print('db_user:', db_user)
print('db_port:', db_port)
print('db_pass:', db_pass)
print('db_threads:', threads)
print('db_processors:', processors)
'''

class ConfigReader:

    def read(self):
        """获取数据库配置文件中的连接信息"""
        cf = ConfigParser.ConfigParser()
        cf.read('/Users/fulishang/development/python/python_demos/file_handler/test.conf')
        return cf

if __name__ == '__main__':
    configReader = ConfigReader()
    configs = configReader.read()
    print(configs, type(configs))
    db_schema = configs.get('db','db_schema')
    print(db_schema)

