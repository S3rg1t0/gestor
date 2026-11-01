from django import forms
from .models import Motor


class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = ('code_bar', 'defects',)

        widgets = {
            'defects': forms.CheckboxSelectMultiple(),
        }

    def clean_code_bar(self):

        code_bar = self.cleaned_data['code_bar'].strip()
        parts = code_bar.split('TD')

        if len(parts) != 2 or not all(parts):
            raise forms.ValidationError('Introduce un código correcto')
        return code_bar

    def clean_defects(self):

        defects = self.cleaned_data['defects']

        if not defects.exists():
            raise forms.ValidationError('Selecciona un defecto al menos')

        return defects

    def save(self, commit=True):
        instance = super().save(commit=False)

        n_engine, reference = instance.code_bar.split('TD', 1)
        instance.n_engine = n_engine
        instance.reference = reference

        if commit:
            instance.save()
            self.save_m2m()

        return instance


