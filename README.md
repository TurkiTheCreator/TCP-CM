# TCP-CM (TCP Chat Messenger)


This repository contains a simple command-line chat application built with Python. It uses a client-server architecture with TCP sockets for communication and threading to handle multiple clients simultaneously.

## Features

*   **Multi-Client Chat:** The server can handle multiple clients connecting and chatting in a shared room.
*   **Nickname Support:** Users choose a nickname upon connecting.
*   **Admin Role:** A special `admin` user with a password has elevated privileges.
*   **Admin Commands:**
    *   `/kick <nickname>`: Forcibly disconnects a user from the server.
    *   `/ban <nickname>`: Kicks and permanently bans a user from rejoining.
*   **Persistent Bans:** Banned user nicknames are stored in a `bans.txt` file to prevent them from reconnecting in future sessions.
*   **Real-time Notifications:** Join and leave messages are broadcast to all users.

## How to Run

### Prerequisites
*   Python 3

### 1. Clone the Repository
```bash
git clone https://github.com/TurkiTheCreator/TCP-CM.git
cd TCP-CM
```

### 2. Start the Server
Open a terminal and run the server script. The server will start listening for connections on `127.0.0.1:55555`.

```bash
python server.py
```
You will see the message: `Server is listening...`

### 3. Start the Client
Open one or more new terminal windows and run the client script.

```bash
python client.py
```

The client will prompt you to choose a nickname.

```
Choose your nickname:
```

### 4. Chat!
Once connected, you can start sending messages. Messages you type will be broadcast to all other connected clients.

## Admin Functionality

There is a built-in administrator account with special privileges to moderate the chat.

#### Connecting as Admin
1.  Run `client.py`.
2.  When prompted, enter `admin` as your nickname.
3.  When prompted for the password, enter `adminpass`.

#### Admin Commands
As the admin, you can type the following commands into the chat prompt:

*   **Kick a User:** To temporarily remove a user from the chat session.
    ```
    /kick <nickname>
    ```
    Example: `/kick Steve`

*   **Ban a User:** To permanently ban a user. The user will be kicked and their nickname will be added to `bans.txt`, preventing them from rejoining.
    ```
    /ban <nickname>
    ```
    Example: `/ban John`

## File Descriptions

*   `server.py`: The server application. It binds to a host and port, listens for incoming client connections, and manages message broadcasting and user administration.
*   `client.py`: The client application. It connects to the server, allowing a user to send messages and receive messages from other clients.
*   `bans.txt` (auto-generated): A text file created by the server to store the nicknames of banned users.
