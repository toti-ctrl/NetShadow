📄 README.md para NetShadow
markdown
<h1 align="center">🌐 NetShadow</h1>
<p align="center">
  <img src="https://img.shields.io/badge/status-active-brightgreen" alt="status">
  <img src="https://img.shields.io/badge/python-3.10+-blue" alt="python">
  <img src="https://img.shields.io/badge/license-MIT-yellow" alt="license">
</p>

<p align="center"><b>OSINT 🔍 y escaneo extremo para identificar usuarios, correos y rastros en la red.</b></p>

---

## 🚀 ¿Qué es NetShadow?

**NetShadow** es una herramienta avanzada de reconocimiento que combina técnicas de OSINT, verificación de cuentas y escaneo de plataformas para detectar:

- Cuentas activas en redes sociales 🕵️‍♂️  
- Correos electrónicos asociados 📧  
- Huellas digitales en servicios populares 🌍  
- Resultados visuales con paneles enriquecidos 🎨

---

## 🧪 Características

✅ Escaneo de nombres de usuario en múltiples plataformas  
✅ Búsqueda inteligente de direcciones Gmail vinculadas  
✅ Interfaz CLI con salida visual (usando `rich`)  
✅ Totalmente extensible y modular  
✅ Compatible con Kali Linux / Parrot OS

---

## 📸 Capturas (demo)

> Añade aquí una captura con `netshadow.py` corriendo:
```bash
python netshadow.py --username pepe
⚙️ Instalación
bash
Copiar
Editar
# Clona el repo
git clone git@github.com:toti-ctrl/NetShadow.git
cd NetShadow

# Crea un entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instala dependencias
pip install -r requirements.txt
🧑‍💻 Uso
bash
Copiar
Editar
python netshadow.py --username <usuario> [opciones]

Opciones:
  --emails           Intenta buscar Gmail vinculados
  --platforms all    Escanea en todas las plataformas soportadas
  --json             Exporta los resultados en formato JSON
📂 Estructura del Proyecto
Copiar
Editar
NetShadow/
├── netshadow.py
├── modules/
│   ├── scanner.py
│   ├── visualizer.py
├── utils/
│   ├── gmail_hunter.py
├── README.md
└── requirements.txt
🛡️ Licencia
Este proyecto está bajo la licencia MIT. Libre de usar, compartir y modificar.

🤝 Créditos
Desarrollado por Toti Ctrl con ❤️ para la comunidad hacker de habla hispana.

yaml
Copiar
Editar

---

### ✅ ¿Qué debes hacer ahora?

1. Crea un archivo:

```bash
nano README.md
Pega el contenido anterior.

Guarda y haz:

bash
Copiar
Editar
git add README.md
git commit -m "Añadido README visual"
git push
