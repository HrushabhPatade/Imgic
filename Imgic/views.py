from django.shortcuts import render
import openai,os,requests
from dotenv import load_dotenv
from django.core.files.base import ContentFile
from images.models import Image
load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)
openai.api_key = api_key

def generate_image(request):
    obj = None
    if api_key is not None and request.method == 'POST':
        user_text = request.POST.get('user_input')
        print(user_text)
        response = openai.Image.create(
            prompt = user_text,
        
            size='256x256'
        )
        print(response)
        img_url = response["data"][0]["url"]
        response= requests.get(img_url)
        print(response)
        img_file = ContentFile(response.content)
        
        count = Image.objects.count() + 1
        fname = f"image-{count}.jpg"
        
        obj = Image(text=user_text)
        obj.generated_image.save(fname, img_file)
        obj.save()
        
        print(obj)
    return render(request, "Main.html", {"object":obj})
