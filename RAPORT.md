#Warcaby - Raport
##Założenia projektowe
Założeniem projektu było stworzenie gry w warcaby w języku python.
Gra została zrobiona na zasadach:
* Plansza 8x8
* Pionki poruszają się o jedno pole i zbijają tylko w przód
* Damy mogą poruszać się i zbijać we wszystkie strony, przy zbijaniu dama zatrzymują się na polu za zbitym pionkiem 
##Ogólny opis kodu
Cały program został zawarty w jednym pliku oraz w jednej klasie, która implementuje wszystko co jest jej potrzebne
do przeprowadzenia rozgrywki. Do stworzenia okna z grą wykorzystałem bibliotekę tkinter, która była polecana w treści projektu.
Pola przeznaczone do ruchu pionków oparte są na przyciskach. Pionek jest napisem, który jest aktualizowany na danym polu po każdym ruchu.
##Co udało się zrobić
Udało się zrealizować następujące rzeczy:
* Planszę 8x8
* Wyświetlanie nad planszą informacji czyja jest tura
* Wyświetlanie pionków oraz dam wraz z ich zaznaczaniem
* Logikę poruszania się danego pionka
* Zakończenie rozgrywki, gdy jeden z graczy nie będzie miał już pionków
* Resetowanie rozgrywki bez zamykania głównego okna
##Z czym były problemy
Największe problemy były z napisaniem funckji odpowiedzialnej za ruch oraz możliwość zbijania pionków. Napotkałem tutaj
wiele problemów, najtrudniej było ze sprawdzaniem, czy na lini ruchu, który chcemy wykonać damą, nie stoją inne pionki.
##Linki do istotnych fragmentów kodu
[Lambda 1](https://github.com/dawrop/Warcaby/blob/b8cca0837b6b0f1281178772013717656ae268ad/game.py#L63-L64) <br>
[Lambda 2](https://github.com/dawrop/Warcaby/blob/b8cca0837b6b0f1281178772013717656ae268ad/game.py#L96) <br><br>
[List comprehensions](https://github.com/dawrop/Warcaby/blob/b8cca0837b6b0f1281178772013717656ae268ad/game.py#L53-L54)
##Link do repozytorium
[Repozytorium projektu](https://github.com/dawrop/Warcaby)


