"""
    基础写入配置文件
        -write(fp)                         将config对象写入至某个 .init 格式的文件  Write an .ini-format representation of the configuration state.
        -add_section(section)              添加一个新的section
        -set(section, option, value)       对section中的option进行设置，需要调用write将内容写入配置文件 ConfigParser2
        -remove_section(section)           删除某个 section
        -remove_option(section, option)    删除某个 section 下的 option
"""
import configparser


class Write_Config:
    def __init__(self, path, module):
        # 实例化配置对象
        self.cf = configparser.ConfigParser()
        # 获取写入文件路径，若采用w+方式则该文件可以不存在
        self.path = path
        # 配置写入方式，写入方式"w+"清空写
        self.module = module

    # 写入配置文件
    def write_ini_file(self):
        with open(self.path, self.module) as f:
            self.cf.write(f)

    # 新增section
    def add_section(self, section):
        self.cf.add_section(section=section)
        self.write_ini_file()

    # 删除某个 section
    def remove_section(self, section):
        self.cf.remove_section(section=section)
        self.write_ini_file()

    # 删除某个 section 下的 option
    def remove_option(self, section, option):
        self.cf.remove_option(section=section, option=option)
        self.write_ini_file()
