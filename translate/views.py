#from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from .models import Translate, Result
from .forms import TranslateForm

from textblob import TextBlob


def home(request):
	return render(request, 'translate/home.html')


def translate_page(request):
	form = TranslateForm()
	context = {'form': form}

	return render(request, 'translate/translate.html', context)


def translate_text(request):
	if request.method == 'POST':
		form = TranslateForm(request.POST)
		if form.is_valid():
			search = Translate(
				user=request.user,
				lang_1=request.POST['lang_1'],
				text=request.POST['text'],
				lang_2=request.POST['lang_2'])
			search.save()

	# Get the last object
	last = Translate.objects.latest('id')
	last_id = last.id
	last_obj = Translate.objects.get(id=last_id)
	# Translate
	in_blob = TextBlob(last_obj.text)
	out_blob = in_blob.translate(from_lang=last_obj.lang_1, to=last_obj.lang_2)
	# Save the translated text

	# last_obj.translated_text = out_blob
	# last_obj.save()

	output = Result(id_translate=last_id, translated_text=out_blob)
	output.save()

	return redirect('result')

def result(request):

	last_obj = Result.objects.latest('id')
	last_id = last_obj.id
	last_result = Result.objects.get(id=last_id)

	context = {}
	context['result'] = last_result.translated_text
	print(context)

	return render(request, 'translate/result.html', context)
