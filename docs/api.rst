===
API
===

Profiles
========

::

    POST /api/profile/add/
    {"url": "http://about.me/williammwhite"}

Creates a new profile object, returns its 'id'.

::

    POST /api/profile/tag/
    {"profile_id": 1, "tag": "bacon"}

Adds a tag to the specified profile (either by 'profile_id' or by 'url'). Tag must exist first.

::

    GET /api/profile/{id}

Returns the complete profile with comments and summarized rating.

::

    GET /api/profile/?url="http://about.me/williammwhite" 

Returns the complete profile with comments and summarized rating.

::

    GET /api/profiles/

Returns a list of profiles sorted by douchescore (desc.).

::

    GET /api/profiles/?tag=comehither

Returns profiles tagged with comehither.

Tags
====

::

    POST /api/tag/add/
    {"name": "sunglasses", "description": "", "reference_url": ""}

'name' must be unique; 'description' and 'reference_url' are optional but could be useful. 

::

    GET /api/tag/{name}

Returns the average tag rating, tag rating count and all comments associated with this tag.

::

    GET /api/tags/

Returns a list of tags sorted by rating (desc.)

Ratings
=======

::

    POST /api/rating/profile/
    {"id": "PROFILE_ID", "value":2}

Boosts the rating of the profile and returns the old and new scores.

::

    POST /api/rating/tag/
    {"name": "comehither", "value":2}

Boosts the rating of the tag and returns the old and new scores.

