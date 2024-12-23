from flask import request, render_template_string
import ast

def ssti_waf(app):
    @app.route('/', methods=["POST"])
    def template():
        # 从blacklist.txt文件中读取黑名单内容
        try:
            with open('blacklist.txt', 'r') as file:
                blacklist = ast.literal_eval(file.read().strip())
        except (FileNotFoundError, ValueError, SyntaxError) as e:
            # 如果文件不存在或内容格式不正确，返回错误信息
            return f"Error reading blacklist file: {e}"

        waf = request.form.get("waf")
        #根据需求打开大写或小写WAF
        # if waf:
        #     waf = waf.lower()
        # if waf: 
        #     waf = waf.upper()
        for black in blacklist:
            if black in waf:
                return "Forbidden content detected!"

        result = render_template_string(waf)
        print(result)
        return result if result is not None else 'error'