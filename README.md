# TTT (Table Tennis Tracker)

**Project Status**: Work In Progress

## Project Overview

TTT (Table Tennis Tracker) is a farewell gift I built for my office to track table tennis scores between players. It allows players to log in, record their scores against other players, and rate their performance. The app displays leaderboards to highlight the top performers, helping us determine who has the most wins in the office.

## Features

- **Login System**: Users can create accounts and log in to the app.
- **Score Tracking**: Players can log match results against their colleagues.
- **Player Rating**: Track and rate players based on their performance.
- **Leaderboards**: Displays the top players with the most wins in the office.

## Tech Stack

- **Backend**: FastAPI
- **Frontend**: React.js
- **Database**: PostgreSQL (or any SQL database of your choice)
- **Authentication**: FastAPI's OAuth2 or JWT authentication

## Installation Instructions

### Backend Setup (FastAPI)

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/TTT.git
   ```

2. Navigate to the backend directory:

   ```bash
   cd TTT/backend
   ```

3. Set up a virtual environment and install the dependencies:

   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup (React)

1. Navigate to the frontend directory:

   ```bash
   cd TTT/frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the React development server:

   ```bash
   npm start
   ```

### Database Setup

1. Ensure PostgreSQL is running and configure the connection in the `.env` file located in the `backend` directory.
2. Run the database migrations (if using one):

   ```bash
   alembic upgrade head
   ```

## Usage

1. Register or log in to the app.
2. Start adding matches by selecting the players and submitting the scores.
3. Check the leaderboards to see who's currently dominating the office table tennis scene.

## Future Enhancements

- Player statistics and win streaks
- Match history
- Teams and group matches
- Improved ranking algorithms

---

## License

This project is licensed under the MIT License.

## Acknowledgments

- My office colleagues for all the great table tennis matches
- Farewell gift to the amazing work culture!

---

**Note**: This project is still under development, and contributions are welcome!
