#!/usr/bin/env python3
"""
Beckhoff CX9020 Mock Server (Lab Safe)
-------------------------------------
Simula, em laboratório, os serviços necessários para o PoC do CX9020:
 - Responde a SSDP/UPnP (UDP/1900) ao M-SEARCH com uma linha 'usn:uuid:...'
 - Expõe HTTP na porta 5120, com:
     * GET /config -> página simples
     * POST /upnpisapi?uuid:<UNS>+urn:beckhoff.com:serviceId:cxconfig -> 200 OK

Use somente para fins educacionais em ambiente isolado.
"""

import threading
import socket
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

UUID = "12345678-1234-1234-1234-1234567890ab"  # valor fixo para facilitar o teste
HTTP_PORT = 5120
SSDP_PORT = 1900

# -----------------------------
# SSDP mock (UDP)
# -----------------------------

def ssdp_server(stop_event: threading.Event):
    """Escuta em UDP/1900 e responde a M-SEARCH com cabeçalhos esperados pelo PoC."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Permite reutilizar a porta em alguns SOs
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind(("0.0.0.0", SSDP_PORT))
        print(f"[SSDP] Listening on 0.0.0.0:{SSDP_PORT}")
    except OSError as e:
        print(f"[SSDP] Failed to bind UDP/{SSDP_PORT}: {e}")
        return

    sock.settimeout(0.5)
    while not stop_event.is_set():
        try:
            data, addr = sock.recvfrom(4096)
        except socket.timeout:
            continue
        except Exception as e:
            print(f"[SSDP] recv error: {e}")
            continue

        text = data.decode(errors="ignore")
        if "M-SEARCH" in text and "ssdp:discover" in text:
            print(f"[SSDP] M-SEARCH from {addr}")
            # Resposta com a linha exatamente no formato que o PoC procura (':uuid' sem espaço)
            # e com o UUID nas posições esperadas (fatiamento [9:45]) -> 'usn:uuid:' (9 chars) + 36 do UUID
            response = (
                "HTTP/1.1 200 OK\r\n"
                "cache-control:max-age=120\r\n"
                "ext:\r\n"
                f"usn:uuid:{UUID}\r\n"  # <- linha crucial para o PoC
                "st:upnp:rootdevice\r\n"
                f"location:http://{addr[0]}:{HTTP_PORT}/UpnpWebsite/index.htm\r\n"
                "server:Beckhoff-TwinCAT/3.1 UPnP/1.0 Mock\r\n\r\n"
            )
            try:
                sock.sendto(response.encode(), addr)
                print(f"[SSDP] Sent mock response to {addr}")
            except Exception as e:
                print(f"[SSDP] send error: {e}")

    sock.close()
    print("[SSDP] Stopped")

# -----------------------------
# HTTP mock (TCP)
# -----------------------------

class MockHandler(BaseHTTPRequestHandler):
    server_version = "TwinCAT-Mock/0.1"

    def do_GET(self):
        if self.path.startswith("/config"):
            body = (
                "<html><head><title>Beckhoff Mock</title></head>"
                "<body><h1>Beckhoff TwinCAT Mock</h1>"
                "<p>Este é um servidor de laboratório. Porta 5120 ativa.</p>"
                "</body></html>"
            )
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path.startswith("/upnpisapi"):
            length = int(self.headers.get("Content-Length", "0"))
            soap = self.rfile.read(length)
            print("[HTTP] Received SOAPAction:", self.headers.get("SOAPAction"))
            print("[HTTP] Body (first 200 bytes):", soap[:200])
            # Resposta 200 OK para simular sucesso
            body = b"<s:Envelope><s:Body><u:WriteResponse/></s:Body></s:Envelope>"
            self.send_response(200)
            self.send_header("Content-Type", "text/xml; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, fmt, *args):
        # logs mais limpos
        print(f"[HTTP] {self.address_string()} - {fmt % args}")


def http_server(stop_event: threading.Event):
    try:
        httpd = HTTPServer(("0.0.0.0", HTTP_PORT), MockHandler)
    except OSError as e:
        print(f"[HTTP] Failed to bind TCP/{HTTP_PORT}: {e}")
        return

    print(f"[HTTP] Listening on 0.0.0.0:{HTTP_PORT}")
    httpd.timeout = 0.5
    while not stop_event.is_set():
        httpd.handle_request()
    print("[HTTP] Stopped")

# -----------------------------
# Boot
# -----------------------------

if __name__ == "__main__":
    stop = threading.Event()
    t1 = threading.Thread(target=ssdp_server, args=(stop,), daemon=True)
    t2 = threading.Thread(target=http_server, args=(stop,), daemon=True)
    t1.start()
    t2.start()
    print("Mock CX9020 running. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping...")
        stop.set()
        time.sleep(1)
        print("Bye!")
