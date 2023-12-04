from django import forms
from .models import Major, Course
from .user_forms import UserForm

class MajorRequirementsForm(forms.ModelForm):
    communication = forms.ModelMultipleChoiceField(
        queryset=Course.objects.filter(section='communication'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    mathematics = forms.ModelMultipleChoiceField(
        queryset=Course.objects.filter(section='mathematics'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    social_and_behavioral_sciences = forms.ModelMultipleChoiceField(
        queryset=Course.objects.filter(section='social_and_behavioral_sciences'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    component_area_option = forms.ModelMultipleChoiceField(
        queryset=Course.objects.filter(section='component_area_option'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    cis_requirements = forms.ModelMultipleChoiceField(
        queryset=Course.objects.filter(section='cis_requirements'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    nine_hours_from = forms.ModelMultipleChoiceField(
        queryset=Course.objects.filter(section='nine_hours_from'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    advanced_cidm_electives = forms.ModelMultipleChoiceField(
        queryset=Course.objects.filter(section='advanced_cidm_electives'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Major
        fields = [
            'communication', 'mathematics', 'social_and_behavioral_sciences',
            'component_area_option', 'cis_requirements', 'nine_hours_from',
            'advanced_cidm_electives'
        ]

    def __init__(self, *args, **kwargs):
        user_profile = kwargs.pop('user_profile', None)
        super().__init__(*args, **kwargs)

        if user_profile:
            for field_name in self.fields:
                field = self.fields[field_name]
                if isinstance(field.widget, forms.CheckboxSelectMultiple):
                    field.widget.attrs.update({'class': 'form-check-input'})
                field.queryset = Course.objects.filter(section=self.get_section_for_field(field_name))

    def get_section_for_field(self, field_name):
        # Provide the appropriate section based on the field name
        if field_name == 'communication':
            return 'communication'
        elif field_name == 'mathematics':
            return 'mathematics'
        elif field_name == 'social_and_behavioral_sciences':
            return 'social_and_behavioral_sciences'
        elif field_name == 'component_area_option':
            return 'component_area_option'
        elif field_name == 'cis_requirements':
            return 'cis_requirements'
        elif field_name == 'nine_hours_from':
            return 'nine_hours_from'
        elif field_name == 'advanced_cidm_electives':
            return 'advanced_cidm_electives'
        else:
            return ''
