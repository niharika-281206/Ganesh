import turtle
import cv2
import numpy as np
# 1. Load image
image_path = "ganesh.jpg"
img = cv2.imread(image_path)
if img is None:
    print(f"Error: Could not load '{image_path}'. Check file name and path.")
    exit()
# Resize image to fit screen properly
target_width = 650
h, w = img.shape[:2]
target_height = int((h / w) * target_width)
img_resized = cv2.resize(img, (target_width, target_height), interpolation=cv2.INTER_AREA)
# 2. Extract golden ribbon strokes
gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
# Find contours and exact parent-child hierarchy
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# 3. Setup Turtle canvas
screen = turtle.Screen()
screen.setup(width=850, height=850)
bg_color = "#181b22"
screen.bgcolor(bg_color)
screen.title("Ganesha Metallic Gold Clean Animation")
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(1.5)
offset_x = target_width / 2
offset_y = target_height / 2
# Colors
gold_stroke = "#D49B24"  # Metallic Gold Border
gold_fill = "#F5C842"    # Radiant Metallic Gold Fill
# 4. Draw contours with depth/hole awareness
if hierarchy is not None:
    for i, h_info in enumerate(hierarchy[0]):
        area = cv2.contourArea(contours[i])
        # Skip tiny noise dots and the whole canvas frame
        if area < 15 or area > (target_width * target_height * 0.45):
            continue
        # Calculate depth in hierarchy tree
        # depth 0 = gold shapes, depth 1 = holes inside gold (like palms/crown gaps), depth 2 = inner gold details
        depth = 0
        parent = h_info[3]
        while parent != -1:
            depth += 1
            parent = hierarchy[0][parent][3]
        # If it's a hole (inside the hand/crown), fill it with background color to keep it open!
        if depth % 2 == 1:
            pen.pencolor(gold_stroke)
            pen.fillcolor(bg_color)
        else:
            pen.pencolor(gold_stroke)
            pen.fillcolor(gold_fill)
        pen.penup()
        first_pt = contours[i][0][0]
        pen.goto(first_pt[0] - offset_x, offset_y - first_pt[1])
        pen.pendown()
        pen.begin_fill()
        for pt in contours[i][1:]:
            x = pt[0][0] - offset_x
            y = offset_y - pt[0][1]
            pen.goto(x, y)
        pen.goto(first_pt[0] - offset_x, offset_y - first_pt[1])
        pen.end_fill()
        pen.penup()
turtle.done()
