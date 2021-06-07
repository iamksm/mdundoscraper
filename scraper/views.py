from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .forms import ArtistForm, ArtistPrefix
from .scraper import find_songs, list_artists


def indexDF(request):  # indexDF - Index Django Form
    """
    The Main Django Form Page
    Creates 2 Forms using Django Forms
    Form gets input as an artist name
    and displays songs they are involved in
    Form2 gets input to list artists with names
    starting with the prefix provided
    """
    if request.method == "POST":
        form = ArtistForm(request.POST)
        form2 = ArtistPrefix(request.POST)
        if form.is_valid():
            the_songs = find_songs(str(form.cleaned_data["artist_name"]))

            if the_songs == []:
                return HttpResponse(
                    f'No results for {form.cleaned_data["artist_name"]}'
                )

            artistname = str(form.cleaned_data["artist_name"])
            return JsonResponse(
                {f"Search Result for {artistname}": the_songs}, safe=False
            )

        elif form2.is_valid():
            names = list_artists(form2.cleaned_data["name_prefix"])
            the_prefix = str(form2.cleaned_data["name_prefix"])
            if names == []:
                return HttpResponse(
                    f'No results for "{form2.cleaned_data["name_prefix"]}"'
                )

            return JsonResponse(
                {f"Artsits name starting with {the_prefix}": names}, safe=False
            )

        else:
            return HttpResponse("Please input some valid data")

    else:
        form = ArtistForm()
        form2 = ArtistPrefix()
        return render(request, "djangoforms.html", {"form": form, "form2": form2})


def indexHF(request):  # indexHF - index HTML Form
    """
    The Main HTML Forms Landing page
    Just like in indexDF
    this view produces 2 forms that are coded into the HTML file
    Basically has the same functionality as in indexDF
    """
    return render(request, "htmlforms.html")


def HFresultsAN(request):  # HFresultsAN - HTML Form results Artist Name
    """
    This View gets the artist name from the IndexHF artist name form
    and returns the result in JSON Format
    """
    name = request.POST["artist_name"]
    the_songs = find_songs(str(name))
    if the_songs != []:
        return JsonResponse({f"Search Resulst for {name}": the_songs}, safe=False)

    else:
        return HttpResponse("Please Input a valid artist name")


def HFresultsAP(request):  # HFresultsAP - HTML Form results Artist Prefix
    """
    This View gets the prefix from the IndexHF prefix form
    and returns the result in JSON Format
    """
    prefix = request.POST["artist_prefix"]
    names = list_artists(prefix)
    if names != []:
        return JsonResponse({f"Artsits Name starting with {prefix}": names}, safe=False)

    else:
        return HttpResponse("Please input a valid prefix")
