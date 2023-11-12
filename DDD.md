# Domain Driven Design (DDD) - Model Aplikacji Bankowej

## Opis Zadania:

Celem zadania jest zamodelowanie fragmentu bezpiecznej aplikacji bankowej, wykorzystując zasady Domain Driven Design (DDD). W ramach modelowania, skupiono się na kilku kluczowych elementach, takich jak zarządzanie kontem, realizacja przelewów, uwierzytelnianie użytkowników, produkty finansowe, analiza ryzyka oraz obsługa klienta. W pliku znajdują się zdefiniowane Bounded Contexts, Agregaty, Encje, Obiekty Wartości, a także informacje dotyczące akceptowanych formatów danych dla atrybutów poszczególnych encji i obiektów wartości.


# Bounded Context: Zarządzanie Kontem

| Agregat          | Encje            | Atrybuty                              | Formaty Danych                    | Metody                           |
|------------------|------------------|---------------------------------------|-----------------------------------|----------------------------------|
| KontoBankowe     | KontoBankowe     | NumerKonta, Saldo, DataUtworzenia     | NumerKonta: string, Saldo: decimal, DataUtworzenia: datetime | RealizujTransakcję(), ZablokujKonto   |
|                  | Transakcja       | IDTransakcji, TypTransakcji, Kwota, DataTransakcji | IDTransakcji: int, TypTransakcji: string, Kwota: decimal, DataTransakcji: datetime | -                               |

# Bounded Context: Przelewy

| Agregat          | Encje            | Atrybuty                              | Formaty Danych                    | Metody                           |
|------------------|------------------|---------------------------------------|-----------------------------------|----------------------------------|
| Przelew          | Przelew          | IDPrzelewu, Kwota, StatusPrzelewu, DataRozpoczęcia, DataZakończenia | IDPrzelewu: int, Kwota: decimal, StatusPrzelewu: string, DataRozpoczęcia: datetime, DataZakończenia: datetime | InicjujPrzelew(), ZatwierdźPrzelew |
|                  | AdresOdbiorcy    | Ulica, Miasto, KodPocztowy             | Ulica: string, Miasto: string, KodPocztowy: string | -                               |
|                  | AdresNadawcy     | Ulica, Miasto, KodPocztowy             | Ulica: string, Miasto: string, KodPocztowy: string | -                               |
|                  | KwotaPrzelewu    | Wartość, Waluta                       | Wartość: decimal, Waluta: string  | -                               |

# Bounded Context: Uwierzytelnienie

| Agregat          | Encje                   | Atrybuty                              | Formaty Danych                    | Metody                           |
|------------------|-------------------------|---------------------------------------|-----------------------------------|----------------------------------|
| Użytkownik       | Użytkownik              | IDUżytkownika, Login                   | IDUżytkownika: int, Login: string | UstawHasło(), SprawdźUprawnienia |
|                  | DaneUwierzytelniajace   | Login, ZaszyfrowaneHasło               | Login: string, ZaszyfrowaneHasło: string | -                               |

# Bounded Context: Produkty Finansowe

| Agregat          | Encje            | Atrybuty                              | Formaty Danych                    | Metody                           |
|------------------|------------------|---------------------------------------|-----------------------------------|----------------------------------|
| Kredyt           | Kredyt           | IDKredytu, Kwota, Oprocentowanie       | IDKredytu: int, Kwota: decimal, Oprocentowanie: decimal | UdzielKredytu(), SpłaćKredyt      |
|                  | Lokata           | IDLokaty, Kwota, Oprocentowanie        | IDLokaty: int, Kwota: decimal, Oprocentowanie: decimal | ZałóżLokatę(), WypłaćLokatę       |
|                  | RachunekDebetowy | IDRachunku, Saldo, LimitDebetu         | IDRachunku: int, Saldo: decimal, LimitDebetu: decimal | WykonajTransakcję(), SpłaćZadłużenie |

# Bounded Context: Analiza Ryzyka

| Agregat          | Encje            | Atrybuty                              | Formaty Danych                    | Metody                           |
|------------------|------------------|---------------------------------------|-----------------------------------|----------------------------------|
| OcenaRyzyka      | OcenaRyzyka      | IDOceny, TypOceny, WynikOceny           | IDOceny: int, TypOceny: string, WynikOceny: string | ProwadźAnalizę(), GenerujRaport  |
|                  | MonitorowanieZabezpieczeń | IDMonitoringu, Status                | IDMonitoringu: int, Status: string | RozpocznijMonitorowanie(), ZakończMonitorowanie  |

# Bounded Context: Obsługa Klienta

| Agregat          | Encje            | Atrybuty                              | Formaty Danych                    | Metody                           |
|------------------|------------------|---------------------------------------|-----------------------------------|----------------------------------|
| ObsługaZgłoszeń  | Zgłoszenie       | IDZgłoszenia, Treść, Status            | IDZgłoszenia: int, Treść: string, Status: string | PrzyjmijZgłoszenie(), RozwiążZgłoszenie  |
|                  | HistoriaInterakcji | IDInterakcji, Data, Opis               | IDInterakcji: int, Data: datetime, Opis: string | DodajInterakcję(), PobierzHistorię  |
|                  | DaneKontaktowe   | IDDanych, AdresEmail, NumerTelefonu    | IDDanych: int, AdresEmail: string, NumerTelefonu: string | AktualizujDane(), PobierzDane    |
