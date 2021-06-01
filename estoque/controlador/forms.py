from  django.forms import ModelForm
from  controlador.models import Prateleira

class  PrateleiraForm(ModelForm):
    class  Meta:
        model = Prateleira
        fields = ['product_name', 'product_describe'] 