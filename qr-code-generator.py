import pyqrcode

def generate_svg_qr_code(url, filename):
    qr = pyqrcode.create(url)
    
    qr.svg(filename, scale=8)

if __name__ == "__main__":
    website_url = "https://prydan.com/current-opening/"
    
    svg_qr_code_filename = "websiteImage.svg"
    
    generate_svg_qr_code(website_url, svg_qr_code_filename)
    print(f"SVG QR Code generated successfully as {svg_qr_code_filename}")
