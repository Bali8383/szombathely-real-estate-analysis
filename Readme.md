# 🏠 Szombathelyi Ingatlanpiaci Analitika 2026

## 👨‍💻 Fejlesztői Profil
**Kovács Balázs** – *Szoftverfejlesztő BSc hallgató (Brigham Young University - Idaho)*

Ez a projekt a BYU-Idaho egyetemen végzett tanulmányaim során elsajátított adatbázis-kezelési (SQL) és Python programozási ismereteim gyakorlati alkalmazása. A cél egy olyan technikai megoldás bemutatása, amely valós adatokon alapulva segíti a helyi ingatlanpiaci döntéshozatalt.

---

## 🎯 Projekt Áttekintése
A szoftver egy automatizált adatfeldolgozó rendszer, amely a szombathelyi ingatlanpiac összefüggéseit elemzi. Segítségével vizuálisan is átláthatóvá válik az ingatlanok alapterülete és piaci ára közötti kapcsolat a különböző városrészekben (pl. Belváros, Oladi domb, Derkovits-lakótelep).

## 🛠️ Technológiai Eszköztár
* **Nyelv:** Python 3.10+
* **Adatbázis:** SQLite3 (Relációs adatmodellezés)
* **Adatkezelés:** Pandas (DataFrame műveletek)
* **Vizualizáció:** Seaborn & Matplotlib (Haladó statisztikai grafikonok)
* **Verziókezelés:** Git & GitHub

## 🚀 Főbb Funkciók
1.  **Automatizált Adatbázis Életciklus:** A program indításkor automatikusan létrehozza, validálja és naprakész adatokkal tölti fel az SQL táblákat.
2.  **Robusztus Hibakezelés:** Beépített `try-except` blokkok biztosítják a szoftver stabilitását adatbázis-hiba vagy hiányzó függőségek esetén.
3.  **Adatvezérelt Betekintés:**
    * **Színkódolt Pontdiagram:** A pontok színe az árszintet tükrözi (Magma színskála).
    * **Buborék-méretezés:** A pontok mérete az ingatlan alapterületét szemlélteti.
    * **Regressziós Analízis:** Beépített trendvonal segíti a piaci anomáliák és a túlárazott ingatlanok felismerését.



## 📊 Piaci Következtetések (Insights)
Az elemzés rávilágít a lokáció és a presztízsérték hatására a szombathelyi piacon:
* **Prémium Övezetek:** Az Oladi domb és a Sarlay-telep ingatlanai konzisztensen a trendvonal felett helyezkednek el, jelezve a magasabb négyzetméterárat.
* **Befektetési Lehetőségek:** A lakótelepi övezetek (Derkovits, Joskar-Ola) lineárisabb, kiszámíthatóbb árazási modellt mutatnak, ami stabil befektetési környezetet sugall.

## 🛠️ Telepítés és Futtatás

1. A tároló (repository) másolása:
   ```bash
   git clone [https://github.com/kovacsbalazs/szombathely-ingatlan-vizu.git](https://github.com/kovacsbalazs/szombathely-ingatlan-vizu.git)