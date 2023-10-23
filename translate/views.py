from django.shortcuts import render
from django.views import View
from .translator import translate


class TranslateView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        language = request.POST.get('language')
        input_word = request.POST.get('input_word')
        print(language)
        print(input_word)
        if language == 'uzbek':
            full_data = translate('en', 'uz', f'{input_word}')
            data = full_data['translations']['translation']
            return render(request, 'index.html', {'translation': data})
        elif language == 'english':
            full_data = translate('uz', 'en', f'{input_word}')
            data = full_data['translations']['translation']
            return render(request, 'index.html', {'translation': data})
