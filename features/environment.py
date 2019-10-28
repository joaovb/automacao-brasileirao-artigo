from selenium import webdriver


def before_all(context):
	context.web = webdriver.Chrome()

def after_step(context, step):
	print()
	#context.web.save_screenshot(step_name +'screenshot.png')
    

def after_all(context):
	context.web.quit()