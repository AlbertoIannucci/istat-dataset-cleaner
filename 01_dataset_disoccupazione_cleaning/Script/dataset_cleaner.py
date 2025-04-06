
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
        # Drop variabile OBS_STATUS
        df_sistemato = df_sistemato.drop(["OBS_STATUS"], axis=1)
        # Drop variabili con meno di 2 valori univoci
        colonne_unico_valore = df_sistemato.nunique()[df_sistemato.nunique() < 2].index
        df_sistemato = df_sistemato.drop(colonne_unico_valore, axis=1)

        return df_sistemato



modello = DatasetCleaner("../Dataset/dataset.csv")
# Passo 1. Analisi generale del dataset
#modello.analisi_generali(modello.dataframe)
# Risultato:
# Osservazione: 6135; Variabili: 26 (Presenza di variabili nulle); Tipi: object, int64 e float64; Nan: presenti;
# Passo 2. Drop variabili nulle e variabible OBS_STATUS (solo 9 valore non nan su 6135)
# Passo 3. Analisi generale del nuovo dataset
#modello.analisi_generali(modello.dataframe_sistemato)
# Risultato:
# Osservazioni: 6135; Variabili: 12; Tipi: object, int64 e float64; Nan: non sembra
# Passo 4. Analisi valori univoci
#modello.analisi_valori_univoci(modello.dataframe_sistemato)
# Risultato:
# Variabili con <2 valori univoci: DATAFLOW,DATA_TYPE, CITIZENSHIP, LABPROF_STATUS_A, DURATION_UNEMPLOYMENT
# Passo 5. Drop variabili con meno di 2 valori univoci
# Passo 6. Analisi generali del nuovo dataset e analisi valori univoci
#modello.analisi_generali(modello.dataframe_sistemato)
#modello.analisi_valori_univoci(modello.dataframe_sistemato, ["OBS_VALUE"])
# Passo 7. Creazione del nuovo cvs
modello.dataframe_sistemato.to_csv("../Dataset/dataset_nuovo.csv")