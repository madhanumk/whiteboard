# Whiteboard Classroom

A real-time collaborative whiteboard built using Django, Django Channels, and Fabric.js. This application allows users to create classrooms, join via unique URLs (slugs), and draw on a shared whiteboard. All interactions are synchronized in real-time using WebSockets.

## Features

- **Create Classrooms:** Create a new classroom by specifying a name, and generate a unique URL.
- **Real-Time Whiteboard:** Real-time drawing collaboration with other users in the same classroom.
- **Emoji Toolbar:** Includes various emojis and drawing tools for more interactive use.
- **Save and Load Canvas:** Save the current canvas state and load it later.
- **Image Upload:** Upload and add images to the whiteboard canvas.
- **WebSocket Sync:** Updates to the whiteboard are shared instantly with all users in the classroom.

## Demo

You can view the live demo of the application here: [Demo URL] (add your deployed URL here)

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or above
- Redis (for WebSocket support in production)

### Steps to Run Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/madhanumk/whiteboard.git
   cd whiteboard
