from django.forms import ModelForm, TextInput
from product.models import Product

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'small_description', 'description', 'image', 'quantity', 'category']
        localized_fields = ['price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].error_messages={'required': 'Campo obrigatório.'}
        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-sm'})
        
        self.fields['small_description'].error_messages={'required': 'Campo obrigatório'}
        self.fields['small_description'].widget = TextInput()
        self.fields['small_description'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['description'].error_messages={'required': 'Campo obrigatório'}
        self.fields['description'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['category'].error_messages={'required': 'Campo obrigatório'}
        self.fields['category'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['price'].min_value=0
        self.fields['price'].error_messages={'required': 'Campo obrigatório.',
                                             'invalid': 'Valor inválido.',
                                             'max_digits': 'Mais de 5 dígitos no total.',
                                             'max_decimal_places': 'Mais de 2 dígitos decimais.',
                                             'max_whole_digits': 'Mais de 3 dígitos inteiros.'}
        self.fields['price'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })

        self.fields['quantity'].min_value=0
        self.fields['quantity'].error_messages={
            'required': 'Campo obrigatório',
            'min_value': 'A quantidade deve ser maior ou igual a zero.'
        }
        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control form-control-sm',
        })

        self.fields['image'].error_messages={'required': 'Campo obrigatório',
                                              'invalid_image': 'Imagem inválida.'}
        self.fields['image'].widget.attrs.update({'class': 'btn btn-outline-secondary btn-sm'})