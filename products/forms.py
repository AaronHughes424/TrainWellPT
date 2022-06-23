from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductReview


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewProduct(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = [
            'review_product',
        ]

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        labels = {
            'review_content': 'Review',
        }

        self.fields['review_content'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = labels[field] + ""
            if self.fields[field].required:
                placeholder = f'{labels[field]} *'
            else:
                placeholder = labels[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder