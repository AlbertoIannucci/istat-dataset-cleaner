from modello_base import ModelloBase
import pandas as pd

class DatasetCleaner(ModelloBase):

    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato = self.sistemazione()

    # Metodo di sisetmazione del dataframe
    def sistemazione(self):
        # Copia del dataframe
        df_sistemato = self.dataframe.copy()
        # Drop variabili nulle
        df_sistemato = df_sistemato.dropna(axis=1, how="all")
        # Drop variabili con <2 valori univoci
        colonne_unico_valore = df_sistemato.nunique()[df_sistemato.nunique() < 2].index
        df_sistemato = df_sistemato.drop(colonne_unico_valore, axis=1)
        # Sostituizione valori nan
        df_sistemato["NOTE_REF_AREA"] = df_sistemato["NOTE_REF_AREA"].fillna('GENERAL')

        return df_sistemato

modello = DatasetCleaner("../Dataset/dataset.csv")
# Passo 1. Analisi generali del dataset
#modello.analisi_generali(modello.dataframe)
# Risultati:
# Osservazioni: 4167; Variabili: 31 (Presenza di variabili nulle); Tipi: object, int64 e float64; Valori nan: presenti
# Passo 2. Drop variabili nulle
# Passo 3. Analisi valori univoci
#modello.analisi_valori_univoci(modello.dataframe_sistemato)
# Variabili con <2 valori univoci: DATAFLOW, FREQ, DATA_TYPE, MARIT_PROPER_SYSTEMS, MONTH_CELEBRATION,
# AGE_MARRIAGE_BRIDEGROOM, MARITAL_STATUS_BRIDEGRO, EDU_LEV_BRIDEGROOM, AGE_MARRIAGE_BRIDE, MARITAL_STATUS_BRIDE,
# EDU_LEV_BRIDE
# Passo 4. Drop variabili con <2 valori univoci
#modello.analisi_generali(modello.dataframe_sistemato)
# Risultato:
# Osservazioni: 4167; Variabili: 5; Tipi: object, int64 e float64; Valori nan: presenti
# La colonna NOTE_REF_AREA è una sotto-segmentazione di REF_AREA, ma presenta valori mancanti.
# Per evitare di perdere informazioni e abilitare sia analisi generali che dettagliate,
# si è deciso di mantenere la colonna e sostituire i NaN con il valore 'GENERAL'
# Passo 5. Sostituzione di nan con 'GENERAL'
# Passo 6. Creazione del nuovo csv
modello.dataframe_sistemato.to_csv("../Dataset/dataset_nuovo.csv", index=False)


