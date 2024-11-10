from django.shortcuts import render
import qrcode
import uuid

def home(request):
    text = ''  # Initialize text to an empty string
    qr_code_img = None  # Initialize qr_code_img to avoid errors

    if request.method == 'POST':
        text = request.POST.get('text')

        if text:  # Validate if text is not empty before generating QR code
            unique_filename = f'{uuid.uuid4()}.png'  # Generate a unique filename
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=1,
            )
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(f'static /image.png')  # Save image with unique filename in static folder
            qr_code_img = f'static/image.png' # Update qr_code_img for successful generation

        else:
            pass

    return render(request, 'home.html', {'text': text, 'qr_code_img': qr_code_img})

def about(request):
    return render(request, 'about.html')