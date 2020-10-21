from django import forms
from django.contrib.admin import widgets
from core.models import TiendaCategoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = TiendaCategoria
        fields = '__all__'

    subcategorias = forms.ModelMultipleChoiceField(queryset=TiendaCategoria.objects.none(),widget=widgets.FilteredSelectMultiple(verbose_name='Sub Categorías', is_stacked=False), required=False)

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)

        self.fields['abc'] = forms.CharField(required=False)
        self.initial['abc'] = 'test'

        if self.instance:
            self.fields['subcategorias'].queryset = TiendaCategoria.objects.filter(tienda=self.instance.tienda, categoriaPadre=None, activa=True).exclude(id=self.instance.id)