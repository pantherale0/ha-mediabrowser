"""Media Source Implementation."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from homeassistant.components import media_source
from homeassistant.components.media_player import (
    BrowseError,
    BrowseMedia,
    MediaClass,
)
from homeassistant.core import HomeAssistant

from .const import DOMAIN


class UnknownMediaType(BrowseError):
    """Unknown media type."""


EXPANDABLES = ["album", "artist", "playlist", "season", "show"]
ITEM_TYPE_MEDIA_CLASS = {
    "album": MediaClass.ALBUM,
    "artist": MediaClass.ARTIST,
    "clip": MediaClass.VIDEO,
    "episode": MediaClass.EPISODE,
    "mixed": MediaClass.DIRECTORY,
    "movie": MediaClass.MOVIE,
    "playlist": MediaClass.PLAYLIST,
    "season": MediaClass.SEASON,
    "show": MediaClass.TV_SHOW,
    "station": MediaClass.ARTIST,
    "track": MediaClass.TRACK,
    "video": MediaClass.VIDEO,
}
