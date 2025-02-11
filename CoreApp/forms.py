from django import forms
from .models import TodoList


#ModelForm <- Generate a form from django models automaticallySubmit
class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['task','start_date','end_date','completed']
        widgets = {  
            'task': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500', 'placeholder': 'Enter your task'}),  
            'start_date': forms.DateInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500', 'type': 'date'}),  
            'end_date': forms.DateInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500', 'type': 'date'}),  
            'completed': forms.CheckboxInput(attrs={'class': 'w-5 h-5 text-blue-500 rounded focus:ring-blue-500'}),  
        }  


#manual form 
# class TodoForm(forms.Form):
#     task = forms.CharField(max_length=50)
#     start_date = forms.DateField()
#     end_date = forms.DateField()
#     completed = forms.BooleanField(initial=False)


