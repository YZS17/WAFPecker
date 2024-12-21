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

        template_code = request.form.get("waf")

        # 检查黑名单中的词汇是否出现在模板代码中
        for black in blacklist:
            if black in template_code:
                return "Forbidden content detected!"

        result = render_template_string(template_code)
        print(result)
        return result if result is not None else 'error'