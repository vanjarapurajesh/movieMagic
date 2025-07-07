from flask import Blueprint, render_template, request

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    movies = [
        {
            "title": "Inception",
            "poster_url": "https://image.tmdb.org/t/p/w300/edv5CZvWj09upOsy2Y6IwDhK8bt.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "1", "date": "2025-06-25", "time": "18:30"},
                {"show_id": "2", "date": "2025-06-25", "time": "21:00"}
            ]
        },
        {
            "title": "Interstellar",
            "poster_url": "https://image.tmdb.org/t/p/w300/rAiYTfKGqDCRIIqo664sY9XZIvQ.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "3", "date": "2025-06-26", "time": "17:00"},
                {"show_id": "4", "date": "2025-06-26", "time": "20:15"}
            ]
        },
        {
            "title": "The Dark Knight",
            "poster_url": "https://image.tmdb.org/t/p/w300/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "5", "date": "2025-06-27", "time": "19:00"},
                {"show_id": "6", "date": "2025-06-27", "time": "22:00"}
            ]
        },
        {
            "title": "Avatar: The Way of Water",
            "poster_url": "https://image.tmdb.org/t/p/w300/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "7", "date": "2025-06-28", "time": "16:00"},
                {"show_id": "8", "date": "2025-06-28", "time": "19:30"}
            ]
        },
        {
            "title": "Dune: Part Two",
            "poster_url": "https://image.tmdb.org/t/p/w300/8b8R8l88Qje9dn9OE8PY05Nxl1X.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "9", "date": "2025-06-29", "time": "15:45"},
                {"show_id": "10", "date": "2025-06-29", "time": "18:45"}
            ]
        },
        {
            "title": "Avengers: Endgame",
            "poster_url": "https://image.tmdb.org/t/p/w300/or06FN3Dka5tukK1e9sl16pB3iy.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "11", "date": "2025-06-30", "time": "20:00"},
                {"show_id": "12", "date": "2025-06-30", "time": "23:00"}
            ]
        },
        {
            "title": "Oppenheimer",
            "poster_url": "https://image.tmdb.org/t/p/w300/ptpr0kGAckfQkJeJIt8st5dglvd.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "13", "date": "2025-07-01", "time": "17:45"},
                {"show_id": "14", "date": "2025-07-01", "time": "21:15"}
            ]
        },
        {
            "title": "Spider-Man: No Way Home",
            "poster_url": "https://image.tmdb.org/t/p/w300/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "15", "date": "2025-07-02", "time": "18:00"},
                {"show_id": "16", "date": "2025-07-02", "time": "20:45"}
            ]
        }
    ]
    return render_template('index.html', movies=movies)

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/register')
def register():
    return render_template('register.html')

@bp.route('/dashboard')
def dashboard():
    movies = [
        {
            "title": "Inception",
            "poster_url": "https://image.tmdb.org/t/p/w300/edv5CZvWj09upOsy2Y6IwDhK8bt.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "1", "date": "2025-06-25", "time": "18:30"},
                {"show_id": "2", "date": "2025-06-25", "time": "21:00"}
            ]
        },
        {
            "title": "Interstellar",
            "poster_url": "https://image.tmdb.org/t/p/w300/rAiYTfKGqDCRIIqo664sY9XZIvQ.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "3", "date": "2025-06-26", "time": "17:00"},
                {"show_id": "4", "date": "2025-06-26", "time": "20:15"}
            ]
        },
        {
            "title": "The Dark Knight",
            "poster_url": "https://image.tmdb.org/t/p/w300/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "5", "date": "2025-06-27", "time": "19:00"},
                {"show_id": "6", "date": "2025-06-27", "time": "22:00"}
            ]
        },
        {
            "title": "Avatar: The Way of Water",
            "poster_url": "https://image.tmdb.org/t/p/w300/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "7", "date": "2025-06-28", "time": "16:00"},
                {"show_id": "8", "date": "2025-06-28", "time": "19:30"}
            ]
        },
        {
            "title": "Dune: Part Two",
            "poster_url": "https://image.tmdb.org/t/p/w300/8b8R8l88Qje9dn9OE8PY05Nxl1X.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "9", "date": "2025-06-29", "time": "15:45"},
                {"show_id": "10", "date": "2025-06-29", "time": "18:45"}
            ]
        },
        {
            "title": "Avengers: Endgame",
            "poster_url": "https://image.tmdb.org/t/p/w300/or06FN3Dka5tukK1e9sl16pB3iy.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "11", "date": "2025-06-30", "time": "20:00"},
                {"show_id": "12", "date": "2025-06-30", "time": "23:00"}
            ]
        },
        {
            "title": "Oppenheimer",
            "poster_url": "https://image.tmdb.org/t/p/w300/ptpr0kGAckfQkJeJIt8st5dglvd.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "13", "date": "2025-07-01", "time": "17:45"},
                {"show_id": "14", "date": "2025-07-01", "time": "21:15"}
            ]
        },
        {
            "title": "Spider-Man: No Way Home",
            "poster_url": "https://image.tmdb.org/t/p/w300/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg",
            "city": "Hyderabad",
            "showtimes": [
                {"show_id": "15", "date": "2025-07-02", "time": "18:00"},
                {"show_id": "16", "date": "2025-07-02", "time": "20:45"}
            ]
        }
    ]

    return render_template('dashboard.html', movies=movies)

@bp.route('/select-seats')
def select_seats():
    show_id = request.args.get("show_id")
    seats = []
    for row in "ABCDEFG":
        for num in range(1, 9):
            seat_id = f"{row}{num}"
            seats.append({
                "id": seat_id,
                "booked": seat_id in ["A1", "C3", "D4"]
            })
    return render_template("seat_map.html", seats=seats, show_id=show_id)



@bp.route('/payment', methods=["GET", "POST"])
def payment():
    if request.method == "POST":
        selected_seats = request.form.get("selected_seats", "")
        return render_template("payment.html", selected_seats=selected_seats.split(","))
    return render_template("payment.html", selected_seats=[])

@bp.route('/confirm-booking', methods=["POST"])
def confirm_booking():
    selected_seats = request.form.get("selected_seats")
    if not selected_seats:
        return render_template("confirmation.html", seats=[])
    return render_template("confirmation.html", seats=selected_seats.split(","))
