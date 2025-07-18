

from django import forms
from .models import ContactMessage
from skills.models import AddSkills

class ContactForm(forms.ModelForm):
    def __init__(self, *args, qs=None, **kwargs):
        """
        If the user has no available skills 
        we change the form to accommodate that.
        """
        super().__init__(*args, **kwargs)
        self.fields['skill'].queryset = qs or AddSkills.objects.none()

        if not self.fields['skill'].queryset.exists():
            form = self.fields['skill']
            form.empty_label = "No skills to offer"
            form.required = False
            form.widget.attrs['disabled'] = True
    class Meta:
        model= ContactMessage
        fields= ['recipient', 'email', 'message','skill']
        widgets= {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
