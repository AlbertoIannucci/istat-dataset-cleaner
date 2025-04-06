
from modello_base import ModelloBase
import pandas as pd

class DatasetCleaner(ModelloBase):

    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato = self.sistemazione()

    # Metodo di sistemazione del dataframe
    def sistemazione(self):
        # Copia del dataframe
        df_sistemato = self.dataframe.copy()
        # Drop variabili nulle
        df_sistemato = df_sistemato.dropna(axis=1, how="all")
        # Drop variabili con <2 valori univoci
        colonne_unico_valore = df_sistemato.nunique()[df_sistemato.nunique() < 2].index
        df_sistemato = df_sistemato.drop(colonne_unico_valore, axis=1)

        return df_sistemato



modello = DatasetCleaner("../Dataset/dataset.csv")
# Passo 1. Analisi generali del dataset
#modello.analisi_generali(modello.dataframe)
# Risultati:
# Osservazione: 45493; Variabili: 25 (Presenza di variabili nulle); Tipi: object, int64 e float64; Nan: sembra nessuno
# Passo 2. Drop varabili nulle
# Passo 3. Analisi generali del nuovo dataset
#modello.analisi_generali(modello.dataframe_sistemato)
# Risultati:
# Osservazione: 45493; Variabili: 12; Tipi: object e int64; Nan = sembra nessuno
# Passo 4. Analisi valori univoci
#modello.analisi_valori_univoci(modello.dataframe_sistemato)
# Variabili con <2 valori univoci: DATAFLOW, FREQ, DATA_TYPE, AGE, EDU_LEV_HIGHEST
# Nan = nessuno
# Passo 5. Drop variabili con <2 valori univoci
# Passo 6. Creazione del nuovo csv
modello.dataframe_sistemato.to_csv("../Dataset/dataset_nuovo.csv")