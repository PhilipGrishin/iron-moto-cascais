#!/usr/bin/env python3
"""Import an approved partner hero using the existing responsive image encoder."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageOps
from authorized_dealer_data import COPY_DEALER_PAGES
from stage_pages_data import STAGE_PAGES
from import_project_images import save_variants

SITE_ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--family', choices=('dealer','stage'), default='dealer')
    parser.add_argument('slug')
    parser.add_argument('source', type=Path)
    args = parser.parse_args()
    registry = STAGE_PAGES if args.family == 'stage' else COPY_DEALER_PAGES
    media = registry[args.slug]['hero']
    if media.get('source_sha256') and hashlib.sha256(args.source.read_bytes()).hexdigest() != media['source_sha256']:
        raise ValueError('Hero source checksum differs from the approved registry')
    base = SITE_ROOT / media['base'].lstrip('/')
    base.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(args.source) as raw:
        image = ImageOps.exif_transpose(raw).convert('RGB')
        image.info.clear()
        if max(media['widths']) > image.width: raise ValueError('Hero upscaling is forbidden')
        if round(image.height * media['width'] / image.width) != media['height']:
            raise ValueError('Registered hero aspect ratio differs from the supplied image')
        save_variants(image, base, media['widths'], jpeg_fallback=True)
    entries=[]
    for width in media['widths']:
        for ext in ('avif','webp','jpg'):
            path=base.with_name(f'{base.name}-{width}.{ext}')
            with Image.open(path) as item:
                if item.getexif(): raise ValueError(f'EXIF remains: {path.name}')
                dimensions=list(item.size)
            entries.append({'path':str(path.relative_to(SITE_ROOT)), 'bytes':path.stat().st_size,'dimensions':dimensions,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    manifest={'source_filename':args.source.name,'source_sha256':hashlib.sha256(args.source.read_bytes()).hexdigest(),'files':entries}
    base.with_name(f'{args.slug}-media.json').write_text(json.dumps(manifest,indent=2)+'\n')


if __name__=='__main__': main()
