from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from case_study.models import Response
from django.utils.safestring import mark_safe


class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model= User
        fields = ('username', 'email', 'password',)

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label=""
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label=""
        self.fields['email'].help_text='<span class="form-text text-muted"><small>We\'ll never share your email with anyone else.</small></span>'


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", help_text='<span class="form-text text-muted"><small>We\'ll never share your email with anyone else.</small></span>', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label=""
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label=""
        self.fields['password1'].help_text='<ul class="form-text text-muted"><small><li>Your password must contain at least 8 characters.</li></small></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label=""
        self.fields['password2'].help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


####################### MY ADDITION STARTS HERE #############################################################

class EditPasswordForm(PasswordChangeForm):

# PasswordChangeForm is not a ModelForm so Meta.widgets is not working here. You have
# to set widget's attrs in the __init__() constructor as done below:

    def __init__(self, *args, **kwargs):
        super(EditPasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['placeholder'] = 'Enter Old Password'
        self.fields['old_password'].label=""

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Enter New Password'
        self.fields['new_password1'].label=""
        self.fields['new_password1'].help_text='<span class="form-text text-muted"><small>Your password must contain at least 8 characters.</small></span>'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'
        self.fields['new_password2'].label=""
        self.fields['new_password2'].help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

# the entire line under "super(EditPasswordForm, self).__init__(*args, **kwargs)"
# in the function __init__ above can be written as:
#
# for field in ('old_password', 'new_password1', 'new_password2'):
#     self.fields[field].widget.attrs = {'class': 'form-control'}
#
# However, writing it this way limits the freedom to change the attr of all
# fields. hence, wrote the code as above. Note that 'old_password',
# 'new_password1', 'new_password2' are original fields in the database
# and must be used as it is.



class ResponseForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta():
        model = Response
        fields = ('student', 'professional', 'creativity_meaning','creative', 'creativity_example', 'hand', 'trial_signup',)

        widgets = {
            'student': forms.Select(), 'professional': forms.Select(), 'creative': forms.RadioSelect(), 'hand': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super(ResponseForm, self).__init__(*args, **kwargs)

        self.fields['student'].label="1. Select your current level of education if you are a student"
        self.fields['student'].help_text='<span> </span>'

        self.fields['professional'].label="2. Select your years of experience if you are a professional or not a student"
        self.fields['professional'].help_text='<span> </span>'

        self.fields['creativity_meaning'].widget.attrs['class'] = 'form-control'
        self.fields['creativity_meaning'].widget.attrs['placeholder'] = 'Type in your response here. If you do not know what creativity or to be creative means, please state here.'
        self.fields['creativity_meaning'].label=mark_safe("3. In your own understanding, what does it mean when someone is said to be creative? <br /> (Please feel free to provide as much details as you possibly can)")
        self.fields['creativity_meaning'].help_text='<span class="form-text text-muted"><small>Up to 2000 characters can be typed.</small></span>'

        self.fields['creative'].label="4. Do you consider yourself creative?"
        self.fields['creative'].help_text='<span><div></div></span>'

        self.fields['creativity_example'].widget.attrs['class'] = 'form-control'
        self.fields['creativity_example'].widget.attrs['placeholder'] = 'Type in your response here.'
        self.fields['creativity_example'].label=mark_safe("5. Consider your response in question 4. Why do you think you are creative or not creative? <br /> (That is, the things you can or cannot do that makes you creative or not creative)")
        self.fields['creativity_example'].help_text='<span class="form-text text-muted"><small>Up to 2000 characters can be typed.</small></span>'

        self.fields['hand'].label="6. Which of your hands do you predominantly use for writing?"
        self.fields['hand'].help_text=mark_safe('<span><small>____________ <br /> At SRL, we are developing a computational creativity tool: Pro-Explora, to support design engineers in difficult creativity tasks. If you would like to try this tool, please check the Accept box below.</small></span>')

        self.fields['trial_signup'].label= "Accept"
        self.fields['trial_signup'].help_text='<span><div></div></span>'
