# Treść zadania:
```
Stwórz projekt "API w DRF to skracania urli"- coś w rodzaju https://tinyurl.com/app tylko samo API.

Funkcjonalność ma być ekstremalnie minimalistyczna, nie chodzi o dodawanie super features (potraktuj to jako podpowiedź :) tu nie trzeba wiele kodować).

Projekt powinien umożliwiać:

Stworzenie skróconego urla, czyli np. wkładamy `http://example.com/very-very/long/url/even-longer` w zamian dostajemy krótki url wygenerowany przez API, np `http://localhost:8000/shrt/`

Rozwinięcie skróconego urla do oryginalnego, czyli odwrotność poprzedniej operacji.

Jak coś nie jest zrozumiałe to improwizuj i krótko opisz co było niejasne i jaka decyzja została podjęta.
```

# Instalacja


Projekt bazuje na `poetry` (https://github.com/python-poetry/poetry),

Instalacja pakietów:
1. `poetry install --no-root` - Run in current folder create virtualenv and installs packages from `pyproject.toml`
2`poetry shell` - Uruchamia powłokę shell z wirtualnym środowiskiem

# Uruchomienie projektu

Uruchomienie lokale:
* `python manage.py migrate`
* `python manage.py runserver`

Przykład zapytania:

```
curl --location 'localhost:8000/reduce_url/' \
--header 'Content-Type: application/json' \
--data '{
	"original_url": "https://justjoin.it/job-offer/szko-a-w-chmurze-product-owner-warszawa-pm"
}'
```

Przykładowa odpowiedź:

```
{
    "short_url": "http://localhost:8000/YKY5ImU7"
}
```

Example get short url:
```
curl --location 'localhost:8000/YKY5ImU7/'
```


Z uwagi na to, jakiego zagadnienia dotyczy zadanie, rozwiązać je można na kilka sposobów.

Zgodnie z wytycznymi zrobiłem zadanie jak najprościej, wykorzystując gotowe elementy DRF. Dodałem również podstawową walidację i zabezpieczenie przed możliwymi do wystąpienia błędami.

Z uwagi na wbudowaną walidację serializerów oraz gotowe mixiny do tworzenia wpisów w bazie, zdecydowałem się na użycie mixina CreateModelMixin.

W przypadku przekierowania na krótki URL, zdecydowałem się na użycie decoratora api_view, gdyż mamy do czynienia z sytuacją, gdy chcemy pobierać element inaczej niż po id. Wtedy gotowe widoki wymagają więcej zmian.

W związku z możliwym wystąpieniem kolizji w czasie tworzenia obiektu, zdecydowałem się na kilkukrotne generowanie skrótów z skończoną liczbą powtórzeń, aby nie zablokować aplikacji.
Są możliwe różne podejścia do rozwiązania problemu kolizji w przypadku generowania skrótów.

Na dalszym etapie można rozważyć usuwanie przestarzałych wpisów w celu zwolnienia zajętych już skrótów.
