from django import forms

class URLShortenForm(forms.Form):
    url = forms.URLField(label='URL', required=True)

