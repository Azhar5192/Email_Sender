## load template
def load_template():
    with open("template.txt",'r' , encoding="utf-8") as f:
        template = f.read()
    return template