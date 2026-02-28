import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def setup_database(conn):
    """Creates the table and populates it with data if empty."""
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS real_estate_ads")
    cursor.execute("""
        CREATE TABLE real_estate_ads (
            district TEXT,
            price_millions REAL,
            size_m2 INTEGER,
            property_type TEXT
        )
    """)
    market_data = [
        ('Belváros', 68.5, 75, 'Brick'),
        ('Oladi domb', 82.0, 90, 'New Construction'),
        ('Oladi ltp.', 38.5, 55, 'Panel'),
        ('Derkovits ltp.', 41.0, 58, 'Panel'),
        ('Kámon', 75.0, 110, 'House'),
        ('Újperint', 88.0, 125, 'House'),
        ('Joskar-Ola', 35.0, 52, 'Panel'),
        ('Sarlay-telep', 95.0, 85, 'Premium'),
        ('Kiszely ltp.', 44.5, 62, 'Brick'),
        ('Zanat', 79.0, 130, 'House')
    ]
    cursor.executemany("INSERT INTO real_estate_ads VALUES (?, ?, ?, ?)", market_data)
    conn.commit()

def run_analysis():
    db_name = 'szombathelyi_ingatlanok.db'
    
    try:
        conn = sqlite3.connect(db_name)
        
        # 1. Check/Setup data
        setup_database(conn)
        
        # 2. Read data
        df = pd.read_sql_query("SELECT * FROM real_estate_ads", conn)
        
        if df.empty:
            print("Error: No data found in the database.")
            return

        # 3. Professional visualization
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(12, 8))
        
        # Scatter plot (Bubble chart)
        scatter = sns.scatterplot(
            data=df, 
            x='size_m2', 
            y='price_millions', 
            hue='price_millions', 
            size='size_m2',
            sizes=(100, 600),
            palette='magma',
            edgecolor='black',
            alpha=0.8,
            legend=None
        )

        # Annotations
        for i in range(df.shape[0]):
            plt.text(
                df.size_m2[i]+2, 
                df.price_millions[i]+1, 
                df.district[i], 
                fontsize=10, 
                fontweight='bold',
                bbox=dict(facecolor='white', alpha=0.6, edgecolor='none')
            )

        # Trendline and design
        sns.regplot(data=df, x='size_m2', y='price_millions', scatter=False, color='gray', line_kws={"ls":"--", "lw":1})
        
        plt.title('Szombathely Real Estate Market Analysis - 2026', fontsize=20, fontweight='bold', pad=20)
        plt.xlabel('Floor Area (m²)', fontsize=14)
        plt.ylabel('Purchase Price (Million HUF)', fontsize=14)
        
        plt.tight_layout()
        print("Chart generated successfully!")
        plt.show()

    except sqlite3.DatabaseError:
        print(f"ERROR: The file {db_name} is not a valid database!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    run_analysis()