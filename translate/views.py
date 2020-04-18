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

'''
def get_text_to_translate(request):
	if request.method == 'POST':
		form = TranslateForm(request.POST)
		if form.is_valid():
		#search = form.save(commit=False)
		#search.user = user.request
			search = Translate(
				user=request.user,
				lang_1=request.POST['lang_1'],
				text=request.POST['text'],
				lang_2=request.POST['lang_2'])
			search.save()

		return redirect("translate-home")



	else:
		form = TranslateForm()
	#return redirect('gettext:translate')
	return rrender(request, 'translate/home.html', {'form': form})
'''
'''
def get_text_to_translate(request):
	form = TranslateForm(request.POST)
	if form.is_valid():
		new_search = Translate(
						lang_1=request.POST['lang_1'],
						lang_2=request.POST['lang_2'],
						text=request.POST['text'])
		new_search.user = request.user
		new_search.save()

	return redirect('translate')
'''
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

'''

def new_search(request):
	if request.method == 'POST':
		form = TranslateForm(request.POST)
		if form.is_valid():
			obj = Translate()
			obj.lang_1 = form.cleaned_data['lang_1']
			obj.lang_2 = form.cleaned_data['lang_2']
			obj.text = form.cleaned_data['text']
			obj.user = request.user
			obj.save()
			return redirect("home")

	else:
		form = TranslateForm()

	return render(request, 'translate/home.html', {'form': form})




class TranslateView(TemplateView):
	template_name = 'translate/translate.html'

	def get(self, request):
		form = TranslateForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = TranslateForm(request.POST)
		if form.is_valid():
			search = form.save(commit=False)		# Wait for user to save
			search.user = request.user				# Add user to the object
			search.save()							# Save object to DB

			#input = form.cleaned_data['lang_1', 'text_1', 'lang_2', 'text_2']
			#form.TranslateForm()
			return redirect("translate:translate")

		#args = {'form': form, 'input': input}
		return render(request, self.template_name, {'form': form})#args)


def home(request):
	return render(request, 'translate/home.html')

def translate(request):
	return render(request, 'translate/translate.html')
'''
