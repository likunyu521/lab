from selenium import webdriver


class Crawler:
    def __init__(self):
        self.browswer = webdriver.Chrome()
        self.browswer.get('https://www.qiushibaike.com/text/')

    def print_content(self):

        # 获取 class 为 col1 的元素
        main_content = self.browswer.find_element_by_class_name('col1')
        # 获取 class 为 content 的元素
        contents = main_content.find_elements_by_class_name('content')

        i = 1
        for content in contents:
            print(str(i) + '.' + content.text + '\n')
            i += 1

        self.quit()

    def quit(self):
        self.browswer.quit()


Crawler().print_content()