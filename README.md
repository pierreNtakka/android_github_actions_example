# Simple GitHub Actions Project

## Descrizione del Progetto

Questo progetto è un'applicazione Android sviluppata utilizzando Kotlin e Java, gestita con Gradle. Il progetto include un flusso di lavoro di integrazione continua (CI) configurato tramite GitHub Actions per automatizzare vari processi di build, test e rilascio.

## Peculiarità del Progetto

### Linguaggi e Framework Utilizzati
- **Kotlin**
- **Java**
- **Gradle**

### GitHub Actions

Il progetto utilizza GitHub Actions per automatizzare i seguenti processi:

1. **Configurazione dell'Ambiente di Build**:
    - Checkout del progetto.
    - Configurazione del JDK (Java Development Kit) versione 20.
    - Concessione dei permessi di esecuzione per `gradlew`.

2. **Gestione delle Variabili di Ambiente**:
    - Creazione di file di credenziali di servizio utilizzando Python.
    - Test delle variabili di ambiente utilizzate da Gradle.

3. **Build e Rilascio**:
    - Assemblaggio e caricamento delle build su Firebase App Distribution per vari ambienti (dev, uat, preprod, prod).
    - Incremento delle versioni dell'SDK e dell'applicazione.
    - Disabilitazione e abilitazione dell'implementazione locale tramite modifiche al file `gradle.properties`.

4. **Gestione delle Versioni**:
    - Stampa delle versioni di Java e Gradle.
    - Stampa delle versioni dell'SDK e dell'applicazione prima e dopo l'incremento.
    - Commit e push delle modifiche al repository Git.
    - Creazione di tag Git e release su GitHub.

5. **Pulizia**:
    - Rimozione dei file JSON di configurazione e delle variabili di ambiente al termine del flusso di lavoro.

### Esempio di Flusso di Lavoro

Il file `.github/workflows/android.yml` contiene la configurazione del flusso di lavoro principale, che include vari step per la gestione delle build e dei rilasci. Un esempio di configurazione di un flusso di lavoro di test è presente nel file `.github/workflows/android_test.yml`.

## Come Utilizzare

1. **Configurazione dei Segreti**:
    - Aggiungere i segreti necessari nel repository GitHub, come `APP_DISTR_FILE_CONTENT_KEY` e `MAVEN_UPLOAD_TOKEN`.

2. **Esecuzione del Flusso di Lavoro**:
    - Il flusso di lavoro può essere eseguito manualmente tramite l'interfaccia di GitHub Actions o automaticamente in base agli eventi configurati.

3. **Debug**:
    - Abilitare l'input `debug` per stampare informazioni utili per il debug durante l'esecuzione del flusso di lavoro.

## Conclusione

Questo progetto dimostra come utilizzare GitHub Actions per automatizzare il processo di build, test e rilascio di un'applicazione Android, migliorando l'efficienza e riducendo gli errori manuali.