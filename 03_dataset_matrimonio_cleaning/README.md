# DatasetCleaner per ISTAT 📊🧹

Uno script Python per ripulire automaticamente dataset ISTAT in formato CSV, utile per analisi statistiche, reportistica o machine learning.

## 🔍 Obiettivo

Il progetto nasce dall'esigenza di rendere più analizzabili i dataset ISTAT, spesso contenenti colonne non informative o incomplete. Automatizza alcune fasi fondamentali del preprocessing.

## ⚙️ Funzionalità

- Rimozione di colonne completamente vuote
- Eliminazione automatica di variabili con meno di 2 valori univoci
- Caricamento dati e salvataggio del nuovo dataset ripulito
- Decisione strategica sulla gestione dei valori nan
- Estendibile tramite una superclasse astratta con metodi di analisi

## 🧱 Architettura

La classe `DatasetCleaner` eredita da `ModelloBase`, una superclasse astratta che contiene metodi generici per analizzare dataset pandas (es. distribuzioni, valori univoci, tipologie).
