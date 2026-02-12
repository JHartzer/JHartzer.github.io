---
layout: post
title: Bringing Life to an Old Tablet
author: Jacob Hartzer
date: 2025-08-16
description:
tags: Software
---

While in engineering school, I purchased a simple 2-in-1 Tablet and Keyboard: the ASUS Transformer Mini T103H. It served me well, being able to both run basic Python programs for class, as well as take complex notes using the included stylus. However, it’s been nearly 10 years and simply can't handle running Windows anymore (even with the custom lightweight version of Windows it was loaded with).

As a result, I’ve been looking into lightweight Linux distributions to make it a YouTube player/cheap Android tablet. Ideally, I’d just run an Android device, but since this has an x86 processor, that’s not possible (since [Android-x86](https://www.android-x86.org/) stopped development a while ago). As such, I needed some 64-bit OS that was very light and ideally mimicked an Android tablet. The OS I eventually settled on was [BlissOS](https://blissos.org/) due to it’s clean interface, regular updates, and support for other touch devices.

The primary issue I ran into with installing Bliss on this tablet is the Transformer Mini BIOS very old and limited to 32-bit. As such, many OS default installers simply don't work. The installation would typically work just fine, but the OS wouldn't be recognized on the next book. It took a bit of trial and error to find a version of the installer and disk format that would be recognized correctly by the BIOS.

The version of Bliss that finally worked: [Bliss-v16.9.7-x86_64-OFFICIAL-gapps-20241011](https://sourceforge.net/projects/blissos-x86/files/Official/BlissOS16/Gapps/Generic/)

During the installation, I created the following partitions on a cleanly wiped drive:

- 0.5 GB EFI
- 1.0 GB Swap
- 115 GB Linux Filesystem (ext4)

From there, I ran the installation as normal and now have a *Blissful* Tablet!
