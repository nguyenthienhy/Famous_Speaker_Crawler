import os

def download(url, keyname):
    os.system("youtube-dl \
        -i \
        --extract-audio \
        --audio-format mp3 \
        --audio-quality 0 \
        --write-auto-sub \
        --sub-lang vi \
        --convert-subs srt \
        --rm-cache-dir \
        --output " \
        + keyname \
        + "/%(title)s.%(ext)s " \
        + str(url))

def download_many_urls(urls_file, keyname):
    os.system("youtube-dl \
        -i \
        --extract-audio \
        --audio-format mp3 \
        --audio-quality 0 \
        --write-auto-sub \
        --sub-lang vi \
        --convert-subs srt \
        --rm-cache-dir \
        --output " \
        + keyname \
        + "/%(title)s.%(ext)s " \
        + str(urls_file))