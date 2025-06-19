from flask import Flask, render_template_string, request

app = Flask(__name__)

# Genre-specific movie mapping
genre_movies = {
    "Crime": ["The Godfather", "Pulp Fiction"],
    "Drama": ["The Shawshank Redemption", "Forrest Gump"],
    "Action": ["The Dark Knight", "Gladiator"],
    "Sci-Fi": ["Inception", "The Matrix", "Interstellar"],
    "Fantasy": ["The Lord of the Rings"]
}

genres = list(genre_movies.keys())

# Movie posters (TMDB URLs for reliability)
movie_posters = {
    "The Godfather": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
    "Pulp Fiction": "https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg",
    "The Shawshank Redemption": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
    "Forrest Gump": "https://image.tmdb.org/t/p/w500/saHP97rTPS5eLmrLQEcANmKrsFl.jpg",
    "The Dark Knight": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
    "Gladiator": "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg",
    "Inception": "https://image.tmdb.org/t/p/w500/edv5CZvWj09upOsy2Y6IwDhK8bt.jpg",
    "The Matrix": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
    "Interstellar": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
    "The Lord of the Rings": "https://image.tmdb.org/t/p/w500/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg"
}

# Fallback poster image
fallback_poster = "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"

# Movie streaming/info links (for demo, IMDb or streaming links)
movie_links = {
    "The Godfather": "https://www.justwatch.com/us/movie/the-godfather",
    "Pulp Fiction": "https://www.justwatch.com/us/movie/pulp-fiction",
    "The Shawshank Redemption": "https://www.justwatch.com/us/movie/the-shawshank-redemption",
    "Forrest Gump": "https://www.justwatch.com/us/movie/forrest-gump",
    "The Dark Knight": "https://www.justwatch.com/us/movie/the-dark-knight",
    "Gladiator": "https://www.justwatch.com/us/movie/gladiator",
    "Inception": "https://www.justwatch.com/us/movie/inception",
    "The Matrix": "https://www.justwatch.com/us/movie/the-matrix",
    "Interstellar": "https://www.justwatch.com/us/movie/interstellar",
    "The Lord of the Rings": "https://www.justwatch.com/us/movie/the-lord-of-the-rings-the-fellowship-of-the-ring"
}

