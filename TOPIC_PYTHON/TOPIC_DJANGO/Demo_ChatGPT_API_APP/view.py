from django.shortcuts import render
from django.contrib import messages

def home(request):
    # API opent AI
    lang_list = ['c', 'clike', 'cpp', 'csharp', 'css'  ]
    
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']
        
        #Check to make sure they picked a lang
        if lang == "Select Programing Language":
            messages.success(request, "HEY! You Forgot to picked Language")
            return render(request, 'home.html', {'lang_list': lang_list})
        else:
            return render(request, 'home.html', {'lang_list': lang_list})
    return render(request, 'home.html', {'lang_list': lang_list})

    #OpenAI key
    openai.api_key = 'nhap key vao day'
    # Create OpenAI Instance
    openai.Model.list()
    #Make an OpenAI request
    try: 
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt =f"Respond only with code. Fix this {lang} code: {code}",
            temperature =  0,
            max_tokens = 1000,
            frequency_penalty = 0.0,
            presence_penalty = 0.0,       
            )
        return render(request, 'home.html', {'lang_list': lang_list, 'response': code})
    except Exception as e: 
        return render(request, 'home.html', {'lang_list': lang_list}, 'code': e, 'lang':lang)
