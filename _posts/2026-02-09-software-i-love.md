---
layout: post
title: Software I love
author: Jacob Hartzer
date: 2026-02-09
thumbnail:
tags: Software
---

This is a list, in no particular order, of software that I love, use regularly, and maybe go as far as recommend to strangers.

# Media

### [Jellyfin](https://jellyfin.org/)

Jellyfin is an open-source alternative to Plex. It provides an excellent way to organize and stream my music and movies to any device from TVs to Phones. The metadata handling is excellent for movies tagged using IMDB references, and I utilize a python script to automatically create playlists from directories. While the [jellyfin](https://play.google.com/store/search?q=jellyfin&c=apps) app is great for streaming, I use [finamp](https://play.google.com/store/search?q=finamp&c=apps) for music for its offline capabilities.

### [Audiobookshelf](https://www.audiobookshelf.org/)

If you’re an avid audiobook listener like me, Audiobookshelf is a game-changer. It does what it says on the tin: it creates a bookshelf-like interface for audiobooks, with powerful metadata handling. A great resource if you purchase audiobooks from a source such as [libro.fm](https://libro.fm/), and the companion [audiobookshelf](https://play.google.com/store/apps/details?id=com.audiobookshelf.app&hl=en-US) app is fantastic.

### [Calibre-Web](https://github.com/janeczku/calibre-web)

My personal Library of Alexandria. It provides a gorgeous clean interface for browsing and sending my e-books to my devices. This pairs nicely with a epub reader, with my current favorite being [Moon+ Reader](https://play.google.com/store/apps/details?id=com.flyersoft.moonreader) for its simple-yet-customizable interface, though I have used [Freda](https://play.google.com/store/apps/details?id=freda.freda&hl=en-US) in the past and liked that, too, but switched after hitting too many paywalls.

### [Wallabag](https://wallabag.org/)

Wallabag is my 'read-it-later' solution that I found after Mozilla killed Pocket (RIP). Whenever I come across an article I either want to read later or come back to, I save it here. It strips the ads and clutter, leaving me with just the text I want to consume. Because I host the database, I don't have to worry about losing data or paying a high fee for the low bandwidth of syncing text between my browser and phone.

# Memories and Documents

### [Immich](https://immich.app/)

Immich is, in my opinion, the best self-hosted competitor to Google Photos. It’s super fast so handles massive libraries with ease. Immich has made it so my family can actually look through the massive backlog of photos and videos we have instead of needing to download them off a drive somewhere just to preview it. The facial recognition features are nice, any my only complaint is sometimes the image backup won't start until you open the app (or only happens once a day when the app is closed? I'm not sure I assume it's a battery issue.) Either way I love it and it's been fun to use [immich-kiosk](https://github.com/damongolding/immich-kiosk) to transform some albums into digital photo frames.

### [Nextcloud](https://nextcloud.com/)

Nextcloud is my Google Drive replacement since I kept running up against their 15 GB limit across all services. I specifically wanted something that acted as a storage drive for documents and also supported collaborative editing in the browser. Adding [Collabora Online](https://www.collaboraonline.com/partners/nextcloud/) was a killer feature for me, and made it so Nextcloud was truly a drop-in replacement. The DAVS interface and native desktop clients are nice too for large file transfers and a snappier interface. Especially on windows, the virtual files feature is awesome for managing offline files.

# Productivity

### [Obsidian](https://obsidian.md/)

Obsidian is my Zettelkasten for personal and work life management. It’s a markdown-based note-taking app that stores files locally with a rich extension marketplace and many customization options. I like the idea that I can open my notes in other file editors and integrate into other tools as needed. Additionally, the openness of Obsidian allows me to roll my own sync server via the excellent [Self-hosted LiveSync](https://github.com/vrtmrz/obsidian-livesync) extension. I use the templates to create weekly notes for work and manage my to-do list.

### [Remember The Milk](https://www.rememberthemilk.com/)

I have tried *a lot* of different to-do list tools, but Remember the Milk is by far my favorite. Being able to add **start dates** separate from **due dates** is table stakes for any task management app, and RTMs advanced filtering capability is excellent for context management and task prioritization. Any one that follows the "Getting Things Done" method would really enjoy RTM.

# Utilities

### [OctoPrint](https://octoprint.org/)

Do you ever get tired of moving the same SD card between your computer and the 3D printer? Do you have a Raspberry Pi lying around collecting dust? If yes to these two things, then OctoPrint is perfect for you! This server acts as my 3D printer's interface client. It allows for file uploading, status monitoring, camera feeds, and time estimation all from a web server. Now I don't have to walk across the room to start a print, assuming the printer is even on!

### [Uptime Kuma](https://uptimekuma.org/)

At the end of the day, there is no point to doing any of these things if they don't work consistently. Also, if I want my family to use these tools (and enjoy using them instead of seeing it as a burden) I need it all to be consistent. Uptime Kuma is how I know that my services are working so I can catch errors before someone else does. The queries are very powerful handling raw JSON to regular HTTP, and allows for retries for a powerful monitoring tool. Combining this with a simple Telegram notification bot (via [BotFather](https://telegram.me/BotFather)), I can get notified any time any of my services goes down.

### [Vaultwarden](https://github.com/dani-garcia/vaultwarden)

Vaultwarden is a lightweight implementation of Bitwarden that is compatible with the APIs of the various first-party clients. It’s the vault for my digital life—passwords, 2FA, passkeys, and secure notes. The password sharing is very powerful within my household (across multiple devices, too) so gone are the days of sharing passwords via sticky notes. Especially with the increasing prevalence of passkeys, Vaultwarden supports syncing of passkeys between my desktop and phone, which drastically reduces the risk if my phone takes a dip in the lake.

### [Handy](https://handy.computer/)

Handy is a free, open-source speech-to-text tool that runs entirely on your local machine. It can be tied to a hotkey and acts as a virtual keyboard that types the text into whatever window is active. This means you don't have to wait for whatever app you're using to support dictation, giving a consistent experience across the desktop.

# Home-Lab

### [Pi-Hole](https://pi-hole.net/)

Pi-Hole runs as my network’s DNS authority and blocks ads, trackers, and analytics at the source, before they even can leave the premises. This makes for cleaner pages, faster load times, and an overall more pleasant browsing experience. There are definitely some growing pains, though, as you figure out what services *absolutely require ads* to run, so you will inevitably need to whitelist some things.

### [Caddy](https://caddyserver.com/)

Caddy is the "it just works" HTTPS reverse proxy. I use it in front of every self-hosted service I run, and I basically never think about TLS anymore. Certificate renewals are automatic and the configs are human-readable and hand-customizable. On top of all that, Caddy plays nicely with docker containers, so I don't even have to remap ports or clutter up my localhost since I can point to port 80 on a dozen different docker containers without any need for deconfliction.

### [ZFS](https://docs.unraid.net/unraid-os/advanced-configurations/optimize-storage/zfs-storage/)

After losing access to my terabytes of storage upon graduation, I needed an alternative. Since the going rate for my current storage needs (~2 TB) is ~$200/year, it was a bit of a no-brainer to roll my own on-site storage and off-site backup since I could create a Raid Z2 with four 1 TB SSD drives for about the same one-time price and have much higher bandwidth on a local network. Say goodbye to partitioned zip file downloads at 5 MB/s from Google Drive! RAID-Z2 gives me breathing room when disks fail (because they will), and snapshots make “oops” moments trivial to recover from.

### [Docker Engine](https://docs.docker.com/engine/install/)

Docker Engine is the substrate all my other services run on. Nearly all my services live in containers, which means clean isolation, reproducible setups, and upgrades are a breeze. If something breaks, I can tear it down and redeploy in minutes, not hours. Using volumes for data storage and configuration files means I can re-deploy from scratch without fears of data-loss. Docker makes self-hosting feel modular and disposable in the best possible way, which is exactly how a lab should be.
