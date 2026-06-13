#!/usr/bin/env python3
"""Generate per-song Spotify-save landing pages for Solomon Nights.

Add a song: append {title, trackId} to songs.json and re-run. Each song gets
its own page at /<slug>/ ; root index.html is an artist hub. Cover art is
fetched from Spotify oEmbed at build time. No secrets here (pixel id is public).
"""
import json, re, os, sys, urllib.request

PIXEL    = "1022464693584913"
PLAYLIST = "053laY69PHb8Sy27Xnb7Yh"
ARTIST   = "Solomon Nights"
DOMAIN   = "music.solomonnights.com"
TAGLINE  = "Raw acoustic · contemporary Christian"
HERE     = os.path.dirname(os.path.abspath(__file__))
ROOT     = os.path.dirname(HERE)

def slugify(t):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", t.lower())).strip("-")

def cover(track_id):
    url = "https://open.spotify.com/oembed?url=https://open.spotify.com/track/" + track_id
    with urllib.request.urlopen(url, timeout=25) as r:
        thumb = json.load(r).get("thumbnail_url", "")
    return thumb.replace("ab67616d00001e02", "ab67616d0000b273")

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<title>Solomon Nights — @@TITLE@@</title>
<meta name="description" content="Listen to Solomon Nights and save the playlist on Spotify. Raw, stripped-back, acoustic contemporary Christian music." />
<meta property="og:type" content="music.song" />
<meta property="og:title" content="Solomon Nights — @@TITLE@@" />
<meta property="og:description" content="Save the playlist on Spotify. Raw acoustic contemporary Christian music." />
<meta property="og:image" content="@@COVER@@" />
<meta property="og:url" content="https://@@DOMAIN@@/@@SLUG@@" />
<meta name="theme-color" content="#15110f" />
<link rel="icon" href="@@COVER@@" />
<style>
  * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
  html, body { margin: 0; height: 100%; }
  body { background: #15110f; color: #f3ece4; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; display: flex; align-items: center; justify-content: center; min-height: 100svh; padding: 24px; }
  .card { width: 100%; max-width: 360px; text-align: center; }
  .artist { color: #c9a27a; font-size: 12px; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 18px; }
  .artist a { color: inherit; text-decoration: none; }
  .cover { width: 100%; aspect-ratio: 1/1; border-radius: 10px; border: 0.5px solid #3a322c; display: block; object-fit: cover; background: #221b16; }
  .title { font-size: 22px; font-weight: 600; margin: 20px 0 4px; }
  .tag { color: #9c8a7b; font-size: 13px; margin: 0 0 24px; }
  .save { display: flex; align-items: center; justify-content: center; gap: 9px; background: #1db954; color: #0b3d20; font-size: 16px; font-weight: 600; text-decoration: none; padding: 15px; border-radius: 26px; width: 100%; }
  .save:active { transform: scale(0.985); }
  .hint { color: #8a7b6d; font-size: 12px; margin-top: 12px; line-height: 1.5; }
  .foot { color: #6f6157; font-size: 11px; margin-top: 22px; padding-top: 16px; border-top: 0.5px solid #2c251f; }
  .foot a { color: #8a7b6d; text-decoration: none; }
</style>
</head>
<body>
  <main class="card">
    <div class="artist"><a href="/">Solomon Nights</a></div>
    <img class="cover" alt="@@TITLE@@ — Solomon Nights cover art" src="@@COVER@@" />
    <h1 class="title">@@TITLE@@</h1>
    <p class="tag">@@TAGLINE@@</p>
    <a id="save" class="save" href="https://open.spotify.com/track/@@TRACK@@?context=spotify:playlist:@@PLAYLIST@@">
      <svg width="19" height="19" viewBox="0 0 24 24" fill="#0b3d20" aria-hidden="true"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Zm4.59 14.44a.62.62 0 0 1-.86.21c-2.35-1.44-5.3-1.76-8.79-.96a.62.62 0 1 1-.28-1.21c3.82-.88 7.09-.5 9.72 1.1.3.18.39.57.21.86Zm1.22-2.72a.78.78 0 0 1-1.07.26c-2.69-1.66-6.79-2.14-9.97-1.17a.78.78 0 1 1-.45-1.49c3.63-1.1 8.15-.57 11.24 1.33.36.22.48.7.25 1.07Zm.11-2.84C14.8 8.92 9.5 8.74 6.45 9.67a.93.93 0 1 1-.54-1.78c3.5-1.06 9.35-.86 12.99 1.3a.93.93 0 1 1-.95 1.6Z"/></svg>
      Save on Spotify
    </a>
    <p class="hint">Opens in the Spotify app on this song —<br>tap the heart to save the playlist</p>
    <div class="foot">Part of the <a href="https://open.spotify.com/playlist/@@PLAYLIST@@">“This is Solomon Nights”</a> playlist</div>
  </main>
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','@@PIXEL@@');
var utm={};location.search.replace(/^\\?/,'').split('&').forEach(function(p){
  if(!p)return;var kv=p.split('=');if(/^utm_/.test(kv[0]))utm[kv[0]]=decodeURIComponent(kv[1]||'');});
var meta=Object.assign({artist:'solomon_nights',song:'@@TITLE@@',content_name:'@@TITLE@@',content_category:'solomon_nights'},utm);
fbq('track','PageView',meta);
fbq('track','ViewContent',meta);
document.getElementById('save').addEventListener('click',function(){fbq('trackCustom','SpotifySaveClick',meta);});
</script>
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=@@PIXEL@@&ev=PageView&noscript=1"/></noscript>
</body>
</html>
"""

HUB = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<title>Solomon Nights</title>
<meta name="description" content="Solomon Nights — raw, stripped-back acoustic contemporary Christian music. Save the playlist on Spotify." />
<meta property="og:title" content="Solomon Nights" />
<meta property="og:description" content="Save the playlist on Spotify. Raw acoustic contemporary Christian music." />
<meta name="theme-color" content="#15110f" />
<style>
  * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
  html, body { margin: 0; }
  body { background: #15110f; color: #f3ece4; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; display: flex; justify-content: center; min-height: 100svh; padding: 32px 24px; }
  .wrap { width: 100%; max-width: 380px; }
  .artist { text-align: center; color: #c9a27a; font-size: 13px; letter-spacing: 3px; text-transform: uppercase; }
  .lead { text-align: center; color: #9c8a7b; font-size: 13px; margin: 8px 0 22px; }
  .save { display: flex; align-items: center; justify-content: center; gap: 9px; background: #1db954; color: #0b3d20; font-size: 16px; font-weight: 600; text-decoration: none; padding: 15px; border-radius: 26px; margin-bottom: 26px; }
  .save:active { transform: scale(0.985); }
  .row { display: flex; align-items: center; gap: 12px; padding: 9px; border-radius: 10px; text-decoration: none; color: #f3ece4; }
  .row:active { background: #221b16; }
  .row img { width: 48px; height: 48px; border-radius: 7px; object-fit: cover; border: 0.5px solid #3a322c; }
  .row .t { font-size: 15px; }
  .row .c { margin-left: auto; color: #5f5147; font-size: 18px; }
  .foot { text-align: center; color: #6f6157; font-size: 11px; margin-top: 24px; }
</style>
</head>
<body>
  <div class="wrap">
    <div class="artist">Solomon Nights</div>
    <div class="lead">@@TAGLINE@@</div>
    <a class="save" href="https://open.spotify.com/playlist/@@PLAYLIST@@">Save the playlist on Spotify</a>
@@ROWS@@
    <div class="foot">@@COUNT@@ songs · all on the “This is Solomon Nights” playlist</div>
  </div>
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','@@PIXEL@@');fbq('track','PageView',{artist:'solomon_nights'});
</script>
</body>
</html>
"""

ROW = '    <a class="row" href="/@@SLUG@@"><img src="@@COVER@@" alt="" /><span class="t">@@TITLE@@</span><span class="c">›</span></a>'

def render(tmpl, **kw):
    for k, v in kw.items():
        tmpl = tmpl.replace("@@" + k + "@@", v)
    return tmpl

def main():
    songs = json.load(open(os.path.join(HERE, "songs.json")))
    rows = []
    for s in songs:
        slug = slugify(s["title"])
        cov = cover(s["trackId"])
        page = render(PAGE, TITLE=s["title"], SLUG=slug, COVER=cov, TRACK=s["trackId"],
                      PLAYLIST=PLAYLIST, PIXEL=PIXEL, DOMAIN=DOMAIN, TAGLINE=TAGLINE)
        os.makedirs(os.path.join(ROOT, slug), exist_ok=True)
        open(os.path.join(ROOT, slug, "index.html"), "w", encoding="utf-8").write(page)
        rows.append(render(ROW, SLUG=slug, COVER=cov, TITLE=s["title"]))
        print("built /%s" % slug)
    hub = render(HUB, TAGLINE=TAGLINE, PLAYLIST=PLAYLIST, PIXEL=PIXEL,
                 ROWS="\n".join(rows), COUNT=str(len(songs)))
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(hub)
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    print("built / (hub) + .nojekyll : %d songs" % len(songs))

if __name__ == "__main__":
    main()
