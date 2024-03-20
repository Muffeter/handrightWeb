from flask import Flask, jsonify, request, send_from_directory, send_file
from flask_cors import CORS,cross_origin
from PIL import Image, ImageFont
from handright import Template, handwrite
import engine

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Endpoint to serve static files (e.g., HTML, CSS, JavaScript)
@app.route('/static/<path:filename>')
@cross_origin()
def serve_static(filename):
    return send_from_directory('static', filename)

def create_template(line_spacing, fill, left_margin, top_margin, right_margin, bottom_margin, word_spacing, line_spacing_sigma, font_size_sigma, word_spacing_sigma, start_chars, end_chars, perturb_x_sigma, perturb_y_sigma, perturb_theta_sigma, width, height):
    background = Image.new(mode="1", size=(width, height), color=1)
    font_path = r"D:\App\Handright\tests\fonts\Bo Le Locust Tree Handwriting Pen Chinese Font-Simplified Chinese Fonts.ttf"
    font_size = 80
    font = ImageFont.truetype(font_path, size=font_size)
    
    template = Template(
        background=background,
        font=font,
        line_spacing=line_spacing,
        fill=fill,
        left_margin=left_margin,
        top_margin=top_margin,
        right_margin=right_margin,
        bottom_margin=bottom_margin,
        word_spacing=word_spacing,
        line_spacing_sigma=line_spacing_sigma,
        font_size_sigma=font_size_sigma,
        word_spacing_sigma=word_spacing_sigma,
        start_chars=start_chars,
        end_chars=end_chars,
        perturb_x_sigma=perturb_x_sigma,
        perturb_y_sigma=perturb_y_sigma,
        perturb_theta_sigma=perturb_theta_sigma
    )
    
    return template

@app.route('/api/generate')
def generate():
    # Get parameters from the query string
    text = str(request.args.get('text', 'Hello, world!'))
    line_spacing = int(request.args.get('line_spacing', 90))
    fill = int(request.args.get('fill', 0))
    left_margin = int(request.args.get('left_margin', 30))
    top_margin = int(request.args.get('top_margin', 0))
    right_margin = int(request.args.get('right_margin', 30))
    bottom_margin = int(request.args.get('bottom_margin', 0))
    word_spacing = int(request.args.get('word_spacing', -10))
    line_spacing_sigma = int(request.args.get('line_spacing_sigma', 1))
    font_size_sigma = int(request.args.get('font_size_sigma', 1))
    word_spacing_sigma = int(request.args.get('word_spacing_sigma', 1))
    start_chars = request.args.get('start_chars', '“（[<')
    end_chars = request.args.get('end_chars', '，。')
    perturb_x_sigma = int(request.args.get('perturb_x_sigma', 1))
    perturb_y_sigma = int(request.args.get('perturb_y_sigma', 1))
    perturb_theta_sigma = float(request.args.get('perturb_theta_sigma', 0.05))
    width = int(request.args.get('width', 3072))
    height = int(request.args.get('height', 3920))
    # Create a template based on the parameters
    template = create_template(
        line_spacing, fill, left_margin, top_margin, right_margin, bottom_margin, word_spacing,
        line_spacing_sigma, font_size_sigma, word_spacing_sigma, start_chars, end_chars,
        perturb_x_sigma, perturb_y_sigma, perturb_theta_sigma, width, height
    )

    # Assuming `engine.run()` performs the generation process
    filename = engine.run(text, template)  # You should define `engine` somewhere in your code
    filepath = f"static/{filename}.png"
    # Return a JSON response indicating success
    return send_file(filepath, as_attachment=True, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
