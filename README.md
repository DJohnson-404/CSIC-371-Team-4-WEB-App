# CSIC-371-Team-4-WEB-App

Group project for CSIC-371 Fall 2025

## BurgB Restaurant Management Application

A full-stack web application for managing restaurant menu items, built with Python Flask backend and plain HTML/CSS/JavaScript frontend.

## Features

- 🍔 View all menu items with prices and units
- ➕ Add new items to the menu
- 🗑️ Delete items from the menu
- 🎨 Beautiful, modern UI with responsive design
- 🔄 Real-time updates

## Project Structure

```
burgb_app/
├── backend/
│   ├── app.py              # Flask API server
│   ├── items_dao.py        # Data access object for items
│   ├── sql_connection.py   # MySQL database connection
│   └── requirements.txt    # Python dependencies
└── frontend/
    └── index.html          # Single-page HTML application
```

## Prerequisites

- Python 3.7+
- MySQL 8.0+
- MySQL database named `burgb` (see `burgb database.sql` for schema)
- A modern web browser

## Setup Instructions

### 1. Database Setup

1. Create a MySQL database named `burgb`
2. Import the database schema:

```bash
mysql -u root -p burgb < "burgb database.sql"
```

### 2. Backend Setup

1. Navigate to the backend directory:

```bash
cd burgb_app/backend
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Update database credentials in `sql_connection.py` if needed (currently set to `root`/`SQLOran_0404`)

4. Start the Flask server (this serves both the API and the frontend):

```bash
python app.py
```

The server will run on `http://localhost:5000`

### 3. Access the Application

1. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

That's it! Flask serves both the frontend HTML and the API endpoints from the same server, so there are no CORS issues to worry about.

**Alternative**: You can also open `burgb_app/frontend/index.html` directly in your browser if you prefer, but you'll need to make sure the Flask backend is running on `http://localhost:5000`.

## API Endpoints

- `GET /api/items` - Get all menu items
- `POST /api/items` - Add a new item (requires: `item_name`, `unit_id`, `price_per_item`)
- `DELETE /api/items/:id` - Delete an item by ID
- `GET /api/units` - Get available units (each, lb)

## Usage

1. Start the Flask server (see Backend Setup)
2. Open `http://localhost:5000` in your browser
3. View existing items, add new ones, or delete items using the intuitive interface

The Flask server automatically serves the frontend HTML file, so everything works seamlessly without any CORS issues!

## Technologies Used

- **Backend**: Python, Flask, MySQL
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: MySQL 8.0