template = '''
<!DOCTYPE html>
<html>
<head>
    <title>FlickVibe: What's Your Mood?</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap" rel="stylesheet">
    <style>
        html, body { height: 100%; }
        body {
            background: #141414;
            color: #fff;
            font-family: 'Roboto', Arial, sans-serif;
            margin: 0;
            padding: 0;
            min-height: 100vh;
            overflow-x: hidden;
        }
        .bg-collage {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            z-index: 0;
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            grid-template-rows: repeat(3, 1fr);
            gap: 0;
            opacity: 0.55;
        }
        .bg-collage img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: none;
            box-shadow: 0 8px 32px #e50914cc, 0 2px 8px #000a;
        }
        .bg-overlay {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(20, 20, 20, 0.55);
            z-index: 1;
        }
        .container {
            max-width: 700px;
            margin: 32px auto 0 auto;
            background: #181818;
            border-radius: 12px;
            box-shadow: 0 0 20px #000;
            padding: 24px 10px 18px 10px;
            position: relative;
            z-index: 2;
        }
        h1 {
            color: #e50914;
            font-size: 2.1em;
            margin-bottom: 10px;
            letter-spacing: 2px;
            text-align: center;
            font-family: 'Roboto', Arial, sans-serif;
        }
        .subtitle {
            text-align: center;
            color: #fff;
            font-size: 1.08em;
            margin-bottom: 24px;
            font-weight: 400;
        }
        label, select, input[type="submit"] {
            display: block;
            width: 100%;
            margin-bottom: 16px;
        }
        select {
            background: #222;
            color: #fff;
            border: 1.5px solid #e50914;
            border-radius: 5px;
            padding: 12px;
            font-size: 1.08em;
        }
        input[type="submit"] {
            background: #e50914;
            color: #fff;
            border: none;
            border-radius: 5px;
            padding: 14px;
            font-size: 1.13em;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.2s;
        }
        input[type="submit"]:hover {
            background: #b0060f;
        }
        .recommendations {
            margin-top: 28px;
        }
        .recommendations h2 {
            color: #e50914;
            margin-bottom: 16px;
            font-size: 1.18em;
        }
        .movie-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
            justify-content: center;
        }
        .movie-card {
            background: #222;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
            width: 150px;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 12px 8px 8px 8px;
            transition: transform 0.2s, box-shadow 0.2s;
            cursor: pointer;
            text-decoration: none;
        }
        .movie-card:hover {
            transform: translateY(-4px) scale(1.03);
            box-shadow: 0 6px 24px #e50914aa;
        }
        .movie-poster {
            width: 100px;
            height: 150px;
            object-fit: cover;
            border-radius: 6px;
            margin-bottom: 8px;
            box-shadow: 0 2px 8px #000a;
        }
        .movie-title {
            color: #fff;
            font-size: 1em;
            text-align: center;
            font-weight: 500;
            margin-bottom: 2px;
        }
        .no-movies {
            color: #bbb;
            text-align: center;
            margin-top: 16px;
        }
        @media (max-width: 900px) {
            .container { max-width: 98vw; padding: 8px; }
            .movie-card { width: 38vw; min-width: 110px; }
            .movie-poster { width: 80px; height: 120px; }
            .bg-collage { grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(5, 1fr); }
        }
        @media (max-width: 600px) {
            .container { max-width: 100vw; padding: 2vw; }
            .movie-card { width: 80vw; min-width: 90px; }
            .movie-poster { width: 60vw; height: 90vw; max-width: 140px; max-height: 210px; }
            .bg-collage { grid-template-columns: repeat(2, 1fr); grid-template-rows: repeat(6, 1fr); }
            h1 { font-size: 1.3em; }
            .subtitle { font-size: 0.98em; }
        }
        @media (max-width: 400px) {
            .movie-card { width: 96vw; }
            .movie-poster { width: 80vw; height: 120vw; }
        }
    </style>
</head>
<body>
    <div class="bg-collage">
        {% for poster in movie_posters.values() %}
        <img src="{{ poster }}" alt="Movie Poster" onerror="this.onerror=null;this.src='{{ fallback_poster }}';">
        {% endfor %}
        {% for poster in movie_posters.values() %}
        <img src="{{ poster }}" alt="Movie Poster" onerror="this.onerror=null;this.src='{{ fallback_poster }}';">
        {% endfor %}
    </div>
    <div class="bg-overlay"></div>
    <div class="container">
        <h1>FlickVibe: What's Your Mood?</h1>
        <div class="subtitle">Pick a genre and discover your next binge-worthy flick!</div>
        <form method="post">
            <label for="genre">Choose your preferred genre:</label>
            <select name="genre" id="genre">
                {% for genre in genres %}
                <option value="{{ genre }}" {% if genre == selected_genre %}selected{% endif %}>{{ genre }}</option>
                {% endfor %}
            </select>
            <input type="submit" value="Show Me Flicks!">
        </form>
        {% if recommendations is not none %}
        <div class="recommendations">
            <h2>Top Picks for {{ selected_genre }}</h2>
            {% if recommendations %}
            <div class="movie-grid">
                {% for movie in recommendations %}
                <a class="movie-card" href="{{ movie_links.get(movie, '#') }}" target="_blank">
                    <img class="movie-poster" src="{{ movie_posters.get(movie, '') }}" alt="{{ movie }} poster" onerror="this.onerror=null;this.src='{{ fallback_poster }}';">
                    <div class="movie-title">{{ movie }}</div>
                </a>
                {% endfor %}
            </div>
            {% else %}
            <p class="no-movies">No movies found for that genre.</p>
            {% endif %}
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = None
    selected_genre = genres[0]  # Default to first genre
    if request.method == 'POST':
        selected_genre = request.form['genre']
        recommendations = genre_movies.get(selected_genre, [])
    return render_template_string(
        template,
        genres=genres,
        recommendations=recommendations,
        selected_genre=selected_genre,
        movie_posters=movie_posters,
        movie_links=movie_links,
        fallback_poster=fallback_poster
    )

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
