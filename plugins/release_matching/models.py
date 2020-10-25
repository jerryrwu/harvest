import re

RELEASE_IDENTIFIERS = {
    'deluxe',
    'remastered',
    'deluxe edition',
    'edición remasterizada',
    'radio edit',
}


def _normalize_artist(artist):
    artist = artist.lower()
    artist = artist.replace('/', ' ').replace('-', ' ')
    artist = re.sub(' +', ' ', artist)
    artist = artist.strip()
    return artist


def _normalize_title(title):
    title = title.lower()
    for release_identifier in RELEASE_IDENTIFIERS:
        title = title.replace('({})'.format(release_identifier), '')
    title = title.replace('/', ' ').replace('-', ' ')
    title = re.sub(
        r'\([^()]*(deluxe|remaster|score|music|anniversary|edition|soundtrack|live)[^()]*\)',
        '',
        title,
    )
    title = re.sub(' +', ' ', title)
    title = title.strip()
    return title


class ReleaseMatchInfo:
    def __init__(self, artists, title):
        self.artists = artists
        self.title = title

        self.joined_artists = ', '.join(self.artists)
        self.normalized_artists = [_normalize_artist(artist) for artist in artists]
        self.normalized_artists_joined = ' '.join(self.normalized_artists)
        self.normalized_title = _normalize_title(self.title)

    def equals(self, match_info):
        if self.normalized_title != match_info.normalized_title:
            return False
        if len(set(self.normalized_artists) & set(match_info.normalized_artists)) == 0:
            return False
        return True

    def __str__(self):
        return 'MatchInfo({} - {})'.format(self.joined_artists, self.title)