# System Monitor

A lightweight desktop application built with **CustomTkinter** and **psutil** that displays real-time CPU, RAM, and Disk usage in a clean, dark-themed interface. Usage values turn red when they exceed 80%, giving an instant visual warning of high system load.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

---

## 🇬🇧 English

### Features
- Real-time CPU usage monitoring
- Real-time RAM (memory) usage monitoring
- Real-time Disk usage monitoring
- Automatic red warning color when usage exceeds 80%
- Updates every second
- Simple, modern dark-themed UI

### Requirements
- Python 3.10 or higher
- `customtkinter`
- `psutil`

### Installation
```bash
pip install customtkinter psutil
```

### Usage
```bash
python system_monitor.py
```

The application window will open and immediately start displaying live system stats. No configuration is required.

### How it works
The app uses `psutil.cpu_percent()`, `psutil.virtual_memory()`, and `psutil.disk_usage()` to read system metrics every second via a recurring `after()` callback in CustomTkinter. Each metric's label color switches to red automatically once it passes the 80% threshold, making resource spikes easy to spot at a glance.

### License
This project is licensed under the MIT License.

---

## 🇩🇪 Deutsch

### Funktionen
- Echtzeit-Überwachung der CPU-Auslastung
- Echtzeit-Überwachung der RAM-Auslastung (Arbeitsspeicher)
- Echtzeit-Überwachung der Festplattenauslastung
- Automatische rote Warnfarbe bei Überschreitung von 80 %
- Aktualisierung jede Sekunde
- Einfache, moderne Benutzeroberfläche im Dunkelmodus

### Voraussetzungen
- Python 3.10 oder höher
- `customtkinter`
- `psutil`

### Installation
```bash
pip install customtkinter psutil
```

### Verwendung
```bash
python system_monitor.py
```

Das Anwendungsfenster öffnet sich und zeigt sofort die aktuellen Systemwerte an. Es ist keine zusätzliche Konfiguration erforderlich.

### Funktionsweise
Die Anwendung liest die Systemwerte mithilfe von `psutil.cpu_percent()`, `psutil.virtual_memory()` und `psutil.disk_usage()` jede Sekunde über einen wiederkehrenden `after()`-Callback in CustomTkinter aus. Sobald ein Wert die 80 %-Schwelle überschreitet, wechselt die Farbe des jeweiligen Labels automatisch auf Rot, sodass hohe Auslastungen sofort erkennbar sind.

### Lizenz
Dieses Projekt steht unter der MIT-Lizenz.

---

## 🇹🇷 Türkçe

### Özellikler
- Gerçek zamanlı CPU kullanım takibi
- Gerçek zamanlı RAM (bellek) kullanım takibi
- Gerçek zamanlı Disk kullanım takibi
- Kullanım %80'i geçtiğinde otomatik kırmızı uyarı rengi
- Her saniye güncelleme
- Sade ve modern karanlık temalı arayüz

### Gereksinimler
- Python 3.10 veya üzeri
- `customtkinter`
- `psutil`

### Kurulum
```bash
pip install customtkinter psutil
```

### Kullanım
```bash
python system_monitor.py
```

Uygulama penceresi açılır açılmaz canlı sistem verilerini göstermeye başlar. Herhangi bir ek ayara gerek yoktur.

### Nasıl çalışır?
Uygulama, `psutil.cpu_percent()`, `psutil.virtual_memory()` ve `psutil.disk_usage()` fonksiyonlarını kullanarak sistem verilerini her saniye CustomTkinter'ın `after()` mekanizmasıyla tekrar tekrar okur. Her metrik %80 eşiğini geçtiğinde ilgili etiketin rengi otomatik olarak kırmızıya döner, böylece yüksek kaynak kullanımı bir bakışta fark edilir.

### Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.
