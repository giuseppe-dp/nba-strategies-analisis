# NBA Strategies Analysis 🏀📊

Un'analisi quantitativa sull'evoluzione delle strategie di gioco nell'NBA dal 1985 al 2022, con un focus particolare sull'impatto dell'introduzione del tiro da 3 punti.

## 🎯 Cosa ho fatto
Il progetto analizza come il tiro da tre punti abbia alterato l'equilibrio strategico tra attacco e difesa nell'NBA moderna, imponendo un nuovo paradigma di gioco. L'obiettivo è quantificare il successo agonistico superando la semplice analisi del volume di tiri, focalizzandosi sull'efficienza realizzativa e sulla gestione del possesso.

Nello specifico, sono state calcolate e messe in relazione con le vittorie le seguenti metriche:
*   **eFG% (Effective Field Goal Percentage):** Per valutare l'efficienza pesando il maggior valore (+50%) del tiro da tre rispetto a quello da due.
*   **TOV% (Turnover Percentage):** Per misurare la dissipazione dei possessi a causa delle palle perse.
*   **ORB% (Offensive Rebound Percentage):** Per valutare l'efficacia della rigenerazione di un nuovo possesso dopo un errore al tiro.

## 🛠️ Come l'ho fatto
L'elaborazione dei dati si è articolata in tre fasi principali, gestite interamente tramite script Python eseguiti sequenzialmente da terminale:
1.  **Acquisizione e Preprocessing:** I dati grezzi (games) sono stati estratti da un database SQLite tramite query SQL. La pulizia e il filtraggio temporale (1985-2022) sono stati eseguiti con la libreria `pandas`.
2.  **Analisi Statistica:** Dopo un'ispezione esplorativa con `D-Tale`, sono stati generati modelli di regressione lineare. I coefficienti di correlazione di Pearson (r) e i relativi p-value sono stati calcolati utilizzando `scipy.stats`.
3.  **Visualizzazione:** L'impatto visivo e grafico dei risultati è stato realizzato mediante `matplotlib`.

## 📈 Risultati Principali
*   **Il paradosso del volume:** L'aumento dei tiri da 3 non garantisce un aumento diretto della probabilità di vittoria (r ≈ 0.09). 
*   **L'efficienza domina:** L'efficienza effettiva (eFG%) è invece un indicatore primario del successo agonistico (r ≈ 0.48), confermando che conta la qualità dell'esecuzione rispetto al numero di tentativi.
*   **Gestione dell'errore:** La protezione del pallone (TOV%) è critica per vincere (r ≈ -0.27), mentre il rimbalzo offensivo (ORB%) è diventato una metrica irrilevante per la vittoria (r ≈ 0.03). 
*   **Evoluzione storica:** A causa del maggiore spacing, le squadre hanno progressivamente rinunciato ai rimbalzi offensivi per favorire la transizione difensiva, portando a un crollo storico della metrica nel tempo (r ≈ -0.82).

## 🚀 Utilizzo del codice
Il progetto è strutturato tramite programmi Python progettati per essere lanciati da terminale, passo dopo passo. 

I file principali sono:
*   `Analisi_Strategie_Nba.pdf`: Lo studio completo scritto in LaTeX, comprensivo di grafici e risultati dettagliati.
*   `data_import.py`: Script per scaricare e importare il dataset da Kaggle.
*   `three_script.py`: Script principale per eseguire l'analisi dei dati e generare i grafici.



# NBA Strategies Analysis 🏀📊

A quantitative analysis of the evolution of NBA game strategies from 1985 to 2022, focusing specifically on the impact of the 3-point shot.

## 🎯 What I Did
This project analyzes how the three-point shot has altered the strategic balance between offense and defense in the modern NBA, establishing a new game paradigm. The goal is to quantify competitive success beyond simple shot volume analysis, focusing instead on scoring efficiency and possession management.

Specifically, the following metrics were calculated and correlated with team wins:
*   **eFG% (Effective Field Goal Percentage):** To evaluate scoring efficiency by weighting the added value (+50%) of a three-point shot compared to a two-pointer.
*   **TOV% (Turnover Percentage):** To measure possession waste due to turnovers.
*   **ORB% (Offensive Rebound Percentage):** To evaluate the effectiveness of generating a new possession after a missed shot.

## 🛠️ How I Did It
Data processing was divided into three main phases, entirely managed via Python scripts executed sequentially from the terminal:
1.  **Acquisition and Preprocessing:** Raw data (games) was extracted from an SQLite database using SQL queries. Data cleaning and temporal filtering (1985-2022) were performed using the `pandas` library.
2.  **Statistical Analysis:** Following an exploratory inspection with `D-Tale`, linear regression models were generated. Pearson correlation coefficients (r) and their respective p-values were calculated using `scipy.stats`.
3.  **Visualization:** The visual and graphical representation of the results was created using `matplotlib`.

## 📈 Key Findings
*   **The volume paradox:** The increase in 3-point shot attempts does not guarantee a direct increase in win probability (r ≈ 0.09).
*   **Efficiency dominates:** Effective efficiency (eFG%) is a primary indicator of competitive success (r ≈ 0.48), confirming that execution quality matters far more than the sheer volume of attempts.
*   **Error management:** Ball protection (TOV%) is critical for winning (r ≈ -0.27), whereas offensive rebounding (ORB%) has become an irrelevant metric for victory (r ≈ 0.03).
*   **Historical evolution:** Due to increased floor spacing, teams have progressively abandoned offensive rebounds to prioritize defensive transition, leading to a historic collapse of this metric over time (r ≈ -0.82).

## 🚀 How to Use the Code
The project is structured around Python programs designed to be executed step-by-step via the terminal.

The main files are:
*   `nba_strategies_analysis.pdf`: The complete study written in LaTeX, including detailed graphs and results.
*   `data_import.py`: The script used to download and import the dataset from Kaggle.
*   `three_script.py`: The main script to perform data analysis and generate the various plots.

**Cloning and setup**
```bash
git clone https://github.com/giuseppe-dp/nba-strategies-analisis.git
cd nba-strategies-analisis
pip install -r requirements.txt
