# from typing_extensions import self
from django import forms

from .models import contact, Content_List

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = [
            'Email',
            'Subject',
            'Pesan'
        ]

class Content_List(forms.ModelForm):
    class Meta:
        model = Content_List
        fields = [
            'Judul',
            'Isi',
            'Kategori'
        ]


#Untuk desain forms nya:
    def __init__(self, *args, **kwargs):
        super(ContactForm,self).__init__(*args, **kwargs)
        # self.fields['email', 'subject', 'messages'].widget = contact()
        for idx in self.fields:
            self.fields[idx].widget.attrs['class'] = 'form-control'