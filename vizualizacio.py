import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def setup_database(conn):
    """Létrehozza a táblát és feltölti adatokkal, ha üres."""
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS hirdetesek")
    cursor.execute("""
        CREATE TABLE hirdetesek (
            varosresz TEXT,
            ar_millio REAL,
            meret_m2 INTEGER,
            tipus TEXT
        )
    """)
    piaci_adatok = [
        ('Belváros', 68.5, 75, 'Tégla'),
        ('Oladi domb', 82.0, 90, 'Új építésű'),
        ('Oladi ltp.', 38.5, 55, 'Panel'),
        ('Derkovits ltp.', 41.0, 58, 'Panel'),
        ('Kámon', 75.0, 110, 'Családi ház'),
        ('Újperint', 88.0, 125, 'Családi ház'),
        ('Joskar-Ola', 35.0, 52, 'Panel'),
        ('Sarlay-telep', 95.0, 85, 'Prémium'),
        ('Kiszely ltp.', 44.5, 62, 'Tégla'),
        ('Zanat', 79.0, 130, 'Családi ház')
    ]
    cursor.executemany("INSERT INTO hirdetesek VALUES (?, ?, ?, ?)", piaci_adatok)
    conn.commit()

def run_analysis():
    db_name = 'szombathelyi_ingatlanok.db'
    
    try:
        conn = sqlite3.connect(db_name)
        
        # 1. Adatok ellenőrzése/beállítása
        setup_database(conn)
        
        # 2. Adatok beolvasása
        df = pd.read_sql_query("SELECT * FROM hirdetesek", conn)
        
        if df.empty:
            print("Hiba: Nincsenek adatok az adatbázisban.")
            return

        # 3. Professzionális vizualizáció
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(12, 8))
        
        # Buborékdiagram
        scatter = sns.scatterplot(
            data=df, 
            x='meret_m2', 
            y='ar_millio', 
            hue='ar_millio', 
            size='meret_m2',
            sizes=(100, 600),
            palette='magma',
            edgecolor='black',
            alpha=0.8,
            legend=None
        )

        # Feliratozás
        for i in range(df.shape[0]):
            plt.text(
                df.meret_m2[i]+2, 
                df.ar_millio[i]+1, 
                df.varosresz[i], 
                fontsize=10, 
                fontweight='bold',
                bbox=dict(facecolor='white', alpha=0.6, edgecolor='none')
            )

        # Trendvonal és design
        sns.regplot(data=df, x='meret_m2', y='ar_millio', scatter=False, color='gray', line_kws={"ls":"--", "lw":1})
        
        plt.title('Szombathelyi Ingatlanpiaci Elemzés - 2026', fontsize=20, fontweight='bold', pad=20)
        plt.xlabel('Alapterület (m²)', fontsize=14)
        plt.ylabel('Vételár (Millió Ft)', fontsize=14)
        
        plt.tight_layout()
        print("Grafikon sikeresen elkészült!")
        plt.show()

    except sqlite3.DatabaseError:
        print(f"HIBA: A(z) {db_name} fájl nem érvényes adatbázis!")
    except Exception as e:
        print(f"Hiba történt: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    run_analysis()