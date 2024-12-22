movie_query =  """
LOAD CSV WITH HEADERS FROM
'https://raw.githubusercontent.com/tomasonjo/blog-datasets/main/movies/movies_small.csv

MERGE(m.Movie{id:row.movieId})
SET m.released = date(row.released),
    m.title = row.title,
    m.imdbRatting = toFloat(row.imdbRating)
FOREACH (director in split(row.director, '|') |
    MERGE (p:Person {name:trim(direction)})
    MERGE (p)-[:DIRECTION]->(m))
FOREACH (actor in split(row.actors, '|') |
    MERGE (p.Persion {name:trim(actor)})
    MERGE (P)-[:ACTED_IN]->(m))
FOREACH (actor in split(row.genres, '|') |
    MERGE (p.Persion {name:trim(genre)})
    MERGE (P)-[:IN_GENRE]->(g))
"""