# ISTAT Dataset Cleaner 📊🧹

Uno script Python per sistemare e pulire dataset ISTAT in formato CSV, rimuovendo colonne vuote, valori ridondanti e preparando i dati per analisi statistiche o machine learning.

## 🔍 Obiettivo

Il progetto nasce dall'esigenza di rendere più analizzabili i dataset ISTAT, spesso contenenti colonne non informative o incomplete. Automatizza alcune fasi fondamentali del preprocessing.

## ⚙️ Funzionalità

- Rimozione di colonne completamente vuote
- Rimozione di colonne con un solo valore univoco
- Rimozione della colonna `OBS_STATUS`
- Salvataggio del nuovo dataset pulito
- Estendibile facilmente per analisi avanzate

## 🧱 Architettura

La classe `DatasetCleaner` eredita da `ModelloBase`, una superclasse astratta che contiene metodi generici per analizzare dataset pandas (es. distribuzioni, valori univoci, tipologie).
