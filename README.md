# iderp

Custom Frappe app for ERPNext by idstudio AI (ai@idstudio.org)

---

## Setup

Questa app è progettata per Frappe/ERPNext 14.  
Puoi installarla usando:

bench get-app iderp https://github.com/haringk/iderp.git
bench --site tuo_sito install-app iderp

---

## Funzionalità principali

- Gestione articoli e servizi per grafica e stampa con campi dedicati per dimensioni, colore e personalizzazione.
- Sconti automatici per quantità e sconti cliente cumulabili tramite DocType "Customer Discount".
- Copia automatica dei campi personalizzati tra documenti di vendita (Quotation, Sales Order, Sales Invoice).
