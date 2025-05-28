from mcp.server.fastmcp import FastMCP
from app import searchMovie

# Initialize MCP server
mcp = FastMCP("movie-mcp")

@mcp.tool()
async def search_movie(query: str) -> str:
    """
    Search for movies and TV shows.
    
    Args:
        query: The movie or TV show name to search for
    
    Returns:
        Detailed information about the movie/TV show including cast, rating, overview, and poster
    """
    # Get movie/TV show info from the app
    movie_info = searchMovie(query)
    if not movie_info:
        return "No movie or TV show information found."

    return movie_info

if __name__ == "__main__":
    mcp.run(transport="stdio")
