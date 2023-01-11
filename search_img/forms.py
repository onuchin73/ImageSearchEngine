from django import forms


class SearchForm(forms.Form):
    IMAGE_TYPE = [
        ('', ''),
        ('jpg', '.JPG'),
        ('gif', '.GIF'),
        ('png', '.PNG'),
    ]

    image_type = forms.CharField(label='Image type', max_length=3, widget=forms.Select(choices=IMAGE_TYPE))
    count = forms.TypedChoiceField(label='Image count', choices=[(i, str(i)) for i in range(1, 11)], coerce=int)
