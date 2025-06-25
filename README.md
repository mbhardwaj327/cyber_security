# TCP Client-Server Example

This repository contains a simple multi-threaded TCP server and two client implementations that demonstrate basic socket communication in Python. The server listens for incoming connections, spawns a new thread for each client, and echoes back processed messages. The clients connect to the server and exchange two rounds of messages.

## Features

* **Multi-threaded server**: Handles multiple clients concurrently.
* **Message processing**: Server converts incoming messages to uppercase.
* **Two client variants**: Demonstrates two different client workflows with unique message prefixes.
* **Robust error handling**: Clients gracefully handle connection errors.

## Requirements

* Python 3.6+

## Setup & Installation

1. Clone this repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies (none required beyond the Python standard library).

## Configuration

By default, both server and clients use the following settings:

* **Host**: `10.6.2.240`
* **Port**: `12345`

To change these values, modify the `SERVER_ADDRESS` / `HOST` and `SERVER_PORT` / `PORT` variables at the top of each script.

## Usage

### Server

Run the server with:

```bash
python server.py
```

The server will start listening for incoming TCP connections and print logs to the console.

### Client 1

Run the first client variant with:

```bash
python client1.py
```

* You will be prompted to enter two messages.
* Each message is prefixed (`MSG01>>` and `MSG02>>`) before sending.
* The responses from the server are displayed.

### Client 2

Run the second client variant with:

```bash
python client2.py
```

* You will be prompted to enter two messages.
* Each message is prefixed (`PKT1>>` and `PKT2>>`) before sending.
* The responses from the server are displayed.

## File Overview

* `server.py`: Multi-threaded TCP server implementation.
* `client1.py`: First client variant with custom prefixes and error handling.
* `client2.py`: Second client variant with alternative naming and workflow.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

Feel free to customize and expand upon these examples for your own learning and testing purposes!
