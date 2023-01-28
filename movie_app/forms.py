from django import forms

from .models import Reviews, Rating, RatingStar

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ReviewsForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    """Форма отзывов"""

    class Meta:
        model = Reviews
        fields = ("name", "email", "text", "captcha")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border"}),
            "email": forms.EmailInput(attrs={"class": "form-control border"}),
            "text": forms.Textarea(attrs={"class": "form-control border"}),
        }


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""

    star = forms.ModelChoiceField(queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None)

    class Meta:
        model = Rating
        fields = ("star",)
