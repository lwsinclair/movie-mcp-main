import requests
import json

def searchMovie(query: str) -> str:
    """
    Search for movies and TV shows using TMDB API.
    """
    try:
        # TMDB API key (free tier)
        api_key = "8265bd1679663a7ea12ac168da84d2e8"  # Public demo key
        
        # Search for movies and TV shows
        search_url = f"https://api.themoviedb.org/3/search/multi?api_key={api_key}&query={query}"
        
        response = requests.get(search_url)
        
        if response.status_code != 200:
            return f"Error: Could not search for '{query}'"
        
        data = response.json()
        
        if not data.get('results') or len(data['results']) == 0:
            return f"No results found for '{query}'"
        
        # Get the first result (most relevant)
        result = data['results'][0]
        
        # Determine if it's a movie or TV show
        media_type = result.get('media_type', 'unknown')
        
        if media_type == 'movie':
            return formatMovieDetails(result, api_key)
        elif media_type == 'tv':
            return formatTVDetails(result, api_key)
        else:
            return formatBasicDetails(result)
            
    except Exception as e:
        return f"Error searching for '{query}': {str(e)}"

def formatMovieDetails(movie: dict, api_key: str) -> str:
    """Format movie details."""
    try:
        movie_id = movie['id']
        
        # Get detailed movie info
        details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&append_to_response=credits"
        details_response = requests.get(details_url)
        
        if details_response.status_code == 200:
            details = details_response.json()
        else:
            details = movie
        
        title = details.get('title', 'Unknown Title')
        release_date = details.get('release_date', 'Unknown')
        overview = details.get('overview', 'No overview available')
        rating = details.get('vote_average', 0)
        vote_count = details.get('vote_count', 0)
        runtime = details.get('runtime', 'Unknown')
        
        # Get genres
        genres = [genre['name'] for genre in details.get('genres', [])]
        genre_str = ', '.join(genres) if genres else 'Unknown'
        
        # Get cast (first 5 actors)
        cast = []
        if 'credits' in details and 'cast' in details['credits']:
            cast = [actor['name'] for actor in details['credits']['cast'][:5]]
        cast_str = ', '.join(cast) if cast else 'Cast information not available'
        
        # Get director
        director = 'Unknown'
        if 'credits' in details and 'crew' in details['credits']:
            for crew_member in details['credits']['crew']:
                if crew_member['job'] == 'Director':
                    director = crew_member['name']
                    break
        
        # Format poster URL
        poster_path = details.get('poster_path')
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else "No poster available"
        
        movie_info = f"""🎬 **{title}** ({release_date[:4] if release_date != 'Unknown' else 'Unknown'})

⭐ **Rating:** {rating}/10 ({vote_count:,} votes)
🎭 **Genres:** {genre_str}
⏱️ **Runtime:** {runtime} minutes
🎬 **Director:** {director}

👥 **Cast:** {cast_str}

📝 **Overview:**
{overview}

🖼️ **Poster:** {poster_url}"""
        
        return movie_info
        
    except Exception as e:
        return formatBasicDetails(movie)

def formatTVDetails(tv_show: dict, api_key: str) -> str:
    """Format TV show details."""
    try:
        tv_id = tv_show['id']
        
        # Get detailed TV info
        details_url = f"https://api.themoviedb.org/3/tv/{tv_id}?api_key={api_key}&append_to_response=credits"
        details_response = requests.get(details_url)
        
        if details_response.status_code == 200:
            details = details_response.json()
        else:
            details = tv_show
        
        name = details.get('name', 'Unknown Title')
        first_air_date = details.get('first_air_date', 'Unknown')
        overview = details.get('overview', 'No overview available')
        rating = details.get('vote_average', 0)
        vote_count = details.get('vote_count', 0)
        seasons = details.get('number_of_seasons', 'Unknown')
        episodes = details.get('number_of_episodes', 'Unknown')
        
        # Get genres
        genres = [genre['name'] for genre in details.get('genres', [])]
        genre_str = ', '.join(genres) if genres else 'Unknown'
        
        # Get cast (first 5 actors)
        cast = []
        if 'credits' in details and 'cast' in details['credits']:
            cast = [actor['name'] for actor in details['credits']['cast'][:5]]
        cast_str = ', '.join(cast) if cast else 'Cast information not available'
        
        # Get creators
        creators = []
        if 'created_by' in details:
            creators = [creator['name'] for creator in details['created_by']]
        creator_str = ', '.join(creators) if creators else 'Unknown'
        
        # Format poster URL
        poster_path = details.get('poster_path')
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else "No poster available"
        
        tv_info = f"""📺 **{name}** ({first_air_date[:4] if first_air_date != 'Unknown' else 'Unknown'})

⭐ **Rating:** {rating}/10 ({vote_count:,} votes)
🎭 **Genres:** {genre_str}
📺 **Seasons:** {seasons} | **Episodes:** {episodes}
🎬 **Created by:** {creator_str}

👥 **Cast:** {cast_str}

📝 **Overview:**
{overview}

🖼️ **Poster:** {poster_url}"""
        
        return tv_info
        
    except Exception as e:
        return formatBasicDetails(tv_show)

def formatBasicDetails(item: dict) -> str:
    """Format basic details when detailed info is not available."""
    title = item.get('title') or item.get('name', 'Unknown Title')
    release_date = item.get('release_date') or item.get('first_air_date', 'Unknown')
    overview = item.get('overview', 'No overview available')
    rating = item.get('vote_average', 0)
    media_type = item.get('media_type', 'unknown')
    
    type_emoji = "🎬" if media_type == 'movie' else "📺" if media_type == 'tv' else "🎭"
    
    basic_info = f"""{type_emoji} **{title}** ({release_date[:4] if release_date != 'Unknown' else 'Unknown'})

⭐ **Rating:** {rating}/10
📝 **Overview:** {overview}"""
    
    return basic_info
