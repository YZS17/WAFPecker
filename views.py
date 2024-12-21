from flask import render_template_string, request

def configure_routes(app):
    @app.route('/', methods=["GET"])
    def index():
        image_url_top = "https://xu17-1326239041.cos.ap-guangzhou.myqcloud.com/xu17/202412211958444.png"
        image_url_bottom = "https://xu17-1326239041.cos.ap-guangzhou.myqcloud.com/xu17/202412212016990.png"
        
        github_url = "https://github.com/YZS17" 

        return render_template_string("""
        <html>
        <head>
            <title>WAF-Pecker</title>
            <style>
                body {
                    text-align: center;
                    padding-top: 50px;
                    font-family: Arial, sans-serif;
                }
                .image-container {
                    margin: 20px auto;
                    display: block;
                }
                a {
                    display: inline-block;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <!-- Show top image -->
            <div class="image-container">
                <img src="{{ image_url_top }}" alt="Top Image" style="display: block; margin: 0 auto;">
            </div>
            <!-- Show bottom image -->
            <div class="image-container">
                <img src="{{ image_url_bottom }}" alt="Bottom Image" style="display: block; margin: 0 auto;">
            </div>
            <!-- Show GitHub link -->
            <a href="{{ github_url }}" target="_blank">XU17's GitHub</a>
        </body>
        </html>
        """, image_url_top=image_url_top, image_url_bottom=image_url_bottom, github_url=github_url)