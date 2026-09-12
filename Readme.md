# Ganesha Metallic Gold Animation

A Python script that converts an image into a beautiful metallic gold line drawing using computer vision and Turtle graphics. Perfect for creating elegant visualizations of religious artwork, portraits, or any image you'd like to render as a clean, geometric outline.

## Features

✨ **Automatic Contour Detection** – Uses OpenCV to detect image edges and shapes
🎨 **Metallic Gold Styling** – Renders with premium gold stroke and fill colors
⚫ **Smart Hole Handling** – Intelligently preserves interior spaces (eyes, crown gaps, hand details)
🐢 **Turtle Graphics Animation** – Smooth, clean visualization with real-time drawing
🔧 **Customizable Colors** – Easy to modify the gold palette to suit your needs

## Requirements

- Python 3.7+
- `opencv-python` (cv2)
- `numpy`
- `turtle` (usually included with Python)

## Installation

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd ganesha-animation
   ```

2. **Install dependencies**
   ```bash
   pip install opencv-python numpy
   ```

3. **Prepare your image**
   - Place your image file in the same directory as the script
   - Default filename: `ganesh.jpg`
   - Supported formats: JPG, PNG, BMP, etc.

## Usage

1. **Basic Usage** (with default image name)
   ```bash
   python script.py
   ```

2. **With a different image** – Edit the script and change:
   ```python
   image_path = "your_image.jpg"
   ```

3. **Watch the animation** – A Turtle graphics window will open and draw your contours in real-time

## How It Works

### Image Processing Pipeline

1. **Load & Resize** – Image is loaded via OpenCV and resized to fit the display (target width: 650px)

2. **Grayscale Conversion** – Converts BGR color to grayscale for edge detection

3. **Binary Thresholding** – Applies threshold (value: 70) to create black & white regions
   - Darker areas → black
   - Lighter areas → white
   - Adjust threshold value in the code to capture more/fewer details

4. **Contour Detection** – OpenCV finds all shape contours with hierarchy tracking
   - `RETR_TREE` mode captures parent-child relationships (outer shapes vs. holes)

5. **Hierarchy-Based Rendering** – Contours are drawn based on depth in the hierarchy tree
   - **Depth 0** (outer shapes) → Filled with gold
   - **Depth 1** (holes inside) → Filled with background color (to keep them open)
   - **Depth 2** (inner details) → Filled with gold again

### Turtle Graphics Output

- **Gold Stroke** – `#D49B24` (metallic border)
- **Gold Fill** – `#F5C842` (radiant gold interior)
- **Background** – `#181b22` (dark navy/black)
- Canvas size: 850×850 pixels

## Customization

### Change Colors

Edit these lines in the script:

```python
bg_color = "#181b22"      # Background color
gold_stroke = "#D49B24"   # Contour outline color
gold_fill = "#F5C842"     # Fill color
```

### Adjust Image Thresholding

```python
_, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
#                              ↑↑ change this value (0-255)
```

- **Lower value** (e.g., 50) → captures more details, potentially noisier
- **Higher value** (e.g., 100) → fewer details, cleaner result

### Change Contour Sizes

Skip very small noise or very large contours:

```python
if area < 15 or area > (target_width * target_height * 0.45):
    continue
```

### Modify Canvas Size

```python
screen.setup(width=850, height=850)  # Change these values
```

### Adjust Line Thickness

```python
pen.pensize(1.5)  # Change line width (higher = thicker)
```

## Troubleshooting

### Image Not Found Error
```
Error: Could not load 'ganesh.jpg'. Check file name and path.
```
**Solution:** 
- Ensure the image file is in the same directory as the script
- Check the filename spelling (case-sensitive on Linux/Mac)
- Use absolute path if needed: `image_path = "/full/path/to/ganesh.jpg"`

### Slow Performance
- Reduce `target_width` for a smaller image
- Increase threshold value to reduce contour count
- Disable anti-aliasing in resize: change `INTER_AREA` to `INTER_NEAREST`

### Too Much Noise / Not Enough Detail
- **More noise?** Increase threshold value (e.g., 100)
- **Want more details?** Decrease threshold value (e.g., 50)
- **Remove tiny contours?** Increase the `area < 15` value to `area < 50`

### Drawing is Slow
- Reduce `target_width` to process a smaller image
- Increase `pen.speed()` value (0 is fastest)

## Project Structure

```
.
├── script.py           # Main Python script
├── ganesh.jpg          # Your input image
└── README.md           # This file
```

## Tips for Best Results

✅ **Use high-contrast images** – Clear subjects with distinct backgrounds work best
✅ **Test different thresholds** – Try values between 50-150 for different effects
✅ **Resize input images** – Smaller images (under 1000px) process faster
✅ **Save the output** – Right-click the Turtle window to save as PostScript (.eps)
✅ **Experiment with colors** – Try different gold tones or even non-metallic palettes

## Example Color Palettes

**Blue Ocean Theme**
```python
bg_color = "#0a1628"
gold_stroke = "#1e90ff"
gold_fill = "#87ceeb"
```

**Sunset Theme**
```python
bg_color = "#2c1810"
gold_stroke = "#ff6b35"
gold_fill = "#ffa500"
```

**Silver Elegance**
```python
bg_color = "#1a1a1a"
gold_stroke = "#c0c0c0"
gold_fill = "#e8e8e8"
```

## Performance Notes

- Processing time depends on image complexity and size
- 650px width typically processes in 10-30 seconds
- Turtle drawing is real-time; close the window to exit

## License

This project is open source. Modify and use freely!

## Contributing

Found a bug or have ideas? Feel free to improve the code:
- Add more color themes
- Implement different hierarchy rendering strategies
- Add SVG export functionality
- Create a GUI for parameter tuning

---

**Created with ❤️ for beautiful algorithmic art**

Happy drawing! 🐢✨