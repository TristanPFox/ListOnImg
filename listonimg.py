from PIL import Image, ImageDraw

items = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5"]
canvas = Image.open("canvas.png")
draw = ImageDraw.Draw(canvas)
line_spacing = canvas.height // (len(items) + 1)

for index, item in enumerate(items):
  line_pos = (index + 1) * line_spacing
  text_width, text_height = draw.textsize(item)
  text_pos = (canvas.width - text_width) // 2
  draw.text((text_pos, line_pos), item)

canvas.save("result.png")