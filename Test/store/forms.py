from django import forms


from .models import Member, Course,Department

gender_choice = [
    ('1', 'Male'),
    ('2', 'Female'),
    ('3', 'Other')
]


purpose_choice = [
 ('To Order', 'To Order'),
 ('Return', 'Return'),
 ('Enquiry', 'Enquiry'),
 ('Stock check', 'Stock check'),
]


Materials_choice = [
 ('Pen', 'Pen'),
 ('Pencil', 'Pencil'),
 ('Textbooks', 'Textbooks'),
 ('Notebooks', 'Notebooks'),
]

class MemberCreationForm(forms.ModelForm):


    gender = forms.ChoiceField(choices=gender_choice, widget=forms.RadioSelect)

    materials = forms.MultipleChoiceField(label='Materials', choices=Materials_choice,widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Member
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'dob':forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
                   'age':forms.NumberInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'address':forms.TextInput(attrs={'class': 'form-control'}),
                   'ph_no': forms.NumberInput(attrs={'class': 'form-control'}),
                   'department': forms.Select(attrs={'class': 'form-select'}),
                   'course': forms.Select(attrs={'class': 'form-select'}),
                   'purpose': forms.Select(choices=purpose_choice,attrs={'class': 'form-select'}),

        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()
        self.fields['dob'].queryset = Member.objects.none()
        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')