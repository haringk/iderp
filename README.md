# iderp

Custom Frappe app for ERPNext by idstudio AI (ai@idstudio.org)

---

## Setup

Questa app è progettata per Frappe/ERPNext 14.  
Puoi installarla usando:

bench get-app iderp https://github.com/haringk/iderp.git
bench --site tuo_sito install-app iderp

---

## Features

- Manage print and graphic items with dimension fields
- Apply quantity-based and per-customer discounts
- Automatically copy custom item fields between documents

---

Gli asset pubblici si trovano in `public/js/iderp.js` e `public/css/iderp.css`.
Questi vengono inclusi globalmente tramite `hooks.py` affinché la build degli asset
non abbia percorsi mancanti.

