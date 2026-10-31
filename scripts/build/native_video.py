"""Shared native video markup and opt-in deferred activation for page families."""

from html import escape as a


def render_native_video(video: dict, title: str, title_key: str, wrapper_class: str = "blog-native-video") -> str:
    layout_style = ""
    player_aspect_ratio = video.get("playerAspectRatio")
    if player_aspect_ratio:
        layout_style = f' style="aspect-ratio:{a(player_aspect_ratio)};width:100%"'
    elif video["width"] > video["height"]:
        layout_style = f' style="aspect-ratio:{video["width"]}/{video["height"]};width:100%"'
    deferred_attr = ' data-deferred-video=""' if video.get("deferUntilPlay") else ""
    source_attr = "data-src" if video.get("deferUntilPlay") else "src"
    return f'''<div class="{a(wrapper_class)}"{layout_style}>
<video controls{deferred_attr} height="{video["height"]}" playsinline poster="{a(video["poster"])}" preload="none" title="{a(title)}" data-i18n-title="{title_key}" width="{video["width"]}">
<source {source_attr}="{a(video["contentUrl"])}" type="video/mp4"/>
</video>
</div>'''


DEFERRED_VIDEO_SCRIPT = '''
<script>
document.querySelectorAll('video[data-deferred-video]').forEach(function(video) {
  video.addEventListener('click', function activateDeferredVideo() {
    var source = video.querySelector('source[data-src]');
    if (!source) return;
    source.src = source.dataset.src;
    source.removeAttribute('data-src');
    video.load();
    video.play();
  }, { once: true });
});
</script>'''
