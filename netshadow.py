#!/usr/bin/env python3
import subprocess
import socket
import platform
import threading
from queue import Queue
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

console = Console()

# Banner visual
BANNER = r"""
███╗   ██╗███████╗████████╗██╗  ██╗██╗  ██╗██╗   ██╗
████╗  ██║██╔════╝╚══██╔══╝██║  ██║██║  ██║██║   ██║
██╔██╗ ██║█████╗     ██║   ███████║███████║██║   ██║
██║╚██╗██║██╔══╝     ██║   ██╔══██║██╔══██║██║   ██║
██║ ╚████║███████╗   ██║   ██║  ██║██║  ██║╚██████╔╝
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ 
        [bold green]NetShadow 2.0[/bold green]
"""

# Puertos comunes para escaneo rápido
COMMON_PORTS = [22, 80, 443, 53, 21, 25, 110, 995, 143, 993, 3306, 8080, 8443, 23]

def scan_wifi():
    """Escanea redes WiFi visibles y ocultas usando nmcli."""
    result = subprocess.run(['nmcli', '-f', 'SSID,SECURITY', 'device', 'wifi', 'list'], capture_output=True, text=True)
    networks = []
    for line in result.stdout.split('\n')[1:]:
        if line.strip():
            ssid = line[:30].strip()
            sec = line[30:].strip()
            if ssid == "--":
                ssid = "[red]RED OCULTA[/red]"
            networks.append((ssid, sec))
    return networks

def scan_arp():
    """Escanea la red local para detectar dispositivos."""
    result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    devices = []
    macs = set()
    duplicates = set()
    for line in result.stdout.split('\n'):
        if line.strip():
            parts = line.split()
            ip = parts[1].strip('()')
            mac = parts[3]
            if mac in macs:
                duplicates.add(mac)
            macs.add(mac)
            devices.append((ip, mac))
    return devices, duplicates

def ping_sweep(base_ip):
    """Ping a rango 1-254 para detectar IPs activas"""
    active_ips = []
    def ping(ip):
        param = '-n' if platform.system().lower()=='windows' else '-c'
        command = ['ping', param, '1', '-W', '1', ip]
        if subprocess.run(command, stdout=subprocess.DEVNULL).returncode == 0:
            active_ips.append(ip)

    threads = []
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        t = threading.Thread(target=ping, args=(ip,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return active_ips

def scan_ports(ip):
    """Escanea puertos comunes para una IP dada"""
    open_ports = []
    for port in COMMON_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            sock.connect((ip, port))
            open_ports.append(port)
        except:
            pass
        sock.close()
    return open_ports

def reverse_dns(ip):
    """Intenta obtener nombre de host por DNS inverso"""
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "-"

def main():
    console.clear()
    console.print(Align.center(Text(BANNER, justify="center")))

    console.print("\n[bold cyan]1. Escaneo de redes WiFi (visibles y ocultas)[/bold cyan]")
    wifi_networks = scan_wifi()
    table_wifi = Table(title="Redes WiFi detectadas")
    table_wifi.add_column("SSID", justify="left")
    table_wifi.add_column("Seguridad", justify="left")
    for ssid, sec in wifi_networks:
        table_wifi.add_row(ssid, sec)
    console.print(table_wifi)

    console.print("\n[bold cyan]2. Escaneo ARP en red local (IP y MAC)[/bold cyan]")
    devices, duplicates = scan_arp()
    table_devices = Table(title="Dispositivos en red local")
    table_devices.add_column("IP")
    table_devices.add_column("MAC")
    table_devices.add_column("Host")
    for ip, mac in devices:
        host = reverse_dns(ip)
        mac_text = f"[red]{mac} (duplicada)[/red]" if mac in duplicates else mac
        table_devices.add_row(ip, mac_text, host)
    console.print(table_devices)

    console.print("\n[bold cyan]3. Escaneo de IPs activas (ping sweep) en tu red local[/bold cyan]")
    base_ip = '.'.join(devices[0][0].split('.')[:-1])
    active_ips = ping_sweep(base_ip)
    table_active = Table(title=f"IPs activas en rango {base_ip}.1-254")
    table_active.add_column("IP")
    for ip in active_ips:
        table_active.add_row(ip)
    console.print(table_active)

    console.print("\n[bold cyan]4. Escaneo rápido de puertos en dispositivos detectados[/bold cyan]")
    for ip, _ in devices:
        open_ports = scan_ports(ip)
        ports_str = ', '.join(str(p) for p in open_ports) if open_ports else "Ninguno"
        console.print(f"[yellow]Puertos abiertos en {ip}:[/yellow] {ports_str}")

    console.print("\n[bold green]Escaneo completado. Mantente alerta a dispositivos o redes desconocidas.[/bold green]")

if __name__ == "__main__":
    main()
