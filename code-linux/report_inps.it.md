# Report OSINT: inps.it

Data: 2026-07-07T15:04:07.030360

**Report OSINT: Analisi Dominio inps.it**

**1. RIEPILOGO**
Il dominio inps.it è registrato all'Istituto Nazionale Previdenza Sociale dal 1997 e ha una data di scadenza nel novembre 2026. L'infrastruttura DNS è gestita da Fastweb S.p.A., che funge anche da registrar e contatto tecnico. Il dominio utilizza servizi di posta elettronica basati su Outlook.com e server MX proprietari, e integra diverse verifiche di servizi di terze parti come Google, Cisco, Adobe e Microsoft, indicando un ecosistema tecnologico complesso.

**2. INFRASTRUTTURA**
*   **Dominio:** inps.it
*   **Registrante:** Istituto Nazionale Previdenza Sociale (dal 1997-02-11)
*   **Registrar:** Fastweb s.p.a. (FASTWEB-REG)
*   **Contatti WHOIS:**
    *   **Registrante:** Istituto Nazionale Previdenza Sociale, via civiltà del lavoro, 46, Roma.
    *   **Contatto Amministrativo:** Giulio Blandamura, via civiltà del lavoro, 46, Roma (ultimo aggiornamento 2011-03-07).
    *   **Contatto Tecnico:** Gestione Domini, Fastweb S.p.A., Piazza Adriano Olivetti, 1, Milano (ultimo aggiornamento 2019-05-24).
*   **Server DNS (NS):** dns1.fweds-spc.it, dns2.fweds-spc.it (gestiti da Fastweb S.p.A.).
*   **Record A:** 151.101.3.10, 151.101.195.10, 151.101.67.10, 151.101.131.10 (indirizzi IP che tipicamente appartengono a servizi CDN come Fastly).
*   **Server di Posta (MX):** mx10.inps.it, mx20.inps.it, mx30.inps.it, mx40.inps.it.
*   **Record TXT:**
    *   **SPF:** "v=spf1 include:spf.protection.outlook.com ip4:89.97.177.19 ip4:89.97.177.3 ip4:93.63.43.112 ip4:93.63.43.115 ip4:93.63.43.113 ip4:93.63.43.114 ip4:89.97.59.100 ip4:89.97.59.101 -all" - Indica l'utilizzo di Outlook.com per l'invio di email, oltre a specifici IP di proprietà INPS. La direttiva `-all` impone un "hard fail" per mittenti non autorizzati.
    *   **Verifiche Servizi:**
        *   `google-site-verification`: Utilizzo di servizi Google (es. Search Console, Analytics).
        *   `cisco-ci-domain-verification`: Utilizzo di servizi Cisco (es. Cisco Cloud Security).
        *   `adobe-idp-site-verification`: Utilizzo di servizi Adobe (es. Adobe Identity Provider).
        *   `actalis-dcv`: Verifica di dominio per certificati SSL/TLS tramite Actalis.
        *   `MS=ms70335819`: Verifica di servizi Microsoft.
*   **CNAME:** Non disponibile.
*   **DNSSEC:** Non abilitato.

**3. RISCHI**
*   **Mancanza di DNSSEC:** Il dominio non ha DNSSEC abilitato, rendendolo potenzialmente vulnerabile ad attacchi di cache poisoning o manipolazione dei record DNS.
*   **Contatto Amministrativo Obsoleto/Personale:** L'ultimo aggiornamento del contatto amministrativo risale al 2011 e fa riferimento a una persona specifica (Giulio Blandamura). Questo potrebbe rappresentare un rischio se la persona non è più in carica o se le informazioni di contatto non sono aggiornate, complicando la gestione del dominio in caso di emergenza.
*   **Dipendenza da Terze Parti:** L'ampio utilizzo di servizi di terze parti (Google, Cisco, Adobe, Microsoft, Outlook.com) aumenta la superficie di attacco e la dipendenza da fornitori esterni. Ogni servizio integrato deve essere configurato e monitorato attentamente per evitare vulnerabilità.
*   **Scadenza Dominio:** La data di scadenza del dominio (2026-11-23) è relativamente vicina rispetto alla data di raccolta dati (2026-07-07). Sebbene non sia un rischio immediato, la mancata tempestiva estensione potrebbe portare a interruzioni del servizio.

**4. RACCOMANDAZIONI**
*   **Abilitare DNSSEC:** Implementare DNSSEC per proteggere l'integrità dei record DNS e prevenire attacchi di spoofing.
*   **Aggiornare Contatti WHOIS:** Verificare e aggiornare le informazioni del contatto amministrativo, preferibilmente utilizzando un indirizzo email generico o basato su un ruolo (es. `hostmaster@inps.it`) anziché un nominativo personale, e assicurarsi che siano regolarmente revisionate.
*   **Audit dei Servizi di Terze Parti:** Condurre un audit approfondito di tutti i servizi di terze parti verificati tramite i record TXT per comprendere la loro funzione, la configurazione di sicurezza e la necessità.
*   **Monitoraggio Scadenza Dominio:** Impostare avvisi per il rinnovo del dominio con largo anticipo rispetto alla data di scadenza per evitare interruzioni del servizio.
*   **Revisione Record SPF:** Sebbene l'SPF sia ben configurato con `-all`, è consigliabile una revisione periodica degli indirizzi IP e degli `include` per assicurarsi che siano tutti necessari e aggiornati, riducendo il rischio di abusi.