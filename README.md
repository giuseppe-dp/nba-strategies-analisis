# NBA Strategies Analysis 🏀📊

Un'analisi quantitativa sull'evoluzione delle strategie di gioco nell'NBA dal 1985 al 2022, con particolare focus sull'impatto dell'introduzione del tiro da 3 punti.

## 🎯 Cosa ho fatto
Il progetto analizza come il tiro da tre punti abbia alterato l'equilibrio strategico tra attacco e difesa nell'NBA moderna, imponendo un nuovo paradigma di gioco. L'obiettivo è quantificare il successo agonistico superando la semplice analisi del volume di tiri, focalizzandosi sull'efficienza realizzativa e sulla gestione del possesso.

Nello specifico, sono state calcolate e messe in relazione con le vittorie le seguenti metriche:
*   **eFG% (Effective Field Goal Percentage)**: Per valutare l'efficienza pesando il maggior valore (+50%) del tiro da tre rispetto a quello da due.
*   **TOV% (Turnover Percentage)**: Per misurare la dissipazione dei possessi a causa delle palle perse.
*   **ORB% (Offensive Rebound Percentage)**: Per valutare l'efficacia della rigenerazione di un nuovo possesso dopo un errore al tiro.

## 🛠️ Come l'ho fatto
L'elaborazione dei dati si è articolata in tre fasi principali, gestite interamente tramite script Python eseguiti sequenzialmente da terminale:
1.  **Acquisizione e Preprocessing**: I dati grezzi (games) sono stati estratti da un database SQLite tramite query SQL. La pulizia e il filtraggio temporale (1985-2022) sono stati eseguiti con la libreria `pandas`.
2.  **Analisi Statistica**: Dopo un'ispezione esplorativa con `D-Tale`, sono stati generati modelli di regressione lineare. I coefficienti di correlazione di Pearson ($r$) e i relativi $p_{value}$ sono stati calcolati utilizzando `scipy.stats`.
3.  **Visualizzazione**: L'impatto visivo e grafico dei risultati è stato realizzato mediante `matplotlib`.

## 📈 Risultati Principali
*   **Il paradosso del volume**: L'aumento dei tiri da 3 non garantisce un aumento diretto della probabilità di vittoria ($r \approx 0.09$). 
*   **L'efficienza domina**: L'efficienza effettiva (eFG%) è invece un indicatore primario del successo agonistico ($r \approx 0.48$), confermando che conta la qualità dell'esecuzione rispetto al numero di tentativi.
*   **Gestione dell'errore**: La protezione del pallone (TOV%) è critica per vincere ($r \approx -0.27$), mentre il rimbalzo offensivo (ORB%) è diventato una metrica irrilevante per la vittoria ($r \approx 0.03$). 
*   **Evoluzione storica**: A causa del maggiore spacing, le squadre hanno progressivamente rinunciato ai rimbalzi offensivi per garantire la transizione difensiva, portando a un crollo storico della metrica nel tempo ($r \approx -0.82$).

## 🚀 Utilizzo del codice
Il progetto è strutturato tramite programmi Python da lanciare a terminale passo dopo passo.

i file si dividono in:
* Analisi_Strategie_Nba.pdf è lo studio completo scritto in latex con rispettivi grafici e risultati.
* data_import.py serve per importare i file da Kaggle.
* three_script.py è lo script per fare l'analisi dati e generare i vari grafici.

**Clonazione e setup**
```bash
git clone [https://github.com/giuseppe-dp/nba-strategies-analisis.git](https://github.com/giuseppe-dp/nba-strategies-analisis.git)
cd nba-strategies-analisis
pip install -r requirements.txt
