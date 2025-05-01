# Uppercase TCP/UDP Server with Docker & systemd

This project contains two simple servers — one for TCP and one for UDP — that receive text messages, convert them to uppercase, and send the result back. Everything is containerized using Docker and managed via `docker-compose` and `systemd`.

---

## 📁 Project Structure

```
Uppercase/
├── tcp_server/
│   ├── tcp_server.py
│   └── Dockerfile
├── udp_server/
│   ├── udp_server.py
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Setup Steps

### 1. Clone the Repository

```bash
git clone https://github.com/AminDenizer/Internet-4032.git
cd project
```

---

### 2. Build Docker Images and Start Containers

```bash
docker compose build
docker compose up -d
```

To verify running containers:

```bash
docker compose ps
```

---

### 3. Open Required Ports

#### On the Linux system:

```bash
sudo ufw allow 12345/udp
sudo ufw allow 23456/tcp
```

#### On MikroTik router:

1. Open **Winbox**.
2. Navigate to `IP > Firewall > NAT`.
3. Add a new rule:
   - Chain: `dstnat`
   - Protocol: `tcp` or `udp`
   - Dst. Port: `23456` (TCP) or `12345` (UDP)
   - Action: `dst-nat`
   - To Address: IP of your Linux server
   - To Port: same as destination

---

### 4. Create and Enable a `systemd` Service

Find the path to `docker-compose`:

```bash
which docker-compose
```

Then create the service file:

```bash
sudo nano /etc/systemd/system/uppercase-server.service
```

Paste the following content:

```ini
[Unit]
Description=Uppercase TCP/UDP Docker Servers
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
WorkingDirectory=/home/amindenizer/Documents/Uppercase/project
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down
RemainAfterExit=true
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable uppercase-server.service
sudo systemctl start uppercase-server.service
```

---

## ✅ Testing the Servers (LAN)

From another device on the same local network:

### TCP test:

```bash
echo "hello" | nc 192.168.88.250 23456
```

### UDP test:

```bash
echo "hello" | nc -u 192.168.88.250 12345
```

---

## 🌐 Using with a Domain Name

If you’re using a custom domain (e.g., `domain.com`) and Cloudflare is enabled, **make sure** the DNS record for your domain is set to **DNS Only (gray cloud ☁️)**.  
Otherwise, Cloudflare will block direct access to custom TCP/UDP ports.

---

## 🧼 Stopping the Service

To stop everything:

```bash
sudo systemctl stop uppercase-server.service
```

---

## 📌 Notes

- Python 3.11 is used in this project.
- Ports:
  - TCP: `23456`
  - UDP: `12345`
- You can modify the port numbers in `*.py`, `Dockerfile`, and `docker-compose.yml` files as needed.

---

> Developed by [amindenizer](https://github.com/amindenizer)
