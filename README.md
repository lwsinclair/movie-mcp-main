# Movie MCP Server

[![smithery badge](https://smithery.ai/badge/@yusaaztrk/movie-mcp-main)](https://smithery.ai/server/@yusaaztrk/movie-mcp-main)

A Model Context Protocol (MCP) server that provides movie and TV show information using The Movie Database (TMDB) API.

## Features

- Search for movies and TV shows by name
- Get detailed information including:
  - Title, release date, and rating
  - Cast and crew information
  - Genres and runtime/episodes
  - Plot overview
  - Poster images
- Supports both movies and TV shows
- High-quality data from TMDB

## Usage

The server provides one tool:

### search_movie(query: str)

Search for movies and TV shows by name.

**Parameters:**
- `query`: The movie or TV show name to search for

**Returns:**
- Detailed information including:
  - Title and release year
  - IMDb-style rating and vote count
  - Genres and runtime/season info
  - Cast and director/creator information
  - Plot overview
  - Poster image URL

## Installation

### Installing via Smithery

To install movie-mcp-main for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@yusaaztrk/movie-mcp-main):

```bash
npx -y @smithery/cli install @yusaaztrk/movie-mcp-main --client claude
```

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python server.py
```

## API

This MCP server uses The Movie Database (TMDB) API which provides comprehensive movie and TV show data.
