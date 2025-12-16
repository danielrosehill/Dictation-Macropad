# Dictation Macropad Planning

![alt text](screenshots/banner.png)

## Purpose

This repository is for planning, designing, and configuring macropads optimized for speech-to-text dictation workflows. Speech recognition has replaced traditional typing as the primary text input method, requiring dedicated hardware controls for seamless voice recording and transcription operations.

## Scope

This is a comprehensive planning and development project covering:

- **Configuration Planning**: Key layout design and mapping strategies for existing hardware
- **Custom Hardware Design**: Physical layout design for purpose-built dictation controllers
- **Bill of Materials (BOM)**: Component planning for custom builds
- **Custom Keycaps**: Design and sourcing of labeled keycaps for specific dictation functions
- **3D Printing**: Case and enclosure design for custom macropads
- **Ergonomic Optimization**: Hand positioning and button placement for all-day use

## The Gap

While USB foot pedals and single-button devices exist, there's a gap for specialized multi-button controllers designed specifically for dictation workflows. This project aims to fill that gap with custom solutions tailored for intensive speech-to-text usage.

## Core Functions

The macropads control these essential dictation operations:

- Start/stop recording
- Stop and transcribe (combined operation)
- Send for transcription
- Append to existing recording
- Delete recording
- Format selection (notes, blog ideas, etc.)

## Approach

1. Document existing hardware inventory
2. Design optimal key layouts for each device type
3. Create configuration profiles for current macropads
4. Design custom hardware solutions
5. Develop BOMs and 3D printable designs
6. Build and test prototypes
7. Refine based on real-world usage

## System Environment

- **OS**: Ubuntu 25.10 (KDE Plasma on Wayland)
- **Key Remapping**: Input Remapper
- **Firmware**: QMK for compatible devices
- **Integration**: Custom voice notepad interface

## Repository Structure

- `/macropads/` - Existing hardware documentation
- `/configurations/` - Key mapping configurations
- `/designs/` - Custom hardware designs and CAD files
- `/bom/` - Bills of materials for custom builds
- `/keycaps/` - Custom keycap designs and specifications

---

**Note**: This is a personal project focused on creating optimal tools for speech-to-text workflows, not a commercial endeavor.