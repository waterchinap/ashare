from calendar import HTMLCalendar
from playwright.sync_api import sync_playwright
from PIL import Image
import io

def generate_html_calendar(year, month):
    # 创建HTMLCalendar对象
    cal = HTMLCalendar()
    
    # 生成指定年月的HTML日历
    html_calendar = cal.formatmonth(year, month)
    
    # 添加自定义CSS样式
    css = """
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            height: 100%;
            table-layout: fixed;
        }
        th, td {
            border: 1px solid #ccc;
            text-align: center;
            vertical-align: middle;
            font-size: 4em;
            padding: 10px;
        }
        th {
            background-color: #ddd;
        }
        td {
            background-color: #fff;
        }
    </style>
    """
    
    # 将CSS样式添加到HTML日历中
    html_calendar = f"<html><head>{css}</head><body>{html_calendar}</body></html>"
    
    return html_calendar

def html_to_image_buffer(html_content, image_size=(1872, 1404)):
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # 设置页面尺寸
        page.set_viewport_size({"width": image_size[0], "height": image_size[1]})
        
        # 将HTML内容加载到页面
        page.set_content(html_content)
        
        # 截取页面截图并保存到缓冲区
        buffer = page.screenshot(full_page=True)
        
        # 关闭浏览器
        browser.close()
        
        return buffer

def rotate_image_buffer(buffer, output_image, angle=270):
    # 从缓冲区打开图片
    img = Image.open(io.BytesIO(buffer))
    
    # 旋转图片
    rotated_img = img.rotate(angle, expand=True)
    
    # 保存旋转后的图片
    rotated_img.save(output_image)

def main():
    years = [2024, 2025]
    months = range(1, 13)
    for year in years:
        for mon in months:
            html_calendar = generate_html_calendar(year, mon)
            fn = f'cal{year}{mon:02}.png'
            # 将HTML日历转换为图片缓冲区
            buffer = html_to_image_buffer(html_calendar)
            
            # 旋转图片缓冲区并保存
            rotate_image_buffer(buffer, fn)

if __name__ == "__main__":
    main()