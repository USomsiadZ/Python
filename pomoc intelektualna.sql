
--zad a
SELECT do.imie, do.nazwisko, COUNT(*) AS liczba_wnukow 
FROM osoba o 
JOIN dane_osoby do ON o.Id = do.Dane_ID
JOIN rodzic r ON o.Id = r.rodzic_id
JOIN rodzic r2 ON r.dziecko_id = r2.rodzic_id
GROUP BY do.imie, do.nazwisko
ORDER BY liczba_wnukow DESC
LIMIT 1;

--zad b stare
SELECT f.Nazwa, t.Nazwa, COUNT(*) as liczba_pracownikow FROM osoba do
JOIN praca p ON p.Praca_ID = do.Praca_ID
JOIN typ_pracy t on p.Typ_pracy_id = t.Typ_pracy_id
JOIN firma f ON f.ID = p.Firma_ID
GROUP BY f.Nazwa, p.Typ_pracy_id;

--zadanie b nowe
SET @wszyscy =(SELECT COUNT(*) FROM praca);
SELECT t.Nazwa, convert((COUNT(p.Pracownik_ID) / @wszyscy * 100),UNSIGNED) as procent_zatrudnienia
FROM praca p 
JOIN firma f ON f.ID = p.Firma_ID
JOIN typ_pracy t on p.Typ_pracy_id = t.Typ_pracy_id
GROUP BY t.Nazwa

--zad c 2 pokolenia stare
SELECT o.Dane_ID,do.imie, do.nazwisko, COALESCE(p.Zarobki, 0) + COALESCE(mp.Zarobki, 0) + COALESCE(pr.Zarobki, 0) as zarobki FROM osoba o 
JOIN dane_osoby do ON o.Dane_ID = do.Dane_ID
LEFT JOIN osoba m on o.Malzonek_ID = m.ID
LEFT JOIN praca mp on m.Praca_ID = mp.Praca_ID
LEFT JOIN praca p ON o.Praca_ID = p.Praca_ID
LEFT JOIN rodzic r ON r.Rodzic_ID = o.Id
LEFT JOIN osoba orr ON orr.id = r.rodzic_id
LEFT JOIN Praca pr On orr.Praca_ID = pr.Praca_ID
GROUP BY do.imie, do.nazwisko
ORDER BY zarobki DESC
LIMIT 1

--zad c 1 pokolenie stare
SELECT o.Dane_ID,do.imie, do.nazwisko, COALESCE(p.Zarobki, 0) + COALESCE(mp.Zarobki, 0) as zarobki FROM osoba o 
JOIN dane_osoby do ON o.Dane_ID = do.Dane_ID
LEFT JOIN osoba m on o.Malzonek_ID = m.ID
LEFT JOIN praca mp on m.Praca_ID = mp.Praca_ID
LEFT JOIN praca p ON o.Praca_ID = p.Praca_ID
GROUP BY do.imie, do.nazwisko
ORDER BY zarobki DESC
LIMIT 1

--zad c 1 pokolenie nowe                         
SELECT p.Pracownik_ID, SUM(p.Zarobki) as Zarobki, sum(pr.Zarobki) as Zarobki_Malzonka
FROM praca p
JOIN osoba o ON o.ID = p.Pracownik_ID --*Łączy tabele osoba z praca jako o
JOIN osoba om ON om.ID = o.Malzonek_ID --*Przyłącza tabele małżonka jako om
JOIN praca pr ON om.ID = pr.Pracownik_ID--*Przyłącza tabele pracy małżonka
GROUP BY p.Pracownik_ID;--* grupuje według osób
--! Kiedy sumuje się zarobki z kilku prac SUM(pp.Zarobki) to zarobki małżona stają się o ilość prac razy większe tutaj o 2


--zad c 1 pokolenie nowe
SELECT p.Pracownik_ID, SUM(p.Zarobki) as Zarobki, 
(SELECT SUM(pr.Zarobki) FROM praca pr WHERE om.ID = pr.Pracownik_ID) as Zarobki_Malzonka
FROM praca p
JOIN osoba o ON o.ID = p.Pracownik_ID 
JOIN osoba om ON om.ID = o.Malzonek_ID 
GROUP BY p.Pracownik_ID;


























--pokazuje kontakty mysql
SELECT u.email as Twoj_email, ku.email as Kontakt_email FROM kontakty k 
LEFT JOIN uzytkownicy u on k.uzytkownik_ID = u.Uzytkownik_ID 
LEFT JOIN uzytkownicy ku on k.kontakt_ID = ku.Uzytkownik_ID 
WHERE u.email = 1
--zmien email na id
select k.kontakt_ID from kontakty k 
JOIN uzytkownicy u on u.uzytkownik_ID 