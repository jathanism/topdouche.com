===
API
===

POST /profile
{"url"="http://about.me/williammwhite" | "http://facebook.com/wiliammwhite" | "http://twitter.com/opensolar"}
Creates a new profile object, returns its ID

GET /profile/ID
Returns the complete profile with comments and summarized rating

GET /profile/?url="http://about.me/williammwhite" | "http://facebook.com/wiliammwhite" | "http://twitter.com/opensolar"
Returns the complete profile with comments and summarized rating

POST /tag
{"name":"sunglasses","description":"","url":""}
I think providing for a description and reference URL could be useful.  "name" should be unique.

GET /tag/<name>
eg. http://topdouche.com/v1/tag/comehither
Returns the average tag rating, tag rating count and all comments associated with this tag

GET /profiles/?tag=comehither
Returns profiles tagged with comehither

POST /rating/profile
{"id":"PROFILE_ID", "value":2}
OR
{"url"="http://about.me/williammwhite" | "http://facebook.com/wiliammwhite" | "http://twitter.com/opensolar","value":2}

POST /rating/tag
{"name":"comehither", "value":2}

