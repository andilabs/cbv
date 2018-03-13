from django.forms import ModelForm, CharField, Textarea
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from demo.models import Item


class ItemForm(ModelForm):
    description = CharField(widget=Textarea)

    class Meta:
        model = Item
        fields = ['code', 'amount']

    def save(self, commit=True):
        item = super(ItemForm, self).save(commit=commit)
        item.code.description = self.cleaned_data['description']
        item.code.save()

    def get_initial_for_field(self, field, field_name):
        if field_name == 'description':
            return self.instance.code.description
        else:
            return super(ItemForm, self).get_initial_for_field(field, field_name)


class ItemUpdateView(UpdateView):

    form_class = ItemForm
    model = Item

    def get_success_url(self):
        return reverse_lazy('item-detail', kwargs={'pk': 1})
