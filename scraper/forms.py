from django import forms


class ArtistForm(forms.Form):
    artist_name = forms.CharField(label="Artist Name ", max_length=20)


class ArtistPrefix(forms.Form):
    name_prefix = forms.CharField(label="Name Prefix ", max_length=1)
