import allure


class Print:
    
allure.attach(context.web.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
    