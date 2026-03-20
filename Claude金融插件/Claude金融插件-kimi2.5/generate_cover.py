#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# 创建封面图
width, height = 1792, 1024
img = Image.new('RGB', (width, height), color='#1a1f5c')
draw = ImageDraw.Draw(img)

# 绘制渐变背景
for y in range(height):
    r = int(26 + (124 - 26) * y / height)
    g = int(31 + (58 - 31) * y / height)
    b = int(92 + (237 - 92) * y / height)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# 尝试加载字体
try:
    title_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 120)
    subtitle_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 60)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()

# 绘制标题
title = "Claude 金融插件"
subtitle = "AI 重塑金融分析"

# 获取文字尺寸
title_bbox = draw.textbbox((0, 0), title, font=title_font)
subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)

title_width = title_bbox[2] - title_bbox[0]
subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]

# 居中绘制
title_x = (width - title_width) // 2
subtitle_x = (width - subtitle_width) // 2

draw.text((title_x, 300), title, fill='white', font=title_font)
draw.text((subtitle_x, 480), subtitle, fill='#fbbf24', font=subtitle_font)

# 绘制装饰元素 - 柱状图
bar_colors = ['#3b82f6', '#8b5cf6', '#ec4899', '#f59e0b']
for i, color in enumerate(bar_colors):
    bar_height = 150 + i * 50
    draw.rectangle([200 + i*120, 700 - bar_height, 280 + i*120, 700], fill=color)

# 折线图
points = [(600, 600), (700, 550), (800, 580), (900, 500), (1000, 520), (1100, 480)]
for i in range(len(points)-1):
    draw.line([points[i], points[i+1]], fill='#10b981', width=4)

# 保存图片
img.save('claude_finance_cover.png')
print("封面图已生成：claude_finance_cover.png")
