# Database Schema Documentation

## Overview
This database schema is designed to effectively manage and analyze data related to movies, TV shows, people involved in their creation, ratings, and other related metadata. It is normalized to ensure efficient storage, maintainability, and scalability. The schema supports a variety of use cases, including querying data about ratings, collaborations, genre trends, and title details.

---

## Tables and Relationships

### 1. **Title_basic**
**Purpose**: Stores fundamental information about titles (movies, TV shows, etc.).

- **Columns**:
  - `tconst`: Unique identifier for each title (Primary Key).
  - `title_type`: Type of the title (e.g., movie, tvSeries).
  - `primary_title`: Main title used for release.
  - `original_title`: Original language title.
  - `is_adult`: Indicates whether the title is adult content.
  - `start_year`: Year of release or series start.
  - `end_year`: End year for TV series.
  - `runtime_minutes`: Duration of the title in minutes.

- **Relationships**:
  - Linked to `Title_ratings`, `Title_crew`, `Title_episode`, and `Title_principals`.

---

### 2. **Name_basic**
**Purpose**: Contains information about people (actors, directors, writers, etc.).

- **Columns**:
  - `nconst`: Unique identifier for each person (Primary Key).
  - `primary_name`: Name of the person.
  - `birth_year`: Year of birth.
  - `death_year`: Year of death (if applicable).

- **Relationships**:
  - Linked to `Title_principals`, `Title_directors`, and `Title_writers`.

---

### 3. **Title_ratings**
**Purpose**: Stores aggregated ratings and vote counts for titles.

- **Columns**:
  - `tconst`: Unique identifier for each title (Primary Key).
  - `average_rating`: Weighted average rating.
  - `num_votes`: Total number of votes.

- **Relationships**:
  - Linked to `Title_basic` via `tconst`.

---

### 4. **Title_crew**
**Purpose**: Contains information about directors and writers of titles.

- **Columns**:
  - `tconst`: Unique identifier for each title (Primary Key).
  - `directors`: List of `nconst` values for directors.
  - `writers`: List of `nconst` values for writers.

- **Relationships**:
  - Linked to `Name_basic` via `nconst` for directors and writers.

---

### 5. **Title_episode**
**Purpose**: Manages relationships between episodes and their parent series.

- **Columns**:
  - `tconst`: Unique identifier for each episode (Primary Key).
  - `parent_tconst`: Identifier for the parent series.
  - `season_number`: Season number of the episode.
  - `episode_number`: Episode number within the season.

- **Relationships**:
  - Linked to `Title_basic` for both episode and parent series details.

---

### 6. **Title_principals**
**Purpose**: Lists principal cast and crew members for titles.

- **Columns**:
  - `tconst`: Unique identifier for the title.
  - `ordering`: Specifies order of appearance.
  - `nconst`: Identifier for the person.
  - `category`: Job category (e.g., actor, director).
  - `job`: Specific job title.
  - `characters`: Roles played (if applicable).

- **Relationships**:
  - Linked to `Name_basic` via `nconst`.
  - Linked to `Title_basic` via `tconst`.

---

### 7. **Title_akas**
**Purpose**: Stores alternative names or localized versions of titles.

- **Columns**:
  - `tconst`: Identifier for the title.
  - `ordering`: Unique row identifier for a title.
  - `title`: Localized or alternative title.
  - `region`: Region associated with the title.
  - `language`: Language of the title.
  - `types`: Attributes describing the title type.
  - `attributes`: Additional descriptors.
  - `is_original_title`: Indicates whether it's the original title.

- **Relationships**:
  - Linked to `Title_basic` via `tconst`.

---

### 8. **Title_genre**
**Purpose**: Maps titles to their genres.

- **Columns**:
  - `tconst`: Identifier for the title.
  - `genre`: Genre associated with the title.

- **Relationships**:
  - Linked to `Title_basic` via `tconst`.

---

### 9. **Name_profession**
**Purpose**: Stores professions of people.

- **Columns**:
  - `nconst`: Identifier for the person.
  - `profession`: Profession of the person (e.g., actor, director).

- **Relationships**:
  - Linked to `Name_basic` via `nconst`.

---

### 10. **Known_for_title**
**Purpose**: Lists titles a person is known for.

- **Columns**:
  - `nconst`: Identifier for the person.
  - `known_title`: Identifier for the title.

- **Relationships**:
  - Linked to `Name_basic` and `Title_basic` via `nconst` and `tconst`, respectively.

---

## Design Rationale
1. **Normalization**:
   - The schema is normalized to minimize redundancy and ensure data integrity. Each table represents a single concept (e.g., titles, people, ratings, etc.).

2. **Flexibility**:
   - Designed to handle complex relationships, such as multiple directors, writers, genres, and cast members for a single title.

3. **Query Optimization**:
   - Clear relationships between tables enable efficient joins and indexing for common queries.

4. **Scalability**:
   - The structure supports the addition of new fields or relationships (e.g., adding new title attributes) without significant schema changes.

5. **Data Analysis**:
   - The schema supports a wide range of analytical queries, such as genre trends, collaboration patterns, and performance metrics.

---

## Usage Scenarios
- **Trend Analysis**:
  - Analyze ratings trends by decade or genre.
- **Collaboration Networks**:
  - Study relationships between directors, writers, and actors.
- **Popularity Insights**:
  - Identify popular titles, genres, or individuals.
- **Localization**:
  - Track regional trends using `Title_akas`.

---

## Future Enhancements
- Add tables for:
  - Audience demographics.
  - Revenue and box office data.
  - Streaming platform availability.


