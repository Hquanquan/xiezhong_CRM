import configparser
import os

'''
    基础读取配置文件
        -read(filename)         直接读取文件内容
        -sections()             得到所有的section，并以列表的形式返回
        -options(section)       得到该section的所有option
        -items(section)         得到该section的所有键值对
        -get(section,option)    得到section中option的值，返回为string类型
        -getint(section,option) 得到section中option的值，返回为int类型，还有相应的getboolean()和getfloat() 函数。
'''


class Get_Config:

    # 初始化配置文件对象
    def __init__(self, path):
        # 实例化
        self.config = configparser.ConfigParser()
        # 读取配置文件
        self.config.read(path, encoding='utf-8')

    # 获取所有的sections
    def get_sections(self):
        sections = self.config.sections()
        return sections

    # 获取section下的所有key
    def get_options(self, section):
        opts = self.config.options(section=section)
        return opts

    # 获取section下的所有键值对
    def get_kvs(self, section):
        kvs = self.config.items(section=section)
        return kvs

    # 根据section和option获取指定的value
    def get_key_value(self, section, option):
        opt_val = self.config.get(section=section, option=option)
        return opt_val

    # 更新指定section的option下的value
    # def update_section_option_val(self,section,option,value,path,module):
    #     self.cf.set(section=section,option=option,value=value)
    #     with open(path,module) as f:
    #         self.cf.write(f)


if __name__ == '__main__':
    # file = r"E:\learning\PycharmProjects\taobao_test\config\config.ini"
    root_path = os.path.abspath(os.path.dirname(__file__)).split('taobao_test')[0] + 'taobao_test'
    file = root_path + '\\config\\config.ini'
    print(file)
    g = Get_Config(file)
    print(g)
    sections = g.get_sections()
    print(sections)

    for my_section in sections:
        options = g.get_options(my_section)
        print("%s ====> %s" % (my_section, options))
        for one in options:
            key = g.get_key_value(my_section, one)
            print("%s ====> %s" % (one, key))
        print("=============")

