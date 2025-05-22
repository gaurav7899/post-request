from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit,Div

class DemoRegister(forms.Form):
    name= forms.CharField()
    email=forms.EmailField()
    age=forms.FloatField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_class = 'border p-8'
        # self.helper.layout = Layout(
        #     Div(
        #         Div('name', css_class="md:w-[50%]"),
        #         Div('email', css_class="md:w-[50%]"),
        #         css_class="md:flex md:justify-between"
        #     ),
        #     'email',
        #     Submit('submit', 'Submit', css_class='text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800'),
        # )