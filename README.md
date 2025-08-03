# Uppercase TCP/UDP/QUIC Server with Docker

This project contains three simple servers — one for TCP, one for UDP, and one for QUIC — that receive text messages, convert them to uppercase, and send the result back. Everything is containerized using Docker and managed via `docker-compose`.

A graphical user interface (GUI) client is also provided to easily test the servers.

---

## 📁 Project Structure

```
.
├── client/
│   ├── gui_client.py
│   ├── tcp_client.py
│   └── udp_client.py
├── servers/
│   ├── quic_server/
│   │   ├── Dockerfile
│   │   ├── quic_server.py
│   │   ├── server.crt
│   │   └── server.key
│   ├── tcp_server/
│   │   ├── Dockerfile
│   │   └── tcp_server.py
│   └── udp_server/
│       ├── Dockerfile
│       └── udp_server.py
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup and Run

### Prerequisites

- Docker
- Docker Compose
- Python 3.7+
- `tkinter` (usually included with Python)

### 1. Clone the Repository

```bash
git clone https://github.com/AminDenizer/Internet-4032.git
cd Internet-4032
```

### 2. Build Docker Images and Start Servers

This will start the TCP, UDP, and QUIC servers in the background.

```bash
docker-compose build
docker-compose up -d
```

To verify the running containers:

```bash
docker-compose ps
```

### 3. Run the GUI Client

The client is a desktop application built with `tkinter`.

```bash
python3 client/gui_client.py
```

From the GUI, you can:
- Select the protocol (TCP, UDP, or QUIC).
- Enter the server address (default is `localhost`).
- Type your message and send it to the selected server.
- View the server's uppercase response.

---

## ✅ Testing the Servers (Command Line)

You can also test the servers from the command line.

### TCP test:

```bash
echo "hello" | nc localhost 23456
```

### UDP test:

```bash
echo "hello" | nc -u localhost 12345
```

---

## 🧼 Stopping the Servers

To stop all the running servers:

```bash
docker-compose down
```

---

## 📌 Notes

- **QUIC Server:** The QUIC server uses a self-signed certificate for testing purposes. The provided GUI client is configured to work with this setup.
- **Ports:**
  - TCP: `23456`
  - UDP: `12345`
  - QUIC: `4433`

---

> Original project by [amindenizer](https://github.com/amindenizer)
> Modified to include QUIC and a GUI client.
